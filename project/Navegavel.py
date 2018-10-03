import sys
from PyQt5 import QtGui, QtWidgets, QtCore, QtTest

class Botao(QtWidgets.QMainWindow):
	def __init__(self, string, parent):
		super(QtWidgets.QMainWindow, self).__init__()
		self.botao = QtWidgets.QPushButton(string, parent)

class CaixaMarcar(QtWidgets.QMainWindow):
	def __init__(self, string, parent):
		super(QtWidgets.QMainWindow, self).__init__()
		self.checkBox = QtWidgets.QCheckBox(string, parent)

class MenuSuperior(QtWidgets.QMainWindow):
	def __init__(self, parent):
		super(QtWidgets.QMainWindow, self).__init__()
		self.mainMenu = parent.menuBar()

class AcaoMenu(QtWidgets.QMainWindow):
	def __init__(self, string, parent):
		super(QtWidgets.QMainWindow, self).__init__()
		self.extractAction = QtWidgets.QAction(string, parent)

class CaixaMenssagemOK(QtWidgets.QMainWindow):
	def __init__(self, nomecaixa, texto, parent):
		super(QtWidgets.QMainWindow, self).__init__()
		self.pop = QtWidgets.QMessageBox.question(parent, nomecaixa, texto, QtWidgets.QMessageBox.Ok)

class CaixaMenssagemYESNO(QtWidgets.QMainWindow):
	def __init__(self, nomecaixa, texto, parent):
		super(QtWidgets.QMainWindow, self).__init__()
		self.pop = QtWidgets.QMessageBox.question(parent, nomecaixa, texto, QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)

class BarraFerramentas(QtWidgets.QMainWindow):
	def __init__(self, string, parent):
		super(QtWidgets.QMainWindow, self).__init__()
		self.toolBar = parent.addToolBar(string)

class AcaoBarraFerranentas(QtWidgets.QMainWindow):
	def __init__(self, nomeArquivo, texto, parent):
		super(QtWidgets.QMainWindow, self).__init__()
		self.extractAction = QtWidgets.QAction(QtGui.QIcon(nomeArquivo), texto, parent)

class TelaLogin(QtWidgets.QMainWindow):
	def __init__(self, parent=None):
		super(TelaLogin, self).__init__()

		self.setGeometry(50, 50, 500, 300)
		self.setMinimumSize(800, 600)
		self.setMaximumSize(800, 600)
		self.setWindowTitle("Organizador PET-CoCE")
		self.setWindowIcon(QtGui.QIcon('IconePetGrande.png'))

		self.label = QtWidgets.QLabel(self)
		self.label.setGeometry(280, 210, 64, 15)
		self.label.setObjectName("label")
		self.label_2 = QtWidgets.QLabel(self)
		self.label_2.setGeometry(500, 210, 64, 15)
		self.label_2.setObjectName("label_2")
		self.label_3 = QtWidgets.QLabel(self)
		self.label_3.setGeometry(320, 260, 181, 20)
		self.label_3.setObjectName("label_3")
		self.label_4 = QtWidgets.QLabel(self)
		self.label_4.setGeometry(300, 260, 221, 20)
		self.label_4.setObjectName("label_3")

		self.lineEdit = QtWidgets.QLineEdit(self)
		self.lineEdit.setGeometry(240, 230, 113, 23)
		self.lineEdit.setObjectName("lineEdit")
		self.lineEdit_2 = QtWidgets.QLineEdit(self)
		self.lineEdit_2.setGeometry(460, 230, 113, 23)
		self.lineEdit_2.setObjectName("lineEdit_2")

		self.btn1 = Botao("Acessar", self)
		self.btn1.botao.move(300, 280)
		self.btn1.botao.resize(83, 23)
		self.btn2 = Botao("Cancelar", self)
		self.btn2.botao.move(430, 280)
		self.btn2.botao.resize(83, 23)

		self.home()

	def home(self):
		self.btn1.botao.clicked.connect(self.VerificaDadosVazios)
		self.btn1.botao.clicked.connect(self.VerificaLogin)
		self.btn2.botao.clicked.connect(self.close_application)

		self.label.setText("Login")
		self.label_2.setText("Senha")
		self.label_3.setText("login ou senha incorretos")
		self.label_3.setStyleSheet('color: red')
		self.label_3.hide()
		self.label_4.setText("nao podem existir campos vazios")
		self.label_4.setStyleSheet('color: red')
		self.label_4.hide()

		self.show()

	def AbreTelaInicial(self):
		self.GIU2 = TelaInicial(self)

	def VerificaLogin(self):
		login = self.lineEdit.text()
		senha = self.lineEdit_2.text()
		loginADM = "admin"
		senhaADM = "admin"
		if(str(login) == loginADM and str(senha) == senhaADM):
			self.AbreTelaInicial()
			self.hide()
		elif((str(login) != loginADM or str(senha) != senhaADM) and (str(login) != '' and str(senha) != '')):
			self.label_3.show()
			QtTest.QTest.qWait(1000)
			self.label_3.hide()

	def VerificaDadosVazios(self):
		login = self.lineEdit.text()
		senha = self.lineEdit_2.text()
		if(str(login) == '' or str(senha) == ''):
			self.label_4.show()
			QtTest.QTest.qWait(1000)
			self.label_4.hide()

	def close_application(self):
		print("Programa Fechado")
		sys.exit()

class TelaInicial(QtWidgets.QMainWindow):
	def __init__(self, parent):
		super(TelaInicial, self).__init__(parent)
		self.setGeometry(50, 50, 500, 300)
		self.setMinimumSize(800, 600)
		self.setMaximumSize(800, 600)
		self.setWindowTitle("Tela Inicial")
		self.setWindowIcon(QtGui.QIcon('IconePetGrande.png'))

		self.btn1 = Botao("Equipamentos", self)
		self.btn1.botao.move(212, 200)
		self.btn1.botao.resize(101, 23)
		self.btn2 = Botao("Emprestimos", self)
		self.btn2.botao.move(450, 200)
		self.btn2.botao.resize(101, 23)
		self.btn3 = Botao("Cancelar", self)
		self.btn3.botao.move(340, 310)
		self.btn3.botao.resize(83, 23)

		self.home()

	def home(self):
		self.btn1.botao.clicked.connect(self.abreEquipamentos)
		self.btn2.botao.clicked.connect(self.abreEmprestimos)
		self.btn3.botao.clicked.connect(self.close_application)

		self.show()

	def abreEmprestimos(self, parent):
		self.GIU5 = Emprestimos(self)
		self.hide()

	def abreEquipamentos(self, parent):
		self.GIU6 = Equipamentos(self)
		self.hide()

	def close_application(self, parent):
		self.hide()
		self.parent().show()

	def realizaListagem(self, parent):
		self.GIU9 = OperacoesComDados(self)
		self.hide()

class Equipamentos(QtWidgets.QMainWindow):
	def __init__(self, parent):
		super(Equipamentos, self).__init__(parent)
		self.setGeometry(50, 50, 500, 300)
		self.setMinimumSize(800, 600)
		self.setMaximumSize(800, 600)
		self.setWindowTitle("Equipamentos")
		self.setWindowIcon(QtGui.QIcon('IconePetGrande.png'))

		self.btn1 = Botao("Realiza Listagem", self)
		self.btn1.botao.move(320, 270)
		self.btn1.botao.resize(131, 23)
		self.btn2 = Botao("Cancelar", self)
		self.btn2.botao.move(320, 370)
		self.btn2.botao.resize(131, 23)

		self.home()

	def home(self):
		self.btn1.botao.clicked.connect(self.realizaListagem)
		self.btn2.botao.clicked.connect(self.cancelar)

		self.show()

	def realizaListagem(self, parent):
		self.GIU9 = OperacoesComDadosEQ(self)
		self.hide()

	def cancelar(self, parent):
		self.hide()
		self.parent().show()

