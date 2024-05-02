import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget,
                               QStackedWidget, QHBoxLayout, QFrame,QMessageBox,QLabel, QLineEdit,
                                 QTableWidget, QHeaderView, QTableWidgetItem, QGridLayout,
                                 QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QWidget)
from PySide6.QtGui import QPalette, QColor,QIcon, QPixmap
from PySide6.QtCore import Qt



from pl import optimize_paint_mix
from plne import solve_backpack
pl_labels = ["Nombre de composants", "Entrez la viscosité maximale accepté:", "Entrez les dechets maximum accepté"]
plne_labels = ["Nom de l'objet", "Valeur", "Poids"]
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Recherche Opérationnelle")
        
        self.setFixedSize(1400, 700)

        central_widget = QWidget(self)

        self.setCentralWidget(central_widget)
        
        pal = QPalette()
        
        self.setPalette(pal)
        sidebar_color = QColor(26,24,24)  # Dark gray
        content_color = QColor(57, 57, 57)  # Light gray for the content area

        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)  # No margins around the layout
        layout.setSpacing(0)  # No spacing between widgets in the layout

        # Sidebar frame
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

        # Sidebar layout
        sidebar_layout2 = QVBoxLayout(sidebar_frame2)
        sidebar_layout2.setAlignment(Qt.AlignTop)
        sidebar_layout2.setContentsMargins(0, 0, 0, 0)
        sidebar_layout2.setSpacing(0)


        # Buttons for the sidebar
        global btn_page1 
        btn_page1 = QPushButton("Home")
        btn_page1.setFixedHeight(50)

        global btn_page2 
        btn_page2 = QPushButton("PL")
        btn_page2.setFixedHeight(50)

        global btn_page3 
        btn_page3= QPushButton("PLNE")
        btn_page3.setFixedHeight(50)
        # Setting stylesheets to the buttons to ensure no margins or padding
        btn_page1.setFlat(True)
        btn_page1.setFlat(False)
        btn_page1.setStyleSheet("background-color: #82028d; border: none;")
        btn_page2.setFlat(True)
        btn_page3.setFlat(True)

        sidebar_layout2.addWidget(btn_page1)
        sidebar_layout2.addWidget(btn_page2)
        sidebar_layout2.addWidget(btn_page3)

        # Content frame
        content_frame = QFrame()
        content_frame.setPalette(pal)
        content_frame.setAutoFillBackground(True)
        pal.setColor(QPalette.Window, content_color)
        content_frame.setPalette(pal)

        # Layout for the content frame
        content_layout = QVBoxLayout(content_frame)  # Set the layout for the content frame
        content_layout.setContentsMargins(0, 0, 0, 0)  # No margins around the layout
        content_layout.setSpacing(0)  # No spacing between widgets in the layout

        # Stacked widget for managing pages
        self.stacked_widget = QStackedWidget()
        self.stacked_widget.addWidget(self.create_homepage(self.stacked_widget))
        self.stacked_widget.addWidget(self.create_pl_page())
        self.stacked_widget.addWidget(self.create_plne_page())
        content_layout.addWidget(self.stacked_widget) 
        # Connect buttons to switch pages
        btn_page1.clicked.connect(lambda:self.toggle(0))
        btn_page2.clicked.connect(lambda:self.toggle(1))
        btn_page3.clicked.connect(lambda:self.toggle(2))
        


        layout.addWidget(sidebar_frame)
        layout.addWidget(content_frame)
        central_widget.setLayout(layout)



    
    def create_homepage(self, widget):
        """Helper function to create a homepage with labels and buttons."""
        page = QWidget()
        layout = QVBoxLayout(page)

        # Main page label
        label = QLabel("Projet: Application de Recherche Opérationnelle")
        label.setStyleSheet("font-size: 36px; font-weight: bold; color: #82028d")
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)

        label2 = QLabel("Presentation des problèmes de programmation linéaire : \n Par Ladhari Adam, Ben Achour Skander, Oudi Louay et Jeder Seif")
        label2.setStyleSheet("font-size: 16px; font-weight: bold;")
        label2.setAlignment(Qt.AlignCenter)
        layout.addWidget(label2)

        # Placeholder for PL button and its description
        pl_layout = QVBoxLayout()  # Vertical layout for icon, text, and button

        # Icon for PL (Placeholder)
        pl_icon_label = QLabel()
        paint_icon = QPixmap("purple_paint.png")
        paint_icon = paint_icon.scaled(120, 120, Qt.KeepAspectRatio)
        pl_icon_label.setPixmap(paint_icon)  # Assuming you have an icon file
        pl_icon_label.setAlignment(Qt.AlignCenter)
        
        pl_layout.addWidget(pl_icon_label)

        # Text description for PL
        pl_text_label = QLabel("L'entreprise doit préparer un lot de peinture  pour \nune commande spécifique tout en optimisant \n les coûts de production et en minimisant l'impact \n environnemental. Le challenge réside dans l'équilibre \n entre l'utilisation de  composants coûteux \n qui améliorent la qualité et ceux qui sont moins  \n chers mais peut-être moins performants ou plus \n polluants.")
        pl_text_label.setAlignment(Qt.AlignCenter)
        pl_layout.addWidget(pl_text_label)

        # PL Button
        pl_button = QPushButton("PL")
        pl_button.clicked.connect(lambda: widget.setCurrentIndex(1))
        pl_button.setFixedHeight(100)
        pl_button.setFixedWidth(300)
        pl_layout.addWidget(pl_button)

        # Placeholder for PLNE button and its description
        plne_layout = QVBoxLayout()  # Vertical layout for icon, text, and button

        # Icon for PLNE (Placeholder)
        plne_icon_label = QLabel()
        backpack_icon = QPixmap("purple-backpack.png")
        backpack_icon = backpack_icon.scaled(120, 120, Qt.KeepAspectRatio)
        plne_icon_label.setPixmap(backpack_icon)  # Assuming you have an icon file
        
        plne_icon_label.setAlignment(Qt.AlignCenter)
        plne_layout.addWidget(plne_icon_label)

        # Text description for PLNE
        plne_text_label = QLabel("Le problème du sac à dos consiste à sélectionner \nun ensemble d'articles chacun ayant un poids et \n une valeur spécifique afin de maximiser la \n valeur totale portée dans un sac à dos. \nLe défi réside dans la limite de capacité \nde poids du sac à dos nécessitant des choix \nstratégiques pour atteindre la meilleure\n valeur sans dépasser la contrainte de poids.")
        plne_text_label.setAlignment(Qt.AlignCenter)
        plne_layout.addWidget(plne_text_label)

        # PLNE Button
        plne_button = QPushButton("PLNE")
        plne_button.clicked.connect(lambda: widget.setCurrentIndex(2))
        plne_button.setFixedHeight(100)
        plne_button.setFixedWidth(300)
        plne_layout.addWidget(plne_button)

        # Horizontal layout to contain both button layouts
        hbox = QHBoxLayout()
        hbox.addLayout(pl_layout)
        hbox.addLayout(plne_layout)

        layout.addLayout(hbox)

        return page
    
    def create_pl_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)

        # Input fields setup
        grid_layout = QGridLayout()
        self.inputs = []
        for i, label_text in enumerate(pl_labels):
            label = QLabel(label_text)
            line_edit = QLineEdit()
            self.inputs.append(line_edit)
            grid_layout.addWidget(label, i, 0)
            grid_layout.addWidget(line_edit, i, 1)
        
        layout.addLayout(grid_layout)
        
        hlayout = QHBoxLayout()
        layout.addLayout(hlayout)
         # app Button
        app_button = QPushButton("Appliquer")
        app_button.clicked.connect(self.populate_table)
        hlayout.addWidget(app_button)
        app_button.setFixedWidth(200)
        app_button.setFixedHeight(50)
        default_button = QPushButton("Valeurs par defauts")
        default_button.clicked.connect(self.apply_default_values)
        hlayout.addWidget(default_button)
        default_button.setFixedWidth(200)
        default_button.setFixedHeight(50)

        # Table setup
        self.table = QTableWidget()
        self.table.setColumnCount(4)  # "Nom"," Coût/kg", "Viscosité", "Dechet"
        self.table.setHorizontalHeaderLabels(["Nom"," Profit/kg", "Viscosité", "Dechet"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        layout.addWidget(self.table)

        # Solve Button
        solve_button = QPushButton("Solve")
        solve_button.clicked.connect(self.solve_pl)
        solve_button.setFixedHeight(100)
        layout.addWidget(solve_button)

        return page

    def populate_table(self):
        try:
            # Check if the number of components field is empty or invalid
            if not self.inputs[0].text().strip():
                raise ValueError("Le champ 'Nombre de composants' ne peut pas être vide.")
            
            num_products = int(self.inputs[0].text().strip())
            if num_products < 1:
                raise ValueError("Le nombre de composants doit être supérieur à zéro.")

            # Initialize list to store numerical values
            numerical_values = []
            for i in range(1, 3):
                input_value = self.inputs[i].text().strip()
                if not input_value:  # Check if the field is empty
                    raise ValueError(f"Le champ '{pl_labels[i]}' ne peut pas être vide.")
                # Try converting to float
                float_value = float(input_value)
                if float_value < 0:  # Check if the value is positive
                    raise ValueError(f"La valeur '{pl_labels[i]}' doit être positive.")
                numerical_values.append(float_value)
            


            self.table.setRowCount(num_products)
            for i in range(num_products):
                for j in range(3):
                    self.table.setItem(i, j, QTableWidgetItem(""))

        except ValueError as e:
            QMessageBox.critical(None, "Erreur d'entrée", str(e))
            self.table.setRowCount(0)  # Clear table if input is invalid

    def apply_default_values(self):
        self.inputs[0].setText('4')  # Total number of products
        self.inputs[1].setText('500')  # Minimum viscosity, adjusted to a realistic scenario
        self.inputs[2].setText('30')  # Maximum viscosity, high flexibility

        self.populate_table()  # Resize and clear table
        self.fill_dummy_values()  # Fill table with dummy data

    def fill_dummy_values(self):
        num_products = int(self.inputs[0].text())
        
        default_values = [
            ("Produit A", "100", "33", "0.8"),    # Common component, moderate cost, moderate effectiveness
            ("Produit B", "200", "40", "0.5"),   # High-performance additive, high cost, high effectiveness, low garbage
            ("Produit C", "30", "15.2", "1.2"),     # Economical filler, low cost, low effectiveness, higher garbage
            ("Produit D", "300", "22.2", "2")    # Specialty chemical, very high cost, very high effectiveness, minimal garbage
        ]

        for i in range(num_products):
            for j, value in enumerate(default_values[i]):
                self.table.setItem(i, j, QTableWidgetItem(value))

    def solve_pl(self):
        try:
            n = self.table.rowCount()
            composants = []
            couts = {}
            viscosite = {}
            densite = {}
            
            for i in range(n):
                comp_name = self.table.item(i, 0).text().strip()
                composants.append(comp_name)
                couts[comp_name] = float(self.table.item(i, 1).text().strip())
                if couts[comp_name]<0:
                    QMessageBox.warning(self, "Input invalid","Profit de "+comp_name +" ne peut pas etre negative ")
                    return
                viscosite[comp_name] = float(self.table.item(i, 2).text().strip())
                if viscosite[comp_name]<0:
                    QMessageBox.warning(self, "Input invalid","Viscosite de "+ comp_name +" ne peut pas etre negative ")
                    return
                densite[comp_name] = float(self.table.item(i, 3).text().strip())
                if densite[comp_name]<0:
                    QMessageBox.warning(self, "Input invalid","Dechet de "+ comp_name +" ne peut pas etre negative ")
                    return
                
            
            
            visco_max = float(self.inputs[1].text().strip())
            if visco_max<0:
                QMessageBox.warning(self, "Input invalid","Viscosite maximale ne peut pas etre negative ")
                return
            max_garbage = float(self.inputs[2].text().strip())
            if max_garbage<0:
                QMessageBox.warning(self, "Input invalid","Dechet maximal ne peut pas etre negative ")
                return
           

            # Call the paint mixing optimization function
            results = optimize_paint_mix(n, composants, couts, viscosite, densite,visco_max,max_garbage)
            if results["status"] == "Optimal":
                message = "La solution optimal:\n"
                message += f"Profit maximum: ${results['total_cost']:.2f}\n"
                for comp, quantity in results["results"].items():
                    message += f"{comp}: {quantity:.2f} kg\n"
                QMessageBox.information(self, "Optimization Results", message)
            elif results["status"] == "Infeasible":
                QMessageBox.warning(self, "Optimization Results", "Problem is infeasible: " + results["message"])
            else:
                QMessageBox.critical(self, "Optimization Results", "Error: " + results["message"])

        except ValueError as e:
            QMessageBox.critical(None, "Erreur d'entrée", str(e))


    def create_plne_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        
        # Grid layout for initial inputs
        grid_layout = QGridLayout()
        self.nb_produits_input = QLineEdit()
        self.capacite_stockage_input = QLineEdit()
        grid_layout.addWidget(QLabel("Nombre de produits:"), 0, 0)
        grid_layout.addWidget(self.nb_produits_input, 0, 1)
        grid_layout.addWidget(QLabel("Capacité du sac a dos:"), 1, 0)
        grid_layout.addWidget(self.capacite_stockage_input, 1, 1)

        layout.addLayout(grid_layout)

        hbox = QHBoxLayout()
        layout.addLayout(hbox)

        generate_button = QPushButton("Appliquer")
        generate_button.clicked.connect(self.generate_product_inputs)
        generate_button.setFixedWidth(200)
        generate_button.setFixedHeight(50)
        hbox.addWidget(generate_button)

        # Default values button
        default_button = QPushButton("Valeurs par défaut")
        default_button.clicked.connect(self.fill_with_default_values)
        default_button.setFixedWidth(200)
        default_button.setFixedHeight(50)
        hbox.addWidget(default_button)

        

        # Table for product-specific inputs
        self.product_table = QTableWidget()

        self.product_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        layout.addWidget(self.product_table)

        # Solve Button
        solve_button = QPushButton("Solve")
        solve_button.clicked.connect(self.solve_plne)
        solve_button.setFixedHeight(100)
        layout.addWidget(solve_button)

        return page

    def generate_product_inputs(self):
        nb_produits = int(self.nb_produits_input.text())
        self.product_table.setColumnCount(len(plne_labels))
        self.product_table.setHorizontalHeaderLabels(plne_labels)
        self.product_table.setRowCount(nb_produits)
        for i in range(nb_produits):
            for j in range(len(plne_labels)):
                self.product_table.setItem(i, j, QTableWidgetItem())

    def fill_with_default_values(self):
        self.nb_produits_input.setText("3")
        self.generate_product_inputs()
        self.capacite_stockage_input.setText("50")
        default_values = [
            ("Bague Or", "60", "10"),
            ("Colier", "100", "15"),
            ("Contract de la maison ", "120", "30")
        ]
        for i in range(min(3, len(default_values))):
            for j, value in enumerate(default_values[i]):
                self.product_table.setItem(i, j, QTableWidgetItem(value))
    def solve_plne(self):
        try:
            nb_produits = int(self.nb_produits_input.text())
            if nb_produits < 1:
                raise ValueError("Le nombre de produits doit être supérieur à zéro.")
            capacite_stockage = float(self.capacite_stockage_input.text())
            if capacite_stockage < 0:
                raise ValueError("La capacité de stockage doit être positive.")
            noms = []
            valeurs = []
            poids = []
            for i in range(nb_produits):
                nom = self.product_table.item(i, 0).text().strip()
                valeur = float(self.product_table.item(i, 1).text().strip())
                if valeur<0:
                    QMessageBox.warning(self, "Input invalid","Valeur de "+nom +" ne peut pas etre negative ")
                    return
                poid = float(self.product_table.item(i, 2).text().strip())
                if poid<0:
                    QMessageBox.warning(self, "Input invalid","Poid de "+nom +" ne peut pas etre negative ")
                    return
                noms.append(nom)
                valeurs.append(valeur)
                poids.append(poid)
            # Call the backpack optimization function
            results = solve_backpack(noms, valeurs, poids, capacite_stockage)
            if results["status"] == "Optimal":
                message = "Solution optimale trouvée:\n"
                message += f"Valeur totale: ${results['total_value']:.2f}\n"
                for item, quantity in results["results"].items():
                    message += f"{item}: {quantity} unités\n"
                QMessageBox.information(self, "Résultats de l'optimisation", message)
            elif results["status"] == "Infeasible":
                QMessageBox.warning(self, "Résultats de l'optimisation", "Le problème est infaisable: " + results["message"])
            else:
                QMessageBox.critical(self, "Résultats de l'optimisation", "Erreur: " + results["message"])
        except ValueError as e:
            QMessageBox.critical(None, "Erreur d'entrée", str(e))

    def toggle(self, index):
        
        self.stacked_widget.setCurrentIndex(index)
        if index == 0:
            btn_page3.setFlat(True)
            btn_page3.setStyleSheet("background-color: #1a1818")
            btn_page2.setFlat(True)
            btn_page2.setStyleSheet("background-color: #1a1818")
            btn_page1.setFlat(False)
            btn_page1.setStyleSheet("background-color: #82028d; border: none;")
        elif index == 1:
            btn_page1.setFlat(True)
            btn_page1.setStyleSheet("background-color: #1a1818")
            btn_page3.setFlat(True)
            btn_page3.setStyleSheet("background-color: #1a1818")
            
            btn_page2.setFlat(False)
            btn_page2.setStyleSheet("background-color: #82028d; border: none;")
        else:
            btn_page1.setFlat(True)
            btn_page1.setStyleSheet("background-color: #1a1818")
            btn_page2.setFlat(True)
            btn_page2.setStyleSheet("background-color: #1a1818")
            btn_page3.setFlat(False)
            btn_page3.setStyleSheet("background-color: #82028d; border: none;")
        
        



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
