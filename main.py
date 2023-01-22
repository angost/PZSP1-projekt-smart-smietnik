from PySide2.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from PySide2.QtCore import Qt
from ui_main_window import Ui_TurnWaste
from adding_window_classes import AddTransmitterWindow, AddLocationWindow, AddWasteTypeWindow
from show_location_waste_type_classes import ShowLocations, ShowWasteTypes
from removing_window_classes import RemoveTransmitterWindow, RemoveLocationWindow, RemoveWasteTypeWindow
from filter_window_classes import FilterWasteTypeWindow, FilterLocationWindow, FilterFillingLevelWindow
import requests
from domain import domain

class Interface(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_TurnWaste()
        self.ui.setupUi(self)
        self._show_transmitters_table()
        self.ui.actionAdd_trasmitter.triggered.connect(self._add_transmitter)
        self.ui.actionAdd_location.triggered.connect(self._add_location)
        self.ui.actionAdd_waste_type.triggered.connect(self._add_waste_type)
        self.ui.actionShow_all_transmitters.triggered.connect(self._show_transmitters_table)
        self.ui.actionShow_all_locations.triggered.connect(self._show_locations)
        self.ui.actionShow_all_waste_types.triggered.connect(self._show_waste_types)
        self.ui.actionRemove_trasmitter.triggered.connect(self._remove_transmitter)
        self.ui.actionRemove_location.triggered.connect(self._remove_location)
        self.ui.actionRemove_waste_type.triggered.connect(self._remove_waste_type)
        self.ui.actionBy_waste_type.triggered.connect(self._show_only_given_waste_type)
        self.ui.actionBy_location.triggered.connect(self._show_only_given_location)
        self.ui.actionBy_filling_level.triggered.connect(self._show_only_given_filling)

    def _get_full_and_all_dumpsters(self):
        full_list = requests.get(domain + 'get-transmitters-where-status?status=' + str(90)).json()
        trasmitters = requests.get(domain + 'get-all-transmitters').json()
        return len(full_list), len(trasmitters)

    def _set_text_label(self, full, all):
        self.ui.numberOfFull.setText(f"Full dumpsters: {full}/{all}.")

    def _set_progress_bar_value(self, full, all):
        try:
            value = int((full/all)*100)
        except ZeroDivisionError:
            value = 0
        finally:
            self.ui.progressBar.setValue(value)

    def _show_transmitters_table(self):
        transmitters = requests.get(domain + 'get-all-transmitters').json()
        full, all = self._get_full_and_all_dumpsters()
        self._show_table(transmitters)
        self._set_text_label(full, all)
        self._set_progress_bar_value(full, all)

    def _show_table(self, trasmitters):
        table = self.ui.transmittersTable
        table.setRowCount(len(trasmitters))
        table.setColumnCount(6)
        table.setHorizontalHeaderLabels(["Id", "Waste type", "Location id", "Active", "Status [%]", "Text Identificator"])
        for i, transmitter in enumerate(trasmitters):
            item_id = QTableWidgetItem(str(transmitter['id']))
            item_waste_type_id = QTableWidgetItem(str(transmitter['waste_type']))
            item_location_id = QTableWidgetItem(str(transmitter['location']['id']))
            item_is_active = QTableWidgetItem(str(transmitter['active']))
            item_status = QTableWidgetItem(str(transmitter['status']))
            item_identity = QTableWidgetItem(transmitter['identificator'])
            item_id.setFlags(item_id.flags() ^ Qt.ItemIsEditable)
            item_waste_type_id.setFlags(item_waste_type_id.flags() ^ Qt.ItemIsEditable)
            item_location_id.setFlags(item_location_id.flags() ^ Qt.ItemIsEditable)
            item_is_active.setFlags(item_is_active.flags() ^ Qt.ItemIsEditable)
            item_status.setFlags(item_status.flags() ^ Qt.ItemIsEditable)
            item_identity.setFlags(item_identity.flags() ^ Qt.ItemIsEditable)
            table.setItem(i, 0, item_id)
            table.setItem(i, 1, item_waste_type_id)
            table.setItem(i, 2, item_location_id)
            table.setItem(i, 3, item_is_active)
            table.setItem(i, 4, item_status)
            table.setItem(i, 5, item_identity)
            table.horizontalHeader().setStretchLastSection(True)

    def _show_locations(self):
        self.widget = ShowLocations()
        self.widget.show()

    def _show_waste_types(self):
        self.widget = ShowWasteTypes()
        self.widget.show()

    def _add_transmitter(self):
        self.widget = AddTransmitterWindow()
        self.widget.show()

    def _add_location(self):
        self.widget = AddLocationWindow()
        self.widget.show()

    def _add_waste_type(self):
        self.widget = AddWasteTypeWindow()
        self.widget.show()

    def _remove_transmitter(self):
        self.widget = RemoveTransmitterWindow()
        self.widget.show()

    def _remove_location(self):
        self.widget = RemoveLocationWindow()
        self.widget.show()

    def _remove_waste_type(self):
        self.widget = RemoveWasteTypeWindow()
        self.widget.show()

    def _show_only_given_waste_type(self):
        self.widget = FilterWasteTypeWindow()
        self.widget.show()
        self.widget.ui.buttonBox.accepted.connect(self._show_transmitters_waste_type)

    def _show_transmitters_waste_type(self):
        id = self.widget.waste_type_id
        filtered = requests.get(domain + "get-transmitters-where-waste-type?id=" + str(id)).json()
        full = self.count_full(filtered, 90)
        self._show_table(filtered)
        self._set_text_label(full, len(filtered))
        self._set_progress_bar_value(full, len(filtered))

    def _show_only_given_location(self):
        self.widget = FilterLocationWindow()
        self.widget.show()
        self.widget.ui.buttonBox.accepted.connect(self._show_transmitters_location)

    def _show_transmitters_location(self):
        id = self.widget.location_id
        filtered = requests.get(domain + "get-transmitters-from-location?id=" + str(id)).json()
        full = self.count_full(filtered, 90)
        self._show_table(filtered)
        self._set_text_label(full, len(filtered))
        self._set_progress_bar_value(full, len(filtered))

    def _show_only_given_filling(self):
        self.widget = FilterFillingLevelWindow()
        self.widget.show()
        self.widget.ui.buttonBox.accepted.connect(self._show_transmitters_filling_level)

    def _show_transmitters_filling_level(self):
        value = self.widget.value
        filtered = requests.get(domain + "get-transmitters-where-status?status=" + str(value)).json()
        full = self.count_full(filtered, 90)
        self._show_table(filtered)
        self._set_text_label(full, len(filtered))
        self._set_progress_bar_value(full, len(filtered))

    def count_full(self, transmitters: list, status: int):
        count = 0
        for transmitter in transmitters:
            if transmitter['status'] >= status:
                count += 1
        return count

def guiMain():
    app = QApplication()
    window = Interface()
    window.show()
    return app.exec_()


if __name__ == '__main__':
    guiMain()
