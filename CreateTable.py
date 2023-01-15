import sqlite3 as sql

def main():
    try: 
        db = sql.connect('Levelling.db')
        cur = db.cursor()
        tablequery = "CREATE TABLE points (id VARCHAR, timestamp DATE, level FLOAT, unixtimestamp INT)"
        cur.execute(tablequery)
        print("Table Created Succesfully")

    except sql.Error as e:
        print("Error create DB - Check if DB exists")

    finally:
        db.close()
        
if __name__ == "__main__":
    main()