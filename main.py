import sys 
from interface import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow

class MeuApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.adicionar_tarefa)
        self.ui.pushButton_2.clicked.connect(self.remover_tarefa)
    

    # Botão de adicionar tarefa
    def adicionar_tarefa(self):
        texto_digitado = self.ui.lineEdit.text() 
        self.ui.listWidget.addItem(texto_digitado)
        self.ui.listWidget.edit()
        self.ui.lineEdit.clear()

    # def lista_editada(self):

    # Botão de remover tarefa
    def remover_tarefa(self):
        posicao = self.ui.listWidget.currentRow()
        self.ui.listWidget.takeItem(posicao)
      
app = QApplication(sys.argv)
janela = MeuApp()
janela.show()
sys.exit(app.exec_())