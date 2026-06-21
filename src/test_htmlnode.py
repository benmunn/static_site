import unittest
import textwrap
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", "check",None, {"href": "wow.com", "alt_text":"wowdude"})
        text_node = textwrap.dedent(
        '''Tag:p
Value:check
Children:None
Props: href="wow.com" alt_text="wowdude"''')
        self.assertEqual(repr(node), text_node)
    def test_eq2(self):
        node = HTMLNode("p", None,HTMLNode("l", "hi"), None)
        text_node = textwrap.dedent('''Tag:p\nValue:None\nChildren:Tag:l\nValue:hi\nChildren:None\nProps:\nProps:''')
        self.assertEqual(repr(node), text_node)


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        text_node = "<p>Hello, world!</p>"
        self.assertEqual(node.to_html(), text_node)
    def test_leaf_to_html_h(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        text_node = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(node.to_html(), text_node)
    def test_leaf_to_html_raw(self):
        node = LeafNode(None, "Hi")
        text_node = 'Hi'
        self.assertEqual(node.to_html(), text_node)
    def test_leaf_to_html_raw(self):
        node = LeafNode(None, "Hi")
        text_node = 'Hi'
        self.assertEqual(node.to_html(), text_node)
    def test_leaf_to_html_noval(self):
        with self.assertRaises(ValueError):
            node = LeafNode("p", None)
            node.to_html()
    def test_leaf_to_html_raw(self):
        node = LeafNode(None, "Hi")
        text_node = 'Tag:None\nValue:Hi\nProps:'
        self.assertEqual(repr(node), text_node)
 
class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")
    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(),"<div><span><b>grandchild</b></span></div>")
    def test_to_html_with_no_children(self):
        with self.assertRaises(ValueError):
            node = ParentNode("p", None)
            node.to_html()
    def test_to_html_with_children_prop(self):
        child_node = LeafNode("span", "child", {"href":"lol.com"})
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), '<div><span href="lol.com">child</span></div>')
    def test_to_html_with_grandchildren(self):
        grandchild_node1 = LeafNode("b", "grandchild")
        grandchild_node2 = LeafNode("p", "life is fun", {"style":"cool"})
        child_node = ParentNode("span", [grandchild_node1, grandchild_node2])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            '<div><span><b>grandchild</b><p style="cool">life is fun</p></span></div>',
        )

