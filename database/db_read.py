import sqlite3 as sql


def read_data(dbname, table_name):
    try:
        dbname = dbname + ".db"
        con = sql.connect(dbname)
        cur = con.cursor()
        read_query = "SELECT * FROM " + table_name
        cur.execute(read_query)
        data = cur.fetchall()
        con.commit()
        cur.close()
        return data
    except Exception as e:
        print("Exception occurred while trying to read data from the db:", e)


"""if __name__ == '__main__':
    read_data("new_task", "task")"""
