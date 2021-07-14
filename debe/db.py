import psycopg2

sql = "SELECT * FROM users where id = 10"
try:
    conn = psycopg2.connect(database='tnt', user='tnt', host='10.4.0.3', password='tnt')
    cur = conn.cursor()
    cur.execute(sql)

    print("The number of rows: ", cur.rowcount)
    row = cur.fetchone()

    while row is not None:
        print(row)
        row = cur.fetchone()
    cur.close()
    conn.close()
except:
    print("db error")

