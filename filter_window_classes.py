from ui_python_files.ui_filter_waste_type_window import Ui_Form as Ui_FilterWasteType
from ui_python_files.ui_filter_location_window import Ui_Form as Ui_FilterLocation
from ui_python_files.ui_filter_filling_level_window import Ui_Form as Ui_FilterFillingLevel
from PySide2.QtWidgets import QWidget
import requests
from domain import domain
import json


class FilterWasteTypeWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_FilterWasteType()
        self.ui.setupUi(self)
        self._setup_waste_type_dropdown()
        self.ui.buttonBox.accepted.connect(self._get_waste_type)
        self.ui.buttonBox.rejected.connect(self._reject)
        self.waste_type_id = None

    def _setup_waste_type_dropdown(self):
        waste_type_data = requests.get(domain + 'show-all-waste-types').json()
        for item in waste_type_data:
            self.ui.select_waste_type_dropdown.addItem(item['name'])

    def _get_waste_type(self):
        waste_type_data = requests.get(domain + 'show-all-waste-types').json()
        chosen_waste_type_dropdown_id = self.ui.select_waste_type_dropdown.currentIndex()
        waste_type_id = waste_type_data[chosen_waste_type_dropdown_id]['id']
        self.waste_type_id = waste_type_id
        self.hide()

    def _reject(self):
        self.hide()


class FilterLocationWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_FilterLocation()
        self.ui.setupUi(self)
        self._setup_location_dropdown()
        self.ui.buttonBox.accepted.connect(self._get_location)
        self.ui.buttonBox.rejected.connect(self._reject)
        self.location_id = None

    def _setup_location_dropdown(self):
        location_data = requests.get(domain + 'get-all-locations').json()
        jsn_list = json.loads(json.dumps(location_data))

        for item in jsn_list:
            item_data = [str(val) for key, val in item.items()]
            self.ui.select_location_dropdown.addItem(', '.join(item_data))

    def _get_location(self):
        location_data = requests.get(domain + 'get-all-locations').json()
        chosen_location = self.ui.select_location_dropdown.currentIndex()
        location_id = location_data[chosen_location]['id']
        self.location_id = location_id
        self.hide()

    def _reject(self):
        self.hide()


class FilterFillingLevelWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_FilterFillingLevel()
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(self._get_value)
        self.ui.buttonBox.rejected.connect(self._reject)
        self.value = None

    def _get_value(self):
        self.value = self.ui.filling_level.value()
        self.hide()

    def _reject(self):
        self.hide()
