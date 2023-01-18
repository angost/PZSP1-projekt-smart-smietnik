import json
import random
import string
from PySide2.QtWidgets import QWidget, QComboBox

from domain import domain
from ui_python_files.ui_add_transmitter_window_copied import Ui_Form as Ui_Add_Transmitter_Window
from ui_python_files.ui_add_location_window_copied import Ui_Form as Ui_Add_Location_Window
from ui_python_files.ui_add_waste_type_window_copied import Ui_Form as Ui_Add_Waste_Type_Window
import requests

class AddTransmitterWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_Add_Transmitter_Window()
        self.ui.setupUi(self)
        self._setup_waste_type_dropdown()
        self._setup_location_dropdown()
        self.ui.window_control.accepted.connect(self._get_new_transmitter_data)
        self.ui.window_control.rejected.connect(self._reject)

    def _setup_waste_type_dropdown(self):
        waste_type_data = requests.get(domain + 'show-all-waste-types').json()
        for item in waste_type_data:
            self.ui.select_waste_type_dropdown.addItem(item['name'])

    def _setup_location_dropdown(self):
        location_data = requests.get(domain + 'get-all-locations').json()
        jsn_list = json.loads(json.dumps(location_data))

        for item in jsn_list:
            item_data = [str(val) for key, val in item.items()]
            self.ui.select_location_dropdown.addItem(', '.join(item_data))

    def _reject(self):
        self.hide()

    def _get_new_transmitter_data(self):
        waste_type_data = requests.get(domain + 'show-all-waste-types').json()
        chosen_waste_type_dropdown_id = self.ui.select_waste_type_dropdown.currentIndex()
        waste_type_id = waste_type_data[chosen_waste_type_dropdown_id]['id']

        location_data = requests.get(domain + '/get-all-locations').json()
        chosen_location_dropdown_id = self.ui.select_location_dropdown.currentIndex()
        location_id = location_data[chosen_location_dropdown_id]['id']
        identificator = get_random_string(9)

        transmitter_data = {
            "waste_type_id": waste_type_id,
            "location_id": location_id,
            "active": "True",
            "status": 0,
            "identificator": identificator,
        }
        response = requests.post(domain + '/add-transmitter', json=transmitter_data)
        print("Status Code", response.status_code)
        self.hide()


class AddLocationWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_Add_Location_Window()
        self.ui.setupUi(self)
        self.ui.window_control.accepted.connect(self._get_new_location_data)
        self.ui.window_control.rejected.connect(self._reject)

    def _get_new_location_data(self):
        country = self.ui.enter_country.text()
        city = self.ui.enter_city.text()
        street = self.ui.enter_street.text()
        number = self.ui.enter_number.text()
        notes = self.ui.enter_notes.text()
        if country and city and street and number:
            location_data = {
                "country": country,
                "city": city,
                "street": street,
                "number": number,
                "notes": notes,
            }
            response = requests.post(domain + '/add-location', json=location_data)
            print("Status Code", response.status_code)
            self.hide()

    def _reject(self):
        self.hide()


class AddWasteTypeWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_Add_Waste_Type_Window()
        self.ui.setupUi(self)
        self.ui.window_control.accepted.connect(self._get_new_waste_type_data)
        self.ui.window_control.rejected.connect(self._reject)

    def _get_new_waste_type_data(self):
        name = self.ui.enter_waste_type_name.text()
        if name != '':
            waste_type_data = {
                "name": name,
            }
            response = requests.post(domain + 'add-waste-type', json=waste_type_data)
            print("Status Code", response.status_code)
            self.hide()

    def _reject(self):
        self.hide()


# It's only fo testing usage
def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str
