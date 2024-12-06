# Index.md Generator
# Updated 2024 November 13
# Version 1.3


import os
import re
import yaml
import shutil
from datetime import datetime


class Blog:

    def __init__(self, file_path, metadata):

        self.file_path = file_path
        self.metadata = metadata

        # Dynamically set attributes based on metadata

        for key, value in metadata.items():

            setattr(self, key, value)
        # Ensure the 'date' field exists

        if "date" in metadata:

            self.date = self.parse_date(metadata["date"])
        else:

            self.date = None

    def normalize_date_string(self, date_str):

        # do not remove

        date_str = date_str.replace("Sept", "Sep")

        return date_str

    def parse_date(self, date_str):

        # Normalize the date string

        date_str = self.normalize_date_string(date_str)

        # Define possible date formats, including string-based months

        date_formats = [
            "%d-%m-%Y",  # e.g. 8-08-2024
            "%d/%m/%Y",  # e.g. 8/08/2024
            "%d-%B-%Y",  # e.g. 8-August-2024
            "%d-%b-%Y",  # e.g. 8-Aug-2024
            "%d %B %Y",  # e.g. 8 August 2024
            "%d %b %Y",  # e.g. 8 Aug 2024
            "%d %B, %Y",  # e.g. 8 August, 2024
            "%d %b, %Y",  # e.g. 8 Aug, 2024
        ]

        for fmt in date_formats:

            try:
                return datetime.strptime(date_str, fmt)
            except ValueError:
                continue
        print(f"Invalid date format in {self.file_path}: {date_str}")

        return None

    def __repr__(self):

        return f"Blog(file_path='{self.file_path}', metadata={self.__dict__})"


def find_readme_files(root_dir):

    readme_files = []

    for dirpath, dirnames, filenames in os.walk(root_dir):

        for filename in filenames:

            if filename.lower() == "readme.md":  # Case-insensitive matching

                full_path = os.path.join(dirpath, filename)

                readme_files.append(full_path)
    return readme_files


def extract_metadata(file_path):

    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
    # Regular expression to match YAML front matter

    yaml_pattern = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)

    match = yaml_pattern.match(content)

    if match:

        yaml_content = match.group(1)

        try:

            metadata = yaml.safe_load(yaml_content)

            return metadata
        except yaml.YAMLError as e:

            print(f"Error parsing YAML in {file_path}: {e}")

            return None
    else:

        print(f"No metadata found in {file_path}.")

        return None


def create_blog_objects(readme_files):

    blog_objects = []

    for file_path in readme_files:

        metadata = extract_metadata(file_path)

        if metadata:

            blog = Blog(file_path, metadata)

            blog_objects.append(blog)
        else:

            print(f"Skipping {file_path}: No valid metadata found.")
    return blog_objects


def sort_blogs_by_date(blogs):

    # Filter out blogs without valid dates and sort by date

    blogs_with_date = [blog for blog in blogs if blog.date is not None]

    return sorted(blogs_with_date, key=lambda blog: blog.date, reverse=True)


def grab_authors(authors_list):

    author_pages_dir = (
        "./blogs/authors"  # Directory where author markdown files are stored
    )

    author_links = []

    for author in authors_list:

        # Clean author name and format it correctly for the file system

        author_name = author.strip().replace(" ", "-").lower()

        # Path to the author's markdown file in the 'authors' directory

        author_file = os.path.join(author_pages_dir, f"{author_name}.md")

        print(f"Checking for author file: {author_file}")  # Debug print

        if os.path.exists(author_file):

            # If the author file exists, create a clickable link to the author's page

            author_page = author_file.replace(
                ".md", ".html"
            )  # Convert .md to .html for the link

            print(author_page)

            author_page = author_page.replace("blogs", ".")

            author_links.append(f'<a href="{author_page}">{author.strip()}</a>')
        else:

            # If no author page exists, display the author's name as plain text

            print(f"Author file {author_file} does not exist.")

            author_links.append(author.strip())
    return ", ".join(author_links) if author_links else ""


