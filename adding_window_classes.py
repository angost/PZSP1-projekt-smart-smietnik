import random
import string
from PySide2.QtWidgets import QWidget, QComboBox
from src.database.database import insert_into_table, show_table
from ui_add_transmitter_window_copied import Ui_Form as Ui_Add_Transmitter_Window
from ui_add_location_window_copied import Ui_Form as Ui_Add_Location_Window
from ui_add_waste_type_window_copied import Ui_Form as Ui_Add_Waste_Type_Window

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
        data = show_table("src/database/pythonsqlite.db", "waste_type")
        for item in data:
            self.ui.select_waste_type_dropdown.addItem(item[1])

    def _setup_location_dropdown(self):
        # Potrzebuję końcówki show_table(location)
        data = show_table("src/database/pythonsqlite.db", "location")
        for item in data:
            item_data = [str(i) for i in item[1:]]
            self.ui.select_location_dropdown.addItem(', '.join(item_data))

    def _reject(self):
        self.hide()

    def _get_new_transmitter_data(self):
        waste_type_data = show_table("src/database/pythonsqlite.db", "waste_type")
        chosen_waste_type_dropdown_id = self.ui.select_waste_type_dropdown.currentIndex()
        waste_type_id = waste_type_data[chosen_waste_type_dropdown_id][0]

        location_data = show_table("src/database/pythonsqlite.db", "location")
        chosen_location_dropdown_id = self.ui.select_location_dropdown.currentIndex()
        location_id = location_data[chosen_location_dropdown_id][0]

        isActive = 1
        status = 0
        identificator = get_random_string(9)
        transmitter_data = (waste_type_id, location_id, isActive, status, identificator)
        insert_into_table("src/database/pythonsqlite.db", "transmitter", transmitter_data)
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
            location_data = (country, city, street, number, notes)
            insert_into_table("src/database/pythonsqlite.db", "location", location_data)
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
        name = self.ui.enter_watse_type_name.text()
        if name != '':
            waste_type_data = (name,)
            insert_into_table("src/database/pythonsqlite.db", "waste_type", waste_type_data)
            self.hide()

    def _reject(self):
        self.hide()


# It's only fo testing usage
def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str