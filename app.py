import sys
from googletrans import Translator
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QLineEdit, QTextEdit, QPushButton
from PyQt5.QtCore import Qt, pyqtSlot

class MainWindow(QMainWindow):

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
        self.button.setToolTip('Okay')
        self.button.move(10, 340)
        self.button.clicked.connect(self.on_click)

        # Setup Copy button
        self.copyButton = QPushButton('Copy', self)
        self.copyButton.setToolTip('Copy')
        self.copyButton.move(120, 340)

        # Setup translator
        self.translator = Translator()

        # Setup display box
        self.textboxRes = QTextEdit(self)
        self.textboxRes.move(10, 380)
        self.textboxRes.resize(380, 320)
        self.textboxRes.setReadOnly(True)
        self.textboxRes.setPlaceholderText('Angielski')

        
        

    @pyqtSlot()
    def on_click(self):
        s = self.textbox.toPlainText()
        print("Translating {}".format(s))
        res = self.translator.translate(text=s, src='pl', dest='en')
        print(res.text)
        self.textboxRes.clear()
        self.textboxRes.setText(res.text)


app = QApplication([])

window = MainWindow()
window.show()

app.exec_()