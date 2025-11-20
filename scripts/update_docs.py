import os
import re
import shutil
from pathlib import Path
from datetime import datetime

import frontmatter
import ruamel.yaml
from ruamel.yaml.scalarstring import LiteralScalarString

# ----------------------------
# Paths (run this script from /scripts or project root)
# ----------------------------
ROOT = Path(__file__).resolve().parent
REPO_ROOT = ROOT.parent
DOCS_DIR = REPO_ROOT / "docs"
DOCS_POSTS_DIR = DOCS_DIR / "_posts"
DOCS_IMAGES_DIR = DOCS_DIR / "images"
DOCS_CONFIG = DOCS_DIR / "_config.yml"

PROJECTS_DIR = REPO_ROOT / "Projects" / "Projects"
EXT_PROJECTS_DIR = REPO_ROOT / "Projects" / "Extended-Team-Projects"

PROJECTS_PATHLIST = [REPO_ROOT / "Projects" / "projects.md"]
PROJECTS_PROJECTS_PATHLIST = PROJECTS_DIR.rglob("*.md")
PROJECTS_EXTENDED_PATHLIST = EXT_PROJECTS_DIR.rglob("*.md")
RESEARCH_PATHLIST = [REPO_ROOT / "Research" / "research.md"]

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
def load_baseurl() -> str:
    """
    Reads baseurl from docs/_config.yml.
    Falls back to '/DLFIXES' if not present (your site is https://v3x-0e.github.io/DLFIXES/).
    Ensures it starts with '/' and does not end with '/' (Jekyll convention).
    """
    default_baseurl = "/DLFIXES"
    if not DOCS_CONFIG.exists():
        return default_baseurl

    try:
        import yaml as pyyaml
        cfg = pyyaml.safe_load(DOCS_CONFIG.read_text(encoding="utf-8")) or {}
        baseurl = cfg.get("baseurl", "") or default_baseurl
        if not baseurl.startswith("/"):
            baseurl = "/" + baseurl
        baseurl = baseurl.rstrip("/")
        return baseurl
    except Exception:
        return default_baseurl


BASEURL = load_baseurl()

# ----------------------------
# Utilities
# ----------------------------
def clean():
    DOCS_POSTS_DIR.mkdir(parents=True, exist_ok=True)
    # wipe posts dir
    shutil.rmtree(DOCS_POSTS_DIR, ignore_errors=True)
    DOCS_POSTS_DIR.mkdir(parents=True, exist_ok=True)

def slugify(filename: str) -> str:
    """
    Build a URL-safe slug from the filename (without extension).
    Lowercase, replace non [a-z0-9-] with '-'.
    """
    stem = Path(filename).stem
    slug = re.sub(r'[^a-z0-9\-]+', '-', stem.lower()).strip('-')
    return slug or "post"

def norm_date(meta) -> str:
    """
    Accepts:
      - front matter key 'date' or 'publication-date'
      - datetime or string
    Returns: 'YYYY-MM-DD'
    """
    if meta is None:
        return None
    if isinstance(meta, datetime):
        return meta.strftime("%Y-%m-%d")
    s = str(meta)
    try:
        # Handles 'YYYY-MM-DD' and full ISO timestamps
        return datetime.fromisoformat(s).strftime("%Y-%m-%d")
    except ValueError:
        # Fallback: first 10 chars
        return s[:10]

