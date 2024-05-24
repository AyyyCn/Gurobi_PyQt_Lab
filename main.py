import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget,
                               QStackedWidget, QHBoxLayout, QFrame, QMessageBox, QLabel, QLineEdit,
                               QTableWidget, QHeaderView, QTableWidgetItem, QGridLayout, QInputDialog, QComboBox)
from PySide6.QtGui import QPalette, QColor, QIcon, QPixmap
from PySide6.QtCore import Qt

from pl import optimize_paint_mix
from plne import solve_backpack

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Recherche Opérationnelle")
        self.setFixedSize(1400, 700)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        pal = QPalette()
        self.setPalette(pal)
        sidebar_color = QColor(26, 24, 24)
        content_color = QColor(57, 57, 57)

        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        sidebar_frame = QFrame()
        sidebar_frame.setFixedWidth(50)
        sidebar_frame.setPalette(pal)
        sidebar_frame.setAutoFillBackground(True)
        sidebar_frame.setContentsMargins(0, 0, 0, 0)

        pal.setColor(QPalette.Window, sidebar_color)
        sidebar_frame.setPalette(pal)

        sidebar_layout = QVBoxLayout(sidebar_frame)
        sidebar_layout.setContentsMargins(0, 0, 0, 0)
        sidebar_layout.setSpacing(0)

        sidebar_frame2 = QFrame()
        sidebar_frame2.setFixedHeight(200)
        sidebar_frame2.setPalette(pal)
        sidebar_frame2.setAutoFillBackground(True)
        sidebar_frame2.setContentsMargins(0, 0, 0, 0)

        sidebar_layout.addWidget(sidebar_frame2)

        sidebar_layout2 = QVBoxLayout(sidebar_frame2)
        sidebar_layout2.setAlignment(Qt.AlignTop)
        sidebar_layout2.setContentsMargins(0, 0, 0, 0)
        sidebar_layout2.setSpacing(0)

        global btn_page1
        btn_page1 = QPushButton("Home")
        btn_page1.setFixedHeight(50)

        global btn_page2
        btn_page2 = QPushButton("PL")
        btn_page2.setFixedHeight(50)

        global btn_page3
        btn_page3 = QPushButton("PLNE")
        btn_page3.setFixedHeight(50)

        btn_page1.setFlat(True)
        btn_page1.setFlat(False)
        btn_page1.setStyleSheet("background-color: #82028d; border: none;")
        btn_page2.setFlat(True)
        btn_page3.setFlat(True)

        sidebar_layout2.addWidget(btn_page1)
        sidebar_layout2.addWidget(btn_page2)
        sidebar_layout2.addWidget(btn_page3)

        content_frame = QFrame()
        content_frame.setPalette(pal)
        content_frame.setAutoFillBackground(True)
        pal.setColor(QPalette.Window, content_color)
        content_frame.setPalette(pal)

        content_layout = QVBoxLayout(content_frame)
        content_layout.setContentsMargins(0, 0, 0, 0)
        content_layout.setSpacing(0)

        self.stacked_widget = QStackedWidget()
        self.stacked_widget.addWidget(self.create_homepage(self.stacked_widget))
        self.stacked_widget.addWidget(self.create_pl_page())
        self.stacked_widget.addWidget(self.create_plne_page())
        content_layout.addWidget(self.stacked_widget)

        btn_page1.clicked.connect(lambda: self.toggle(0))
        btn_page2.clicked.connect(lambda: self.toggle(1))
        btn_page3.clicked.connect(lambda: self.toggle(2))

        layout.addWidget(sidebar_frame)
        layout.addWidget(content_frame)
        central_widget.setLayout(layout)

    def create_homepage(self, widget):
        page = QWidget()
        layout = QVBoxLayout(page)

        label = QLabel("Projet: Application de Recherche Opérationnelle")
        label.setStyleSheet("font-size: 36px; font-weight: bold; color: #82028d")
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)

        label2 = QLabel("Presentation des problèmes de programmation linéaire : \n Par Ladhari Adam, Ben Achour Skander, Oudi Louay et Jeder Seif")
        label2.setStyleSheet("font-size: 16px; font-weight: bold;")
        label2.setAlignment(Qt.AlignCenter)
        layout.addWidget(label2)

        pl_layout = QVBoxLayout()

        pl_icon_label = QLabel()
        paint_icon = QPixmap("purple_paint.png")
        paint_icon = paint_icon.scaled(120, 120, Qt.KeepAspectRatio)
        pl_icon_label.setPixmap(paint_icon)
        pl_icon_label.setAlignment(Qt.AlignCenter)

        pl_layout.addWidget(pl_icon_label)

        pl_text_label = QLabel("L'entreprise doit préparer un lot de peinture pour une commande spécifique tout en optimisant les coûts de production et en minimisant l'impact environnemental.")
        pl_text_label.setAlignment(Qt.AlignCenter)
        pl_layout.addWidget(pl_text_label)

        pl_button = QPushButton("PL")
        pl_button.clicked.connect(lambda: widget.setCurrentIndex(1))
        pl_button.setFixedHeight(100)
        pl_button.setFixedWidth(300)
        pl_layout.addWidget(pl_button)

        plne_layout = QVBoxLayout()

        plne_icon_label = QLabel()
        backpack_icon = QPixmap("purple-backpack.png")
        backpack_icon = backpack_icon.scaled(120, 120, Qt.KeepAspectRatio)
        plne_icon_label.setPixmap(backpack_icon)
        plne_icon_label.setAlignment(Qt.AlignCenter)
        plne_layout.addWidget(plne_icon_label)

        plne_text_label = QLabel("Le problème du sac à dos consiste à sélectionner un ensemble d'articles chacun ayant un poids et une valeur spécifique afin de maximiser la valeur totale portée dans un sac à dos.")
        plne_text_label.setAlignment(Qt.AlignCenter)
        plne_layout.addWidget(plne_text_label)

        plne_button = QPushButton("PLNE")
        plne_button.clicked.connect(lambda: widget.setCurrentIndex(2))
        plne_button.setFixedHeight(100)
        plne_button.setFixedWidth(300)
        plne_layout.addWidget(plne_button)

        hbox = QHBoxLayout()
        hbox.addLayout(pl_layout)
        hbox.addLayout(plne_layout)

        layout.addLayout(hbox)

        return page

    def create_pl_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)

        grid_layout = QGridLayout()
        self.constraints_grid_layout = QGridLayout()
        self.inputs = []
        self.dynamic_columns = ["Profit/kg"]

        self.add_dynamic_column_button = QPushButton("Ajouter une colonne")
        self.add_dynamic_column_button.clicked.connect(self.add_dynamic_column)

        for i, label_text in enumerate(["Nombre de composants"]):
            label = QLabel(label_text)
            line_edit = QLineEdit()
            self.inputs.append({"label": label_text, "value": line_edit})
            self.constraints_grid_layout.addWidget(label, i, 0)
            self.constraints_grid_layout.addWidget(line_edit, i, 1)

        grid_layout.addLayout(self.constraints_grid_layout, 0, 1)
        grid_layout.addWidget(self.add_dynamic_column_button, 1, 0, 1, 2)

        layout.addLayout(grid_layout)

        hlayout = QHBoxLayout()
        layout.addLayout(hlayout)

        app_button = QPushButton("Appliquer")
        app_button.clicked.connect(self.populate_table)
        hlayout.addWidget(app_button)
        app_button.setFixedWidth(200)
        app_button.setFixedHeight(50)

        self.table = QTableWidget()
        self.table.setColumnCount(len(self.dynamic_columns) + 1)
        self.table.setHorizontalHeaderLabels(["Nom"] + self.dynamic_columns)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        layout.addWidget(self.table)

        solve_button = QPushButton("Solve")
        solve_button.clicked.connect(self.solve_pl)
        solve_button.setFixedHeight(100)
        layout.addWidget(solve_button)

        return page

    from PySide6.QtWidgets import QInputDialog, QComboBox, QLabel

    def add_dynamic_column(self):
        column_name, ok = QInputDialog.getText(self, "Nouvelle colonne", "Entrez le nom de la nouvelle colonne:")
        if ok and column_name:
            # Append the column name to dynamic_columns
            self.dynamic_columns.append(column_name)
            constraint_name = column_name + " Max"
            label = QLabel(constraint_name)
            line_edit = QLineEdit()
            self.inputs.append({"label": constraint_name, "value": line_edit})
            self.constraints_grid_layout.addWidget(label, len(self.inputs), 0)
            self.constraints_grid_layout.addWidget(line_edit, len(self.inputs), 1)
            
            self.table.setColumnCount(len(self.dynamic_columns) + 1)
            self.table.setHorizontalHeaderLabels(["Nom"] + self.dynamic_columns)

    def populate_table(self):
        try:
            if not self.inputs[0]["value"].text().strip():
                raise ValueError("Le champ 'Nombre de composants' ne peut pas être vide.")

            num_products = int(self.inputs[0]["value"].text().strip())
            if num_products < 1:
                raise ValueError("Le nombre de composants doit être supérieur à zéro.")
            if(len(self.inputs) <= 1):
                raise IndexError("Ajouter des colonnes")
            
            numerical_values = []
            for i in range(1, len(self.inputs)):
                text = self.inputs[i]["value"].text().strip()
                if text:
                    numerical_values.append(float(text))

            self.table.setRowCount(num_products)
            for i in range(num_products):
                for j, col_name in enumerate(self.dynamic_columns):
                    item = QTableWidgetItem("")
                    self.table.setItem(i, j + 1, item)
                self.table.setItem(i, 0, QTableWidgetItem(f"Composant {i + 1}"))

        except ValueError as e:
            self.show_error_message(str(e))

    def show_error_message(self, message):
        error_dialog = QMessageBox()
        error_dialog.setIcon(QMessageBox.Critical)
        error_dialog.setText("Erreur")
        error_dialog.setInformativeText(message)
        error_dialog.setWindowTitle("Erreur")
        error_dialog.exec()

    def solve_pl(self):
        try:
            if(len(self.inputs) <= 1):
                raise IndexError("Ajouter des colonnes")
            
            num_products = int(self.inputs[0]["value"].text().strip())

            profits = []

            additional_data = {}

            for i in range(num_products):
                profit_item = self.table.item(i, self.dynamic_columns.index("Profit/kg") + 1)

                if not profit_item:
                    raise ValueError(f"Missing data for component {i + 1}.")
                
                try:
                    profits.append(float(profit_item.text().strip()))
                except:
                    raise ValueError(f"Valeur invalide dans la colonne Profit/kg pour le produit {i + 1}.")


                for col_name in self.dynamic_columns:
                    if col_name not in ["Profit/kg"]:
                        item = self.table.item(i, self.dynamic_columns.index(col_name) + 1)
                        if item:
                            if col_name not in additional_data:
                                additional_data[col_name] = []
                            try:
                                additional_data[col_name].append(float(item.text().strip()))
                            except:
                                raise ValueError(f"Valeur invalide dans la colonne {col_name} pour le produit {i + 1}.")

            # Constraints: Each sublist should correspond to one constraint
            constraints = []
            limits = []

            # Add additional constraints to the constraints list
            for key, values in additional_data.items():
                input_index = self.dynamic_columns.index(key)
                if input_index < len(self.inputs):
                    try:
                        max_limit = float(self.inputs[input_index]["value"].text().strip())
                    except:
                        raise ValueError(f"Valeur invalide dans {self.inputs[input_index]['label']}.")
                    constraints.append(values)
                    limits.append(max_limit)
                else:
                    raise IndexError(f"No input field found for constraint '{key}'.")

            decision_vars = list(range(num_products))
            to_maximize = profits

            # Call the optimization function
            result = optimize_paint_mix(decision_vars, to_maximize, constraints, limits)

            # Process the result
            if result["status"] == "Optimal":
                solution_message = "Optimal Solution Found:\n"
                for var in result["results"]:
                    solution_message += f"Component {var + 1}: {result['results'][var]:.4f}\n"
                solution_message += f"Total Profit: {result['total_value']:.4f}"
            elif result["status"] == "Infeasible":
                solution_message = "No feasible solution found that meets all constraints."
            else:
                solution_message = "Optimization did not solve successfully."

            QMessageBox.information(self, "Solution", solution_message)

        except ValueError as e:
            self.show_error_message(str(e))
        except IndexError as e:
            self.show_error_message(f"Configuration error: {str(e)}")

    def create_plne_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)

        self.dynamic_columns_plne = ["Poids"]
        self.inputs_plne = []

        self.add_dynamic_column_button_plne = QPushButton("Ajouter une colonne")
        self.add_dynamic_column_button_plne.clicked.connect(self.add_dynamic_column_plne)

        self.constraints_grid_layout_plne = QGridLayout()

        layout.addWidget(self.add_dynamic_column_button_plne)
        layout.addLayout(self.constraints_grid_layout_plne)

        self.populate_default_constraints()

        self.table_plne = QTableWidget()
        self.table_plne.setColumnCount(len(self.dynamic_columns_plne) + 1)
        self.table_plne.setHorizontalHeaderLabels(["Nom"] + self.dynamic_columns_plne)
        self.table_plne.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        layout.addWidget(self.table_plne)

        app_button_plne = QPushButton("Appliquer")
        app_button_plne.clicked.connect(self.populate_table_plne)
        layout.addWidget(app_button_plne)

        solve_button_plne = QPushButton("Solve")
        solve_button_plne.clicked.connect(self.solve_plne)
        layout.addWidget(solve_button_plne)

        return page

    def add_dynamic_column_plne(self):
        column_name, ok = QInputDialog.getText(self, "Nouvelle colonne", "Entrez le nom de la nouvelle colonne:")
        if ok and column_name:
            # Append the column name to dynamic_columns
            self.dynamic_columns_plne.append(column_name)
            constraint_name = column_name + " Max"
            label = QLabel(constraint_name)
            line_edit = QLineEdit()
            self.inputs_plne.append({"label": constraint_name, "value": line_edit})
            self.constraints_grid_layout_plne.addWidget(label, len(self.inputs_plne), 0)
            self.constraints_grid_layout_plne.addWidget(line_edit, len(self.inputs_plne), 1)
            
            self.table_plne.setColumnCount(len(self.dynamic_columns_plne) + 1)
            self.table_plne.setHorizontalHeaderLabels(["Nom"] + self.dynamic_columns_plne)


    def populate_table_plne(self):
        try:
            num_items, ok = QInputDialog.getInt(self, "Nombre d'articles", "Entrez le nombre d'articles:")
            if not ok or num_items <= 0:
                raise ValueError("Nombre d'articles invalide.")
            self.table_plne.setRowCount(num_items)
            self.apply_default_values_plne(num_items)
        except ValueError as e:
            QMessageBox.warning(self, "Erreur", str(e))

    def apply_default_values_plne(self, num_items):
        for row in range(num_items):
            item_name = f"Article {row + 1}"
            self.table_plne.setItem(row, 0, QTableWidgetItem(item_name))
            for col in range(1, self.table_plne.columnCount()):
                default_value = "0"
                self.table_plne.setItem(row, col, QTableWidgetItem(default_value))

    def solve_plne(self):
        try:
            names = []
            values = []
            constraints = []
            limits = []

            for row in range(self.table_plne.rowCount()):
                names.append(self.table_plne.item(row, 0).text())
                values.append(float(self.table_plne.item(row, 1).text()))
                constraints.append([float(self.table_plne.item(row, col).text()) for col in range(2, self.table_plne.columnCount())])

            for input_data in self.inputs_plne:
                limits.append(float(input_data["value"].text()))

            result = solve_backpack(names, values, constraints, limits)
            self.show_solution_plne(result)
        except ValueError as e:
            QMessageBox.warning(self, "Erreur", str(e))

    def show_solution_plne(self, result):
        solution_text = f"Statut: {result['status']}\n"
        if 'results' in result:
            solution_text += "Résultats:\n"
            for name, value in result['results'].items():
                solution_text += f"  {name}: {value}\n"
            solution_text += f"Valeur totale: {result['total_value']}\n"
        if 'message' in result:
            solution_text += f"Message: {result['message']}\n"

        QMessageBox.information(self, "Solution", solution_text)

    def toggle(self, page):
        btn_page1.setFlat(True)
        btn_page2.setFlat(True)
        btn_page3.setFlat(True)
        if page == 0:
            btn_page1.setFlat(False)
            btn_page1.setStyleSheet("background-color: #82028d; border: none;")
        if page == 1:
            btn_page2.setFlat(False)
            btn_page2.setStyleSheet("background-color: #82028d; border: none;")
        if page == 2:
            btn_page3.setFlat(False)
            btn_page3.setStyleSheet("background-color: #82028d; border: none;")
        self.stacked_widget.setCurrentIndex(page)

    def populate_default_constraints(self):
        constraint_names = ["Poids Max"]
        for i, constraint_name in enumerate(constraint_names):
            label = QLabel(constraint_name)
            line_edit = QLineEdit()
            self.inputs_plne.append({"label": constraint_name, "value": line_edit})
            self.constraints_grid_layout_plne.addWidget(label, i, 0)
            self.constraints_grid_layout_plne.addWidget(line_edit, i, 1)
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
