import os
import re
import shutil
from pathlib import Path
from datetime import datetime
from io import StringIO

import frontmatter
import ruamel.yaml
from ruamel.yaml.scalarstring import LiteralScalarString

# ----------------------------
# Paths (relative to this script)
# ----------------------------
SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent          # adjust if your script is deeper nested
DOCS_DIR = REPO_ROOT / "docs"
DOCS_POSTS_DIR = DOCS_DIR / "_posts"
DOCS_IMAGES_DIR = DOCS_DIR / "images"
DOCS_CONFIG = DOCS_DIR / "_config.yml"

PROJECTS_DIR = REPO_ROOT / "Projects" / "Projects"
EXT_PROJECTS_DIR = REPO_ROOT / "Projects" / "Extended-Team-Projects"

PROJECTS_PATHLIST = [REPO_ROOT / "Projects" / "projects.md"]
PROJECTS_PROJECTS_PATHLIST = PROJECTS_DIR.rglob("*.md")
PROJECTS_EXTENDED_PATHLIST = EXT_PROJECTS_DIR.rglob("*.md")
RESEARCH_PATHLIST = [REPO_ROOT / "Research" / "research.md"]  # currently unused but kept for future

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
def load_baseurl(default="/Arm-Developer-labs") -> str:
    """
    Reads baseurl from docs/_config.yml.
    - Falls back to provided default if file or key missing.
    - Returns a Jekyll-style baseurl: starts with '/', no trailing '/'.
    """
    if not DOCS_CONFIG.exists():
        return default

    yaml = ruamel.yaml.YAML()
    try:
        cfg = yaml.load(DOCS_CONFIG.read_text(encoding="utf-8")) or {}
    except Exception:
        return default

    baseurl = cfg.get("baseurl", "") or default
    if not isinstance(baseurl, str):
        baseurl = str(baseurl)

    if not baseurl.startswith("/"):
        baseurl = "/" + baseurl
    baseurl = baseurl.rstrip("/") or "/"
    return baseurl

BASEURL = load_baseurl()

# ----------------------------
# Utilities
# ----------------------------
def clean():
    """
    Clears and recreates the docs/_posts directory.
    """
    if DOCS_POSTS_DIR.exists():
        shutil.rmtree(DOCS_POSTS_DIR)
    DOCS_POSTS_DIR.mkdir(parents=True, exist_ok=True)


def slugify(filename: str) -> str:
    """
    Build a URL-safe slug from the filename (without extension).
    Lowercase, replace non [a-z0-9-] with '-'.
    """
    stem = Path(filename).stem
    slug = re.sub(r"[^a-z0-9\-]+", "-", stem.lower()).strip("-")
    return slug or "post"


def normalize_date(meta_value, fallback_timestamp: float) -> str:
    """
    Accepts:
      - a datetime
      - a string 'YYYY-MM-DD' or ISO format
      - None
    Returns: 'YYYY-MM-DD' string, or mtime-based fallback.
    """
    if meta_value is None:
        return datetime.fromtimestamp(fallback_timestamp).strftime("%Y-%m-%d")

    if isinstance(meta_value, datetime):
        return meta_value.strftime("%Y-%m-%d")

    s = str(meta_value)
    try:
        return datetime.fromisoformat(s).strftime("%Y-%m-%d")
    except ValueError:
        # Fallback: first 10 chars if something odd comes through
        return s[:10]


# ----------------------------
# Content transforms
# ----------------------------
def convert_md_images_to_html(md_text: str, doc_path: Path) -> str:
    """
    - Finds Markdown images ![alt](path)
    - Only rewrites *relative* image paths (no http(s)://, no leading /)
    - Copies each such image into docs/images/
    - Rewrites to <img class="image ..." src="{BASEURL}/images/<filename>" />
    - Skips the README banner ./images/DeveloperLabs_Header.png entirely.
    """
    pattern = r'!\[[^\]]*\]\(([^)]+)\)'

    def replace(match):
        img_path = match.group(1).strip()

        # 1) If this is an absolute URL or already site-rooted, leave it alone
        if img_path.startswith("http://") or img_path.startswith("https://") or img_path.startswith("/"):
            return match.group(0)  # return the original markdown image unchanged

        # 2) Skip a specific header if converting README.md
        readme_path = REPO_ROOT / "README.md"
        if doc_path.resolve() == readme_path.resolve() and img_path == "./images/DeveloperLabs_Header.png":
            return ""

        # 3) Treat as a relative filesystem path
        source_path = (doc_path.parent / img_path).resolve()
        DOCS_IMAGES_DIR.mkdir(parents=True, exist_ok=True)

        if source_path.is_file():
            try:
                shutil.copy2(source_path, DOCS_IMAGES_DIR)
            except Exception as e:
                print(f"[WARN] Could not copy {source_path} -> {DOCS_IMAGES_DIR}: {e}")
        else:
            print(f"[WARN] {source_path} does not exist (referenced in {doc_path})")

        fname = Path(img_path).name
        new_img_path = f"{BASEURL}/images/{fname}"

        # Special class override for certain badges
        if "ACA_badge.jpg" in fname:
            return f'<img class="image image--l" src="{new_img_path}" loading="lazy" decoding="async" />'
        return f'<img class="image image--xl" src="{new_img_path}" loading="lazy" decoding="async" />'

    return re.sub(pattern, replace, md_text)


