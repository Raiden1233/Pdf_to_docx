from pdf2docx import Converter
import multiprocessing

def pdf_to_docx(pdf_path):

    try:
        pdf_file_path_input = pdf_path

        if pdf_file_path_input.endswith(".pdf"):

            pdf_file_path_confirmed = pdf_file_path_input.replace("\\", "\\")

            docx_path = pdf_path.replace(".pdf", "")
            conv = Converter(pdf_file_path_confirmed)
            conv.convert(f"{docx_path}.docx")
            conv.close()
            
    except Exception as e:
        print(e)

def main():
    pdf_count = input("How many pdfs you want to convert? (Max 10 is recommended.)\n--> ")
    
    list_of_pdf_file_paths = []

    if pdf_count == "0":
        print("Invalid value! try again ")
        return
    
    if int(pdf_count) > 1:
        
        for i in range(int(pdf_count)):
            pdf_file_path = input("\n\nEnter the absolute path of .pdf file path\nExample path:'E:\\important.pdf'\n\n--> ") 
           # checking if the file within the path even exist.
            if pdf_file_path.endswith(".pdf") != True:
                print("HINT: The script wouldn't work properly, if you don't provide .pdf file within your all paths. ")
                break 
            list_of_pdf_file_paths.append(pdf_file_path)

            
        with multiprocessing.Pool() as p:
            p.map(pdf_to_docx, list_of_pdf_file_paths)
            print(f"\nDocument Path Confirmed: Current directory\n")
        
    else:
        one_pdf_file_path = input("Enter the absolute path of .pdf file path\nExample path:'E:\\important.pdf'\n\n--> ")
        
        if one_pdf_file_path.endswith(".pdf") != True:
            print("\nPlease provide the .pdf file only along withine the absolute path. Try again!\n")
            return
        pdf_to_docx(one_pdf_file_path)
        print(f"\nDocument Path Confirmed: Current directory\n")
if __name__ == "__main__":

    main()

