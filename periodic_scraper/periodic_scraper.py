# WARNING - importing parlpy after mysql.connector results in error with urllib, relating to SSL certs
# todo: fix this

from parlpy.bills.bill_list_fetcher import BillsOverview

import mysql.connector
from mysql.connector.constants import ClientFlag


# clear all rows and reset increment
def clear_bills_table(conn, cursor):
    cursor.execute("DELETE FROM bills_app_db.Bills")
    cursor.execute("ALTER TABLE bills_app_db.Bills AUTO_INCREMENT = 1")
    conn.commit()


def insert_all_bill_overview_data(conn, cursor, bill_data):
    for b in bill_data.itertuples():
        # this code gets govt provided bill detail path, could be used as unique id?
        # bill_detail_path_number = int(getattr(b, "bill_detail_path").rsplit("/")[-1])
        # print("int bill id: {}".format(bill_detail_path_number))

        bill_name = getattr(b, "bill_title")
        command_string = "INSERT INTO bills_app_db.Bills (title) VALUES (\"{0}\")".format(bill_name)
        cursor.execute(command_string)

    conn.commit()

def print_all_rows_of_table(cursor, table_name):
    cursor.execute(f"SELECT * FROM bills_app_db.{table_name}")
    print("all items in table:")
    for x in cursor:
        print(x)

sql_config = {
    "user": "root",
    "password": "",
    "host": "35.223.77.43",
    "client_flags": [ClientFlag.SSL],
    "ssl_ca": "certs/server-ca.pem",
    "ssl_cert": "certs/client-cert.pem",
    "ssl_key": "certs/client-key.pem"
}

def insert_and_update_data():
    conn = mysql.connector.connect(**sql_config)
    cursor = conn.cursor()

    bills_this_session = BillsOverview()
    bills_this_session.update_all_bills_in_session()

    # clear the table and insert everything back in
    clear_bills_table(conn, cursor)
    insert_all_bill_overview_data(conn, cursor, bills_this_session.bills_overview_data)

    print_all_rows_of_table(cursor, "Bills")

    cursor.close()
    conn.close()

database_demo()
