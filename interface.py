# importy
from PySide2.QtWidgets import QMainWindow, QApplication, QWidget
from ui import Ui_MainWindow
from ui_new_window import Ui_Form
import sys


class Interface(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionAdd_trasmitter.triggered.connect(self._add_transmitter)

    def _list_transmitters(self):
        pass

    def _show_transmitter_data(self):
        pass

    def _add_transmitter(self):
        self.widget = NewWindow()
        self.widget.show()

    def _remove_transmitter(self):
        pass

    def _add_location(self):
        pass

    def _remove_location(self):
        pass

    def _add_waste_type(self):
        pass

    def _remove_waste_type(self):
        pass

    def _show_only_given_waste_type(self):
        pass

    def _show_only_given_location(self):
        pass

    def _show_only_full(self):
        pass


class NewWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)


def guiMain(args):
    app = QApplication(args)
    window = Interface()
    window.show()
    return app.exec_()


if __name__ == '__main__':
    guiMain(sys.argv)
