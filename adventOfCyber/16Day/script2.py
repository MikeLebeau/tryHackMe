import os
import exiftool

m_count = 0
file = []

# Read all the metadata in decom2 and scan for 'version 1.1' metadata
ListFile = os.listdir('./')
for l in ListFile:
        file.append(l)

with exiftool.ExifTool() as et:
        metadata = et.get_metadata_batch(file)
for d in metadata:
        try:
                if(d[u'XMP:Version']):
                        m_count = m_count + 1
        except:
                continue

print("Number of files in version 1.1: " + str(m_count))
