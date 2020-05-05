import json
import csv
import sys
import os

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLineEdit, QMessageBox, QFileDialog, QLabel
from PyQt5.QtCore import pyqtSlot

source_file = ""
destination_file = ""

#-------- Code for packaging as exe --------
def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# -------- Converter Code --------
def output_file(source, destination, filename):
    # Import the file
    filename = source + "\\" + filename
    with open(filename, 'r') as file:
        data = json.load(file)

    # Initialise arrays to hold: who sent the message, when it was sent and the contents
    sender = []
    time = []
    content = []

    # Loop over every message in the JSON file
    for elt in data["messages"]:
        sender.append(str(elt["sender_name"]))
        time.append(str(elt["timestamp_ms"]))
        # Default content to [PHOTO/GIF/VIDEO]
        content.append(elt.get("content", "[PHOTO/GIF/VIDEO]"))

    out_arr = []
    for mess_num in range(len(sender)):
        out_arr.append([sender[mess_num], time[mess_num], content[mess_num]])

    with open(os.path.join(destination + "\\out.csv"), "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        for elt in out_arr:
            writer.writerow(elt)


def main(source, destination, num_files):
    for i in range(num_files):
        infile = "message_" + str(i+1) + ".json"
        output_file(source, destination, infile)


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 textbox - pythonspot.com'
        self.left = 500
        self.top = 500
        self.width = 575
        self.height = 270
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Facebook Message JSON-CSV Convertor")
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create intro text label
        self.intro_text = QLabel(self)
        self.intro_text.move(10,0)
        self.intro_text.resize(2000, 60)
        self.intro_text.setText("Welcome to the Facebook Message JSON to CSV converter! \nPlease use the options below to enter the folder where the JSONs are stored,\nthe folder to save the CSV into and the number of JSONs to convert")

        # Create a button in the window
        self.source_button = QPushButton('Source', self)
        self.source_button.move(310, 80)

        # Create source text label
        self.source_text = QLabel(self)
        self.source_text.move(10, 45)
        self.source_text.resize(290, 100)
        self.source_text.setText("Enter folder where the JSONs are stored:")

        # connect button to function on_click
        self.source_button.clicked.connect(self.source_on_click)

        # Create a destination button in the window
        self.destination_button = QPushButton('Destination', self)
        self.destination_button.move(340, 135)

        # Create destination text label
        self.destination_text = QLabel(self)
        self.destination_text.move(10, 100)
        self.destination_text.resize(320, 100)
        self.destination_text.setText("Enter folder where the CSV should be stored:")

        # connect destination button to function on_click
        self.destination_button.clicked.connect(self.destination_on_click)

        # Create destination text label
        self.num_file_text = QLabel(self)
        self.num_file_text.move(10, 150)
        self.num_file_text.resize(340, 100)
        self.num_file_text.setText("Enter the number of JSON files to be converted:")

        # Create number of files textbox
        self.file_num_box = QLineEdit(self)
        self.file_num_box.move(360, 185)
        self.file_num_box.resize(50, 30)

        # Create submit in the window
        self.submit_button = QPushButton('Submit', self)
        self.submit_button.move(10, 220)

        # Connect submit button to function submit_on_click
        self.submit_button.clicked.connect(self.submit_on_click)

        self.show()

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        if fileName:
            print(fileName)
            return fileName



    @pyqtSlot()
    def source_on_click(self):
        global source_file
        source_file = self.openFileNameDialog()
        self.show()

    @pyqtSlot()
    def destination_on_click(self):
        global destination_file
        destination_file = self.openFileNameDialog()
        self.show()

    @pyqtSlot()
    def submit_on_click(self):
        global source_file
        global destination_file
        try:
            main(source_file, destination_file, int(self.file_num_box.text()))
            print("Successful")
            successful_msg = QMessageBox()
            successful_msg.setWindowTitle("Success")
            successful_msg.setText("JSONs successfully converted. Thanks for using!")
            successful_msg.exec()
        except:
            print("There has been an error")
            fail_msg = QMessageBox()
            fail_msg.setWindowTitle("Error")
            fail_msg.setText("There has been an error converting JSONs. \nPlease check that you entered a number \nand that there is no file named out.csv in the destination folder")
            fail_msg.exec()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(resource_path('JSON_logo.gif')))
    ex = App()
    sys.exit(app.exec_())


