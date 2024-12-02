# print((6*10)+(10+10))

from pdf2docx import Converter
import time

def main():

    pdf_file_path_input = input("Enter the pdf file path\nExample path:'E:\\important.pdf'\n\n--> ")

    if pdf_file_path_input.endswith(".pdf"):

        pdf_file_path_confirmed = pdf_file_path_input.replace("\\", "\\")

        confirmation_for_docx_filename = input("Do you want to give custome name for docx file? yes|no --> ")

        if confirmation_for_docx_filename != 'yes':
        
            print("\ncontinuing with default option..\n")
            print(f"Path: {pdf_file_path_confirmed.replace('.pdf', '.docx')}\n")
            time.sleep(2)

            docx_file_path = pdf_file_path_confirmed
            docx_file_path_conf = docx_file_path.replace(".pdf", ".docx")
            conv = Converter(pdf_file_path_confirmed)
            conv.convert(docx_file_path_conf)
            conv.close()
        else:

            docx_custome_file_path = input("Enter the docx file path\n Example path: 'D:\\document.docx'\n --> ")
        
         
            if docx_custome_file_path.endswith(".docx") != True:
           
            
                docx_custome_file_path_fixed = docx_custome_file_path + ".docx"
                print(f"\nPath confirmed! \nPath: {docx_custome_file_path_fixed}")

                time.sleep(2)

            
                conv = Converter(pdf_file_path_confirmed)
                conv.convert(docx_custome_file_path_fixed)
                conv.close()
            else:

                print(f"\nPATH CONFIRMED:\nPath: {docx_custome_file_path}\n")
            
            
                time.sleep(1)
                docx_file_path = docx_custome_file_path
                conv = Converter(pdf_file_path_confirmed)
                conv.convert(docx_custome_file_path)
                conv.close()

    
    else:
        print("Enter absolute file path, .pdf file isn't captured. TRY AGAIN!") 


if __name__ == "__main__":
    main()
