import zipfile


def extract_archieve(archevepath, dest_path):
    with zipfile.ZipFile(archevepath, "r") as archieve:
        archieve.extractall(dest_path)