# ----------------------------
# Content transforms
# ----------------------------
def convert_md_images_to_html(md_text: str, doc_path: Path) -> str:
    """
    - Finds Markdown images ![alt](path)
    - Copies each image into docs/images/
    - Rewrites to <img class="image ..." src="{BASEURL}/images/<filename>" />
    - Skips the README banner ./images/DeveloperLabs_Header.png entirely.
    """
    pattern = r'!\[[^\]]*\]\(([^)]+)\)'

    def replace(match):
        img_path = match.group(1).strip()
        # Skip a specific header if converting README.md
        if doc_path.resolve() == (REPO_ROOT / "README.md").resolve() and img_path == "./images/DeveloperLabs_Header.png":
            return ""

        source_path = (doc_path.parent / img_path).resolve()
        DOCS_IMAGES_DIR.mkdir(parents=True, exist_ok=True)

        if source_path.is_file():
            try:
                shutil.copy2(source_path, DOCS_IMAGES_DIR)
            except Exception as e:
                print(f"Warning: could not copy {source_path} -> {DOCS_IMAGES_DIR}: {e}")
        else:
            print(f"Warning: {source_path} does not exist (referenced in {doc_path})")

        fname = Path(img_path).name
        new_img_path = f"{BASEURL}/images/{fname}"

        # Special size override
        if "ACA_badge.jpg" in fname:
            return f'<img class="image image--l" src="{new_img_path}" loading="lazy" decoding="async"/>'
        return f'<img class="image image--xl" src="{new_img_path}" loading="lazy" decoding="async"/>'

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

    replaced_md = md_text
    if pattern_youtube in replaced_md:
        replaced_md = replaced_md.replace(pattern_youtube, replacement_youtube)
    if pattern_link in replaced_md:
        replaced_md = replaced_md.replace(pattern_link, replacement_link)
    return replaced_md

# ----------------------------
# Main formatter
# ----------------------------
def write_post_from_path(path: Path, out_dir: Path):
    """
    Read a markdown file with front matter, normalize, and emit a Jekyll post
    into out_dir with name YYYY-MM-DD-<slug>.md
    """
    if path.name == "README.md":
        return

    raw_text = path.read_text(encoding="utf-8")
    post = frontmatter.loads(raw_text)

    # Prefer 'date', fallback to 'publication-date'; else file mtime.
    date_str = norm_date(post.metadata.get("date")) or norm_date(post.metadata.get("publication-date"))
    if not date_str:
        date_str = datetime.fromtimestamp(path.stat().st_mtime).strftime("%Y-%m-%d")

    slug = slugify(path.name)

    # Force layout; add sidebar nav for project-level md except the index 'projects.md'
    post.metadata["layout"] = "article"
    if path.name != "projects.md":
        post.metadata.setdefault("sidebar", {})["nav"] = "projects"

    # If you want the entire original content also in front matter as a scalar:
    # (Your theme might not need this; keep if used)
    post.metadata["full_description"] = post.content

    # YAML writing with ruamel (preserve quotes; literal scalars for multiline)
    yaml = ruamel.yaml.YAML()
    yaml.preserve_quotes = True
    yaml.width = 4096

    metadata_copy = dict(post.metadata)
    for key, value in list(metadata_copy.items()):
        if isinstance(value, str) and "\n" in value:
            metadata_copy[key] = LiteralScalarString(value)

    from io import StringIO
    stream = StringIO()
    yaml.dump(metadata_copy, stream)
    yaml_content = stream.getvalue()

    front = f"---\n{yaml_content}---\n{post.content}"

    # Convert Markdown-specific bits and images
    front = convert_md(front)
    front = convert_md_images_to_html(front, path)

    new_filename = f"{date_str}-{slug}.md"
    out_path = out_dir / new_filename
    out_path.write_text(front, encoding="utf-8")
    print(f"[OK] Wrote {out_path.relative_to(REPO_ROOT)}")

def format_index():
    src = REPO_ROOT / "README.md"
    combined = INDEX_FRONTMATTER + src.read_text(encoding="utf-8")
    combined = convert_md(combined)
    combined = convert_md_images_to_html(combined, src)
    out_file = DOCS_DIR / "index.md"
    out_file.write_text(combined, encoding="utf-8")
    print(f"[OK] Wrote {out_file.relative_to(REPO_ROOT)}")

def main():
    print(f"Detected baseurl: {BASEURL}")
    clean()
    format_index()

    # Explicit lists and globs
    for p in PROJECTS_PATHLIST:
        if Path(p).exists():
            write_post_from_path(Path(p), DOCS_POSTS_DIR)

    for p in PROJECTS_PROJECTS_PATHLIST:
        write_post_from_path(Path(p), DOCS_POSTS_DIR)

    for p in PROJECTS_EXTENDED_PATHLIST:
        write_post_from_path(Path(p), DOCS_POSTS_DIR)

if __name__ == "__main__":
    main()
