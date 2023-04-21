import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QTextEdit, QPushButton
from PyQt5.QtCore import QFile, QTextStream
from PyQt5.QtGui import QPixmap


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Création des widgets
        self.label_date = QLabel('Date :')
        self.edit_date = QLineEdit()
        self.label_programme = QLabel('Programme :')
        self.edit_programme = QTextEdit()
        self.button_add = QPushButton('Ajouter')
        self.button_save = QPushButton('Enregistrer')
        self.list_programmes = QTextEdit()
        self.list_programmes.setReadOnly(True)

        # Ajout des widgets au layout vertical
        vbox = QVBoxLayout()
        vbox.addWidget(self.label_date)
        vbox.addWidget(self.edit_date)
        vbox.addWidget(self.label_programme)
        vbox.addWidget(self.edit_programme)
        hbox = QHBoxLayout()
        hbox.addWidget(self.button_add)
        hbox.addWidget(self.button_save)
        vbox.addLayout(hbox)
        vbox.addWidget(self.list_programmes)
        self.setLayout(vbox)

        # Connexion du bouton Ajouter à la méthode add_programme
        self.button_add.clicked.connect(self.add_programme)

        # Connexion du bouton Enregistrer à la méthode save_programmes
        self.button_save.clicked.connect(self.save_programmes)

        # Configuration de la fenêtre
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle('Ma liste de programmes')
        self.show()

    def add_programme(self):
        # Récupération des données
        date = self.edit_date.text()
        programme = self.edit_programme.toPlainText()

        # Ajout des données à la liste
        self.list_programmes.append(f"      \nVOICI TON AGENDA \nDATE : {date}  \nPROGRAMME : {programme}")

        # Effacement des champs de saisie
        self.edit_date.clear()
        self.edit_programme.clear()

    def save_programmes(self):
        # Récupération des données
        programmes = self.list_programmes.toPlainText()

        # Ouverture du fichier en écriture
        file = QFile("programmes.txt")
        if file.open(QFile.WriteOnly | QFile.Text):
            # Écriture des données dans le fichier
            stream = QTextStream(file)
            stream << programmes
            file.close()

    def closeEvent(self, event):
        # Sauvegarde des programmes avant de fermer l'application
        self.save_programmes()
        event.accept()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
