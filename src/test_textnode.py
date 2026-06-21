import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_text_not_eq(self):
        node = TextNode("Testy", TextType.BOLD)
        node2 = TextNode("Testier", TextType.BOLD)
        self.assertNotEqual(node, node2)
    def test_type_not_eq(self):
        node = TextNode("Testy", TextType.BOLD)
        node2 = TextNode("Testy", TextType.LINK)
        self.assertNotEqual(node, node2)
    def test_url_not_eq(self):
        node = TextNode("Testy", TextType.BOLD, "Hello.com")
        node2 = TextNode("Testy", TextType.BOLD, "Hey.com")
        self.assertNotEqual(node, node2)
    def test_url_none(self):
        node = TextNode("Testy", TextType.BOLD, "aurl.com")
        node2 = TextNode("Testy", TextType.BOLD)
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()