def convert_md(md_text: str) -> str:
    """
    Specific content replacements:
    - Replace 'Developer Labs Website' link with 'Developer Labs Repository'
    - Replace a specific YouTube thumbnail link with an <iframe>
    """
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
        '</iframe>'
    )

    replaced = md_text
    if pattern_youtube in replaced:
        replaced = replaced.replace(pattern_youtube, replacement_youtube)
    if pattern_link in replaced:
        replaced = replaced.replace(pattern_link, replacement_link)
    return replaced


# ----------------------------
# Main formatter
# ----------------------------
def write_post_from_path(path: Path, out_dir: Path):
    """
    Read a markdown file with front matter, normalize metadata, and emit
    a Jekyll post into out_dir with name YYYY-MM-DD-<slug>.md
    """
    path = Path(path)

    if path.name == "README.md":
        return

    raw_text = path.read_text(encoding="utf-8")
    post = frontmatter.loads(raw_text)

    # Prefer 'date', then 'publication-date', else file mtime
    stat = path.stat()
    date_meta = post.metadata.get("date") or post.metadata.get("publication-date")
    date_str = normalize_date(date_meta, stat.st_mtime)

    slug = slugify(path.name)

    # Force layout to "article"
    post.metadata["layout"] = "article"

    # Only set sidebar nav if it's a project-level file (not the top-level projects.md)
    if path.name != "projects.md":
        sidebar = post.metadata.get("sidebar") or {}
        sidebar.setdefault("nav", "projects")
        post.metadata["sidebar"] = sidebar

    # Optional: store full_description for templates that need it
    post.metadata["full_description"] = post.content

    # YAML writing with ruamel (preserve quotes; literal scalars for multiline strings)
    yaml = ruamel.yaml.YAML()
    yaml.preserve_quotes = True
    yaml.width = 4096

    metadata_copy = dict(post.metadata)
    for key, value in list(metadata_copy.items()):
        if isinstance(value, str) and "\n" in value:
            metadata_copy[key] = LiteralScalarString(value)

    stream = StringIO()
    yaml.dump(metadata_copy, stream)
    yaml_content = stream.getvalue()

    # Build full content: front matter + original content
    formatted = f"---\n{yaml_content}---\n{post.content}"

    # Apply markdown-specific conversions and image rewrite
    formatted = convert_md(formatted)
    formatted = convert_md_images_to_html(formatted, path)

    new_filename = f"{date_str}-{slug}.md"
    out_path = out_dir / new_filename
    out_path.write_text(formatted, encoding="utf-8")
    print(f"[OK] Wrote {out_path.relative_to(REPO_ROOT)}")


def format_index():
    """
    Build docs/index.md from README.md + custom front matter,
    with markdown conversions and image handling.
    """
    src = REPO_ROOT / "README.md"
    combined = INDEX_FRONTMATTER + src.read_text(encoding="utf-8")
    combined = convert_md(combined)
    combined = convert_md_images_to_html(combined, src)

    out_file = DOCS_DIR / "index.md"
    out_file.write_text(combined, encoding="utf-8")
    print(f"[OK] Wrote {out_file.relative_to(REPO_ROOT)}")


def main():
    print(f"[INFO] Using baseurl: {BASEURL}")
    clean()
    format_index()

    # Explicit list: projects.md, then actual project dirs
    for p in PROJECTS_PATHLIST:
        if Path(p).exists():
            write_post_from_path(Path(p), DOCS_POSTS_DIR)

    for p in PROJECTS_PROJECTS_PATHLIST:
        write_post_from_path(Path(p), DOCS_POSTS_DIR)

    for p in PROJECTS_EXTENDED_PATHLIST:
        write_post_from_path(Path(p), DOCS_POSTS_DIR)

    # If you ever want research posts too, uncomment:
    # for p in RESEARCH_PATHLIST:
    #     if Path(p).exists():
    #         write_post_from_path(Path(p), DOCS_POSTS_DIR)


if __name__ == "__main__":
    main()


