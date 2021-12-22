import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from design import Ui_MainWindow


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.nds_percent = 0
        self.summa = 0
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # input values
        self.ui.nds_percent_input.textChanged.connect(self.nds_percent_input_changed)
        self.ui.summa_input.textChanged.connect(self.summa_input_changed)
        self.add_functions()

    def add_functions(self):
        """calculate, when button pressed"""
        self.ui.minus_btn.clicked.connect(self.nds_minus)
        self.ui.plus_btn.clicked.connect(self.nds_plus)

    def summa_input_changed(self):
        """"""
        if self.ui.summa_input.text() == '':
            pass
        else:
            try:
                self.summa = float(self.ui.summa_input.text())
            except ValueError:
                pass

    def nds_percent_input_changed(self):
        """"""
        if self.ui.nds_percent_input.text() == '':
            pass
        else:
            try:
                self.nds_percent = float(self.ui.nds_percent_input.text())
            except ValueError:
                pass

    def nds_plus(self):
        """when plus buton pressed"""
        stavka_nds = self.nds_percent / 100
        result = float('{:.3f}'.format(
            self.summa + (self.summa * stavka_nds))
        )
        result2 = float('{:.3f}'.format(
            self.summa * stavka_nds)
        )
        # reformat float to string
        result = str(result)
        result2 = str(result2)
        # view result
        self.ui.result_summ_main.setText(result)
        self.ui.result_summ.setText(result2)

    def nds_minus(self):
        """when minus button pressed"""
        result = float('{:.3f}'.format(
            (self.summa * self.nds_percent) / 100)
        )
        result2 = float('{:.3f}'.format(
            self.summa - (self.summa / 100 * self.nds_percent))
        )
        # reformat float to string
        result = str(result)
        result2 = str(result2)
        # view result
        self.ui.result_summ_main.setText(result2)
        self.ui.result_summ.setText(result)


def run():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ != '__main__':
    pass
else:
    run()
