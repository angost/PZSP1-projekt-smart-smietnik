from PySide2.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from PySide2.QtCore import Qt
from ui_main_window import Ui_MainWindow
from adding_window_classes import AddTransmitterWindow, AddLocationWindow, AddWasteTypeWindow
from show_location_waste_type_classes import ShowLocations, ShowWasteTypes
from removing_window_classes import RemoveTransmitterWindow, RemoveLocationWindow, RemoveWasteTypeWindow
import requests
from domain import domain

class Interface(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
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

    def _get_full_and_all_dumpsters(self):
        full_list = requests.get(domain + 'get-transmitters-where-status?status=' + str(90)).json()
        trasmitters = requests.get(domain + 'get-all-transmitters').json()
        return len(full_list), len(trasmitters)

    def _set_text_label(self):
        full, all = self._get_full_and_all_dumpsters()
        self.ui.numberOfFull.setText(f"Full dumpsters: {full}/{all}.")

    def _set_progress_bar_value(self):
        full_list, table = self._get_full_and_all_dumpsters()
        value = int(full_list/table)*100
        self.ui.progressBar.setValue(value)

    def _show_transmitters_table(self):
        trasmitters = requests.get(domain + 'get-all-transmitters').json()
        table = self.ui.transmittersTable
        table.setRowCount(len(trasmitters))
        table.setColumnCount(6)
        table.setHorizontalHeaderLabels(["Id", "Waste type", "Location id", "Active", "Status [%]", "Text Identificator"])
        for i, transmitter in enumerate(trasmitters):
            item_id = QTableWidgetItem(str(transmitter['id']))
            item_waste_type_id = QTableWidgetItem(str(transmitter['waste_type']))
            item_location_id = QTableWidgetItem(str(transmitter['id']))
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
            self._set_text_label()
            self._set_progress_bar_value()

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

    # filters, later
    def _show_only_given_waste_type(self):
        pass

    def _show_only_given_location(self):
        pass

    def _show_only_full(self):
        pass


def guiMain():
    app = QApplication()
    window = Interface()
    window.show()
    return app.exec_()


if __name__ == '__main__':
    guiMain()
