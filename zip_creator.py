import zipfile
import os


def make_archive(filepaths, folder):
    zip_filename = f"{folder}/compressed.zip"
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        for filepath in filepaths:
            zipf.write(filepath, arcname=os.path.basename(filepath))
    return zip_filename

if __name__=="__main__":
    make_archive(filepaths=["gui.py","demo.py"], folder=".")