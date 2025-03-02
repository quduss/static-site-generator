from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    OLIST = "ordered_list"
    ULIST = "unordered_list"

def markdown_to_blocks(markdown):
    blocks = list(map(lambda block: block.strip(), markdown.split('\n\n')))
    new_blocks = []
    for block in blocks:
        if block != '':
            new_blocks.append(block)
    return new_blocks