def generate_blog_grid(
    blogs, output_file="latest_blogs.md", max_blogs=9, max_category=3
):

    index_template = """
---
title: ROCm Blogs
myst:
  html_meta:
    "description lang=en": "AMD ROCm™ software blogs"
    "keywords": "AMD GPU, MI300, MI250, ROCm, blog"
    "property=og:locale": "en_US"
---

<!--
Updated 2024 October 10
Generated {datetime}
-->

<h1><a href="blog/atom.xml"><i class="fa fa-rss fa-rotate-270"></i></a> AMD ROCm™ Blogs</h1>

<script>
  const buttonWrapper = document.getElementById('buttonWrapper');

  const observer = new MutationObserver((mutationsList) => {
    for (const mutation of mutationsList) {
      if (mutation.type === 'attributes' && mutation.attributeName === 'data-mode') {
        console.log(`Data mode changed to: ${newMode}`);
        if (newMode === 'light') {
          buttonWrapper.style.setProperty('--original-background', 'white');
          buttonWrapper.style.setProperty('--hover-background-colour', 'white');
        } else {
          buttonWrapper.style.setProperty('--original-background', 'black');
          buttonWrapper.style.setProperty('--hover-background-colour', 'black');
        }
      }
    }
  });
</script>

<style>
  .bd-main .bd-content .bd-article-container {
    max-width: 100%;
  }
  .bd-sidebar-secondary {
    display: none;
  }
  .sd-card-large.sd-card {}
  #buttonWrapper:hover {
    border-color: hsla(231, 99%, 66%, 1);
    transform: scale(1.05);
    background-color: var(--hover-background-colour);
  }
  .small-sd-card-large.sd-card {}
  #buttonWrapper:hover {
    border-color: hsla(231, 99%, 66%, 1);
    transform: scale(1.05);
    background-color: var(--hover-background-colour);
  }
  #buttonWrapper {
    border-color: #A9A9A9;
    background-color: var(--original-background)
    text-align: center;
    font-weight: bold;
    font-size: 12px;
    border-radius: 1px;
    transition: transform 0.2s, border-color 0.2s;
  }
  h2 {
    margin: 0;
    font-size: 1.5em;
  }
  .container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px;
    box-sizing: border-box;
    width: 100%;
  }
  .read-more-btn {
    font-size: 20px;
    padding: 10px;
    font-weight: bold;
    cursor: pointer;
    display: inline-block;
    align-items: center;
    text-decoration: none;
    overflow: hidden;
    gap: 7px;
    display: block;
    text-align: left;
    margin-left: 0;
    margin-top: 10px;
  }
  .read-more-btn-small {
    font-size: 15px;
    padding: 10px;
    font-weight: bold;
    cursor: pointer;
    display: inline-block;
    align-items: center;
    text-decoration: none;
    overflow: hidden;
    gap: 7px;
    display: block;
    text-align: left;
    margin-left: 0;
    margin-top: 10px;
  }
  .arrows {
    font-size: 20px;
    display: inline-block;
    font-weight: bold;
    transition: transform 0.3s ease, color 0.3s ease, font-size 0.3s ease;
  }
  .read-more-btn:hover .arrows {
    transform: translateX(8px);
  }
  .arrows-small {
    font-size: 15px;
    display: inline-block;
    font-weight: bold;
    transition: transform 0.3s ease, color 0.3s ease, font-size 0.3s ease;
  }
  .read-more-btn-small:hover .arrows-small {
    transform: translateX(10px);
  }
  .date {
    font-size: 13px;
    font-weight: 300;
    line-height: 22.5px;
    text-transform: none;
    margin-bottom: 10px;
  }
  .paragraph {
    font-size: 16px;
    line-height: 24px;
    margin-bottom: 10px;
  }
  .large-sd-card-img-top.sd-card-img-top {
    width: 100%;
    height: 21vw;
    object-fit: cover;
  }
  .small-sd-card-img-top.sd-card-img-top {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }
  .large-sd-card.sd-card-body {
    width: 100%;
    height: 15%;
  }
  .small-sd-card {
    width: 45px;
    height: 0;
    display: none;
  }
  .bd-content .sd-card .sd-card-footer {
    border-top: none;
  }
  .card-header {
    font-size: 16px;
    font-family: 'Arial', sans-serif;
    font-weight: bold;
    line-height: 1.4;
    margin-bottom: 10px;
  }
  .paragraph {
    font-size: 12px;
    font-family: 'Arial', sans-serif;
    line-height: 1.4;
    margin-bottom: 10px;
  }
</style>

<div class="container">
  <h2>Recent Posts</h2>
  <a href="blog.html">
    <button id="buttonWrapper">
      See All >>
    </button>
  </a>
</div>

::::{grid} 1 2 2 3
:margin 2
{grid_items}
::::

<div class="container">
  <h2>Ecosystems and partners</h2>
  <a href="blog/category/ecosystems-and-partners.html">
    <button id="buttonWrapper">
      See All >>
    </button>
  </a>
</div>

::::{grid} 1 2 2 3
:margin 2
{eco_grid_items}
::::

<div class="container">
  <h2>Applications & models</h2>
  <a href="blog/category/applications-models.html">
    <button id="buttonWrapper">
      See All >>
    </button>
  </a>
</div>

::::{grid} 1 2 2 3
:margin 2
{application_grid_items}
::::

<div class="container">
  <h2>Software tools & optimizations</h2>
  <a href="blog/category/software-tools-optimizations.html">
    <button id="buttonWrapper">
      See All >>
    </button>
  </a>
</div>

::::{grid} 1 2 2 3
:margin 2
{software_grid_items}
::::

<h2> Stay informed</h2>
<ul>
  <li><a href="blog/atom.xml"> Subscribe to our <i class="fa fa-rss fa-rotate-270"></i> RSS feed</a></li>
  <li><a href="https://github.com/ROCm/rocm-blogs"> Watch our GitHub repo </a></li>
</ul>

"""

    # remove the first new line

    index_template = index_template[1:]

    grid_items = []
    application_grid_items = []
    software_grid_items = []
    eco_grid_items = []

    holder = []

    for index, blog in enumerate(blogs):

        title = blog.blog_title if hasattr(blog, "blog_title") else "No Title"

        date = blog.date.strftime("%B %d, %Y") if blog.date else "No Date"

        # look at myst description

        if hasattr(blog, "myst"):

            print(blog.myst.get("html_meta").get("description lang=en"))
            description = (
                blog.myst.get("html_meta").get("description lang=en")
                if blog.myst.get("html_meta").get("description lang=en")
                else "No Description"
            )

            if len(description) > 150:
                description = description[:150] + "..."
            else:
                # add invisible characters to ensure the card is the same size

                description = description + "..." + " " * (150 - len(description))
        # Get authors from the blog (assuming it's a comma-separated string)

        authors_list = getattr(blog, "author", "").split(",")

        # Create href by replacing the .md extension with .html

        href = blog.file_path.replace(".md", ".html")
        href = href.replace("blogs", ".")

        # swap href \ to / for windows

        href = href.replace("\\", "/")

        # Generate an image or use default

        image = blog.thumbnail if hasattr(blog, "thumbnail") else "./images/generic.jpg"

        # check if image path is in the correct format

        if not image.startswith("./images/"):

            image = "./images/" + image
        # remove README.html

        image_href = "./blogs" + ((href[1:].replace("/README.html", image[1:])))
        image_href = image_href.replace("\\", "/")

        # check if image is in images directory (blogs/images)

        temp_image = image.replace("//", "/").replace("./", "blogs/")

        print(f"Date: {date}")

        print("\n-------------------------------------------------------------------\n")
        print(f"Link: {href}")

        if not os.path.exists(temp_image):

            print(f"Image {image} does not exist.")

            image = "./images/generic.jpg"

            if os.path.exists(image_href):

                print(f"Image {image_href} exists.")
                image = image_href.replace("./blogs", ".")
            else:

                print(f"Image {image_href} does not exist.")
                image = "./images/generic.jpg"
        # check if images are in the relative blog directory

        elif os.path.exists(href.replace(".html", ".md").replace("blogs", ".")):

            print(href.replace(".html", ".md").replace("blogs", "."))
        else:

            print(f"Image {image} exists.")
        # Join author links with commas

        if authors_list:

            authors_html = grab_authors(authors_list)
        if authors_html:

            authors_html = f"by {authors_html}"
        # Create grid item card with authors

        grid_item = f"""
:::{{grid-item-card}}
:padding: 1
:img-top: {image}
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href="{href}" class="small-card-header-link">
    <h2 class="card-header">{title}</h2>
</a>
<p class="paragraph">{description}</p>
<div class="date">{date} {authors_html}</div>
:::
"""

        if index < max_blogs:

            grid_items.append(grid_item)
        elif (
            blog.category == "Applications & models"
            and len(application_grid_items) < max_category
        ):

            application_grid_items.append(grid_item)
        elif (
            blog.category == "Software tools & optimizations"
            and len(software_grid_items) < max_category
        ):

            software_grid_items.append(grid_item)
        elif (
            blog.category == "Ecosystems and Partners"
            and len(eco_grid_items) < max_category
        ):

            eco_grid_items.append(grid_item)
    print(f"{software_grid_items}")

    grid_content = "".join(grid_items)
    application_grid_content = "".join(application_grid_items)
    software_grid_content = "".join(software_grid_items)
    eco_grid_content = "".join(eco_grid_items)

    # Write the grid content to the Markdown file

    with open(output_file, "w", encoding="utf-8") as f:

        f.write(grid_content)
    print(f"Grid content successfully written to {output_file}")

    index_template = index_template.replace("{grid_items}", grid_content)

    index_template = index_template.replace("{eco_grid_items}", eco_grid_content)

    index_template = index_template.replace(
        "{application_grid_items}", application_grid_content
    )

    index_template = index_template.replace(
        "{software_grid_items}", software_grid_content
    )

    index_template = index_template.replace(
        "{datetime}", datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )

    # dangerous

    # write new index.md

    with open("blogs/index.md", "w", encoding="utf-8") as f:

        f.write(index_template)
    return index_template


