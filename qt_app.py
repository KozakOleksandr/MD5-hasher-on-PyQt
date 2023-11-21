import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFileDialog, QMessageBox, QTextEdit
from PyQt5.QtGui import QPalette, QColor
import hashlib

class MD5HasherApp(QWidget):
    def __init__(self):
        super().__init__()

        self.history = []  # List to store the history entries

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('MD5 Hasher')
        self.setGeometry(300, 300, 400, 300)

        # Set a warm-blue color palette
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(173, 216, 230))  # Warm blue
        palette.setColor(QPalette.WindowText, QColor(0, 0, 128))  # Dark blue
        palette.setColor(QPalette.Button, QColor(100, 149, 237))  # Light blue
        palette.setColor(QPalette.ButtonText, QColor(0, 0, 128))  # Dark blue
        self.setPalette(palette)

        layout = QVBoxLayout()

        # Widgets for input and output
        self.input_label = QLabel('Enter a string:')
        self.input_text = QLineEdit(self)

        self.output_label = QLabel('MD5 Hash:')
        self.output_text = QLineEdit(self)
        self.output_text.setReadOnly(True)

        # Buttons for hash calculation and saving to file
        self.hash_button = QPushButton('Calculate MD5 Hash', self)
        self.hash_button.clicked.connect(self.calculate_md5)

        self.save_button = QPushButton('Save to File', self)
        self.save_button.clicked.connect(self.save_to_file)

        # Widgets for displaying history
        self.history_label = QLabel('History:')
        self.history_text = QTextEdit(self)
        self.history_text.setReadOnly(True)

        # Adding widgets to the layout
        layout.addWidget(self.input_label)
        layout.addWidget(self.input_text)
        layout.addWidget(self.output_label)
        layout.addWidget(self.output_text)
        layout.addWidget(self.hash_button)
        layout.addWidget(self.save_button)
        layout.addWidget(self.history_label)
        layout.addWidget(self.history_text)

        self.setLayout(layout)

    def calculate_md5(self):
        data_to_hash = self.input_text.text()
        md5_hash = hashlib.md5(data_to_hash.encode('utf-8')).hexdigest()
        self.output_text.setText(md5_hash)

        # Add the operation to the history
        self.add_to_history(data_to_hash, md5_hash)

    def save_to_file(self):
        md5_hash = self.output_text.text()
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, "Save to File", "", "Text Files (*.txt);;All Files (*)", options=options)

        if file_name:
            try:
                with open(file_name, 'w') as file:
                    file.write(md5_hash)
                QMessageBox.information(self, 'Success', 'MD5 Hash saved to file: {}'.format(file_name), QMessageBox.Ok)
            except Exception as e:
                QMessageBox.warning(self, 'Error', 'Failed to save to file. Error: {}'.format(str(e)), QMessageBox.Ok)

    def add_to_history(self, query, result):
        # Add the latest operation to the history, limiting it to 5 entries
        history_entry = '{} - {}'.format(query, result)
        self.history.append(history_entry)
        if len(self.history) > 5:
            self.history.pop(0)  # Remove the oldest entry

        # Update the content of the text widget to display the history
        self.update_history_text()

    def update_history_text(self):
        # Update the content of the text widget to display the history
        self.history_text.setPlainText('\n'.join(self.history))