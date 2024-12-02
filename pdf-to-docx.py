

from pdf2docx import Converter
import time

def main(pdf_path, docx_path):


    pdf_file_path_input = pdf_path

    if pdf_file_path_input.endswith(".pdf"):

        pdf_file_path_confirmed = pdf_file_path_input.replace("\\", "\\")

        
        docx_custome_file_path = docx_path
         
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
    


    pdf_count = input("How many pdfs you want to convert? (Max 10 is recommended.)\n--> ")
    
    list_of_pdf_file_paths = []
    list_of_docx_file_paths = []

    if int(pdf_count) > 1:
        try:
            for i in range(int(pdf_count)):
            
                pdf_file_path = input("Enter the absolute path of .pdf file path\nExample path:'E:\\important.pdf'\n\n--> ") 
    
               # checking if the file within the path even exist.
                if pdf_file_path.endswith(".pdf"):
                    
                    

                    list_of_pdf_file_paths.append(pdf_file_path)
        
                    document_path = input("\nEnter the absolute path for docx file\nExample path: 'D:\\document .docx' (if drive letter is not specified, current directory will be a path)\n--> ")
        
                    list_of_docx_file_paths.append(document_path)
                else:
                    print("\nPlease provide the .pdf file within the absolute path. Try again!\n")
                    break

            for i in range(int(pdf_count)):
                main(list_of_pdf_file_paths[i], list_of_docx_file_paths[i])

        except:
            print("HINT: The script wouldn't work properly, if you don't provide .pdf file within your path.")
    else:
        try:
 
            one_pdf_file_path = input("Enter the absolute path of .pdf file path\nExample path:'E:\\important.pdf'\n\n--> ")
            
            if one_pdf_file_path.endswith(".pdf"):

                one_document_path = input("\nEnter the absolute path for docx file\nExample path: 'D:\\document .docx' (if drive letter is not specified, current directory will be a path)\n--> ")
            else:
                print("\nPlease provide the .pdf file along withine the absolute path. Try again!\n")
                

            main(one_pdf_file_path, one_document_path)
        except:
            print("\nHINT: The script wouldn't work properly, if you don't provide .pdf file within your path.")

