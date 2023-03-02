#import pypandoc
import os
import pdfplumber


def save_file(filepath, content):
    with open(filepath, 'w', encoding='ASCII') as outfile:
        outfile.write(content)

#convert many .DocX to TXTs
def convert_docx2txt(src_dir, dest_dir):
    files = os.listdir(src_dir)
    files = [i for i in files if '.docx' in i]
    for file in files:
        try:
            pypandoc.convert_file(src_dir+file, 'plain', outputfile=dest_dir+file.replace('.docx','.txt'))
        except Exception as oops:
            print(oops, file)
            
#convert many PDFs to TXTs
def convert_pdf2txt(src_dir, dest_dir):
    files = os.listdir(src_dir)
    files = [i for i in files if '.pdf' in i]
    for file in files:
        try:
            with pdfplumber.open(src_dir+file) as pdf:
                output = ''
                for page in pdf.pages:
                    output += page.extract_text()
                    output += '\n\nNEW PAGE\n\n'  # change this for your page demarcation
                save_file(dest_dir+file.replace('.pdf','.txt'), output.strip())
        except Exception as oops:
            print(oops, file)

#Convert Single TXT to Single PDF
def convert_txt_to_pdf(pdf_path, txt_path):
    # Extract text from PDF using pdfplumber
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    
    # Convert extracted text to plain text format using pypandoc
    pypandoc.convert_text(text, "plain", format="md", outputfile=txt_path)
    
    print(f"PDF file '{pdf_path}' converted to TXT file '{txt_path}'")

#Convert Single PDF to Single TXT
def convert_pdf_to_txt(pdf_path, txt_path):
    # Extract text from PDF using pdfplumber
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    
    # Save extracted text to TXT file
    with open(txt_path, 'w', encoding='UTF-8') as outfile:
        outfile.write(text.strip())
    
    print(f"PDF file '{pdf_path}' converted to TXT file '{txt_path}'")

#if __name__ == '__main__':
    #convert_docx2txt('docx/', 'converted/')
 #   convert_pdf2txt('PDFs/', 'converted/')