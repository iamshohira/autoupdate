from urllib import request
from zipfile import ZipFile
import shutil, os
from os.path import join as pj

git_dl_url = "https://github.com/iamshohira/autoupdate/archive/refs/heads/master.zip"
folder = "autoupdate-master"
dl_zip = "dl.zip"
exe_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(exe_dir)

path_zip = pj(parent_dir, dl_zip)
path_extract = pj(parent_dir, folder)
with request.urlopen(git_dl_url) as df:
    data = df.read()
    with open(path_zip, "wb") as f:
        f.write(data)

with ZipFile(path_zip) as zp:
    zp.extractall(parent_dir)

shutil.rmtree(exe_dir)
shutil.move(path_extract, exe_dir)

# os.remove("./tmp.zip")
# os.removedirs(folder)