import textnode as tn

def main(text: str, text_type: str, url=None):
   text_node = tn.TextNode(text, text_type, url)
   print(text_node)

if __name__ == "__main__":
    main("testing", "link", "helloworld.com")


