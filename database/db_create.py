import sqlite3
import os


def create_db(db_name, table_name):
    db_name = db_name + ".db"
    if os.path.isfile(db_name):
        print("db already exists with the provided database name:", db_name)
        db_connection = sqlite3.connect(db_name)
        db_cursor = db_connection.cursor()
        table_query = "SELECT name FROM sqlite_master WHERE type = 'table' AND name = " + "'" + table_name + "'"
        table_exist = db_cursor.execute(table_query).fetchall()
        if not table_exist:
            print("Table not found.\nCreating the table " + table_name + ".....")
            table_query = "CREATE TABLE " + str(
                table_name) + "(task_id_value varchar(255), task_title_value varchar(255), " \
                              "task_description_value varchar(255), task_state_dropdown_value varchar(255), " \
                              "task_notes_value varchar(255)," \
                              "task_priority_value varchar(255), task_assigned_to_value varchar(255), " \
                              "task_created_timestamp_value varchar(255)); "
            db_cursor.execute(table_query)
            print("Table " + table_name + " created successfully.")
            db_connection.close()
        else:
            print("Table " + table_name + " already exists.")
    else:
        try:
            db_connection = sqlite3.connect(db_name)
            db_cursor = db_connection.cursor()
            print("Database " + db_name + " created successfully.")

            table_query = "CREATE TABLE " + str(
                table_name) + "(task_id_value varchar(255), task_title_value varchar(255), " \
                              "task_description_value varchar(255), task_state_dropdown_value varchar(255), " \
                              "task_notes_value varchar(255)," \
                              "task_priority_value varchar(255), task_assigned_to_value varchar(255), " \
                              "task_created_timestamp_value varchar(255); "
            db_cursor.execute(table_query)
            print("Table " + table_name + " created successfully.")
            db_connection.close()
        except Exception as e:
            print("Error occurred while creating db for", db_name)


create_db("new_task", "task")
