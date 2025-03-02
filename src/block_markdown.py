def markdown_to_blocks(markdown):
    blocks = list(map(lambda block: block.strip(), markdown.split('\n\n')))
    new_blocks = []
    for block in blocks:
        if block != '':
            new_blocks.append(block)
    return new_blocks