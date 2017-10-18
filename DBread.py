def dbread():
    import sqlite3
    conn = sqlite3.connect('XPfts4.db')
    c = conn.cursor()
    count = 0
    req = 100
    view = raw_input("Search : ")
    for row in c.execute('SELECT rowid, code FROM pages WHERE pages MATCH ?', (view,)):    
        count=count+1
        print (row)[0],"-",(row)[1],"\n"
        if count > req:
            conn.close()
            sys.exit()