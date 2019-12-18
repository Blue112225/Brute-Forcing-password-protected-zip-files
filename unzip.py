import zipfile

def extractFile(zip_file, password):
    try:
        zip_file.extractall(pwd=bytes(password,'utf-8'))
        return True
    except KeyboardInterrupt:
        exit()
    except Exception as e:
        pass

zipfilename = str(input("Zip file to crack: "))
zip_file = zipfile.ZipFile(zipfilename)

wordlist = str(input("Wordlist to use: "))
with open(wordlist) as fil:
    words = fil.read().split("\n")

for w in words:
    if extractFile(zip_file,w):
        print("Password found: "+w+"\nFiles have been extracted.")
        exit()

print('Password not found.')

