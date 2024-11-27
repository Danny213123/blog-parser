# Add author attribution to the README.md files in the blogs directory

import os
import pathlib
import markdown
from datetime import datetime

def find_readme_files(root_dir: str) -> list:

    directories = ['artificial-intelligence', 'high-performance-computing', 'software-tools-optimization']
   
    readme_files = []

    for dirpath, dirnames, filenames in os.walk(root_dir):
        
        # check if the directory is in the list of directories

        for directory in directories:

            if directory in dirpath:

                print(f"Searching in '{dirpath}'...")

                for filename in filenames:

                    if filename.lower() == 'readme.md':  # Case-insensitive matching

                        full_path = os.path.join(dirpath, filename)

                        readme_files.append(full_path)

    return readme_files

def author_attribution(readme_file: str):

    # extract the author name from metadata

    data = pathlib.Path(readme_file).read_text(encoding='utf-8')
    md = markdown.Markdown(extensions=['meta'])
    md.convert(data)

    author_pages_dir = './blogs/authors'

    # grab authors

    authors = md.Meta.get('author', [''])[0]
    date = md.Meta.get('date', [''])[0]

    if authors:

        # Create authors HTML by checking if an author page exists
        author_links = []

        for author in authors.split(','):

            # Clean author name and format it correctly for the file system
            author_name = author.strip().replace(' ', '-').lower()

            # Path to the author's markdown file in the 'authors' directory
            author_file = os.path.join(author_pages_dir, f"{author_name}.md")

            print(f"Checking for author file: {author_file}")  # Debug print

            if os.path.exists(author_file):

                # If the author file exists, create a clickable link to the author's page
                author_page = author_file.replace('.md', '.html')  # Convert .md to .html for the link

                author_page = author_page.replace('blogs', '.')

                author_links.append(f'<a href="{author_page}">{author.strip()}</a>')

            else:

                # If no author page exists, display the author's name as plain text
                print(f"Author file {author_file} does not exist.")

                author_links.append(author.strip())

        # Join author links with commas
        authors_html = ', '.join(author_links) if author_links else ''

        if authors_html:
             
          authors_string = f"{date}, by {authors_html}"
          authors_html = f'<span style="font-size:0.7em;">{authors_string}</span>'

        # find the line with the title

        with open(readme_file, 'r', encoding='utf-8') as file:

            lines = file.readlines()

        title, line_number = None, None

        for i, line in enumerate(lines):

            # only check for # , do not check if there are more than one # in the line
            if line.startswith('#') and line.count('#') == 1:

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

            lines.insert(line_number + 1, f"\n{authors_html}\n")

            with open(readme_file, 'w', encoding='utf-8') as file:

                file.writelines(lines)

            print(f"Author attribution inserted in '{readme_file}'.")

    else:
            
        print("No authors found in metadata.")


def main():

    root_directory = 'blogs'  # Specify the root directory

    print(os.getcwd())

    # change cwd to parent directory
    os.chdir('..')

    if not os.path.exists(root_directory):

      print(f"The directory '{root_directory}' does not exist.")

      return

    print(f"Searching for 'readme.md' files in '{root_directory}' and subdirectories...")

    readme_files = find_readme_files(root_directory)

    if not readme_files:

      print("No 'readme.md' files found.")

      return

    print(f"Found {len(readme_files)} 'readme.md' file(s).")

    # insert a new line in each markdown file

    for readme_file in readme_files:

        author_attribution(readme_file)

    # change back working directory
    os.chdir('blogs')

if __name__ == "__main__":
    main()
