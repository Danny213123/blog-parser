import os
import re
import yaml
from datetime import datetime

class Blog:

    def __init__(self, file_path, metadata):

        self.file_path = file_path
        self.metadata = metadata

        # Dynamically set attributes based on metadata
        for key, value in metadata.items():

            setattr(self, key, value)

        # Ensure the 'date' field exists
        if 'date' in metadata:

            self.date = self.parse_date(metadata['date'])

        else:

            self.date = None 

    def normalize_date_string(self, date_str):

        date_str = date_str.replace("Sept", "Sep")

        return date_str

    def parse_date(self, date_str):

        # Normalize the date string
        date_str = self.normalize_date_string(date_str)

        # Define possible date formats, including string-based months
        date_formats = [
            "%d-%m-%Y",       # e.g. 8-08-2024
            "%d/%m/%Y",       # e.g. 8/08/2024
            "%d-%B-%Y",       # e.g. 8-August-2024
            "%d-%b-%Y",       # e.g. 8-Aug-2024
            "%d %B %Y",       # e.g. 8 August 2024
            "%d %b %Y",       # e.g. 8 Aug 2024
            "%d %B, %Y",      # e.g. 8 August, 2024
            "%d %b, %Y",      # e.g. 8 Aug, 2024
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
            if filename.lower() == 'readme.md':  # Case-insensitive matching
                full_path = os.path.join(dirpath, filename)
                readme_files.append(full_path)
    return readme_files


def extract_metadata(file_path):

    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Regular expression to match YAML front matter
    yaml_pattern = re.compile(r'^---\s*\n(.*?)\n---\s*\n', re.DOTALL)

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

def generate_blog_grid(blogs, output_file='latest_blogs.md', max_blogs=15):

    grid_items = []
    author_pages_dir = 'blogs/authors'  # Directory where author markdown files are stored

    for index, blog in enumerate(blogs[:max_blogs]):

        title = blog.title if hasattr(blog, 'title') else 'No Title'

        date = blog.date.strftime('%B %d, %Y') if blog.date else 'No Date'
        
        description = blog.description if hasattr(blog, 'description') else 'No Description'

        # Get authors from the blog (assuming it's a comma-separated string)
        authors_list = getattr(blog, 'author', '').split(',')

        # Create href by replacing the .md extension with .html
        href = blog.file_path.replace('.md', '.html')

        # Generate an image or use default
        image = getattr(blog, 'image', './images/default.jpg')  # Default image path

        # Create authors HTML by checking if an author page exists
        author_links = []
        for author in authors_list:
            # Clean author name and format it correctly for the file system
            author_name = author.strip().replace(' ', '-').lower()

            # Path to the author's markdown file in the 'authors' directory
            author_file = os.path.join(author_pages_dir, f"{author_name}.md")

            print(f"Checking for author file: {author_file}")  # Debug print

            if os.path.exists(author_file):
                # If the author file exists, create a clickable link to the author's page
                author_page = author_file.replace('.md', '.html')  # Convert .md to .html for the link

                author_links.append(f'<a href="{author_page}">{author.strip()}</a>')

            else:

                # If no author page exists, display the author's name as plain text
                print(f"Author file {author_file} does not exist.")

                author_links.append(author.strip())

        # Join author links with commas
        authors_html = ', '.join(author_links) if author_links else 'Unknown Author'

        # Create grid item card with authors
        grid_item = f"""
:::{{grid-item-card}}
:padding: 1
:img-top: {image}
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card

<a href="{href}" class="small-card-header-link">
    <h2 class="card-header">{title}</h2>
</a>
<div class="date">{date} by {authors_html}</div>

<p class="paragraph">{description}</p>
<a href="{href}" class="read-more-btn-small">Read More <span class="arrows-small">>></span></a>
:::
        """
        grid_items.append(grid_item)

    # Join all grid items into one string
    grid_content = ''.join(grid_items)

    # Write the grid content to the Markdown file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(grid_content)

    print(f"Grid content successfully written to {output_file}")

def main():

    root_directory = 'blogs'  # Specify the root directory
    if not os.path.isdir(root_directory):

        print(f"The directory '{root_directory}' does not exist.")

        return

    print(f"Searching for 'readme.md' files in '{root_directory}' and subdirectories...")
    readme_files = find_readme_files(root_directory)

    if not readme_files:

        print("No 'readme.md' files found.")

        return

    print(f"Found {len(readme_files)} 'readme.md' file(s).")
    blogs = create_blog_objects(readme_files)

    # Sort blogs by date
    sorted_blogs = sort_blogs_by_date(blogs)

    for blog in sorted_blogs:

        if hasattr(blog, 'author'):

            print(blog.author)

    # Generate the grid for the top 15 latest blogs
    grid = generate_blog_grid(sorted_blogs, max_blogs=15)

    # Output the grid (for example, write to a file or print)
    print(grid)

if __name__ == "__main__":
    main()

