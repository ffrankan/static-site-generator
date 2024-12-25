def markdown_to_blocks(markdown_content: str) -> list[str]:
    # Split content into lines and remove leading/trailing whitespace
    lines = [line.strip() for line in markdown_content.strip().split('\n')]
    
    blocks = []
    current_block = []
    
    for line in lines:
        # Skip empty lines between blocks
        if not line and current_block:
            blocks.append('\n'.join(current_block))
            current_block = []
            continue
        # Skip empty lines at the start
        if not line:
            continue
            
        # Check if this is a list item
        if line.startswith(('* ', '- ', '+ ')):
            # If we were building a different type of block, save it
            if current_block and not current_block[-1].startswith(('* ', '- ', '+ ')):
                blocks.append('\n'.join(current_block))
                current_block = []
            current_block.append(line)
        else:
            # If we were building a list block, save it
            if current_block and current_block[-1].startswith(('* ', '- ', '+ ')):
                blocks.append('\n'.join(current_block))
                current_block = []
            current_block.append(line)
    
    # Add the last block if there is one
    if current_block:
        blocks.append('\n'.join(current_block))
    
    return blocks

def identify_block_type(block: str) -> str:
    if block.startswith("# "):
        return "heading1"
    if block.startswith("## "):
        return "heading2"
    if block.startswith("### "):
        return "heading3"
    elif block.startswith("#### "):
        return "heading4"
    elif block.startswith("##### "):
        return "heading5"
    elif block.startswith("###### "):
        return "heading6"
    elif block.startswith("```") and block.endswith("```"):
        return "code"
    elif block.startswith(">"):
        return "quote"
    elif block.startswith("* ") or block.startswith("- "):
        return "unordered_list"
    elif block.startswith("1. "):
        return "ordered_list"
    else:
        return "paragraph"
