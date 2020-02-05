#! python3
import sys
from googletrans import Translator
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QLineEdit, QTextEdit, QPushButton
from PyQt5.QtCore import Qt, pyqtSlot
import clipboard

class MainWindow(QMainWindow):

    polish_to_english = True

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # Main window
        self.setWindowTitle("Translator")
        self.setMinimumWidth(400)
        self.setMinimumHeight(710)
        self.setStyleSheet("QMainWindow {background: 'red';}")

        # Edit text
        self.textbox = QTextEdit(self)
        self.textbox.move(10, 10)
        self.textbox.resize(380, 320)
        self.textbox.setPlaceholderText('Polski')

        # Button when done
        self.button = QPushButton('Translate', self)
        self.button.setToolTip('Translate')
        self.button.move(10, 340)
        self.button.clicked.connect(self.on_click_translate)

        # Setup Copy button
        self.copyButton = QPushButton('Copy', self)
        self.copyButton.setToolTip('Copy')
        self.copyButton.move(120, 340)
        self.button.clicked.connect(self.on_click_copy)

        # Swap button
        self.swapButton = QPushButton('Switch', self)
        self.swapButton.setToolTip('Switch')
        self.swapButton.move(230, 340)
        self.swapButton.clicked.connect(self.on_click_switch)

        # Setup translator
        self.translator = Translator()

        # Setup display box
        self.textboxRes = QTextEdit(self)
        self.textboxRes.move(10, 380)
        self.textboxRes.resize(380, 320)
        self.textboxRes.setReadOnly(True)
        self.textboxRes.setPlaceholderText('Angielski')

    @pyqtSlot()
    def on_click_translate(self):
        s = self.textbox.toPlainText()
        print("Translating: {}".format(s))
        res = ''
        if self.polish_to_english:
            res = self.translator.translate(text=s, src='pl', dest='en')
        else:
            res = self.translator.translate(text=s, src='en', dest='pl')
        print("Result: {}".format(res.text))
        self.textboxRes.clear()
        self.textboxRes.setText(res.text)

    @pyqtSlot()
    def on_click_copy(self):
        s = self.textboxRes.toPlainText()
        clipboard.copy(s)

    @pyqtSlot()
    def on_click_switch(self):
        self.polish_to_english =  not self.polish_to_english
        if self.polish_to_english:
            self.textbox.setPlaceholderText('Polski')
            self.textboxRes.setPlaceholderText('Angielski')
        else:
            self.textbox.setPlaceholderText('Angielski')
            self.textboxRes.setPlaceholderText('Polski')

app = QApplication([])

window = MainWindow()
window.show()

app.exec_()