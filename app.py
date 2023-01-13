import random
import string

from flask import Flask, render_template, request

# from GarbageServer.src.database.database import insert_into_table, show_table, delete_record, \
#     update_transmitter_status, get_record
# from GarbageServer.src.transmitterData.location import Location
# from GarbageServer.src.transmitterData.transmitter import Transmitter

from src.database.database import insert_into_table, show_table, delete_record, \
    update_transmitter_status, get_record
from src.transmitterData.location import Location
from src.transmitterData.transmitter import Transmitter

app = Flask(__name__)

db_file = "./src/database/pythonsqlite.db"


@app.route('/add-transmitter', methods=["POST", "GET"])
def add_transmitter():
    if request.method == "POST":
        waste_type = request.form["waste_type"]
        transmitter = (waste_type, 1, True, 0, get_random_string(9))
        insert_into_table(db_file, "transmitter", transmitter)
        return f"<h1>done</h1>"
    else:
        return render_template("add_transmitter.html")


@app.route('/add-waste-type', methods=["POST", "GET"])
def add_waste_type():
    if request.method == "POST":
        waste_type = request.form["waste_type"]
        insert_into_table(db_file, "waste_type", (waste_type,))
        return f"<h1>done</h1>"
    else:
        return render_template("add_transmitter.html")


@app.route('/add-location', methods=["POST", "GET"])
def add_location():
    if request.method == "POST":

        country = request.form["country"]
        # location.city = request.form["city"]
        # location.street = request.form["street"]
        # location.number = request.form["number"]
        # location.notes = request.form["notes"]
        city = "a"
        street = "b"
        number = "c"
        notes = "d"
        location = (country, city, street, number, notes)
        insert_into_table(db_file, "location", location)
        return f"<h1>done</h1>"
    else:
        return render_template("add_location.html")


@app.get('/change-status')
def dumpster_is_full():
    identificator = request.args.get('identificator')
    status = request.args.get('status', type=int)
    arguments = (status, identificator)
    update_transmitter_status(db_file, arguments)
    return f"<h1>done</h1>"


@app.get('/get-all-transmitters')
def get_all_transmitters():
    all_transmitters = show_table(db_file, "transmitter")
    transmitters = []
    for transmitter in list(all_transmitters):
        tm = Transmitter(bool(transmitter[3]), transmitter[4], transmitter[5])
        tm.waste_type = get_record(db_file, "waste_type", (transmitter[1],))[0][1]
        location_db = get_record(db_file, "location", (transmitter[2],))
        location_db = list(location_db)
        location = Location(location_db[0][1], location_db[0][2], location_db[0][3], location_db[0][4],
                            location_db[0][5])
        tm.location = location
        transmitters.append(tm)

    return f"<h1>{transmitters[0].location.country}</h1>"


@app.get('/show-all-waste-types')
def show_all_waste_types():
    all_waste_types = show_table(db_file, "waste_type")
    all_waste_types = list(all_waste_types)
    return f"<h1>{all_waste_types[0][1]}</h1>"


@app.get('/delete-location')
def delete_location():
    id = request.args.get('id', type=int)
    argument = (id,)
    delete_record(db_file, "location", argument)
    return f"<h1>deleted</h1>"


@app.get('/delete-transmitter')
def delete_transmitter():
    identificator = request.args.get('identificator')
    argument = (identificator,)
    delete_record(db_file, "transmitter", argument)
    return f"<h1>deleted</h1>"


# It's only fo testing usage
def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


if __name__ == '__main__':
    app.run(host='0.0.0.0')
