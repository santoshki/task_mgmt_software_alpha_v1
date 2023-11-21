import yaml


def db_parser():
    with open("C:\\Users\\santosh.a.d.kulkarni\\PycharmProjects\\task_mgmt_software_alpha_v1\\config\\db_config.yaml",
              "r") as stream:
        try:
            data = yaml.safe_load(stream)
            db_data = data['sqlite_db']
            db_name = db_data['db_name']
            db_table_name = db_data['table_name']
            db_location = db_data['db_location']
            # print(db_data)
            # print(db_name)
            # print(db_table_name)
            # print(db_location)
            return db_name, db_table_name, db_location
        except yaml.YAMLError as exc:
            print(exc)

