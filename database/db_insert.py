import sqlite3


def insert_data(db_name, table_name, data):
    try:
        db_name = db_name + ".db"
        db_connection = sqlite3.connect(db_name)
        db_cursor = db_connection.cursor()
        # db_cursor.execute("INSERT INTO " + table_name + " (Name, Job, Skill) VALUES (?,?,?)", (data[0], data[1], data[2]))

        db_cursor.execute("INSERT INTO " + table_name + " (task_id_value, task_title_value, task_description_value,"
                          "task_state_dropdown_value, task_notes_value, task_priority_value, task_assigned_to_value,"
                                                        "task_created_timestamp_value) VALUES (?,?,?,?,?,?,?,?)",
                          (data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7]))
        print("Data successfully inserted into table:", table_name)
        db_cursor.close()
        db_connection.commit()

    except Exception as e:
        print("Exception occurred while inserting data into database:", db_name)
        print("Exception:", e)


if __name__ == '__main__':
    data = ['Santosh', 'developer', 'Python']
    insert_data("new_task", "task", data)
