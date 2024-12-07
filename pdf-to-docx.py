from pdf2docx import Converter

def main(pdf_path):

    pdf_file_path_input = pdf_path

    if pdf_file_path_input.endswith(".pdf"):

        pdf_file_path_confirmed = pdf_file_path_input.replace("\\", "\\")

        docx_path = pdf_path.replace(".pdf", "")
        print(f"\nDocument Path Confirmed: Current directory\n")
        conv = Converter(pdf_file_path_confirmed)
        conv.convert(f"{docx_path}.docx")
        conv.close()

if __name__ == "__main__":

    pdf_count = input("How many pdfs you want to convert? (Max 10 conversion at a time is recommended.)\n--> ")
    
    list_of_pdf_file_paths = []

    if int(pdf_count) > 1:
        try:
            for i in range(int(pdf_count)):
                pdf_file_path = input("\n\nEnter the absolute path of .pdf file path\nExample path:'E:\\important.pdf'\n\n--> ") 
               # checking if the file within the path even exist.
                if pdf_file_path.endswith(".pdf"):
                    list_of_pdf_file_paths.append(pdf_file_path)
                else:
                    break
            for i in range(int(pdf_count)):
                main(list_of_pdf_file_paths[i])
        except:
            print("HINT: The script wouldn't work properly, if you don't provide .pdf file within your all paths. ")
    else:
        one_pdf_file_path = input("Enter the absolute path of .pdf file path\nExample path:'E:\\important.pdf'\n\n--> ")
        
        if one_pdf_file_path.endswith(".pdf") != True:
            print("\nPlease provide the .pdf file only along withine the absolute path. Try again!\n")
        else:
            main(one_pdf_file_path)
