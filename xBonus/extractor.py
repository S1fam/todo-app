import zipfile
import pathlib


def extract_zip_file(zip_path, extract_path):
    dest_path = pathlib.Path(extract_path, zip_path.split('/')[-1])
    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(dest_path)


if __name__ == "__main__":
    extract_zip_file(zip_path='C:/Users/jerxy/Desktop/compressed.zip',
                     extract_path='C:/Users/jerxy/Desktop/Extrahovane')
