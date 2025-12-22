import re
import shutil
from datetime import datetime
from io import StringIO
from pathlib import Path

import frontmatter
from datetime import datetime
import ruamel.yaml
from ruamel.yaml.scalarstring import LiteralScalarString

# ----------------------------
# Paths (relative to this script)
# ----------------------------
SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent  # adjust if your script is deeper nested

DOCS_DIR = REPO_ROOT / "docs"
DOCS_POSTS_DIR = DOCS_DIR / "_posts"
DOCS_IMAGES_DIR = DOCS_DIR / "images"
DOCS_CONFIG = DOCS_DIR / "_config.yml"

PROJECTS_DIR = REPO_ROOT / "Projects" / "Projects"
EXT_PROJECTS_DIR = REPO_ROOT / "Projects" / "Extended-Team-Projects"

PROJECTS_PATHLIST = [REPO_ROOT / "Projects" / "projects.md"]
PROJECTS_PROJECTS_PATHLIST = PROJECTS_DIR.rglob("*.md")
PROJECTS_EXTENDED_PATHLIST = EXT_PROJECTS_DIR.rglob("*.md")
RESEARCH_PATHLIST = [REPO_ROOT / "Research" / "research.md"]  # unused for now, kept for future

README_PATH = REPO_ROOT / "README.md"
README_BANNER = "./images/DeveloperLabs_Header.png"

INDEX_FRONTMATTER = """---
title: Academic Projects Repository
tags: TeXt
article_header:
  type: main_cover
  image:
    src: ./images/DeveloperLabs_Header.png
---
"""

# ----------------------------
# Config helpers
# ----------------------------
def _normalize_baseurl(baseurl: str) -> str:
    baseurl = (baseurl or "/").strip()
    if not baseurl.startswith("/"):
        baseurl = "/" + baseurl
    baseurl = baseurl.rstrip("/") or "/"
    return baseurl


def load_baseurl(default: str = "/Arm-Developer-Labs") -> str:
    """
    Reads baseurl from docs/_config.yml.
    Falls back to default if file/key missing.
    Returns a Jekyll-style baseurl: starts with '/', no trailing '/' (unless '/').
    """
    if not DOCS_CONFIG.exists():
        return _normalize_baseurl(default)

    yaml = ruamel.yaml.YAML()
    try:
        cfg = yaml.load(DOCS_CONFIG.read_text(encoding="utf-8")) or {}
    except Exception:
        return _normalize_baseurl(default)

    baseurl = cfg.get("baseurl", "") or default
    return _normalize_baseurl(str(baseurl))


BASEURL = load_baseurl()

# ----------------------------
# Utilities
# ----------------------------
def clean_posts_dir() -> None:
    """Clears and recreates the docs/_posts directory."""
    if DOCS_POSTS_DIR.exists():
        shutil.rmtree(DOCS_POSTS_DIR)
    DOCS_POSTS_DIR.mkdir(parents=True, exist_ok=True)


def normalize_date(meta_value, fallback_timestamp: float) -> str:
    """Return 'YYYY-MM-DD' from datetime/ISO string, else fallback to file mtime."""
    if meta_value is None:
        return datetime.fromtimestamp(fallback_timestamp).strftime("%Y-%m-%d")
    if isinstance(meta_value, datetime):
        return meta_value.strftime("%Y-%m-%d")
    s = str(meta_value)
    try:
        return datetime.fromisoformat(s).strftime("%Y-%m-%d")
    except ValueError:
        return s[:10]


def filenameify_preserve_punct(stem: str) -> str:
    """
    Preserve case + punctuation from the source filename stem as much as possible.

    Minimal safety:
      - Replace path separators (/ and \\) so we don't create subpaths
      - Replace ':' (Windows-hostile)
    """
    s = str(stem).strip()
    s = s.replace("/", "-").replace("\\", "-").replace(":", "-")
    return s or "post"


def strip_legacy_metadata_block(md: str) -> str:
    """
    Removes legacy CMS-style metadata blocks like:
      Subjects:...
      Platform:...
      SW / HW:...
      Support level:...
      Status:...

    Triggers near the top only and stops when real content begins.
    """
    lines = md.splitlines()
    cleaned: list[str] = []

    key_re = re.compile(
        r"^(Subjects|Platform|SW\s*/\s*HW|Support level|Status):\s*",
        re.IGNORECASE,
    )

    skipping = False
    triggered = False

    for i, line in enumerate(lines):
        # Only trigger near the top
        if not skipping and i < 80 and key_re.match(line):
            skipping = True
            triggered = True
            continue

        if skipping:
            # Skip legacy keys + blank lines until we hit real content
            if key_re.match(line) or line.strip() == "":
                continue
            skipping = False
            cleaned.append(line)
            continue

        cleaned.append(line)

    return "\n".join(cleaned).lstrip() if triggered else md


