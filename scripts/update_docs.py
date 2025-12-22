import os
import sys
import re
import shutil
from pathlib import Path
import frontmatter
from datetime import datetime
import ruamel.yaml

projects_dir = "../Projects/Projects"
extended_projects_dir = "../Projects/Extended-Team-Projects"

projects_pathlist = [Path("../Projects/projects.md")]
projects_projects_pathlist = Path(projects_dir).rglob("*.md")
projects_extended_project_pathlist = Path(extended_projects_dir).rglob("*.md")
research_pathlist = [Path("../Research/research.md")]

docs_posts_dir = "../docs/_posts"

index_frontmatter = """---
title: Academic Projects Repository
tags: TeXt
article_header:
  type: main_cover
  image:
    src: ./images/DeveloperLabs_Header.png
---
"""

def clean():
    clean_lst = [docs_posts_dir]
    for dirpath in clean_lst:
        if os.path.exists(dirpath) and os.path.isdir(dirpath):
            shutil.rmtree(dirpath)
            os.makedirs(dirpath)
        else:
            os.makedirs(dirpath)

def convert_md_images_to_html(md_text: str, doc_path: Path) -> str:
    pattern = r'!\[[^\]]*\]\(([^)]+)\)'
    docs_dir_path = Path("../docs")

    def replace(match):
        img_path = match.group(1)

        # Skip certain banner images entirely
        if doc_path.resolve() == Path("../README.md").resolve() and img_path == "./images/DeveloperLabs_Header.png":
            return ""

        source_path = (doc_path.parent / img_path).resolve()
        target_folder = (docs_dir_path / "images").resolve()
        target_folder.mkdir(parents=True, exist_ok=True)

        if source_path.is_file():
            shutil.copy2(source_path, target_folder)
        else:
            print(f"Warning: {source_path} does not exist in {doc_path}!")

        new_img_path = f"/Arm-Developer-Labs/images/{Path(img_path).name}"

        if "ACA_badge.jpg" in new_img_path:
            return f'<img class="image image--l" src="{new_img_path}"/>'
        return f'<img class="image image--xl" src="{new_img_path}"/>'

    return re.sub(pattern, replace, md_text)

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
        '</iframe>'
    )

    replaced_md = md_text
    if pattern_youtube in replaced_md:
        replaced_md = replaced_md.replace(pattern_youtube, replacement_youtube)
    if pattern_link in replaced_md:
        replaced_md = replaced_md.replace(pattern_link, replacement_link)

    return replaced_md



def format_content(pathlist, docs_path):
    """
    For each Path in pathlist:
      - Load frontmatter metadata.
      - Extract the 'date' field from metadata (expected YYYY-MM-DD or datetime).
      - Use that date plus the filename-slug to name the output: "<date>-<slug>.md".
      - Convert images and special markdown embeds, then write to docs_path.
    """
    for path in pathlist:
        path = Path(path)

        if path.name == "README.md":
            continue

        raw_text = path.read_text(encoding="utf-8")
        post = frontmatter.loads(raw_text)

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

def format_index():
    src = "../README.md"
    docs_path = "../docs"
    with open(src, 'r', encoding='utf-8') as f:
        # Prepend our custom frontmatter, then convert images/embeds
        combined = index_frontmatter + f.read()
        formatted_content = convert_md(combined)
        converted_content = convert_md_images_to_html(
            formatted_content,
            Path(src)
        )
        out_file = os.path.join(docs_path, "index.md")
        with open(out_file, 'w', encoding='utf-8') as out_f:
            out_f.write(converted_content)

def main():
    clean()
    format_index()
    format_content(projects_pathlist, docs_posts_dir)
    format_content(projects_projects_pathlist, docs_posts_dir)
    format_content(projects_extended_project_pathlist, docs_posts_dir)

if __name__ == "__main__":
    main()