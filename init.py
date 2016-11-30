import psycopg2

def createdb():
    DB = psycopg2.connect(dbname="postgres")
    cursor = DB.cursor()
    cursor.execute(open("init.sql").read())
    DB.commit()
    DB.close()
    print("Success")

createdb()
