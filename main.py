import json
import sys
import time

from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import *


class GuiLayout(QWidget):
    def __init__(self):
        super().__init__()
        self.ui()

    def ui(self):

        # def hideSpinBoxFields():
        #     spinBox1.deleteLater()
        #     spinBox2.deleteLater()
        #     spinBox3.deleteLater()
        #     submitButton.deleteLater()

        # def changeSpinBoxLayoutToFinished():
        #     hideSpinBoxFields()
        #
        #     label = QLabel()
        #     label.setText(outputString)
        #     label.setAlignment(QtCore.Qt.AlignCenter)
        #     grid.addWidget(label, 0, 0)

        def wrongAnswer():
            time.sleep(timeAfterWrongInput)
            lineInput.clear()
            msg = QMessageBox()
            msg.setWindowTitle("Falsche Eingabe")
            msg.setText("Ihre Eingabe ist nicht korrekt")
            msg.exec()

        def rightAnswer():
            # changeSpinBoxLayoutToFinished()
            changetextInputLayoutToFinished()

        def changetextInputLayoutToFinished():
            submitButton.deleteLater()
            lineInput.deleteLater()
            label = QLabel()
            label.setText(outputString)
            label.setAlignment(QtCore.Qt.AlignCenter)
            grid.addWidget(label, 0, 0)

        # def validateInputOfSpinBox():
        #     if spinBox1.value() == requiredValue1:
        #         if spinBox2.value() == requiredValue2:
        #             if spinBox3.value() == requiredValue3:
        #                 return True
        #     return False

        def validateInputOfText():
            input = int(lineInput.text())
            return input == requiredValue

        def submitButtonClicked():
            # isValid = validateInputOfSpinBox()
            isValid = validateInputOfText()
            if isValid:
                rightAnswer()
            else:
                wrongAnswer()

        def createSpinBoxButtons():
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

        def createInputFieldButtons():
            lineInput = QLineEdit()
            lineInput.setValidator(QIntValidator())
            lineInput.setMaxLength(3)
            lineInput.setAlignment(Qt.AlignCenter)

            submitButton = QPushButton("Bestätigen")
            return submitButton, lineInput

        def createGrid():

            # spinBox1, spinBox2, spinBox3, submitButton = createSpinBoxButtons()
            submitButton, lineInput = createInputFieldButtons()
            grid = QGridLayout(self)
            # grid.addWidget(spinBox1, 2, 0)
            # grid.addWidget(spinBox2, 2, 1)
            # grid.addWidget(spinBox3, 2, 2)
            grid.addWidget(lineInput, 2, 1)
            grid.addWidget(submitButton, 4, 1)
            # return grid, spinBox1, spinBox2, spinBox3, submitButton
            return grid, lineInput, submitButton

        # grid, spinBox1, spinBox2, spinBox3, submitButton = createGrid()
        grid, lineInput, submitButton = createGrid()
        self.setLayout(grid)
        self.setGeometry(0, 0, 1920, 1080)
        self.setWindowTitle('Escape Room')
        self.showFullScreen()

        submitButton.clicked.connect(submitButtonClicked)


def main():

    app = QApplication(sys.argv)
    ex = GuiLayout()
    sys.exit(app.exec_())


if __name__ == "__main__":
    settings = json.load(open("settings.json"))

    timeAfterWrongInput = settings["timeAfterWrongInput"]
    requiredValue = settings["requiredValue"]
    outputString = settings["outputString"]

    main()