def author_attribution(blogs, minimum_date="September 1, 2024"):

    blogs_to_process = []

    for blog in blogs:

        if blog.date < datetime.strptime(minimum_date, "%B %d, %Y"):

            print(f"Skipping {blog.file_path}: Date is before {minimum_date}.")

            continue
        else:

            blogs_to_process.append(blog)
    print(f"Processing {len(blogs_to_process)} blogs...")

    print(f"Current working directory as of author attribution: {os.getcwd()}")

    print("\n-------------------------------------------------------------------\n")

    for blog in blogs_to_process:

        authors_list = getattr(blog, "author", "").split(",")
        date = blog.date.strftime("%B %d, %Y") if blog.date else "No Date"

        if authors_list:

            authors_html = grab_authors(authors_list)

            if authors_html:

                authors_html = authors_html.replace("././", "../../").replace(
                    ".md", ".html"
                )

                authors_string = f"{date}, by {authors_html}"

                print(authors_html)

                # replace with just blogs/{author_name}.html

                # make it work with markdown and html
                # authors_html = f'<span style="font-size:0.7em;">{authors_string}</span>'

                print(f"Authors: {authors_string}")

                authors_html = f'<div class="date">{authors_string}</div>'
            print(f"Current working directory as of write file: {os.getcwd()}")

            # grab blog link

            readme_file = blog.file_path

            with open(readme_file, "r", encoding="utf-8") as file:

                lines = file.readlines()
            title, line_number = None, None

            for i, line in enumerate(lines):

                # only check for # , do not check if there are more than one # in the line

                if line.startswith("#") and line.count("#") == 1:

                    title = line

                    line_number = i

                    break
            if title:

                # insert the author attribution after the title
                # title
                #
                # author attribution
                #
                # content

                lines.insert(
                    line_number + 1,
                    """
<style>
.date {
  font-size: 13px;
  font-weight: 300;
  line-height: 22.5px;
  text-transform: none;
  margin-bottom: 10px;
}
</style>\n""",
                )

                lines.insert(line_number + 2, f"\n{authors_html}\n")

                with open(readme_file, "w", encoding="utf-8") as file:

                    # add date class style

                    file.writelines(lines)
                print(f"Author attribution inserted in '{readme_file}'.")
        else:

            print("No authors found in metadata.")


def main():

    root_directory = "blogs"  # Specify the root directory

    print(os.getcwd())

    # change cwd to parent directory

    os.chdir("..")

    if not os.path.exists(root_directory):

        print(f"The directory '{root_directory}' does not exist.")

        return
    print(
        f"Searching for 'readme.md' files in '{root_directory}' and subdirectories..."
    )

    readme_files = find_readme_files(root_directory)

    if not readme_files:

        print("No 'readme.md' files found.")

        return
    print(f"Found {len(readme_files)} 'readme.md' file(s).")

    blogs = create_blog_objects(readme_files)

    # Sort blogs by date

    sorted_blogs = sort_blogs_by_date(blogs)

    for blog in sorted_blogs:

        if hasattr(blog, "author"):

            print(blog.author)
    # Generate the grid for the top 15 latest blogs

    generate_blog_grid(sorted_blogs)

    author_attribution(sorted_blogs)

    # change back working directory

    os.chdir("blogs")


if __name__ == "__main__":
    main()
