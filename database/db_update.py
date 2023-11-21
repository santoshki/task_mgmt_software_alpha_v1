import sqlite3
import os
import sys


def delete_table(db_name, table_name):
    try:
        db_name = db_name + ".db"
        if os.path.isfile(db_name):
            db_connection = sqlite3.connect(db_name)
            db_cursor = db_connection.cursor()
            table_query = "SELECT name FROM sqlite_master WHERE type = 'table' AND name = " + "'" + table_name + "'"
            print(table_query)
            table_exist = db_cursor.execute(table_query).fetchall()
            if not table_exist:
                print("Table not found.")
            else:
                table_drop_query = "DROP TABLE " + str(table_name)
                db_connection.execute(table_drop_query)
                print("Table " + table_name + " dropped successfully from the database ", db_name)
        else:
            print(db_name + " database does not exist!")
            sys.exit(1)
    except Exception as e:
        print("Exception occurred while updating db:", e)
        raise Exception(e)


if __name__ == '__main__':
    delete_table("new_task", "task")
