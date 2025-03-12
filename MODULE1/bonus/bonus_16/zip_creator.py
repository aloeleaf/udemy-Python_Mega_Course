import zipfile
import pathlib



def make_archive(filepaths, dest_dir):
    dest_path = pathlib.WindowsPath(dest_dir, "compressed.zip" )
    with zipfile.ZipFile(dest_path, 'w') as archive:
        filepath = 
        for filepath in filepaths:
            archive.write(filepath, arcname=filepath.name)



if __name__ == "__main__":
    make_archive(filepaths=["text1.txt", "text2.txt"], dest_dir='dest')