import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
        return conn
    except Error as e:
        print(e)
    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def main():
    database = r"D:\SQL\db\API_abbayes.db"

    sql_crate_main_regions_table = """
CREATE TABLE IF NOT EXISTS main_regions(
    id integer PRIMARY KEY,
    name text NOT NULL
);
"""
    sql_create_secondary_regions_table = """
CREATE TABLE IF NOT EXISTS secondary_regions(
    id integer PRIMARY KEY,
    name text NOT NULL,
    main_region_id integer,
    FOREIGN KEY(main_region_id) REFERENCES main_regions(id)
);
"""
    sql_create_abbayes_table = """
CREATE TABLE IF NOT EXISTS all_abbayes(
    id integer PRIMARY KEY,
    name text NOT NULL,
    secondary_region_id integer,
    FOREIGN KEY(secondary_region_id) REFERENCES secondary_regions(id)
);
"""
    sql_create_abbayes_data = """
CREATE TABLE IF NOT EXISTS all_abbayes_data(
    id integer PRIMARY KEY,
    name text NOT NULL,
    all_abbayes_id integer,
    FOREIGN KEY(all_abbayes_id) REFERENCES all_abbayes(id)
);
"""
    conn = create_connection(database)
    if conn is not None:
        create_table(conn, sql_crate_main_regions_table)
        create_table(conn, sql_create_secondary_regions_table)
        create_table(conn, sql_create_abbayes_table)
        create_table(conn, sql_create_abbayes_data)
    else:
        print("error cannot create database connection")


if __name__ == '__main__':
    # create_connection(r"D:\SQL\db\API_abbayes.db")
    main()
