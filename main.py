import spacy
import pypdf
import argparse
import os

if __name__ == "__main__":
    
    nlp = spacy.load("model-best")

    parser = argparse.ArgumentParser()
    parser.add_argument('--file_path', type=str, required=True)
    args = parser.parse_args()
    
    if not os.path.exists(args.file_path):
        raise ValueError("File path does not exist")
    else:    

        file_path = args.file_path
            
        with open(file_path, 'rb') as f:
            pdf = pypdf.PdfReader(f)

            # get the first page
            page = pdf.pages[0]

            # extract text from page
            text = page.extract_text()

            doc = nlp(text)
            print(doc.ents[0])