from src.database.database import insert_into_table, show_table, delete_record


# insert_into_table("src/database/pythonsqlite.db", "location", ("Poland", "Warsaw", "nasoad", 4, "none"))
# print(show_table("src/database/pythonsqlite.db", "transmitter"))
delete_record("src/database/pythonsqlite.db", "transmitter", "1")
