import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
        node = LeafNode("p", "Hello, world!", {"class": "red-box", "id": "first"})
        self.assertEqual(node.to_html(), '<p class="red-box" id="first">Hello, world!</p>')
        node = LeafNode(None, "empty tag")
        self.assertEqual(node.to_html(), "empty tag")
    
    def test_error(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()




if __name__ == "__main__":
    unittest.main()