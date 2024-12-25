import os
import shutil
from src.markdown_parser import generate_page

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    """
    Recursively generate HTML pages from markdown files while maintaining directory structure
    """
    # Walk through all directories and files in content directory
    for root, dirs, files in os.walk(dir_path_content):
        # Calculate the relative path to maintain directory structure
        rel_path = os.path.relpath(root, dir_path_content)
        dest_path = os.path.join(dest_dir_path, rel_path)
        
        # Create destination directory if it doesn't exist
        os.makedirs(dest_path, exist_ok=True)
        
        # Process each markdown file
        for file in files:
            if file.endswith('.md'):
                # Generate paths
                md_path = os.path.join(root, file)
                html_filename = os.path.splitext(file)[0] + '.html'
                html_path = os.path.join(dest_path, html_filename)
                
                # Generate the HTML page using existing generate_page function
                generate_page(
                    from_path=md_path,
                    template_path=template_path,
                    dest_path=html_path
                )

def main():
    # Delete public directory and its contents if it exists
    if os.path.exists("public"):
        shutil.rmtree("public")
    
    # Create new public directory
    os.makedirs("public")
    
    # Copy static files to public
    if os.path.exists("static"):
        for item in os.listdir("static"):
            source = os.path.join("static", item)
            destination = os.path.join("public", item)
            if os.path.isfile(source):
                shutil.copy2(source, destination)
            else:
                shutil.copytree(source, destination)
    
    # Generate all pages recursively
    generate_pages_recursive(
        dir_path_content="content",
        template_path="template.html",
        dest_dir_path="public"
    )

if __name__ == "__main__":
    main() 