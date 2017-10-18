import ftplib
import os
def upload(ftp, file):
    ext = os.path.splitext(file)[1]
    ftp.cwd('/jacknorthrup.com/')    
    if ext in (".txt", ".htm", ".html",".ipynb"):
        ftp.storlines("STOR " + file, open(file))
    else:
        ftp.storbinary("STOR " + file, open(file, "rb"), 1024)