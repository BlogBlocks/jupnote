def dbstore(insert):
    import sqlite3
    conn = sqlite3.connect('XPfts4.db')
    c = conn.cursor()
    c.execute("""
    CREATE VIRTUAL TABLE IF NOT EXISTS pages 
    USING FTS3(code);
    """
    )
    c = conn.cursor()
    conn.text_factory = str
    # CREATE VIRTUAL TABLE pages USING fts4(code);
    c.execute("INSERT INTO pages VALUES(?)", (insert,))

    conn.commit()
    conn.close()