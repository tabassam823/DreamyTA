import subprocess
import sys

def get_python_pages(pdf_path, max_pages):
    python_pages = set()
    for p in range(1, max_pages + 1):
        cmd = ["pdftotext", "-f", str(p), "-l", str(p), pdf_path, "-"]
        result = subprocess.run(cmd, capture_output=True, text=True)
        text = result.stdout
        # Simple heuristics for python code
        if "import " in text and ("numpy" in text or "qiskit" in text or "def " in text or "return " in text):
            python_pages.add(p)
        elif "def " in text and "return " in text and (":" in text or "print(" in text):
            python_pages.add(p)
        elif "from " in text and " import " in text:
            python_pages.add(p)
    return python_pages

if __name__ == "__main__":
    pages = get_python_pages("main.pdf", 250)
    print("Python pages:", pages)
