import fitz
from docx import Document


class FileService:

    # method to extract pdf content
    def extract_pdf_content(self, path):
        _text = ""
        _pdf = fitz.open(path)
        for _page in _pdf:
            _text += _page.get_text()
        return _text
    
    # method to extract doc content
    def extract_doc_content(self, path):
        _doc = Document(path)
        _text = "\n".join([_p.text for _p in _doc.paragraphs])
        return _text

    # method to extract text file content
    def extract_txt_content(self, path):
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()

    # main method to extract file contents
    def extract_file_contentt(self, path):
        if path.endswith(".pdf"):
            return self.extract_pdf_content(path)

        elif path.endswith(".docx"):
            return self.extract_doc_content(path)

        elif path.endswith(".txt"):
            return self.extract_txt_content(path)

        else:
            return "File not supported"
        
"""
_file_name = "Kalanadhabhatta-PervasiveHealth2021-Camera.pdf"
_file_path = "C:/Users/AYUSH/Downloads/Kalanadhabhatta-PervasiveHealth2021-Camera (3).pdf"
_content = FileService().extract_file_contentt(_file_path)
print("content is:", _content)
"""