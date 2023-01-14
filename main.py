from PySide2.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from src.database.database import show_table, show_table_depending_on
from PySide2.QtCore import Qt
from ui_main_window import Ui_MainWindow
from adding_window_classes import AddTransmitterWindow, AddLocationWindow, AddWasteTypeWindow
from show_location_waste_type_classes import ShowLocations, ShowWasteTypes


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

    def _get_full_and_all_dumpsters(self):
        # trzeba dopisać końcówkę, która zwraca tylko te recordy których status to 1
        # na razie jest to dopisane to do show_table_depending_on
        full_list = show_table_depending_on("src/database/pythonsqlite.db", "transmitter", "status", "1")
        table = show_table("src/database/pythonsqlite.db", "transmitter")
        return len(full_list), len(table)

    def _set_text_label(self):
        full, all = self._get_full_and_all_dumpsters()
        self.ui.numberOfFull.setText(f"Full dumpsters: {full}/{all}.")

    def _set_progress_bar_value(self):
        full_list, table = self._get_full_and_all_dumpsters()
        value = int(full_list/table)*100
        self.ui.progressBar.setValue(value)

    def _show_transmitters_table(self):
        trasmitters = show_table("src/database/pythonsqlite.db", "transmitter")
        table = self.ui.transmittersTable
        table.setRowCount(len(trasmitters))
        table.setColumnCount(6)
        table.setHorizontalHeaderLabels(["Id", "Waste type id", "Location id", "Active", "Full", "Text Identificator"])
        for i, transmitter in enumerate(trasmitters):
            is_active = "True" if transmitter[3] else "False"
            status = "True" if transmitter[4] else "False"
            item_id = QTableWidgetItem(str(transmitter[0]))
            item_waste_type_id = QTableWidgetItem(str(transmitter[1]))
            item_location_id = QTableWidgetItem(str(transmitter[2]))
            item_is_active = QTableWidgetItem(is_active)
            item_status = QTableWidgetItem(status)
            item_identity = QTableWidgetItem(transmitter[5])
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

    # Kacper
    def _remove_transmitter(self):
        pass

    def _remove_location(self):
        pass

    def _remove_waste_type(self):
        pass

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
