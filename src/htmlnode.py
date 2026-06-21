import textwrap

class HTMLNode:
    def __init__(
        self, 
        tag: str | None = None, 
        value: str | None=None, 
        children: list["HTMLNode"] | None = None,
        props: dict[str, str] | None = None
    ) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    def to_html(self):
        raise NotImplementedError
    def props_to_html(self):
        string = ""
        if self.props:
            for prop in self.props.keys():
                string += f' {prop}="{self.props[prop]}"'
        return string
    def __repr__(self):
        return textwrap.dedent(f"""Tag:{self.tag}\nValue:{self.value}\nChildren:{repr(self.children)}\nProps:{self.props_to_html()}""")

class LeafNode(HTMLNode):
    def __init__(self, tag: str | None, value: str, props: dict[str, str] | None = None
    ) -> None:
        super().__init__(tag, value, None, props)
    def to_html(self):
        if self.value is None:
            raise ValueError
        if self.tag is None:
            return self.value
        elif not self.props:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    def __repr__(self):
        return textwrap.dedent(f"""Tag:{self.tag}\nValue:{self.value}\nProps:{self.props_to_html()}""")

class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list[HTMLNode], props=None):
        super().__init__(tag, None, children)
    def to_html(self):
        if self.children is None:
            raise ValueError("Child nodes not found")
        if self.tag is None:
            raise ValueError("Tag not found")
        return f"<{self.tag}>{"".join(child.to_html() for child in self.children)}</{self.tag}>"

