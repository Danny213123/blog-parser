# check-categories.py 
# check if the categories in the markdown files are approved.
import pathlib
import markdown
import csv
import os


def import_approved_categories() -> list:

    category_path = '.category.csv'
    approved_categories = []

    with open(category_path, 'r') as f:

        approved_categories = csv.DictReader(f)

        for row in approved_categories:
            approved_categories = row['categories']

    return approved_categories

def check_category(file: str, approved_categories: list) -> None:

    # read the markdown file
    data = pathlib.Path(file).read_text(encoding='utf-8')
    md = markdown.Markdown(extensions=['meta'])
    md.convert(data)

    error = 0
    if ('category' in md.Meta):
        md_category = md.Meta['category'][0].split(', ')

        for category in md_category:

            if category not in approved_categories:
                print(f'{file} has an unapproved category: {category}. Please ensure the category matches the allowed categories. If needed, please raise a separate PR to update the category file.')
                error = 1

    return error
    
def main():
    approved_categories = import_approved_categories()

    # get all the markdown files from given bash command
    files = os.popen('git ls-files').read().split('\n')
    files = [file for file in files if file.endswith('.md')]

    print (f'Checking {len(files)} files')
    print ("files: " + str(files))

    error = 0

    for file in files:

        if check_category(file, approved_categories) == 1:

            error = 1
            
    exit(error)

if __name__ == '__main__':
    main()
