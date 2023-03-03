#File named preprocess_tool.py

import re
from nltk.corpus import stopwords
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
import converter

#nltk.download('stopwords')


# Prompt the user to input the location and name of the PDF file
input_file = "/Users/yanni/Downloads/CopperRiverManagement.pdf"

# input('Enter the location and name of the PDF file to preprocess: ')
output_file = "/Users/yanni/Documents/GitHub/ChatGpt-DataCleaning/VsCode/output/output.txt"

#convert PDF file into a TXT file
converter.convert_pdf_to_txt(input_file,output_file)

print("----------Begin Cleaning of Output--------------")
text = None 

with open(f"/Users/yanni/Documents/GitHub/ChatGpt-DataCleaning/VsCode/output/output.txt", "r") as file:
    text = file.read()

with open(f"/Users/yanni/Documents/GitHub/ChatGpt-DataCleaning/VsCode/output/output.txt","w") as outfile:
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


print("----------COMPLETED Cleaning of Output--------------")



