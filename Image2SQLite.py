import sqlite3
import os.path
from os import listdir, getcwd
from IPython.core.display import Image 

def getImage_list(rel_path):
    abs_path = os.path.join(os.getcwd(),rel_path)
    print 'abs_path =', abs_path
    dir_files = os.listdir(abs_path)
    return dir_files

def create_or_open_db(dbname):
    db_is_new = not os.path.exists(db_file)
    conn = sqlite3.connect(db_file)
    if db_is_new:
        print 'Creating schema'
        sql = '''create table if not exists images(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        image BLOB,
        TYPE TEXT,
        imagE TEXT);'''
        conn.execute(sql) # shortcut for conn.cursor().execute(sql)
    else:
        print 'Schema exists\n'
        conn.commit()
        conn.close()
    return conn

def insertImage(dbname, imageFile):
    with open(imageFile, 'rb') as input_file:
        conn = sqlite3.connect(dbname)
        c = conn.cursor()
        ablob = input_file.read()
        base=os.path.basename(imageFile)
        afile, ext = os.path.splitext(base)
        sql = '''INSERT INTO images
        (image, TYPE, imagE)
        VALUES(?, ?, ?);'''
        c.execute(sql,[sqlite3.Binary(ablob), ext, afile]) 
        conn.commit()

def loadimagE(dbname, path):
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    #conn.execute("DELETE FROM images")
    for fn in image_list:
        imageFile = path+"/"+fn
        insertImage(imageFile)

    for r in c.execute("SELECT rowid, imagE FROM images"):
        print r[0],r[1]
   
    conn.commit()
    conn.close()

def image_id(dbname):
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    rows = c.execute("SELECT rowid, TYPE, imagE FROM images")
    for row in rows:
        print row[0],row[2]+row[1]    
    return
    
def get_image(dbname,image_id):
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    c.execute("SELECT image, TYPE, imagE FROM images WHERE id = ?;",(image_id,))
    #sql = "SELECT image, TYPE, imagE FROM images WHERE id = 19"
    param = {'id': image_id}
    #c.execute(sql, param)
    ablob, ext, afile = c.fetchone()
    filename = afile + ext
    with open(filename, 'wb') as output_file:
        output_file.write(ablob)
    return filename