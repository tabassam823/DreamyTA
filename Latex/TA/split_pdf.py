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

def main():
    pdf_path = "main.pdf"
    max_pages = get_pdf_info(pdf_path)
    if max_pages == 0:
        print(f"Error: {pdf_path} not found or empty.")
        sys.exit(1)
        
    image_pages = get_pages_with_images(pdf_path)
    
    # Base rules: 
    # 1. Page with image
    # 2. If odd, include p+1
    # 3. If even, include p-1 and p-3
    color_set = set()
    for p in image_pages:
        color_set.add(p)
        if p % 2 != 0: # Ganjil (Odd)
            if p + 1 <= max_pages:
                color_set.add(p + 1)
        else: # Genap (Even)
            if p - 1 >= 1:
                color_set.add(p - 1)
            if p - 3 >= 1:
                color_set.add(p - 3)
    
    # Explicit exclusions requested by user
    # Document labels: iii (5), xviii (47), 1 (61), 6 (125), 35 (173)
    explicit_exclude = {5, 47, 61, 125, 173}
    color_set = color_set - explicit_exclude
    
    # Accompanied odd page rule:
    # If an odd page is in color_set, it MUST have the next even page in color_set.
    final_color_set = set()
    for p in sorted(list(color_set)):
        if p % 2 != 0: # Ganjil
            if (p + 1) in color_set:
                final_color_set.add(p)
        else: # Genap
            final_color_set.add(p)
            
    color_pages = sorted(list(final_color_set))
    nocolor_pages = [p for p in range(1, max_pages + 1) if p not in final_color_set]
    
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
