def astroread():
    import sqlite3
    conn = sqlite3.connect('AstroStore.db')
    c = conn.cursor()
    count = 0
    req = 100
    view = raw_input("Search : ")
    #for row in c.execute('SELECT rowid, code FROM pages WHERE pages MATCH ?', (view,)):
    for row in c.execute('SELECT rowid, code FROM pages'):        
        count=count+1
        print (row)[0],"-",(row)[1],"\n"
        if count > req:
            conn.close()
            sys.exit()