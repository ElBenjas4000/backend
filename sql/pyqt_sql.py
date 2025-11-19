#me ayude de chatgpt aca porque ptqt5 es muy tedioso, pero las funciones son de las del crud

import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget, QMessageBox

API_URL = "http://127.0.0.1:8000"

class CrudWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CRUD PyQt - Test")
        self.setGeometry(200, 200, 350, 400)

        layout = QVBoxLayout()

        # Crear usuario
        layout.addWidget(QLabel("Crear Usuario:"))
        self.input_id = QLineEdit()
        self.input_id.setPlaceholderText("ID del usuario")
        layout.addWidget(self.input_id)

        self.input_name = QLineEdit()
        self.input_name.setPlaceholderText("Nombre del usuario")
        layout.addWidget(self.input_name)

        btn_crear = QPushButton("Crear Usuario")
        btn_crear.clicked.connect(self.crear_usuario)
        layout.addWidget(btn_crear)

        # Mostrar usuarios
        layout.addWidget(QLabel("Usuarios registrados:"))
        self.lista = QListWidget()
        layout.addWidget(self.lista)

        btn_cargar = QPushButton("Cargar Usuarios")
        btn_cargar.clicked.connect(self.cargar_usuarios)
        layout.addWidget(btn_cargar)

        self.setLayout(layout)

    def crear_usuario(self):
        user_id = self.input_id.text().strip()
        name = self.input_name.text().strip()

        if not user_id or not name:
            QMessageBox.warning(self, "Error", "Complete ID y nombre.")
            return

        r = requests.post(f"{API_URL}/crear_usuario", json={"id": user_id, "name": name})
        data = r.json()

        if data.get("success"):
            QMessageBox.information(self, "OK", "Usuario creado correctamente.")
            self.cargar_usuarios()
        else:
            QMessageBox.warning(self, "Error", data.get("message", "Error"))

    def cargar_usuarios(self):
        r = requests.get(f"{API_URL}/usuarios")
        usuarios = r.json()

        self.lista.clear()
        for u in usuarios:
            self.lista.addItem(f"ID: {u['id']} | Nombre: {u['name']}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CrudWindow()
    window.show()
    sys.exit(app.exec_())