from database import db_read

data = db_read.read_data("new_task", "task")
print(data)
