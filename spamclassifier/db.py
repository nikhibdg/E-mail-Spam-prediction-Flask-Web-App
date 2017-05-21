import sqlite3

conn = sqlite3.connect('reviews.sqlite')
c = conn.cursor()
c.execute('CREATE TABLE review_db (message TEXT, prediction INTEGER, date TEXT)')

example1 = 'Hii Nish,How are you'
c.execute("INSERT INTO review_db (message, prediction, date) VALUES (?, ?, DATETIME('now'))", (example1, 0))

example2 = 'Get thin in one week!!!'
c.execute("INSERT INTO review_db (message, prediction, date) VALUES (?, ?, DATETIME('now'))", (example2, 1))

conn.commit()
conn.close()

conn = sqlite3.connect('reviews.sqlite')
c = conn.cursor()

c.execute("SELECT * FROM review_db WHERE date BETWEEN '2015-01-01 10:10:10' AND DATETIME('now')")
results = c.fetchall()

conn.close()

print(results)

