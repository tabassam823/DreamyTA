import subprocess
import re
import sys
import os

def get_pdf_info(pdf_path):
    if not os.path.exists(pdf_path):
        return 0
    result = subprocess.run(["pdfinfo", pdf_path], capture_output=True, text=True)
    max_pages = 0
    for line in result.stdout.splitlines():
        if line.startswith("Pages:"):
            max_pages = int(line.split(":")[1].strip())
    return max_pages

def get_pages_with_images(pdf_path):
    cmd = ["pdfimages", "-list", pdf_path]
    result = subprocess.run(cmd, capture_output=True, text=True)
    pages = set()
    for line in result.stdout.splitlines():
        match = re.match(r"^\s*(\d+)", line)
        if match:
            pages.add(int(match.group(1)))
    return pages

def get_python_pages(pdf_path, max_pages):
    print("Mencari halaman dengan kode Python...")
    python_pages = set()
    for p in range(1, max_pages + 1):
        cmd = ["pdftotext", "-f", str(p), "-l", str(p), pdf_path, "-"]
        result = subprocess.run(cmd, capture_output=True, text=True)
        text = result.stdout
        # Deteksi heuristik untuk kode Python
        if "import " in text and ("numpy" in text or "qiskit" in text or "def " in text or "return " in text):
            python_pages.add(p)
        elif "def " in text and "return " in text and (":" in text or "print(" in text):
            python_pages.add(p)
        elif "from " in text and " import " in text:
            python_pages.add(p)
        elif "plt." in text or "np." in text or "pd." in text:
            python_pages.add(p)
    print(f"Ditemukan {len(python_pages)} halaman dengan kode Python.")
    return python_pages

def main():
    pdf_path = "main.pdf"
    max_pages = get_pdf_info(pdf_path)
    if max_pages == 0:
        print(f"Error: {pdf_path} not found or empty.")
        sys.exit(1)
        
    image_pages = get_pages_with_images(pdf_path)
    python_pages = get_python_pages(pdf_path, max_pages)
    
    # Gabungkan halaman gambar dan halaman python
    element_pages = image_pages.union(python_pages)
    
    # Tambahan manual untuk memastikan halaman tertentu masuk
    element_pages.update([39, 51, 101, 102])
    
    # Aturan baru:
    # 1. jika elemen berwarna ada di halaman genap, maka masukkan halaman ganjil sebelumnya (p - 1)
    # 2. jika elemen berwarna ada di halaman ganjil, maka masukkan halaman genap setelahnya (p + 1)
    color_set = set()
    for p in element_pages:
        color_set.add(p)
        if p % 2 == 0: # Genap (Even)
            if p - 1 >= 1:
                color_set.add(p - 1)
        else: # Ganjil (Odd)
            if p + 1 <= max_pages:
                color_set.add(p + 1)
    
    # Explicit exclusions requested by user
    # Document labels: iii (9), 1 (65), 6 (129), 35 (177)
    # Note: 45, 46, 63, 64, 65, 66 excluded per user request.
    explicit_exclude = {9, 45, 46, 63, 64, 65, 66, 129, 177}
    color_set = color_set - explicit_exclude
            
    color_pages = sorted(list(color_set))
    nocolor_pages = [p for p in range(1, max_pages + 1) if p not in color_set]
    
    def run_gs(pages, output_file):
        if not pages:
            print(f"No pages for {output_file}, skipping.")
            return
        page_list = ",".join(map(str, pages))
        cmd = [
            "gs", "-sDEVICE=pdfwrite", "-dNOPAUSE", "-dBATCH", "-dSAFER",
            f"-sPageList={page_list}",
            f"-sOutputFile={output_file}",
            pdf_path
        ]
        subprocess.run(cmd, capture_output=True)

    print(f"Splitting PDF ({max_pages} pages)...")
    run_gs(color_pages, "main_color.pdf")
    run_gs(nocolor_pages, "main_nocolor.pdf")
    print(f"Success: Created main_color.pdf ({len(color_pages)} pages) and main_nocolor.pdf ({len(nocolor_pages)} pages).")

if __name__ == "__main__":
    main()