# ----------------------------
# Content transforms
# ----------------------------
_MD_IMAGE_RE = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")


def convert_md_images_to_html(md_text: str, doc_path: Path) -> str:
    """
    - Finds Markdown images ![alt](path)
    - Only rewrites *relative* image paths (no http(s)://, no leading /)
    - Copies each such image into docs/images/
    - Rewrites to <img class="image ..." src="{BASEURL}/images/<filename>" />
    - Skips the README banner ./images/DeveloperLabs_Header.png entirely.
    """
    def replace(match: re.Match) -> str:
        img_path = match.group(1).strip()

        # Absolute URL or site-rooted path: leave unchanged
        if img_path.startswith(("http://", "https://", "/")):
            return match.group(0)

        # Skip README banner (cover handled by INDEX_FRONTMATTER)
        if doc_path.resolve() == README_PATH.resolve() and img_path == README_BANNER:
            return ""

        # Treat as relative filesystem path
        source_path = (doc_path.parent / img_path).resolve()
        target_folder = (docs_dir_path / "images").resolve()
        target_folder.mkdir(parents=True, exist_ok=True)

        if source_path.is_file():
            try:
                shutil.copy2(source_path, DOCS_IMAGES_DIR / source_path.name)
            except Exception as e:
                print(f"[WARN] Could not copy {source_path} -> {DOCS_IMAGES_DIR}: {e}")
        else:
            print(f"Warning: {source_path} does not exist in {doc_path}!")

        new_img_path = f"/Arm-Developer-Labs/images/{Path(img_path).name}"

        if "ACA_badge.jpg" in fname:
            return f'<img class="image image--l" src="{new_img_path}" loading="lazy" decoding="async" />'
        return f'<img class="image image--xl" src="{new_img_path}" loading="lazy" decoding="async" />'

    return _MD_IMAGE_RE.sub(replace, md_text)

def convert_md(md_text: str) -> str:
    pattern_link = "[Developer Labs Website](https://arm-university.github.io/Arm-Developer-Labs/)"
    replacement_link = "[Developer Labs Repository](https://github.com/arm-university/Arm-Developer-Labs)"
    pattern_youtube = "[![Arm-CMU collaboration](https://img.youtube.com/vi/zaRozkrcix0/0.jpg)](https://www.youtube.com/watch?v=zaRozkrcix0)"
    replacement_youtube = (
        '<iframe width="560" height="315" '
        'src="https://www.youtube.com/embed/zaRozkrcix0?si=eRZirXrv5300fnBc" '
        'title="YouTube video player" frameborder="0" '
        'allow="accelerometer; autoplay; clipboard-write; encrypted-media; '
        'gyroscope; picture-in-picture; web-share" '
        'referrerpolicy="strict-origin-when-cross-origin" allowfullscreen>'
        "</iframe>"
    )

    replaced = md_text
    if pattern_youtube in replaced:
        replaced = replaced.replace(pattern_youtube, replacement_youtube)
    if pattern_link in replaced:
        replaced = replaced.replace(pattern_link, replacement_link)
    return replaced


def dump_front_matter(metadata: dict) -> str:
    """Serialize YAML front matter using ruamel, using literal blocks for multiline strings."""
    yaml = ruamel.yaml.YAML()
    yaml.preserve_quotes = True
    yaml.width = 4096

    md_copy = dict(metadata)

    for key, value in list(md_copy.items()):
        if isinstance(value, str) and "\n" in value:
            md_copy[key] = LiteralScalarString(value)

    stream = StringIO()
    yaml.dump(md_copy, stream)
    return stream.getvalue().strip() + "\n"


