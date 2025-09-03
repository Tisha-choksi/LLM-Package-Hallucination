import markdown

def convert_markdown_to_html(markdown_text):
    html = markdown.markdown(markdown_text)
    return html

if __name__ == "__main__":
    md_text = """
# Hello World

This is a sample Markdown text.

- Item 1
- Item 2
- Item 3
"""
    html_output = convert_markdown_to_html(md_text)
    print("Converted HTML:")
    print(html_output)
