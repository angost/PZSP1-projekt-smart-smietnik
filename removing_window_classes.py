from PySide2.QtWidgets import QWidget

from domain import domain
from ui_python_files.ui_remove_transmitter_window import Ui_RemoveTransmitter
from ui_python_files.ui_remove_location_window import Ui_RemoveLocation
from ui_python_files.ui_remove_waste_type_window import Ui_RemoveWasteType
import requests

class RemoveTransmitterWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_RemoveTransmitter()
        self.ui.setupUi(self)
        self._transmitter_dropdown_list()
        self.ui.buttonBox.rejected.connect(self._close_window)
        self.ui.buttonBox.accepted.connect(self._remove_transmitter_database)

    def _transmitter_dropdown_list(self):
        data = requests.get(domain + 'get-all-transmitters').json()
        self.ui.comboBox.addItems([transmitter['identificator'] for transmitter in data])

    def _close_window(self):
        self.hide()

    def _remove_transmitter_database(self):
        data = requests.get(domain + 'get-all-transmitters').json()
        transmitter_index = self.ui.comboBox.currentIndex()
        transmitter_to_remove = str(data[transmitter_index]['id'])
        response = requests.get(domain + 'delete-transmitter?id=' + str(transmitter_to_remove))
        print("Status Code", response.status_code)
        self.hide()


class RemoveLocationWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_RemoveLocation()
        self.ui.setupUi(self)
        self._location_dropdown_list()
        self.ui.buttonBox.rejected.connect(self._close_window)
        self.ui.buttonBox.accepted.connect(self._remove_location_database)

    def _location_dropdown_list(self):
        data = requests.get(domain + 'get-all-locations').json()
        for location in data:
            self.ui.dropdownlist.addItem(f'{location["country"]}, {location["city"]}, {location["street"]}, {location["number"]}')

    def _close_window(self):
        self.hide()

    def _remove_location_database(self):
        data = requests.get(domain + 'get-all-locations').json()
        location_index = self.ui.dropdownlist.currentIndex()
        location_to_remove = str(data[location_index]['id'])
        response = requests.get(domain + 'delete-location?id=' + str(location_to_remove))
        print("Status Code", response.status_code)
        self.hide()

class RemoveWasteTypeWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_RemoveWasteType()
        self.ui.setupUi(self)
        self._waste_type_dropdown_list()
        self.ui.buttonBox.rejected.connect(self._close_window)
        self.ui.buttonBox.accepted.connect(self._remove_waste_type_database)

    def _waste_type_dropdown_list(self):
        data = requests.get(domain + 'show-all-waste-types').json()
        self.ui.dropdownlist.addItems([waste_type['name'] for waste_type in data])

    def _close_window(self):
        self.hide()

    def _remove_waste_type_database(self):
        data = requests.get(domain + 'show-all-waste-types').json()
        waste_type_index = self.ui.dropdownlist.currentIndex()
        waste_type_to_remove = str(data[waste_type_index]['id'])
        response = requests.get(domain + 'delete-waste-type?id=' + str(waste_type_to_remove))
        print("Status Code", response.status_code)
        self.hide()
