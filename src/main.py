from textnode import TextNode, TextType

def main():
    # Create a dummy node
    node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    # Print it to trigger the __repr__ method
    print(node)

# Call the main function
main()
