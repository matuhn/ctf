import zipfile
from shutil import copyfile

# copyfile(src, dst)
for i in range(1000):
	zip_ref = zipfile.ZipFile("unzip.zip", 'r')
	zip_ref.extractall("directory_to_extract_to")
	copyfile("directory_to_extract_to/unzip.zip","unzip.zip")
	zip_ref.close()