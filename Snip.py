def snippet():
    import sqlite3
    import sys
    conn = sqlite3.connect('snippet.db')
    conn.text_factory = str
    c = conn.cursor()
    count=0;req=200
    search = raw_input("Search : ")
    for row in c.execute('SELECT * FROM snippet WHERE text MATCH ?', (search,)):    
        count=count+1
        print (row)[1]," -- KEYWORDS",(row)[2],"\n"
        if count > req:
            conn.close()
            sys.exit()
if __name__=="__main__":
    snippet()