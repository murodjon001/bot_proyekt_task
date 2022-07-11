import psycopg2

def send_ex(command):
    mydb = psycopg2.connect(user="postgres",
                            password="06102000murodjon",
                            host="localhost",
                            port="5432",
                            database="backend group")
    mycursor= mydb.cursor()

    mycursor.execute(command)
    res = mycursor.fetchall()
    mydb.commit()
    mycursor.close()
    mydb.close()

    return res

