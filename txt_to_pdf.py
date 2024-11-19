from fpdf import FPDF
import os

def txt_to_pdf(txt_file, pdf_file):
    
    if not os.path.exists(txt_file):
        print(f"The file {txt_file} does not exist.")
        return
    
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)
    
    with open(txt_file, 'r', encoding='utf-8') as file:
        for line in file:
            pdf.multi_cell(0, 10, line)
    
    pdf.output(pdf_file)
    print(f"Converted {txt_file} to {pdf_file} successfully.")

if __name__ == "__main__":
    # change input_txt target to txt-file.
    # change output_pdf target to where you want pdf-file to be created.
    input_txt = "C:/Users/YourUsername/Documents/sample.txt"
    output_pdf = "C:/Users/YourUsername/Documents/sample.pdf"
    
    txt_to_pdf(input_txt, output_pdf)
