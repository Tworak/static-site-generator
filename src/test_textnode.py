import unittest
from textnode import TextNode, TextType
from htmlnode import LeafNode, HTMLNode

class TestTextNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)


    def test_url(self):
        url = TextNode("www.vg.no", TextType.LINK)
        url2 = TextNode("www.vg.no", TextType.LINK)
        self.assertEqual(url, url2)


    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This not is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)   # passes if they are NOT equal
    

    def test_url_not_equal(self):
        url = TextNode("www.vg.no", TextType.LINK)
        url2 = TextNode("www.nrk.no", TextType.LINK)
        self.assertNotEqual(url, url2)


class TestLeafNode(unittest.TestCase):
    def test_node(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_tag_link(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')


if __name__ == "__main__":
    unittest.main()
