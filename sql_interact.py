from mysql.connector import MySQLConnection, Error
from sql_config import read_db_config


def insert_writeback(name, phone):
    if ';' in name + phone:
        return 1

    query = "INSERT INTO writeback(name, phone) " + "VALUES(%s, %s)"
    args = (name, phone)

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        conn.commit()

    except Error as error:
        return 1

    finally:
        cursor.close()
        conn.close()

    return 0


if __name__ == '__main__':
    insert_writeback('test_name', '+1234567890')
