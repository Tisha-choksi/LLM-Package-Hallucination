import markdown2
from xhtml2pdf import pisa

def convert_markdown_to_pdf(md_file, pdf_file):
    with open(md_file, 'r') as f:
        md_content = f.read()
    
    html = markdown2.markdown(md_content)
    with open(pdf_file, 'w+b') as f:
        pisa.CreatePDF(html, dest=f)

if __name__ == "__main__":
    md_file = input("Enter the Markdown file path: ")
    pdf_file = input("Enter the output PDF file path: ")
    convert_markdown_to_pdf(md_file, pdf_file)
    print(f"Converted {md_file} to {pdf_file}")