class Emprestimos(QtWidgets.QMainWindow):
	def __init__(self, parent):
		super(Emprestimos, self).__init__(parent)
		self.setGeometry(50, 50, 500, 300)
		self.setMinimumSize(800, 600)
		self.setMaximumSize(800, 600)
		self.setWindowTitle("Emprestimos")
		self.setWindowIcon(QtGui.QIcon('IconePetGrande.png'))

		self.btn1 = Botao("Realiza Listagem", self)
		self.btn1.botao.move(320, 270)
		self.btn1.botao.resize(131, 23)
		self.btn2 = Botao("Cancelar", self)
		self.btn2.botao.move(320, 370)
		self.btn2.botao.resize(131, 23)

		self.home()

	def home(self):
		self.btn1.botao.clicked.connect(self.realizaListagem)
		self.btn2.botao.clicked.connect(self.cancelar)

		self.show()

	def realizaListagem(self, parent):
		self.GIU9 = OperacoesComDadosEP(self)
		self.hide()

	def cancelar(self, parent):
		self.hide()
		self.parent().show()	

class OperacoesComDadosEQ(QtWidgets.QMainWindow):
	def __init__(self, parent):
		super(OperacoesComDadosEQ, self).__init__(parent)
		self.setGeometry(50, 50, 500, 300)
		self.setMinimumSize(800, 600)
		self.setMaximumSize(800, 600)
		self.setWindowTitle("Operacoes Com Dados")
		self.setWindowIcon(QtGui.QIcon('IconePetGrande.png'))

		self.btn1 = Botao("Cadastrar", self)
		self.btn1.botao.move(50, 570)
		self.btn1.botao.resize(83, 23)
		self.btn2 = Botao("Editar", self)
		self.btn2.botao.move(180, 570)
		self.btn2.botao.resize(83, 23)
		self.btn3 = Botao("Excluir", self)
		self.btn3.botao.move(310, 570)
		self.btn3.botao.resize(83, 23)
		self.btn4 = Botao("Cancelar", self)
		self.btn4.botao.move(400, 570)
		self.btn4.botao.resize(83, 23)

		self.label = QtWidgets.QLabel(self)
		self.label.setGeometry(610, 10, 64, 21)
		self.label.setObjectName("label")

		self.lineEdit = QtWidgets.QLineEdit(self)
		self.lineEdit.setGeometry(670, 10, 113, 23)
		self.lineEdit.setObjectName("lineEdit")

		self.tabela = QtWidgets.QTableWidget(self)
		self.tabela.setGeometry(0, 50, 800, 500)
		self.tabela.setColumnCount(15)
		item = QtWidgets.QTableWidgetItem()
		self.tabela.setHorizontalHeaderItem(0, item)
		item = QtWidgets.QTableWidgetItem()
		self.tabela.setHorizontalHeaderItem(1, item)
		item = QtWidgets.QTableWidgetItem()
		self.tabela.setHorizontalHeaderItem(2, item)
		item = QtWidgets.QTableWidgetItem()
		self.tabela.setHorizontalHeaderItem(3, item)
		item = QtWidgets.QTableWidgetItem()
		self.tabela.setHorizontalHeaderItem(4, item)
		item = QtWidgets.QTableWidgetItem()
		self.tabela.setHorizontalHeaderItem(5, item)
		item = QtWidgets.QTableWidgetItem()
		self.tabela.setHorizontalHeaderItem(6, item)
		item = QtWidgets.QTableWidgetItem()
		self.tabela.setHorizontalHeaderItem(7, item)
		item = QtWidgets.QTableWidgetItem()
		self.tabela.setHorizontalHeaderItem(8, item)
		item = QtWidgets.QTableWidgetItem()
		self.tabela.setHorizontalHeaderItem(9, item)
		item = QtWidgets.QTableWidgetItem()
		self.tabela.setHorizontalHeaderItem(10, item)
		item = QtWidgets.QTableWidgetItem()
		self.tabela.setHorizontalHeaderItem(11, item)
		item = QtWidgets.QTableWidgetItem()
		self.tabela.setHorizontalHeaderItem(12, item)
		item = QtWidgets.QTableWidgetItem()
		self.tabela.setHorizontalHeaderItem(13, item)
		item = QtWidgets.QTableWidgetItem()
		self.tabela.setHorizontalHeaderItem(14, item)
		self.tabela.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
		self.tabela.setSelectionBehavior(QtWidgets.QTableView.SelectRows)

		self.home()

	def home(self):
		self.btn2.botao.hide()
		self.btn3.botao.hide()

		item = self.tabela.horizontalHeaderItem(0)
		item.setText("Nome")
		item = self.tabela.horizontalHeaderItem(1)
		item.setText("Status")
		item = self.tabela.horizontalHeaderItem(2)
		item.setText("Categoria")
		item = self.tabela.horizontalHeaderItem(3)
		item.setText("Nota")
		item = self.tabela.horizontalHeaderItem(4)
		item.setText("Armario")
		item = self.tabela.horizontalHeaderItem(5)
		item.setText("Sala")
		item = self.tabela.horizontalHeaderItem(6)
		item.setText("Caixa")
		item = self.tabela.horizontalHeaderItem(7)
		item.setText("Limite de Tempo de Emprestimo")
		item = self.tabela.horizontalHeaderItem(8)
		item.setText("Nao Emprestavel")
		item = self.tabela.horizontalHeaderItem(9)
		item.setText("Data da Ultima Revisao")
		item = self.tabela.horizontalHeaderItem(10)
		item.setText("Comentario")
		item = self.tabela.horizontalHeaderItem(11)
		item.setText("Nao Reutilizavel")
		item = self.tabela.horizontalHeaderItem(12)
		item.setText("Numero de Patrimonio")
		item = self.tabela.horizontalHeaderItem(13)
		item.setText("Descricao")
		item = self.tabela.horizontalHeaderItem(14)
		item.setText("Quantidade")
		__sortingEnabled = self.tabela.isSortingEnabled()
		self.tabela.setSortingEnabled(False)
		self.tabela.setSortingEnabled(__sortingEnabled)
		self.tabela.itemClicked.connect(self.showBotaoEditarExcluir)

		self.btn1.botao.clicked.connect(self.cadastro)
		self.btn2.botao.clicked.connect(self.editar)
		self.btn3.botao.clicked.connect(self.excluir)
		self.btn4.botao.clicked.connect(self.cancelar)

		self.label.setText("Pesquisa")

		self.show()

	def showBotaoEditarExcluir(self):
		self.btn1.botao.hide()
		self.btn2.botao.show()
		self.btn3.botao.show()

		self.tabela.itemSelectionChanged.connect(self.hideBotaoEditarExcluir)

	def hideBotaoEditarExcluir(self):
		self.btn1.botao.show()
		self.btn2.botao.hide()
		self.btn3.botao.hide()
		self.tabela.itemSelectionChanged.connect(self.showBotaoEditarExcluir)

	def cadastro(self):
		GIU10 = CadastroEQ(self)

	def incluinatabela(self, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15):
		rowPosition = self.tabela.rowCount()
		self.tabela.insertRow(rowPosition)
		self.tabela.setItem(rowPosition , 0, QtWidgets.QTableWidgetItem(t1))
		self.tabela.setItem(rowPosition , 1, QtWidgets.QTableWidgetItem(t2))
		self.tabela.setItem(rowPosition , 2, QtWidgets.QTableWidgetItem(t3))
		self.tabela.setItem(rowPosition , 3, QtWidgets.QTableWidgetItem(t4))
		self.tabela.setItem(rowPosition , 4, QtWidgets.QTableWidgetItem(t5))
		self.tabela.setItem(rowPosition , 5, QtWidgets.QTableWidgetItem(t6))
		self.tabela.setItem(rowPosition , 6, QtWidgets.QTableWidgetItem(t7))
		self.tabela.setItem(rowPosition , 7, QtWidgets.QTableWidgetItem(t8))
		self.tabela.setItem(rowPosition , 8, QtWidgets.QTableWidgetItem(t9))
		self.tabela.setItem(rowPosition , 9, QtWidgets.QTableWidgetItem(t10))
		self.tabela.setItem(rowPosition , 10, QtWidgets.QTableWidgetItem(t11))
		self.tabela.setItem(rowPosition , 11, QtWidgets.QTableWidgetItem(t12))
		self.tabela.setItem(rowPosition , 12, QtWidgets.QTableWidgetItem(t13))
		self.tabela.setItem(rowPosition , 13, QtWidgets.QTableWidgetItem(t14))
		self.tabela.setItem(rowPosition , 14, QtWidgets.QTableWidgetItem(t15))

	def editar(self):
		GIU11 = EditarEQ(self)

	def editadatabela(self, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15):
		indexes = self.tabela.selectionModel().selectedRows()
		if(t1 != ''):
			for index in sorted(indexes):
				self.tabela.item(int(index.row()), 0).setText(t1)
		if(t2 != ''):
			for index in sorted(indexes):
				self.tabela.item(int(index.row()), 1).setText(t2)
		if(t3 != ''):
			for index in sorted(indexes):
				self.tabela.item(int(index.row()), 2).setText(t3)
		if(t4 != ''):
			for index in sorted(indexes):
				self.tabela.item(int(index.row()), 3).setText(t4)
		if(t5 != ''):
			for index in sorted(indexes):
				self.tabela.item(int(index.row()), 4).setText(t5)
		if(t6 != ''):
			for index in sorted(indexes):
				self.tabela.item(int(index.row()), 5).setText(t6)
		if(t7 != ''):
			for index in sorted(indexes):
				self.tabela.item(int(index.row()), 6).setText(t7)
		if(t8 != ''):
			for index in sorted(indexes):
				self.tabela.item(int(index.row()), 7).setText(t8)
		if(t9 != ''):
			for index in sorted(indexes):
				self.tabela.item(int(index.row()), 8).setText(t9)
		if(t10 != ''):
			for index in sorted(indexes):
				self.tabela.item(int(index.row()), 9).setText(t10)
		if(t11 != ''):
			for index in sorted(indexes):
				self.tabela.item(int(index.row()), 10).setText(t11)
		if(t12 != ''):
			for index in sorted(indexes):
				self.tabela.item(int(index.row()), 11).setText(t12)
		if(t13 != ''):
			for index in sorted(indexes):
				self.tabela.item(int(index.row()), 12).setText(t13)
		if(t14 != ''):
			for index in sorted(indexes):
				self.tabela.item(int(index.row()), 13).setText(t14)
		if(t15 != ''):
			for index in sorted(indexes):
				self.tabela.item(int(index.row()), 14).setText(t15)


	def excluir(self):
		indexes = self.tabela.selectionModel().selectedRows()
		choice = QtWidgets.QMessageBox.question(self, 'Aviso!', "Excluir Linha?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
		if QtWidgets.QMessageBox.Yes:
			for index in sorted(indexes):
				self.tabela.removeRow(int(index.row()))
		else:
			pass

	def cancelar(self, event):
		self.hide()
		self.parent().show()

class CadastroEQ(QtWidgets.QMainWindow):
	def __init__(self, parent):
		super(CadastroEQ, self).__init__(parent)
		self.setMinimumSize(660, 320)
		self.setMaximumSize(660, 320)
		self.setWindowTitle("Cadastro")
		self.setWindowIcon(QtGui.QIcon('IconePetGrande.png'))

		self.label = QtWidgets.QLabel(self)
		self.label.setGeometry(10, 20, 64, 21)
		self.label.setObjectName("label")
		self.label_2 = QtWidgets.QLabel(self)
		self.label_2.setGeometry(10, 70, 64, 21)
		self.label_2.setObjectName("label_2")
		self.label_3 = QtWidgets.QLabel(self)
		self.label_3.setGeometry(3, 120, 71, 20)
		self.label_3.setObjectName("label_3")
		self.label_4 = QtWidgets.QLabel(self)
		self.label_4.setGeometry(10, 170, 64, 21)
		self.label_4.setObjectName("label_4")
		self.label_5 = QtWidgets.QLabel(self)
		self.label_5.setGeometry(10, 220, 64, 21)
		self.label_5.setObjectName("label_5")
		self.label_6 = QtWidgets.QLabel(self)
		self.label_6.setGeometry(200, 20, 64, 21)
		self.label_6.setObjectName("label_6")
		self.label_7 = QtWidgets.QLabel(self)
		self.label_7.setGeometry(200, 70, 64, 21)
		self.label_7.setObjectName("label_7")
		self.label_8 = QtWidgets.QLabel(self)
		self.label_8.setGeometry(200, 110, 81, 41)
		self.label_8.setObjectName("label_8")
		self.label_9 = QtWidgets.QLabel(self)
		self.label_9.setGeometry(200, 170, 91, 31)
		self.label_9.setObjectName("label_9")
		self.label_10 = QtWidgets.QLabel(self)
		self.label_10.setGeometry(200, 210, 101, 41)
		self.label_10.setObjectName("label_10")
		self.label_11 = QtWidgets.QLabel(self)
		self.label_11.setGeometry(430, 20, 81, 21)
		self.label_11.setObjectName("label_11")
		self.label_12 = QtWidgets.QLabel(self)
		self.label_12.setGeometry(430, 70, 81, 31)
		self.label_12.setObjectName("label_12")
		self.label_13 = QtWidgets.QLabel(self)
		self.label_13.setGeometry(430, 120, 81, 31)
		self.label_13.setObjectName("label_13")
		self.label_14 = QtWidgets.QLabel(self)
		self.label_14.setGeometry(430, 170, 64, 21)
		self.label_14.setObjectName("label_14")
		self.label_15 = QtWidgets.QLabel(self)
		self.label_15.setGeometry(430, 220, 81, 20)
		self.label_15.setObjectName("label_15")
		self.label_16 = QtWidgets.QLabel(self)
		self.label_16.setGeometry(280, 250, 131, 31)
		self.label_16.setObjectName("label_16")

		self.lineEdit = QtWidgets.QLineEdit(self)
		self.lineEdit.setGeometry(70, 20, 113, 23)
		self.lineEdit.setObjectName("lineEdit")
		self.lineEdit_2 = QtWidgets.QLineEdit(self)
		self.lineEdit_2.setGeometry(70, 70, 113, 23)
		self.lineEdit_2.setObjectName("lineEdit_2")
		self.lineEdit_3 = QtWidgets.QLineEdit(self)
		self.lineEdit_3.setGeometry(70, 120, 113, 23)
		self.lineEdit_3.setObjectName("lineEdit_3")
		self.lineEdit_4 = QtWidgets.QLineEdit(self)
		self.lineEdit_4.setGeometry(70, 170, 113, 23)
		self.lineEdit_4.setObjectName("lineEdit_4")
		self.lineEdit_5 = QtWidgets.QLineEdit(self)
		self.lineEdit_5.setGeometry(70, 220, 113, 23)
		self.lineEdit_5.setObjectName("lineEdit_5")
		self.lineEdit_6 = QtWidgets.QLineEdit(self)
		self.lineEdit_6.setGeometry(300, 20, 113, 23)
		self.lineEdit_6.setObjectName("lineEdit_6")
		self.lineEdit_7 = QtWidgets.QLineEdit(self)
		self.lineEdit_7.setGeometry(300, 70, 113, 23)
		self.lineEdit_7.setObjectName("lineEdit_7")
		self.lineEdit_8 = QtWidgets.QLineEdit(self)
		self.lineEdit_8.setGeometry(300, 120, 113, 23)
		self.lineEdit_8.setObjectName("lineEdit_8")
		self.lineEdit_9 = QtWidgets.QLineEdit(self)
		self.lineEdit_9.setGeometry(300, 170, 113, 23)
		self.lineEdit_9.setObjectName("lineEdit_9")
		self.lineEdit_10 = QtWidgets.QLineEdit(self)
		self.lineEdit_10.setGeometry(300, 220, 113, 23)
		self.lineEdit_10.setObjectName("lineEdit_10")
		self.lineEdit_11 = QtWidgets.QLineEdit(self)
		self.lineEdit_11.setGeometry(540, 20, 113, 23)
		self.lineEdit_11.setObjectName("lineEdit_11")
		self.lineEdit_12 = QtWidgets.QLineEdit(self)
		self.lineEdit_12.setGeometry(540, 70, 113, 23)
		self.lineEdit_12.setObjectName("lineEdit_12")
		self.lineEdit_13 = QtWidgets.QLineEdit(self)
		self.lineEdit_13.setGeometry(540, 120, 113, 23)
		self.lineEdit_13.setObjectName("lineEdit_13")
		self.lineEdit_14 = QtWidgets.QLineEdit(self)
		self.lineEdit_14.setGeometry(540, 170, 113, 23)
		self.lineEdit_14.setObjectName("lineEdit_14")
		self.lineEdit_15 = QtWidgets.QLineEdit(self)
		self.lineEdit_15.setGeometry(540, 220, 113, 23)
		self.lineEdit_15.setObjectName("lineEdit_15")

		self.btn1 = Botao("Cadastrar", self)
		self.btn1.botao.move(170, 250)
		self.btn1.botao.resize(83, 23)
		self.btn2 = Botao("Cancelar", self)
		self.btn2.botao.move(420, 250)
		self.btn2.botao.resize(83, 23)

		self.home()

	def home(self):
		self.label.setText("Nome")
		self.label_2.setText("Status")
		self.label_3.setText("Categoria")
		self.label_4.setText("Nota")
		self.label_5.setText("Armario")
		self.label_6.setText("Sala")
		self.label_7.setText("Caixa")
		self.label_8.setText("Limite de" + "\n" + "Tempo de" + "\n" + "Emprestimo")
		self.label_9.setText("Nao" + "\n" + "Emprestavel")
		self.label_10.setText("Data da" + "\n" + "Ultima Revisao")
		self.label_11.setText("Comentario")
		self.label_12.setText("Nao" + "\n" + "Reutilizavel")
		self.label_13.setText("Numero de" + "\n" + "Patrimonio")
		self.label_14.setText("Descricao")
		self.label_15.setText("Quantidade")
		self.label_16.setText("Existem campos" + "\n" + "vazios")
		self.label_16.setStyleSheet('color: red')
		self.label_16.hide()

		self.btn1.botao.clicked.connect(self.cadastrar)
		self.btn2.botao.clicked.connect(self.cancelar)

		self.show()

	def cadastrar(self, parent):
		t1 = str(self.lineEdit.text())
		t2 = str(self.lineEdit_2.text())
		t3 = str(self.lineEdit_3.text())
		t4 = str(self.lineEdit_4.text())
		t5 = str(self.lineEdit_5.text())
		t6 = str(self.lineEdit_6.text())
		t7 = str(self.lineEdit_7.text())
		t8 = str(self.lineEdit_8.text())
		t9 = str(self.lineEdit_9.text())
		t10 = str(self.lineEdit_10.text())
		t11 = str(self.lineEdit_11.text())
		t12 = str(self.lineEdit_12.text())
		t13 = str(self.lineEdit_13.text())
		t14 = str(self.lineEdit_14.text())
		t15 = str(self.lineEdit_15.text())

		if(t1 == '' or t2 == '' or t3 == '' or t4 == '' or t5 == '' or t6 == '' or t7 == '' or t8 == '' or t9 == '' or t10 == '' or t11 == '' or t12 == '' or t13 == '' or t14 == '' or t15 == ''):
			self.label_16.show()
			QtTest.QTest.qWait(1000)
			self.label_16.hide()
		else:
			self.parent().incluinatabela(t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15)
			self.hide()

	def cancelar(self, parent):
		self.parent().show()
		self.hide()

class EditarEQ(QtWidgets.QMainWindow):
	def __init__(self, parent):
		super(EditarEQ, self).__init__(parent)
		self.setMinimumSize(660, 320)
		self.setMaximumSize(660, 320)
		self.setWindowTitle("Editar")
		self.setWindowIcon(QtGui.QIcon('IconePetGrande.png'))

		self.label = QtWidgets.QLabel(self)
		self.label.setGeometry(10, 20, 64, 21)
		self.label.setObjectName("label")
		self.label_2 = QtWidgets.QLabel(self)
		self.label_2.setGeometry(10, 70, 64, 21)
		self.label_2.setObjectName("label_2")
		self.label_3 = QtWidgets.QLabel(self)
		self.label_3.setGeometry(3, 120, 71, 20)
		self.label_3.setObjectName("label_3")
		self.label_4 = QtWidgets.QLabel(self)
		self.label_4.setGeometry(10, 170, 64, 21)
		self.label_4.setObjectName("label_4")
		self.label_5 = QtWidgets.QLabel(self)
		self.label_5.setGeometry(10, 220, 64, 21)
		self.label_5.setObjectName("label_5")
		self.label_6 = QtWidgets.QLabel(self)
		self.label_6.setGeometry(200, 20, 64, 21)
		self.label_6.setObjectName("label_6")
		self.label_7 = QtWidgets.QLabel(self)
		self.label_7.setGeometry(200, 70, 64, 21)
		self.label_7.setObjectName("label_7")
		self.label_8 = QtWidgets.QLabel(self)
		self.label_8.setGeometry(200, 110, 81, 41)
		self.label_8.setObjectName("label_8")
		self.label_9 = QtWidgets.QLabel(self)
		self.label_9.setGeometry(200, 170, 91, 31)
		self.label_9.setObjectName("label_9")
		self.label_10 = QtWidgets.QLabel(self)
		self.label_10.setGeometry(200, 210, 101, 41)
		self.label_10.setObjectName("label_10")
		self.label_11 = QtWidgets.QLabel(self)
		self.label_11.setGeometry(430, 20, 81, 21)
		self.label_11.setObjectName("label_11")
		self.label_12 = QtWidgets.QLabel(self)
		self.label_12.setGeometry(430, 70, 81, 31)
		self.label_12.setObjectName("label_12")
		self.label_13 = QtWidgets.QLabel(self)
		self.label_13.setGeometry(430, 120, 81, 31)
		self.label_13.setObjectName("label_13")
		self.label_14 = QtWidgets.QLabel(self)
		self.label_14.setGeometry(430, 170, 64, 21)
		self.label_14.setObjectName("label_14")
		self.label_15 = QtWidgets.QLabel(self)
		self.label_15.setGeometry(430, 220, 81, 20)
		self.label_15.setObjectName("label_15")
		self.label_16 = QtWidgets.QLabel(self)
		self.label_16.setGeometry(280, 250, 131, 31)
		self.label_16.setObjectName("label_16")

		self.lineEdit = QtWidgets.QLineEdit(self)
		self.lineEdit.setGeometry(70, 20, 113, 23)
		self.lineEdit.setObjectName("lineEdit")
		self.lineEdit_2 = QtWidgets.QLineEdit(self)
		self.lineEdit_2.setGeometry(70, 70, 113, 23)
		self.lineEdit_2.setObjectName("lineEdit_2")
		self.lineEdit_3 = QtWidgets.QLineEdit(self)
		self.lineEdit_3.setGeometry(70, 120, 113, 23)
		self.lineEdit_3.setObjectName("lineEdit_3")
		self.lineEdit_4 = QtWidgets.QLineEdit(self)
		self.lineEdit_4.setGeometry(70, 170, 113, 23)
		self.lineEdit_4.setObjectName("lineEdit_4")
		self.lineEdit_5 = QtWidgets.QLineEdit(self)
		self.lineEdit_5.setGeometry(70, 220, 113, 23)
		self.lineEdit_5.setObjectName("lineEdit_5")
		self.lineEdit_6 = QtWidgets.QLineEdit(self)
		self.lineEdit_6.setGeometry(300, 20, 113, 23)
		self.lineEdit_6.setObjectName("lineEdit_6")
		self.lineEdit_7 = QtWidgets.QLineEdit(self)
		self.lineEdit_7.setGeometry(300, 70, 113, 23)
		self.lineEdit_7.setObjectName("lineEdit_7")
		self.lineEdit_8 = QtWidgets.QLineEdit(self)
		self.lineEdit_8.setGeometry(300, 120, 113, 23)
		self.lineEdit_8.setObjectName("lineEdit_8")
		self.lineEdit_9 = QtWidgets.QLineEdit(self)
		self.lineEdit_9.setGeometry(300, 170, 113, 23)
		self.lineEdit_9.setObjectName("lineEdit_9")
		self.lineEdit_10 = QtWidgets.QLineEdit(self)
		self.lineEdit_10.setGeometry(300, 220, 113, 23)
		self.lineEdit_10.setObjectName("lineEdit_10")
		self.lineEdit_11 = QtWidgets.QLineEdit(self)
		self.lineEdit_11.setGeometry(540, 20, 113, 23)
		self.lineEdit_11.setObjectName("lineEdit_11")
		self.lineEdit_12 = QtWidgets.QLineEdit(self)
		self.lineEdit_12.setGeometry(540, 70, 113, 23)
		self.lineEdit_12.setObjectName("lineEdit_12")
		self.lineEdit_13 = QtWidgets.QLineEdit(self)
		self.lineEdit_13.setGeometry(540, 120, 113, 23)
		self.lineEdit_13.setObjectName("lineEdit_13")
		self.lineEdit_14 = QtWidgets.QLineEdit(self)
		self.lineEdit_14.setGeometry(540, 170, 113, 23)
		self.lineEdit_14.setObjectName("lineEdit_14")
		self.lineEdit_15 = QtWidgets.QLineEdit(self)
		self.lineEdit_15.setGeometry(540, 220, 113, 23)
		self.lineEdit_15.setObjectName("lineEdit_15")

		self.btn1 = Botao("Editar", self)
		self.btn1.botao.move(170, 250)
		self.btn1.botao.resize(83, 23)
		self.btn2 = Botao("Cancelar", self)
		self.btn2.botao.move(420, 250)
		self.btn2.botao.resize(83, 23)

		self.home()

	def home(self):
		self.label.setText("Nome")
		self.label_2.setText("Status")
		self.label_3.setText("Categoria")
		self.label_4.setText("Nota")
		self.label_5.setText("Armario")
		self.label_6.setText("Sala")
		self.label_7.setText("Caixa")
		self.label_8.setText("Limite de" + "\n" + "Tempo de" + "\n" + "Emprestimo")
		self.label_9.setText("Nao" + "\n" + "Emprestavel")
		self.label_10.setText("Data da" + "\n" + "Ultima Revisao")
		self.label_11.setText("Comentario")
		self.label_12.setText("Nao" + "\n" + "Reutilizavel")
		self.label_13.setText("Numero de" + "\n" + "Patrimonio")
		self.label_14.setText("Descricao")
		self.label_15.setText("Quantidade")

		self.btn1.botao.clicked.connect(self.editar)
		self.btn2.botao.clicked.connect(self.cancelar)

		self.show()

	def editar(self, parent):
		t1 = str(self.lineEdit.text())
		t2 = str(self.lineEdit_2.text())
		t3 = str(self.lineEdit_3.text())
		t4 = str(self.lineEdit_4.text())
		t5 = str(self.lineEdit_5.text())
		t6 = str(self.lineEdit_6.text())
		t7 = str(self.lineEdit_7.text())
		t8 = str(self.lineEdit_8.text())
		t9 = str(self.lineEdit_9.text())
		t10 = str(self.lineEdit_10.text())
		t11 = str(self.lineEdit_11.text())
		t12 = str(self.lineEdit_12.text())
		t13 = str(self.lineEdit_13.text())
		t14 = str(self.lineEdit_14.text())
		t15 = str(self.lineEdit_15.text())

		self.parent().editadatabela(t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15)
		self.hide()

	def cancelar(self, parent):
		self.parent().show()
		self.hide()

class OperacoesComDadosEP(QtWidgets.QMainWindow):
	def __init__(self, parent):
		super(OperacoesComDadosEP, self).__init__(parent)
		self.setGeometry(50, 50, 500, 300)
		self.setMinimumSize(800, 600)
		self.setMaximumSize(800, 600)
		self.setWindowTitle("Operacoes Com Dados")
		self.setWindowIcon(QtGui.QIcon('IconePetGrande.png'))

		self.btn1 = Botao("Cadastrar", self)
		self.btn1.botao.move(50, 570)
		self.btn1.botao.resize(83, 23)
		self.btn2 = Botao("Editar", self)
		self.btn2.botao.move(180, 570)
		self.btn2.botao.resize(83, 23)
		self.btn3 = Botao("Excluir", self)
		self.btn3.botao.move(310, 570)
		self.btn3.botao.resize(83, 23)
		self.btn4 = Botao("Cancelar", self)
		self.btn4.botao.move(400, 570)
		self.btn4.botao.resize(83, 23)

		self.label = QtWidgets.QLabel(self)
		self.label.setGeometry(610, 10, 64, 21)
		self.label.setObjectName("label")

		self.lineEdit = QtWidgets.QLineEdit(self)
		self.lineEdit.setGeometry(670, 10, 113, 23)
		self.lineEdit.setObjectName("lineEdit")

		self.tabela = QtWidgets.QTableWidget(self)
		self.tabela.setGeometry(0, 50, 800, 500)
		self.tabela.setColumnCount(12)
		item = QtWidgets.QTableWidgetItem()
		self.tabela.setHorizontalHeaderItem(0, item)
		item = QtWidgets.QTableWidgetItem()
		self.tabela.setHorizontalHeaderItem(1, item)
		item = QtWidgets.QTableWidgetItem()
		self.tabela.setHorizontalHeaderItem(2, item)
		item = QtWidgets.QTableWidgetItem()
		self.tabela.setHorizontalHeaderItem(3, item)
		item = QtWidgets.QTableWidgetItem()
		self.tabela.setHorizontalHeaderItem(4, item)
		item = QtWidgets.QTableWidgetItem()
		self.tabela.setHorizontalHeaderItem(5, item)
		item = QtWidgets.QTableWidgetItem()
		self.tabela.setHorizontalHeaderItem(6, item)
		item = QtWidgets.QTableWidgetItem()
		self.tabela.setHorizontalHeaderItem(7, item)
		item = QtWidgets.QTableWidgetItem()
		self.tabela.setHorizontalHeaderItem(8, item)
		item = QtWidgets.QTableWidgetItem()
		self.tabela.setHorizontalHeaderItem(9, item)
		item = QtWidgets.QTableWidgetItem()
		self.tabela.setHorizontalHeaderItem(10, item)
		item = QtWidgets.QTableWidgetItem()
		self.tabela.setHorizontalHeaderItem(11, item)
		self.tabela.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
		self.tabela.setSelectionBehavior(QtWidgets.QTableView.SelectRows)

		self.home()

	def home(self):
		self.btn2.botao.hide()
		self.btn3.botao.hide()

		item = self.tabela.horizontalHeaderItem(0)
		item.setText("Nome da Pessoa")
		item = self.tabela.horizontalHeaderItem(1)
		item.setText("ID do Equipamento")
		item = self.tabela.horizontalHeaderItem(2)
		item.setText("Data do Emprestimo")
		item = self.tabela.horizontalHeaderItem(3)
		item.setText("Data da Devolucao")
		item = self.tabela.horizontalHeaderItem(4)
		item.setText("Comentario")
		item = self.tabela.horizontalHeaderItem(5)
		item.setText("Hora do Emprestimo")
		item = self.tabela.horizontalHeaderItem(6)
		item.setText("Hora da Devolucao")
		item = self.tabela.horizontalHeaderItem(7)
		item.setText("Data Prevista da Devolucao")
		item = self.tabela.horizontalHeaderItem(8)
		item.setText("Status Inicial do Equipamento")
		item = self.tabela.horizontalHeaderItem(9)
		item.setText("Status Final do Equipamento")
		item = self.tabela.horizontalHeaderItem(10)
		item.setText("Motivo")
		item = self.tabela.horizontalHeaderItem(11)
		item.setText("Atraso")
		__sortingEnabled = self.tabela.isSortingEnabled()
		self.tabela.setSortingEnabled(False)
		self.tabela.setSortingEnabled(__sortingEnabled)
		self.tabela.itemClicked.connect(self.showBotaoEditarExcluir)

		self.btn1.botao.clicked.connect(self.cadastro)
		self.btn2.botao.clicked.connect(self.editar)
		self.btn3.botao.clicked.connect(self.excluir)
		self.btn4.botao.clicked.connect(self.cancelar)

		self.label.setText("Pesquisa")

		self.show()

	def showBotaoEditarExcluir(self):
		self.btn1.botao.hide()
		self.btn2.botao.show()
		self.btn3.botao.show()

		self.tabela.itemSelectionChanged.connect(self.hideBotaoEditarExcluir)

	def hideBotaoEditarExcluir(self):
		self.btn1.botao.show()
		self.btn2.botao.hide()
		self.btn3.botao.hide()
		self.tabela.itemSelectionChanged.connect(self.showBotaoEditarExcluir)

	def cadastro(self):
		GIU12 = CadastroEP(self)

	def incluinatabela(self, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12):
		rowPosition = self.tabela.rowCount()
		self.tabela.insertRow(rowPosition)
		self.tabela.setItem(rowPosition , 0, QtWidgets.QTableWidgetItem(t1))
		self.tabela.setItem(rowPosition , 1, QtWidgets.QTableWidgetItem(t2))
		self.tabela.setItem(rowPosition , 2, QtWidgets.QTableWidgetItem(t3))
		self.tabela.setItem(rowPosition , 3, QtWidgets.QTableWidgetItem(t4))
		self.tabela.setItem(rowPosition , 4, QtWidgets.QTableWidgetItem(t5))
		self.tabela.setItem(rowPosition , 5, QtWidgets.QTableWidgetItem(t6))
		self.tabela.setItem(rowPosition , 6, QtWidgets.QTableWidgetItem(t7))
		self.tabela.setItem(rowPosition , 7, QtWidgets.QTableWidgetItem(t8))
		self.tabela.setItem(rowPosition , 8, QtWidgets.QTableWidgetItem(t9))
		self.tabela.setItem(rowPosition , 9, QtWidgets.QTableWidgetItem(t10))
		self.tabela.setItem(rowPosition , 10, QtWidgets.QTableWidgetItem(t11))
		self.tabela.setItem(rowPosition , 11, QtWidgets.QTableWidgetItem(t12))

	def editar(self):
		GIU13 = EditarEP(self)

	def editadatabela(self, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12):
		indexes = self.tabela.selectionModel().selectedRows()
		if(t1 != ''):
			for index in sorted(indexes):
				self.tabela.item(int(index.row()), 0).setText(t1)
		if(t2 != ''):
			for index in sorted(indexes):
				self.tabela.item(int(index.row()), 1).setText(t2)
		if(t3 != ''):
			for index in sorted(indexes):
				self.tabela.item(int(index.row()), 2).setText(t3)
		if(t4 != ''):
			for index in sorted(indexes):
				self.tabela.item(int(index.row()), 3).setText(t4)
		if(t5 != ''):
			for index in sorted(indexes):
				self.tabela.item(int(index.row()), 4).setText(t5)
		if(t6 != ''):
			for index in sorted(indexes):
				self.tabela.item(int(index.row()), 5).setText(t6)
		if(t7 != ''):
			for index in sorted(indexes):
				self.tabela.item(int(index.row()), 6).setText(t7)
		if(t8 != ''):
			for index in sorted(indexes):
				self.tabela.item(int(index.row()), 7).setText(t8)
		if(t9 != ''):
			for index in sorted(indexes):
				self.tabela.item(int(index.row()), 8).setText(t9)
		if(t10 != ''):
			for index in sorted(indexes):
				self.tabela.item(int(index.row()), 9).setText(t10)
		if(t11 != ''):
			for index in sorted(indexes):
				self.tabela.item(int(index.row()), 10).setText(t11)
		if(t12 != ''):
			for index in sorted(indexes):
				self.tabela.item(int(index.row()), 11).setText(t12)


	def excluir(self):
		indexes = self.tabela.selectionModel().selectedRows()
		choice = QtWidgets.QMessageBox.question(self, 'Aviso!', "Excluir Linha?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
		if QtWidgets.QMessageBox.Yes:
			for index in sorted(indexes):
				self.tabela.removeRow(int(index.row()))
		else:
			pass

	def cancelar(self, event):
		self.hide()
		self.parent().show()

class CadastroEP(QtWidgets.QMainWindow):
	def __init__(self, parent):
		super(CadastroEP, self).__init__(parent)
		self.setMinimumSize(660, 320)
		self.setMaximumSize(660, 320)
		self.setWindowTitle("Cadastro")
		self.setWindowIcon(QtGui.QIcon('IconePetGrande.png'))

		self.label = QtWidgets.QLabel(self)
		self.label.setGeometry(3, 20, 71, 31)
		self.label.setObjectName("label")
		self.label_2 = QtWidgets.QLabel(self)
		self.label_2.setGeometry(3, 70, 91, 41)
		self.label_2.setObjectName("label_2")
		self.label_3 = QtWidgets.QLabel(self)
		self.label_3.setGeometry(3, 120, 81, 41)
		self.label_3.setObjectName("label_3")
		self.label_4 = QtWidgets.QLabel(self)
		self.label_4.setGeometry(3, 170, 81, 41)
		self.label_4.setObjectName("label_4")
		self.label_5 = QtWidgets.QLabel(self)
		self.label_5.setGeometry(200, 20, 81, 21)
		self.label_5.setObjectName("label_6")
		self.label_6 = QtWidgets.QLabel(self)
		self.label_6.setGeometry(200, 70, 81, 31)
		self.label_6.setObjectName("label_7")
		self.label_7 = QtWidgets.QLabel(self)
		self.label_7.setGeometry(200, 110, 81, 41)
		self.label_7.setObjectName("label_8")
		self.label_8 = QtWidgets.QLabel(self)
		self.label_8.setGeometry(200, 170, 91, 31)
		self.label_8.setObjectName("label_9")
		self.label_9 = QtWidgets.QLabel(self)
		self.label_9.setGeometry(430, 20, 111, 41)
		self.label_9.setObjectName("label_11")
		self.label_10 = QtWidgets.QLabel(self)
		self.label_10.setGeometry(430, 70, 111, 41)
		self.label_10.setObjectName("label_12")
		self.label_11 = QtWidgets.QLabel(self)
		self.label_11.setGeometry(430, 120, 81, 31)
		self.label_11.setObjectName("label_13")
		self.label_12 = QtWidgets.QLabel(self)
		self.label_12.setGeometry(430, 170, 64, 21)
		self.label_12.setObjectName("label_14")
		self.label_13 = QtWidgets.QLabel(self)
		self.label_13.setGeometry(280, 250, 131, 31)
		self.label_13.setObjectName("label_16")

		self.lineEdit = QtWidgets.QLineEdit(self)
		self.lineEdit.setGeometry(70, 20, 113, 23)
		self.lineEdit.setObjectName("lineEdit")
		self.lineEdit_2 = QtWidgets.QLineEdit(self)
		self.lineEdit_2.setGeometry(70, 70, 113, 23)
		self.lineEdit_2.setObjectName("lineEdit_2")
		self.lineEdit_3 = QtWidgets.QLineEdit(self)
		self.lineEdit_3.setGeometry(70, 120, 113, 23)
		self.lineEdit_3.setObjectName("lineEdit_3")
		self.lineEdit_4 = QtWidgets.QLineEdit(self)
		self.lineEdit_4.setGeometry(70, 170, 113, 23)
		self.lineEdit_4.setObjectName("lineEdit_4")
		self.lineEdit_5 = QtWidgets.QLineEdit(self)
		self.lineEdit_5.setGeometry(300, 20, 113, 23)
		self.lineEdit_5.setObjectName("lineEdit_6")
		self.lineEdit_6 = QtWidgets.QLineEdit(self)
		self.lineEdit_6.setGeometry(300, 70, 113, 23)
		self.lineEdit_6.setObjectName("lineEdit_7")
		self.lineEdit_7 = QtWidgets.QLineEdit(self)
		self.lineEdit_7.setGeometry(300, 120, 113, 23)
		self.lineEdit_7.setObjectName("lineEdit_8")
		self.lineEdit_8 = QtWidgets.QLineEdit(self)
		self.lineEdit_8.setGeometry(300, 170, 113, 23)
		self.lineEdit_8.setObjectName("lineEdit_9")
		self.lineEdit_9 = QtWidgets.QLineEdit(self)
		self.lineEdit_9.setGeometry(540, 20, 113, 23)
		self.lineEdit_9.setObjectName("lineEdit_11")
		self.lineEdit_10 = QtWidgets.QLineEdit(self)
		self.lineEdit_10.setGeometry(540, 70, 113, 23)
		self.lineEdit_10.setObjectName("lineEdit_12")
		self.lineEdit_11 = QtWidgets.QLineEdit(self)
		self.lineEdit_11.setGeometry(540, 120, 113, 23)
		self.lineEdit_11.setObjectName("lineEdit_13")
		self.lineEdit_12 = QtWidgets.QLineEdit(self)
		self.lineEdit_12.setGeometry(540, 170, 113, 23)
		self.lineEdit_12.setObjectName("lineEdit_14")

		self.btn1 = Botao("Cadastrar", self)
		self.btn1.botao.move(170, 250)
		self.btn1.botao.resize(83, 23)
		self.btn2 = Botao("Cancelar", self)
		self.btn2.botao.move(420, 250)
		self.btn2.botao.resize(83, 23)

		self.home()

	def home(self):
		self.label.setText("Nome da" + "\n" + "Pessoa")
		self.label_2.setText("ID do" + "\n" + "Equipamento")
		self.label_3.setText("Data do" + "\n" + "Emprestimo")
		self.label_4.setText("Data da" + "\n" + "Devolucao")
		self.label_5.setText("Comentario")
		self.label_6.setText("Hora do" + "\n" + "Emprestimo")
		self.label_7.setText("Hora de" + "\n" + "Devolucao")
		self.label_8.setText("Data Prevista" + "\n" + "da Devolucao")
		self.label_9.setText("Status Inicial" + "\n" + "do Equipamento")
		self.label_10.setText("Status Final" + "\n" + "do Equipamento")
		self.label_11.setText("Motivo")
		self.label_12.setText("Atraso")
		self.label_13.setText("Existem campos" + "\n" + "vazios")
		self.label_13.setStyleSheet('color: red')
		self.label_13.hide()

		self.btn1.botao.clicked.connect(self.cadastrar)
		self.btn2.botao.clicked.connect(self.cancelar)

		self.show()

	def cadastrar(self, parent):
		t1 = str(self.lineEdit.text())
		t2 = str(self.lineEdit_2.text())
		t3 = str(self.lineEdit_3.text())
		t4 = str(self.lineEdit_4.text())
		t5 = str(self.lineEdit_5.text())
		t6 = str(self.lineEdit_6.text())
		t7 = str(self.lineEdit_7.text())
		t8 = str(self.lineEdit_8.text())
		t9 = str(self.lineEdit_9.text())
		t10 = str(self.lineEdit_10.text())
		t11 = str(self.lineEdit_11.text())
		t12 = str(self.lineEdit_12.text())

		if(t1 == '' or t2 == '' or t3 == '' or t4 == '' or t5 == '' or t6 == '' or t7 == '' or t8 == '' or t9 == '' or t10 == '' or t11 == '' or t12 == ''):
			self.label_13.show()
			QtTest.QTest.qWait(1000)
			self.label_13.hide()
		else:
			self.parent().incluinatabela(t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12)
			self.hide()

	def cancelar(self, parent):
		self.parent().show()
		self.hide()

class EditarEP(QtWidgets.QMainWindow):
	def __init__(self, parent):
		super(EditarEP, self).__init__(parent)
		self.setMinimumSize(660, 320)
		self.setMaximumSize(660, 320)
		self.setWindowTitle("Editar")
		self.setWindowIcon(QtGui.QIcon('IconePetGrande.png'))

		self.label = QtWidgets.QLabel(self)
		self.label.setGeometry(3, 20, 71, 31)
		self.label.setObjectName("label")
		self.label_2 = QtWidgets.QLabel(self)
		self.label_2.setGeometry(3, 70, 91, 41)
		self.label_2.setObjectName("label_2")
		self.label_3 = QtWidgets.QLabel(self)
		self.label_3.setGeometry(3, 120, 81, 41)
		self.label_3.setObjectName("label_3")
		self.label_4 = QtWidgets.QLabel(self)
		self.label_4.setGeometry(3, 170, 81, 41)
		self.label_4.setObjectName("label_4")
		self.label_5 = QtWidgets.QLabel(self)
		self.label_5.setGeometry(200, 20, 81, 21)
		self.label_5.setObjectName("label_6")
		self.label_6 = QtWidgets.QLabel(self)
		self.label_6.setGeometry(200, 70, 81, 11)
		self.label_6.setObjectName("label_7")
		self.label_7 = QtWidgets.QLabel(self)
		self.label_7.setGeometry(200, 110, 81, 41)
		self.label_7.setObjectName("label_8")
		self.label_8 = QtWidgets.QLabel(self)
		self.label_8.setGeometry(200, 170, 91, 31)
		self.label_8.setObjectName("label_9")
		self.label_9 = QtWidgets.QLabel(self)
		self.label_9.setGeometry(430, 20, 111, 41)
		self.label_9.setObjectName("label_11")
		self.label_10 = QtWidgets.QLabel(self)
		self.label_10.setGeometry(430, 70, 111, 41)
		self.label_10.setObjectName("label_12")
		self.label_11 = QtWidgets.QLabel(self)
		self.label_11.setGeometry(430, 120, 81, 31)
		self.label_11.setObjectName("label_13")
		self.label_12 = QtWidgets.QLabel(self)
		self.label_12.setGeometry(430, 170, 64, 21)
		self.label_12.setObjectName("label_14")
		self.label_13 = QtWidgets.QLabel(self)
		self.label_13.setGeometry(280, 250, 131, 31)
		self.label_13.setObjectName("label_16")

		self.lineEdit = QtWidgets.QLineEdit(self)
		self.lineEdit.setGeometry(70, 20, 113, 23)
		self.lineEdit.setObjectName("lineEdit")
		self.lineEdit_2 = QtWidgets.QLineEdit(self)
		self.lineEdit_2.setGeometry(70, 70, 113, 23)
		self.lineEdit_2.setObjectName("lineEdit_2")
		self.lineEdit_3 = QtWidgets.QLineEdit(self)
		self.lineEdit_3.setGeometry(70, 120, 113, 23)
		self.lineEdit_3.setObjectName("lineEdit_3")
		self.lineEdit_4 = QtWidgets.QLineEdit(self)
		self.lineEdit_4.setGeometry(70, 170, 113, 23)
		self.lineEdit_4.setObjectName("lineEdit_4")
		self.lineEdit_5 = QtWidgets.QLineEdit(self)
		self.lineEdit_5.setGeometry(300, 20, 113, 23)
		self.lineEdit_5.setObjectName("lineEdit_6")
		self.lineEdit_6 = QtWidgets.QLineEdit(self)
		self.lineEdit_6.setGeometry(300, 70, 113, 23)
		self.lineEdit_6.setObjectName("lineEdit_7")
		self.lineEdit_7 = QtWidgets.QLineEdit(self)
		self.lineEdit_7.setGeometry(300, 120, 113, 23)
		self.lineEdit_7.setObjectName("lineEdit_8")
		self.lineEdit_8 = QtWidgets.QLineEdit(self)
		self.lineEdit_8.setGeometry(300, 170, 113, 23)
		self.lineEdit_8.setObjectName("lineEdit_9")
		self.lineEdit_9 = QtWidgets.QLineEdit(self)
		self.lineEdit_9.setGeometry(540, 20, 113, 23)
		self.lineEdit_9.setObjectName("lineEdit_11")
		self.lineEdit_10 = QtWidgets.QLineEdit(self)
		self.lineEdit_10.setGeometry(540, 70, 113, 23)
		self.lineEdit_10.setObjectName("lineEdit_12")
		self.lineEdit_11 = QtWidgets.QLineEdit(self)
		self.lineEdit_11.setGeometry(540, 120, 113, 23)
		self.lineEdit_11.setObjectName("lineEdit_13")
		self.lineEdit_12 = QtWidgets.QLineEdit(self)
		self.lineEdit_12.setGeometry(540, 170, 113, 23)
		self.lineEdit_12.setObjectName("lineEdit_14")

		self.btn1 = Botao("Editar", self)
		self.btn1.botao.move(170, 250)
		self.btn1.botao.resize(83, 23)
		self.btn2 = Botao("Cancelar", self)
		self.btn2.botao.move(420, 250)
		self.btn2.botao.resize(83, 23)

		self.home()

		self.home()

	def home(self):
		self.label.setText("Nome da" + "\n" + "Pessoa")
		self.label_2.setText("ID do" + "\n" + "Equipamento")
		self.label_3.setText("Data do" + "\n" + "Emprestimo")
		self.label_4.setText("Data da" + "\n" + "Devolucao")
		self.label_5.setText("Comentario")
		self.label_6.setText("Hora do" + "\n" + "Emprestimo")
		self.label_7.setText("Hora de" + "\n" + "Devolucao")
		self.label_8.setText("Data Prevista" + "\n" + "da Devolucao")
		self.label_9.setText("Status Inicial" + "\n" + "do Equipamento")
		self.label_10.setText("Status Final" + "\n" + "do Equipamento")
		self.label_11.setText("Motivo")
		self.label_12.setText("Atraso")
		self.label_13.setText("Existem campos" + "\n" + "vazios")
		self.label_13.setStyleSheet('color: red')
		self.label_13.hide()

		self.btn1.botao.clicked.connect(self.editar)
		self.btn2.botao.clicked.connect(self.cancelar)

		self.show()

	def editar(self, parent):
		t1 = str(self.lineEdit.text())
		t2 = str(self.lineEdit_2.text())
		t3 = str(self.lineEdit_3.text())
		t4 = str(self.lineEdit_4.text())
		t5 = str(self.lineEdit_5.text())
		t6 = str(self.lineEdit_6.text())
		t7 = str(self.lineEdit_7.text())
		t8 = str(self.lineEdit_8.text())
		t9 = str(self.lineEdit_9.text())
		t10 = str(self.lineEdit_10.text())
		t11 = str(self.lineEdit_11.text())
		t12 = str(self.lineEdit_12.text())

		self.parent().editadatabela(t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12)
		self.hide()

	def cancelar(self, parent):
		self.parent().show()
		self.hide()

app = QtWidgets.QApplication(sys.argv)
GUI1 = TelaLogin()
sys.exit(app.exec_())