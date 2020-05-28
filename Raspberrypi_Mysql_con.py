import MySQLdb


db=MySQLdb.connect(host='210.119.12.52',user='test_usr',password='mysql_p@ssw0rd',db='shopdb',charset='utf8')
cur = db.cursor()
#cur.execute('select * from ("Table name") ')
cur.execute('select COUNT(machine_id) from shopdb.iotmachine')

while True:
    product = cur.fetchone()
    if not product:
        break

    print(product)

cur.close()
db.close()