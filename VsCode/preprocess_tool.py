
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

with open(f"/Users/yanni/Documents/GitHub/ChatGpt-DataCleaning/VsCode/output/output.txt") as file:
    text = file.read()

#create a list with each new element determined by a new whitespace
words = text.split()

#remove symbols and numbers
alphabetic_only = [word for word in words if word.isalpha()]

#remove uppercase
lower_case_only = [word.lower() for word in alphabetic_only]

#remove stopwords
stopwords_nltk = set(stopwords.words('english'))

cleaned_words = [word for word in lower_case_only if word not in stopwords_nltk]





