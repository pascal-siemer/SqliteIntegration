import sqlite3

import queries
import queries_old
import data


# def __fill_template(query, values):
#     for i in range(0, len(values)):
#         query = query.replace(f"?{i}", values[i])
#     return query
#
#
# def insert_values(template_query, values):
#     for line in values:
#         cursor.execute(template_query, line)
#
#
# def show(table_name):
#     cursor.execute(queries.show_table_by_tablename, (table_name,))
#     for line in cursor:
#         print(line)

def show(cursor, query):
    cursor.execute(query)
    content = cursor.fetchall()
    print(content)

with sqlite3.connect("databaseStringsNew.sqlite3") as connection:
    cursor = connection.cursor()

    cursor.execute(queries.enable_foreign_keys)

    cursor.execute(queries.create_person)
    cursor.execute(queries.create_gebaeude)
    cursor.execute(queries.create_merkmal)
    cursor.execute(queries.create_raum)
    cursor.execute(queries.create_zugang)

    cursor.executemany(queries.fill_person_by_parameter, data.personen)
    cursor.executemany(queries.fill_gebaeude_by_parameter, data.gebaeude)
    cursor.executemany(queries.fill_merkmal_by_parameter, data.merkmal)
    cursor.executemany(queries.fill_raum_by_parameter, data.raum)
    cursor.executemany(queries.fill_zugang_by_parameter, data.zugang)

    connection.commit()

    show(cursor, queries.show_personen)
    show(cursor, queries.show_gebaeude)
    show(cursor, queries.show_merkmal)
    show(cursor, queries.show_raum)
    show(cursor, queries.show_zugang)



# fix: https://stackoverflow.com/questions/25387537/inserting-a-table-name-into-a-query-gives-sqlite3-operationalerror-near-sy