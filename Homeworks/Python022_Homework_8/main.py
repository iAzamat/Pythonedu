import sqlite3
import commands

conn = sqlite3.connect(f'db/db.db')
cur = conn.cursor()
commands.changecmd(conn, cur)
cur.close()
conn.close()
