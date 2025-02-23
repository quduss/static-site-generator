from textnode import TextType, TextNode

def main():
    node = TextNode("This is a bold text", TextType.BOLD)
    print(node)

if __name__ == "__main__":
    main()