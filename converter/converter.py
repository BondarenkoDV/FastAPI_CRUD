import os
import csv
import psycopg2
conn = psycopg2.connect("postgresql://postgres:password@127.0.0.1:5433/fastapi_db")
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS posts;")
cur.execute("""CREATE TABLE posts(
id SERIAL PRIMARY KEY,
rubrics text[] NOT NULL,
text text NOT NULL,
created_date timestamp NOT NULL
)
""")

with open('converter/posts.csv', 'r') as f:
    read = csv.reader(f)
    next(read)
    for row in read:
        sql = "INSERT INTO posts (rubrics, text, created_date) VALUES  (%s, %s, %s)"
        cur.execute(sql, (eval(row[2]), row[0], row[1]))
    conn.commit()
    print("Конвертация из csv в базу данных завершена!")