# ----------------------------
# Main formatter
# ----------------------------
def write_post_from_path(path: Path, out_dir: Path) -> None:
    """
    Read a markdown file with front matter and emit a Jekyll post into out_dir
    named YYYY-MM-DD-<SOURCE_STEM>.md, where SOURCE_STEM matches the input filename stem.
    """
    path = Path(path)
    if path.name == "README.md":
        return

    return replaced_md

    # Prefer 'date', then 'publication-date', else file mtime
    stat = path.stat()
    date_meta = post.metadata.get("date") or post.metadata.get("publication-date")
    date_str = normalize_date(date_meta, stat.st_mtime)

    # Force output filename stem to match the input filename stem
    source_stem = path.stem
    safe_stem = filenameify_preserve_punct(source_stem)

    # Clean/convert body content
    post.content = strip_legacy_metadata_block(post.content)
    post.content = convert_md(post.content)
    post.content = convert_md_images_to_html(post.content, path)

    # Required metadata for TeXt/Jekyll posts
    post.metadata["layout"] = "article"
    post.metadata["title"] = post.metadata.get("title") or source_stem

    # Only set sidebar nav if it's a project-level file (not the top-level projects.md)
    if path.name != "projects.md":
        sidebar = post.metadata.get("sidebar") or {}
        sidebar.setdefault("nav", "projects")
        post.metadata["sidebar"] = sidebar

    # Optional: store full_description (cleaned + converted)
    post.metadata["full_description"] = post.content

    yaml_content = dump_front_matter(post.metadata)
    formatted = f"---\n{yaml_content}---\n\n{post.content}"

    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{date_str}-{safe_stem}.md"
    out_path.write_text(formatted, encoding="utf-8")
    print(f"[OK] Wrote {out_path.relative_to(REPO_ROOT)}")

        # If there's a 'date' key in frontmatter, normalize it to "YYYY-MM-DD"
        date_meta = post.metadata.get("publication-date")
        if date_meta is None:
            # If there's no date, fallback to file's modified date
            timestamp = path.stat().st_mtime
            date_str = datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d")
        elif isinstance(date_meta, datetime):
            date_str = date_meta.strftime("%Y-%m-%d")
        else:
            # If it's already a string, trust it but ensure formatting
            try:
                parsed = datetime.fromisoformat(str(date_meta))
                date_str = parsed.strftime("%Y-%m-%d")
            except ValueError:
                # If it isn't ISO, just take the first 10 chars
                date_str = str(date_meta)[:10]

        # Build a slug from the filename (without .md)
        filename = path.name  # e.g. "my-project.md"
        slug = filename.removesuffix(".md")

        # For certain top-level markdowns ("projects.md", "research.md"), 
        # we assign a special article_header override:
        # if path.name in ["projects.md", "research.md"]:
        #     post.metadata["article_header"] = {
        #         "type": "cover",
        #         "image": {
        #             "src": "/images/DeveloperLabs_Header.png",
        #         },
        #     }

        # Always set layout to "article"
        post.metadata["layout"] = "article"

        # Only set sidebar nav if it's a project‐level file (not the top-level README)
        if path.name != "projects.md":
            post.metadata["sidebar"] = {"nav": "projects"}

        data = {"full_description": post.content}
        post.metadata.update(data)
        
        # Use ruamel.yaml for proper literal block scalar formatting
        yaml = ruamel.yaml.YAML()
        yaml.preserve_quotes = True
        yaml.width = 4096
        
        # Create the frontmatter manually to ensure literal block scalars
        metadata_copy = post.metadata.copy()
        
        # Convert multiline strings to literal scalars
        for key, value in metadata_copy.items():
            if isinstance(value, str) and '\n' in value:
                metadata_copy[key] = ruamel.yaml.scalarstring.LiteralScalarString(value)
        
        # Manually construct the frontmatter
        from io import StringIO
        stream = StringIO()
        yaml.dump(metadata_copy, stream)
        yaml_content = stream.getvalue()
        
        # Build the full content with frontmatter
        formatted_content = f"---\n{yaml_content}---\n{post.content}"

        # Convert Markdown image embeds → HTML and copy assets
        converted_content = convert_md_images_to_html(
            formatted_content,
            path
        )

        # Build the new filename: "<date>-<slug>.md"
        new_filename = f"{date_str}-{slug}.md"
        out_file = Path(docs_path, new_filename)
        out_file.write_text(converted_content, encoding="utf-8")

def format_index() -> None:
    """
    Build docs/index.md from README.md + custom front matter,
    with markdown conversions and image handling.
    """
    combined = INDEX_FRONTMATTER + README_PATH.read_text(encoding="utf-8")
    combined = convert_md(combined)
    combined = convert_md_images_to_html(combined, README_PATH)

    out_file = DOCS_DIR / "index.md"
    out_file.write_text(combined, encoding="utf-8")
    print(f"[OK] Wrote {out_file.relative_to(REPO_ROOT)}")


def main() -> None:
    print(f"[INFO] Using baseurl: {BASEURL}")
    clean_posts_dir()
    format_index()

    # Explicit list: projects.md, then actual project dirs
    for p in PROJECTS_PATHLIST:
        if p.exists():
            write_post_from_path(p, DOCS_POSTS_DIR)

    for p in PROJECTS_PROJECTS_PATHLIST:
        write_post_from_path(p, DOCS_POSTS_DIR)

    for p in PROJECTS_EXTENDED_PATHLIST:
        write_post_from_path(p, DOCS_POSTS_DIR)

    # If you ever want research posts too, uncomment:
    # for p in RESEARCH_PATHLIST:
    #     if p.exists():
    #         write_post_from_path(p, DOCS_POSTS_DIR)


if __name__ == "__main__":
    main()
