import sqlite3 as sql

def main():
    try:
       db = sql.connect('Levelling.db')
       print("Database sqlite3 connected.")
    except:
        print("Failed to connect database!")
    finally:
        db.close()

if __name__ == "__main__":
    main()