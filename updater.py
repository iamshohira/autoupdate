from urllib import request
from zipfile import ZipFile
import shutil, os

file_url = "https://github.com/iamshohira/p4LoLZCPKET2VE7VskPMTwVKYwh8QiEkfTzEYgyb6A7TPcCiee/archive/refs/heads/master.zip"
folder = "./p4LoLZCPKET2VE7VskPMTwVKYwh8QiEkfTzEYgyb6A7TPcCiee-master"
with request.urlopen(file_url) as df:
    data = df.read()
    with open("./tmp.zip","wb") as f:
        f.write(data)

with ZipFile("./tmp.zip") as zp:
    zp.extractall("./")

for p in os.listdir(folder):
    print(p)
    shutil.move(os.path.join(folder,p),"./")

os.remove("./tmp.zip")
os.removedirs(folder)