from PySide2.QtWidgets import QWidget, QTableWidgetItem
from ui_python_files.ui_show_locations import Ui_locationsWidget
from ui_python_files.ui_show_waste_types import Ui_wasteTypeWidget
from PySide2.QtCore import Qt
import requests
from domain import domain

class ShowLocations(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_locationsWidget()
        self.ui.setupUi(self)
        self._show_locations()

    def _show_locations(self):
        locations = requests.get(domain + 'get-all-locations').json()
        table = self.ui.locationsTable
        table.setRowCount(len(locations))
        table.setColumnCount(6)
        table.setHorizontalHeaderLabels(["Id", "Country", "City", "Street", "Number", "Notes"])
        for i, location in enumerate(locations):
            item_id = QTableWidgetItem(str(location['id']))
            item_country = QTableWidgetItem(location['country'])
            item_city = QTableWidgetItem(location['city'])
            item_street = QTableWidgetItem(location['street'])
            item_number = QTableWidgetItem(str(location['number']))
            item_notes = QTableWidgetItem(location['notes'])
            item_id.setFlags(item_id.flags() ^ Qt.ItemIsEditable)
            item_country.setFlags(item_country.flags() ^ Qt.ItemIsEditable)
            item_city.setFlags(item_city.flags() ^ Qt.ItemIsEditable)
            item_street.setFlags(item_street.flags() ^ Qt.ItemIsEditable)
            item_number.setFlags(item_number.flags() ^ Qt.ItemIsEditable)
            item_notes.setFlags(item_notes.flags() ^ Qt.ItemIsEditable)
            table.setItem(i, 0, item_id)
            table.setItem(i, 1, item_country)
            table.setItem(i, 2, item_city)
            table.setItem(i, 3, item_street)
            table.setItem(i, 4, item_number)
            table.setItem(i, 5, item_notes)
            table.horizontalHeader().setStretchLastSection(True)


class ShowWasteTypes(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_wasteTypeWidget()
        self.ui.setupUi(self)
        self._show_waste_types()

    def _show_waste_types(self):
        waste_types = requests.get(domain + 'show-all-waste-types').json()
        table = self.ui.wasteTypeTable
        table.setRowCount(len(waste_types))
        table.setColumnCount(2)
        table.setHorizontalHeaderLabels(["Id", "Waste name"])
        for i, waste_type in enumerate(waste_types):
            item_id = QTableWidgetItem(str(waste_type['id']))
            item_name = QTableWidgetItem(waste_type['name'])
            item_id.setFlags(item_id.flags() ^ Qt.ItemIsEditable)
            item_name.setFlags(item_name.flags() ^ Qt.ItemIsEditable)
            table.setItem(i, 0, item_id)
            table.setItem(i, 1, item_name)
            table.horizontalHeader().setStretchLastSection(True)