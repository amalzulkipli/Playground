from docx import Document
import re

def convert_to_superscript(text):
    def _sub(match):
        return match.group(1).replace(",", 	u'\u207b').replace("-", "⁻").replace(" ", "").translate(str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹"))
    
    return re.sub(r"\[(.*?)\]", _sub, text)

def main(input_file, output_file):
    doc = Document(input_file)

    for paragraph in doc.paragraphs:
        paragraph.text = convert_to_superscript(paragraph.text)

    doc.save(output_file)

if __name__ == "__main__":
    input_file = "/Users/admin/Projects/Data Exploration/Playground/Scoping_Review_Text_Only.docx"
    output_file = "/Users/admin/Projects/Data Exploration/Playground/Output.docx"
    main(input_file, output_file)