import time
from usecases import config_parser
from database import db_read


def generate_taskid():
    print("Generating task id for the new task")
    current_timestamp = int(time.time())
    num_part = (int(time.time()) % 1000000)
    prefix = "TASK"
    taskid = prefix + str(num_part)
    print("task id value generated successfully.")
    return taskid


def db_access():
    db_name, db_table_name, db_location = config_parser.db_parser()
    return db_name, db_table_name, db_location



