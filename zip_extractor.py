import zipfile
import os


def extract_archive(filepath, dest_dir):
    with zipfile.ZipFile(filepath, 'r') as zipf:
        zipf.extractall(dest_dir)
    
    
if __name__== '__main__':
    extract_archive("./temporary/compressed.zip", "./temporary/extracted_files")
      
    