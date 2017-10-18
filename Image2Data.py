import sqlite3
import os.path
from os import listdir, getcwd
from IPython.core.display import Image 

def get_picture_list(rel_path):
    abs_path = os.path.join(os.getcwd(),rel_path)
    print 'abs_path =', abs_path
    dir_files = os.listdir(abs_path)
    return dir_files

def create_or_open_db(dbname):
    db_is_new = not os.path.exists(db_file)
    conn = sqlite3.connect(db_file)
    if db_is_new:
        print 'Creating schema'
        sql = '''create table if not exists PICTURES(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        PICTURE BLOB,
        TYPE TEXT,
        FILE_NAME TEXT);'''
        conn.execute(sql) # shortcut for conn.cursor().execute(sql)
    else:
        print 'Schema exists\n'
        conn.commit()
        conn.close()
    return conn

def insert_picture(dbname, picture_file):
    with open(picture_file, 'rb') as input_file:
        conn = sqlite3.connect(dbname)
        c = conn.cursor()
        ablob = input_file.read()
        base=os.path.basename(picture_file)
        afile, ext = os.path.splitext(base)
        sql = '''INSERT INTO PICTURES
        (PICTURE, TYPE, FILE_NAME)
        VALUES(?, ?, ?);'''
        c.execute(sql,[sqlite3.Binary(ablob), ext, afile]) 
        conn.commit()

def loadimages(dbname, path):
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    #conn.execute("DELETE FROM PICTURES")
    for fn in picture_list:
        picture_file = path+"/"+fn
        insert_picture(picture_file)

    for r in c.execute("SELECT rowid, FILE_NAME FROM PICTURES"):
        print r[0],r[1]
   
    conn.commit()
    conn.close()

def image_id(dbname):
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    rows = c.execute("SELECT rowid, TYPE, FILE_NAME FROM PICTURES")
    for row in rows:
        print row[0],row[2]+row[1]    
    return
    
def get_image(dbname,picture_id):
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    c.execute("SELECT PICTURE, TYPE, FILE_NAME FROM PICTURES WHERE id = ?;",(picture_id,))
    #sql = "SELECT PICTURE, TYPE, FILE_NAME FROM PICTURES WHERE id = 19"
    param = {'id': picture_id}
    #c.execute(sql, param)
    ablob, ext, afile = c.fetchone()
    filename = afile + ext
    with open(filename, 'wb') as output_file:
        output_file.write(ablob)
    return filename