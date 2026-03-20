from PyPDF2 import PdfReader

def extract_text(file):
    try:
        reader = PdfReader(file)
        text = ""

        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + " "

        text = text.strip()

        # 🔥 IMPORTANT: handle empty text
        if not text:
            print("⚠️ No extractable text found in PDF")
            return ""

        return text

    except Exception as e:
        print("PDF Error:", e)
        return ""