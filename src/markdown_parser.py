# Extract the title from the markdown file
from src.block_parser import identify_block_type, markdown_to_blocks
from src.leafnode import LeafNode
from src.parent_node import ParentNode
from src.node_parser import CompositeNodeParser, NodeParser
from src.textnode import TextType, text_node_to_html_node
import os

def markdown_to_html(markdown: str) -> ParentNode:
    blocks = markdown_to_blocks(markdown)

    html_nodes = []
    for block in blocks:
        block_type = identify_block_type(block)
        html_nodes.append(create_html_node(block_type, block))
    return ParentNode("div", html_nodes)

def text_to_html(text: str) -> str:
    # 使用 CompositeNodeParser 来处理内联样式
    parser = CompositeNodeParser([
        NodeParser(TextType.BOLD),
        NodeParser(TextType.ITALIC),
        NodeParser(TextType.CODE),
        NodeParser(TextType.LINK),
        NodeParser(TextType.IMAGE)
    ])
    
    # 解析文本节点
    nodes = parser.parse(text)
    
    # 将文本节点转换为HTML
    return "".join([text_node_to_html_node(node).to_html() for node in nodes])

def create_html_node(block_type, block):
    if block_type == "heading1":
        return LeafNode("h1", text_to_html(block.lstrip("# ")))
    elif block_type == "heading2":
        return LeafNode("h2", text_to_html(block.lstrip("## ")))
    elif block_type == "heading3":
        return LeafNode("h3", text_to_html(block.lstrip("### ")))
    elif block_type == "heading4":
        return LeafNode("h4", text_to_html(block.lstrip("#### ")))
    elif block_type == "heading5":
        return LeafNode("h5", text_to_html(block.lstrip("##### ")))
    elif block_type == "heading6":
        return LeafNode("h6", text_to_html(block.lstrip("###### ")))
    elif block_type == "code":
        return LeafNode("code", block.strip("```"))
    elif block_type == "quote":
        return LeafNode("blockquote", text_to_html(block.lstrip("> ")))
    elif block_type == "unordered_list":
        children = []
        for item in block.split("\n"):
            if item:
                children.append(LeafNode("li", text_to_html(item.lstrip("* "))))
        return ParentNode("ul", children)
    elif block_type == "ordered_list":
        children = []
        items = block.split("\n")
        for i in range(len(items)):
            item = items[i]
            if item:
                children.append(LeafNode("li", text_to_html(item.lstrip(f"{i+1}. "))))
        return ParentNode("ol", children)
    else:
        return LeafNode("p", text_to_html(block))

def extract_title(markdown: str) -> str:
    lines = markdown.split('\n')
    for line in lines:
        line = line.strip()
        if line.startswith("# ") and not line.startswith("## "):
            return line.lstrip("#").strip()
    raise ValueError("No h1 header found in markdown file")

def generate_page(from_path: str, template_path: str, dest_path: str) -> None:
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    # Read markdown file
    with open(from_path, 'r') as f:
        markdown_content = f.read()
    
    # Read template file
    with open(template_path, 'r') as f:
        template_content = f.read()
    
    # Convert markdown to HTML and extract title
    html_node = markdown_to_html(markdown_content)
    html_content = html_node.to_html()
    title = extract_title(markdown_content)
    
    # Replace placeholders in template
    final_html = template_content.replace("{{ Title }}", title)
    final_html = final_html.replace("{{ Content }}", html_content)
    
    # Create destination directory if it doesn't exist
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    
    # Write the final HTML to destination
    with open(dest_path, 'w') as f:
        f.write(final_html)
