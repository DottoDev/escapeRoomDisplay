import json
import sys
import time

from PyQt5.QtWidgets import *
from PyQt5 import QtCore


class GuiLayout(QWidget):
    def __init__(self):
        super().__init__()
        self.ui()

    def ui(self):

        def hideInputFields():
            grid.removeWidget(spinBox1)
            spinBox1.deleteLater()
            grid.removeWidget(spinBox2)
            spinBox2.deleteLater()
            grid.removeWidget(spinBox3)
            spinBox3.deleteLater()
            grid.removeWidget(submitButton)
            submitButton.deleteLater()


        def changeLAyoutToFinished(self):
            hideInputFields()

            label = QLabel(self)
            label.setText(outputString)
            label.setAlignment(QtCore.Qt.AlignCenter)
            grid.addWidget(label, 0 , 0)
            print("Done")

        def wrongAnswer():
            hideInputFields()
            time.sleep(3)
            spinBox1, spinBox2, spinBox3, submitButton = createButtons()
            grid.addWidget(spinBox1, 2, 0)
            grid.addWidget(spinBox2, 2, 1)
            grid.addWidget(spinBox3, 2, 2)
            grid.addWidget(submitButton, 4, 1)
            print("a")

        def rightAnswer():
            changeLAyoutToFinished(self)

        def validateInput():
            if spinBox1.value() == requiredValue1:
                if spinBox2.value() == requiredValue2:
                    if spinBox3.value() == requiredValue3:
                        return True
            return False

        def submitButtonClicked():
            isValid = validateInput()
            if isValid:
                rightAnswer()
            else:
                wrongAnswer()

        def createButtons():
            spinBox1 = QSpinBox()
            spinBox1.setRange(0, 9)
            spinBox1.setSingleStep(1)
            spinBox1.setValue(0)
            spinBox2 = QSpinBox()
            spinBox2.setRange(0, 9)
            spinBox2.setSingleStep(1)
            spinBox2.setValue(0)
            spinBox3 = QSpinBox()
            spinBox3.setRange(0, 9)
            spinBox3.setSingleStep(1)
            spinBox3.setValue(0)

            submitButton = QPushButton("Bestätigen")

            return spinBox1, spinBox2, spinBox3, submitButton
        def createGrid():

            spinBox1, spinBox2, spinBox3, submitButton = createButtons()
            grid = QGridLayout(self)
            grid.addWidget(spinBox1, 2, 0)
            grid.addWidget(spinBox2, 2, 1)
            grid.addWidget(spinBox3, 2, 2)
            grid.addWidget(submitButton, 4, 1)
            return grid, spinBox1, spinBox2, spinBox3, submitButton

        grid, spinBox1, spinBox2, spinBox3, submitButton = createGrid()
        self.setLayout(grid)
        self.setGeometry(0, 0, 1920, 1080)
        self.setWindowTitle('Escape Room')
        self.showMaximized()

        submitButton.clicked.connect(submitButtonClicked)


def main():
    app = QApplication(sys.argv)
    ex = GuiLayout()
    sys.exit(app.exec_())


if __name__ == "__main__":


    settings = json.load(open("settings.json"))

    requiredValue1 = settings["requiredValue1"]
    requiredValue2 = settings["requiredValue2"]
    requiredValue3 = settings["requiredValue3"]
    outputString = settings["outputString"]

    main()
