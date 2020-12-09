import zipfile
import exiftool
import os

EXIFTOOL_PATH = '/usr/bin/exiftool'

# 1 - extract all the files in the archives
# 2 - extract metadata from the files
# 3 - extract text from files

# print("lol")

def extractFiles(nameFile):
  print("\t[+] Extract file: " + nameFile)
  with zipfile.ZipFile(nameFile, 'r') as zipRef:
    zipRef.extractall("./")

def extractMetaData():
  for item in os.listdir():
    if item[-3:] == "zip":
      extractFiles(item)
    else:
      with exiftool.ExifTool() as exif:
        meta = exif.get_metadata_batch(item)

        print("[+] Extract text")
        extractText(meta)

def extractText(file):
  with open(file, 'r') as reader:
    print(reader.readlines())

print("[+] Extract files")
extractFiles("./final-final-compressed.zip")

print("[+] Extract metadatas")
extractMetaData()