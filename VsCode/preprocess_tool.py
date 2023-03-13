

#File named preprocess_tool.pyimport fpdf
import re
from nltk.corpus import stopwords
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
import converter

#nltk.download('stopwords')


# Prompt the user to input the location and name of the PDF file
input_file = "/Users/yanni/Downloads/accounting.pdf"

#where should we put the new txt?
output_file = "/Users/yanni/Documents/GitHub/ChatGpt-DataCleaning/VsCode/output/accounting.txt"

# where should we put the post processed pdf?
output_directory = "/Users/yanni/Documents/GitHub/ChatGpt-DataCleaning/VsCode/output/accountingOutput.pdf"

txt_2_pdf_output_directory_filename = "/Users/yanni/Documents/GitHub/ChatGpt-DataCleaning/VsCode/output/output.pdf"



#convert PDF file into a TXT file
converter.convert_pdf_to_txt(input_file,output_file)


print("----------Begin Cleaning of Output--------------")
text = None 

with open(f"{output_file}", "r", encoding='utf-8') as file:
    text = file.read()

with open(f"{output_file}","w", encoding='utf-8') as outfile:
     #remove newlines
    text = re.sub('\n', ' ', text)
    # Remove interpuncts
    text = re.sub('[^\w\s]', '', text)
    #remove extra whitespace
    text = re.sub('\s+',' ', text).strip()

    #create a list with each new element determined by a new whitespace
    words = text.split()

    #remove symbols and numbers
    alphabetic_only = [word for word in words if word.isalpha()]

    #remove uppercase
    lower_case_only = [word.lower() for word in alphabetic_only]

    #remove stopwords
    stopwords_nltk = set(stopwords.words('english'))

    cleaned_words = [word for word in lower_case_only if word not in stopwords_nltk]

    outfile.write(' '.join(cleaned_words))

file = open(output_file)
output_file_text = file.read()
file.close()
converter.convert_txt_to_pdf(output_file_text, output_directory)
print("----------COMPLETED Cleaning of Output--------------")



