import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

#clear the table before reuse it
cur.execute('DROP TABLE IF EXISTS Counts')
#then create a new fresh one
cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'D:\\Coursera_Python\\Using Databases with Python\\week2-Basic Structured Query Language\\mbox.txt'#'mbox-short.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]

    #email is the whole name of a email address,
    #so I have to get the domain name after the @ sign
    #email format: xxx@aaa.com
    emailPieces = email.split('@')
    org = emailPieces[1]

    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (org,))
conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
