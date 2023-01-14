import sqlite3
from sqlite3 import Error

db_file = "pythonsqlite.db"


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.executescript(create_table_sql)
    except Error as e:
        print(e)


def insert_into_table(db_file, table_name, arguments):
    global query
    if table_name == "location":
        query = """INSERT INTO location (country, city, street, number, notes) VALUES (?, ?, ?, ?, ?); """
    elif table_name == "transmitter":
        query = """INSERT INTO transmitter (waste_type_id, location_id, isActive, status, identificator) VALUES (?, ?, ?, ?, ?); """
    elif table_name == "waste_type":
        query = """INSERT INTO waste_type (name) VALUES (?); """
    return operate_on_database(db_file, query, arguments)


def update_transmitter_status(db_file, arguments):
    query = """ UPDATE transmitter SET status = ? WHERE identificator = ?"""
    operate_on_database(db_file, query, arguments)


def get_record(db_file, table_name, arguments):
    global query
    if table_name == "location":
        query = """ SELECT * FROM location WHERE ID = ?"""
    elif table_name == "waste_type":
        query = """ SELECT * FROM waste_type WHERE ID = ?"""

    return operate_on_database(db_file, query, arguments)


def show_table(db_file, table_name):
    global query
    if table_name == "transmitter":
        query = """ SELECT * FROM transmitter"""
    elif table_name == "waste_type":
        query = """ SELECT * FROM waste_type"""
    # dopisane
    elif table_name == "location":
        query = """ SELECT * FROM location"""

    return operate_on_database(db_file, query, arguments=None)


def show_table_depending_on(db_file, table_name, column, id):
    global query
    if table_name == "transmitter" and column == "location_id":
        query = """ SELECT * FROM transmitter WHERE location_id = ?"""
    elif table_name == "transmitter" and column == "waste_type_id":
        query = """ SELECT * FROM transmitter WHERE waste_type_id = ?"""
    # dopisane
    elif table_name == "transmitter" and column == "status":
        query = """ SELECT * FROM transmitter WHERE status = ?"""
    return operate_on_database(db_file, query, id)


def delete_record(db_file, table_name, id):
    global query
    if table_name == "location":
        query = """DELETE FROM location WHERE ID = ?"""
    elif table_name == "transmitter":
        query = """DELETE FROM transmitter WHERE ID = ?;"""
    operate_on_database(db_file, query, id)


def operate_on_database(db_file, query, arguments):
    global sqliteConnection, result
    try:
        sqliteConnection = create_connection(db_file)
        cursor = sqliteConnection.cursor()
        if arguments is not None:
            cursor.execute(query, arguments)
        else:
            cursor.execute(query)
        sqliteConnection.commit()
        result = cursor.fetchall()
        cursor.close()
    except sqlite3.Error as error:
        result = error
        print("Operation unsuccessfull", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")
            return result


def main():
    sql_create_location_table = """ CREATE TABLE `location` (
                                    `ID` INTEGER PRIMARY KEY ,
                                    `country` VARCHAR(30) NOT NULL,
                                    `city` VARCHAR(30) NOT NULL,
                                    `street` VARCHAR(30) NOT NULL,
                                    `number` INT unsigned NOT NULL,
                                    `notes` TEXT
);"""
    sql_create_transmitter_table = """ CREATE TABLE `transmitter` (
                                        `ID` INTEGER PRIMARY KEY ,
                                        `waste_type_id` INT unsigned NOT NULL,
                                        `location_id` INT unsigned NOT NULL,
                                        `isActive` BOOLEAN NOT NULL DEFAULT 'true',
                                        `status` INT unsigned NOT NULL DEFAULT 0 CHECK(status >= 0 and status <= 100),
                                        `identificator` VARCHAR(9) NOT NULL UNIQUE ,

                                        FOREIGN KEY (waste_type_id) REFERENCES waste_type(ID)
                                        FOREIGN KEY (location_id) REFERENCES location(ID)
    );"""

    sql_create_waste_type_table = """ CREATE TABLE `waste_type` (
                                            `ID` INTEGER PRIMARY KEY ,
                                            `name` VARCHAR(30) NOT NULL UNIQUE
        );"""

    conn = create_connection(db_file)
    if conn is not None:
        create_table(conn, sql_create_location_table)
        create_table(conn, sql_create_waste_type_table)
        create_table(conn, sql_create_transmitter_table)
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()

