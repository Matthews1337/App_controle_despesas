
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QPushButton,QVBoxLayout,QHBoxLayout, QMessageBox, QTableWidget,QTableWidgetItem, QHeaderView, QCheckBox,QDateEdit, QLineEdit
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.cm as cm
from matplotlib.colors import Normalize

import numpy as np
from sys import exit



class despesas(QWidget):
    def __init__(self):
        super().__init__()
        self.iniciar_Ui()
        self.settings()
        self.btn_click()
        self.estilo()
        self.carregar_tabelas()




    def settings(self):
        self.setWindowTitle("Controle de despesas")
        self.resize(1280,720)


# criar layout da GUI

    def iniciar_Ui(self):
        self.date_box = QDateEdit()
        self.date_box.setDate(QDate.currentDate())

        self.vl_ganho = QLineEdit()
        self.vl_ganho.setPlaceholderText("Valor do ganho")

        self.vl_abastecimento_carro = QLineEdit()
        self.vl_abastecimento_carro.setPlaceholderText("Valor do abastecimento do carro")

        self.vl_abastecimento_moto = QLineEdit()
        self.vl_abastecimento_moto.setPlaceholderText("Valor do abastecimento da moto")

        self.vl_mercado = QLineEdit()
        self.vl_mercado.setPlaceholderText("Valor do mercado")

        self.vl_fast_food = QLineEdit()
        self.vl_fast_food.setPlaceholderText("Valor do fast food")

        self.vl_shopping = QLineEdit()
        self.vl_shopping.setPlaceholderText("Valor do shopping")

        self.vl_compras_internet = QLineEdit()
        self.vl_compras_internet.setPlaceholderText("Valor das comprar na internet")

        self.vl_internet = QLineEdit()
        self.vl_internet.setPlaceholderText("Valor da internet")

        self.vl_faculdade = QLineEdit()
        self.vl_faculdade.setPlaceholderText("Valor da faculdade")

        self.vl_energia = QLineEdit()
        self.vl_energia.setPlaceholderText("Valor da energia")

        self.vl_gas = QLineEdit()
        self.vl_gas.setPlaceholderText("Valor do gas")

        self.vl_racao = QLineEdit()
        self.vl_racao.setPlaceholderText("Valor da ração")

        self.vl_spotify = QLineEdit()
        self.vl_spotify.setPlaceholderText("Valor do Spotify")

        self.vl_netflix = QLineEdit()
        self.vl_netflix.setPlaceholderText("Valor da Netflix")

        self.vl_internet_movel = QLineEdit()
        self.vl_internet_movel.setPlaceholderText("Valor da internet móvel")

        self.submit_btn = QPushButton("Submit")
        self.add_btn = QPushButton("Add")
        self.delete_btn = QPushButton("Delete")
        self.clear_btn = QPushButton("Clear")
        self.dark_mode = QCheckBox("DarkMode")
        

        self.table = QTableWidget()
        self.table.setColumnCount(17)
        self.table.setHorizontalHeaderLabels([
            "id","Data", "vl_ganho" ,"Vl_total_gasto", "vl_combustivel_carro", "vl_combustivel_moto", 
            "vl_alimentacao", "vl_fast_food", "vl_shopping", "vl_compras_internet", "vl_internet", "vl_faculdade", "vl_energia",
            "vl_gas", "vl_racao", "vl_spotify", "vl_netflix", "vl_internet_movel"                                
        ])
        # self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)

        # Desenhando o layout
        self.master_layout = QHBoxLayout()
        self.col1 = QVBoxLayout()
        self.col2 = QVBoxLayout()


        self.sub_row1 = QVBoxLayout()
        self.sub_row2 = QVBoxLayout()
        self.sub_row3 = QVBoxLayout()
        self.sub_row4 = QVBoxLayout()
        self.sub_row5 = QVBoxLayout()
        self.sub_row6 = QVBoxLayout()
        self.sub_row7 = QVBoxLayout()
        self.sub_row8 = QVBoxLayout()
        self.sub_row9 = QVBoxLayout()
        self.sub_row10 = QVBoxLayout()
        self.sub_row11 = QVBoxLayout()
        self.sub_row12 = QVBoxLayout()
        self.sub_row13= QVBoxLayout()
        self.sub_row14 = QVBoxLayout()
        self.sub_row15 = QVBoxLayout()
        self.sub_row16 = QVBoxLayout()

        
        self.sub_row1.addWidget(self.date_box)
        self.sub_row2.addWidget(self.vl_ganho)
        self.sub_row3.addWidget(self.vl_mercado)
        self.sub_row4.addWidget(self.vl_fast_food)
        self.sub_row5.addWidget(self.vl_shopping)
        self.sub_row6.addWidget(self.vl_abastecimento_carro)
        self.sub_row7.addWidget(self.vl_compras_internet)
        self.sub_row8.addWidget(self.vl_internet)
        self.sub_row9.addWidget(self.vl_faculdade)
        self.sub_row10.addWidget(self.vl_abastecimento_moto)
        self.sub_row11.addWidget(self.vl_energia)
        self.sub_row12.addWidget(self.vl_gas)
        self.sub_row13.addWidget(self.vl_racao)
        self.sub_row14.addWidget(self.vl_spotify)
        self.sub_row15.addWidget(self.vl_netflix)
        self.sub_row16.addWidget(self.vl_internet_movel)



        self.col1.addLayout(self.sub_row1)
        self.col1.addLayout(self.sub_row2)
        self.col1.addLayout(self.sub_row3)
        self.col1.addLayout(self.sub_row4)
        self.col1.addLayout(self.sub_row5)
        self.col1.addLayout(self.sub_row6)
        self.col1.addLayout(self.sub_row7)
        self.col1.addLayout(self.sub_row8)
        self.col1.addLayout(self.sub_row9)
        self.col1.addLayout(self.sub_row10)
        self.col1.addLayout(self.sub_row11)
        self.col1.addLayout(self.sub_row12)
        self.col1.addLayout(self.sub_row13)
        self.col1.addLayout(self.sub_row14)
        self.col1.addLayout(self.sub_row15)
        self.col1.addLayout(self.sub_row16)




        btn_row1 = QHBoxLayout()
        btn_row2 = QHBoxLayout()


        btn_row1.addWidget(self.add_btn)
        btn_row1.addWidget(self.delete_btn)
        btn_row2.addWidget(self.submit_btn)
        btn_row2.addWidget(self.clear_btn)

        self.col1.addWidget(self.dark_mode)

        self.col2.addWidget(self.canvas, 70)
        self.col2.addWidget(self.table, 30)
        self.col2.addLayout(btn_row1)
        self.col2.addLayout(btn_row2)








        self.master_layout.addLayout(self.col1, 20)
        self.master_layout.addLayout(self.col2, 80)
        self.setLayout(self.master_layout)

        self.carregar_tabelas()


    def btn_click(self):
        self.add_btn.clicked.connect(self.add_despesa)
        self.delete_btn.clicked.connect(self.delete_despesa)
        self.submit_btn.clicked.connect(self.calcular_gastos)
        self.clear_btn.clicked.connect(self.reset)
        self.dark_mode.stateChanged.connect(self.toggle_dark_mode)


    def carregar_tabelas(self):
        self.table.setRowCount(0)
        query = QSqlQuery("Select * from despesa ORDER BY data DESC")
        row = 0
        while query.next():
            id_despesa = query.value(0)
            data  = query.value(1)
            vl_ganho  = query.value(2)
            Vl_total_gasto  = query.value(3)
            vl_combustivel_carro  = query.value(4)
            vl_combustivel_moto   = query.value(5)
            vl_alimentacao  = query.value(6)
            vl_fast_food  = query.value(7)
            vl_shopping = query.value(8)
            vl_compras_internet  = query.value(9)
            vl_internet  = query.value(10)
            vl_faculdade  = query.value(11)
            vl_energia  = query.value(12)
            vl_gas   = query.value(13)
            vl_racao  = query.value(14)
            vl_spotify  = query.value(15)
            vl_netflix = query.value(16)
            vl_internet_movel = query.value(17)
            
            self.table.insertRow(row)
            
            self.table.setItem(row, 0, QTableWidgetItem(str(id_despesa)))
            self.table.setItem(row, 1, QTableWidgetItem(data))
            self.table.setItem(row, 2, QTableWidgetItem(str(vl_ganho)))
            self.table.setItem(row, 3, QTableWidgetItem(str(Vl_total_gasto)))
            self.table.setItem(row, 4, QTableWidgetItem(str(vl_combustivel_carro)))
            self.table.setItem(row, 5, QTableWidgetItem(str(vl_combustivel_moto)))
            self.table.setItem(row, 6, QTableWidgetItem(str(vl_alimentacao)))
            self.table.setItem(row, 7, QTableWidgetItem(str(vl_fast_food)))
            self.table.setItem(row, 8, QTableWidgetItem(str(vl_shopping)))
            self.table.setItem(row, 9, QTableWidgetItem(str(vl_compras_internet)))
            self.table.setItem(row, 10, QTableWidgetItem(str(vl_internet)))
            self.table.setItem(row, 11, QTableWidgetItem(str(vl_faculdade)))
            self.table.setItem(row, 12, QTableWidgetItem(str(vl_energia)))
            self.table.setItem(row, 13, QTableWidgetItem(str(vl_gas)))
            self.table.setItem(row, 14, QTableWidgetItem(str(vl_racao)))
            self.table.setItem(row, 15, QTableWidgetItem(str(vl_spotify)))
            self.table.setItem(row, 16, QTableWidgetItem(str(vl_netflix)))
            self.table.setItem(row, 17, QTableWidgetItem(str(vl_internet_movel)))
            row+=1


    def somar_despesas(self):
        try:
            vl_combustivel_carro = float(self.vl_abastecimento_carro.text())
            vl_combustivel_moto = float(self.vl_abastecimento_moto.text())
            vl_alimentacao = float(self.vl_mercado.text())
            vl_fast_food = float(self.vl_fast_food.text())
            vl_shopping = float(self.vl_shopping.text())
            vl_compras_internet = float(self.vl_compras_internet.text())
            vl_internet = float(self.vl_internet.text())
            vl_faculdade = float(self.vl_faculdade.text())
            vl_energia = float(self.vl_energia.text())
            vl_gas = float(self.vl_gas.text())
            vl_racao = float(self.vl_racao.text())
            vl_spotify = float(self.vl_spotify.text())
            vl_netflix = float(self.vl_netflix.text())
            vl_internet_movel = float(self.vl_internet_movel.text())

            vl_despesa_total = (
                vl_combustivel_carro + vl_combustivel_moto + vl_alimentacao + vl_fast_food
                + vl_shopping + vl_compras_internet + vl_internet + vl_faculdade + vl_energia + vl_gas + vl_racao
                + vl_spotify + vl_netflix + vl_internet_movel
            )

            return vl_despesa_total
        except ValueError:
            # Handle the case where the conversion fails (e.g., the text is not a valid number)
            print("One or more inputs are not valid numbers")
            return None


    def add_despesa(self):
        data = self.date_box.date().toString("yyyy-MM-dd")
        vl_ganho = float(self.vl_ganho.text())
        vl_total_gasto = self.somar_despesas()
        vl_combustivel_carro = float(self.vl_abastecimento_carro.text())
        vl_combustivel_moto = float(self.vl_abastecimento_moto.text())
        vl_alimentacao = float(self.vl_mercado.text())
        vl_fast_food = float(self.vl_fast_food.text())
        vl_shopping = float(self.vl_shopping.text())
        vl_compras_internet = float(self.vl_compras_internet.text())
        vl_internet = float(self.vl_internet.text())
        vl_faculdade = float(self.vl_faculdade.text())
        vl_energia = float(self.vl_energia.text())
        vl_gas = float(self.vl_gas.text())
        vl_racao = float(self.vl_racao.text())
        vl_spotify = float(self.vl_spotify.text())
        vl_netflix = float(self.vl_netflix.text())
        vl_internet_movel = float(self.vl_internet_movel.text())

        query = QSqlQuery("""
            INSERT INTO despesa 
                (data,
                vl_ganho,  
                Vl_total_gasto, 
                vl_combustivel_carro, 
                vl_combustivel_moto, 
                vl_alimentacao, 
                vl_fast_food, 
                vl_shopping, 
                vl_compras_internet, 
                vl_internet, 
                vl_faculdade, 
                vl_energia, 
                vl_gas, 
                vl_racao, 
                vl_spotify, 
                vl_netflix, 
                vl_internet_movel)


                VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)

                """)
        
        query.addBindValue(data)
        query.addBindValue(vl_ganho)
        query.addBindValue(vl_total_gasto)
        query.addBindValue(vl_combustivel_carro)
        query.addBindValue(vl_combustivel_moto)
        query.addBindValue(vl_alimentacao)
        query.addBindValue(vl_fast_food)
        query.addBindValue(vl_shopping)
        query.addBindValue(vl_compras_internet)
        query.addBindValue(vl_internet)
        query.addBindValue(vl_faculdade)
        query.addBindValue(vl_energia)
        query.addBindValue(vl_gas)
        query.addBindValue(vl_racao)
        query.addBindValue(vl_spotify)
        query.addBindValue(vl_netflix)
        query.addBindValue(vl_internet_movel)
        query.exec_()

        self.date_box.setDate(QDate.currentDate())
        self.vl_ganho.clear()
        self.vl_abastecimento_carro.clear()
        self.vl_abastecimento_moto.clear()
        self.vl_mercado.clear()
        self.vl_fast_food.clear()
        self.vl_shopping.clear()
        self.vl_compras_internet.clear()
        self.vl_internet.clear()
        self.vl_faculdade.clear()
        self.vl_energia.clear()
        self.vl_gas.clear()
        self.vl_racao.clear()
        self.vl_spotify.clear()
        self.vl_netflix.clear()
        self.vl_internet_movel.clear()

        self.carregar_tabelas()


    def delete_despesa(self):
        linha_selecionada = self.table.currentRow()

        if linha_selecionada == -1:
            QMessageBox.warning(self, "Error", "Por favor selecione uma linha para ser apagada!")
            return
        
        item = self.table.item(linha_selecionada, 0)
        if item is None:
            QMessageBox.warning(self, "Error", "A linha selecionada não existe ou está vazia!")
            return
        
        despesa_id = int(self.table.item(linha_selecionada, 0).text())
        confirmar = QMessageBox.question(self, "Você tem certeza?", "Apagar esta despesa", QMessageBox.Yes | QMessageBox.No)

        if confirmar == QMessageBox.No:
            return

        query = QSqlQuery()
        query.prepare("DELETE FROM despesa WHERE id = ?")
        query.addBindValue(despesa_id)
        query.exec_()

        self.carregar_tabelas()


    def calcular_gastos(self):
        # Initialize lists to store the values from each column
        vls_ganhos = []
        vls_totais_gastos = []
        vls_combustiveis_carro = []
        vls_combustiveis_moto = []
        vls_alimentacoes = []
        vls_fast_foods = []
        vls_shoppings = []
        vls_compras_internet = []
        vls_internet = []
        vls_faculdade = []
        vls_energia = []
        vls_gas = []
        vls_racao = []
        vls_spotify = []
        vls_netflix = []
        vls_internet_movel = []

        # SQL query to fetch all the required columns
        query = QSqlQuery("""
            SELECT 
                vl_ganho,
                vl_total_gasto,
                vl_combustivel_carro,
                vl_combustivel_moto,
                vl_alimentacao,
                vl_fast_food,
                vl_shopping,
                vl_compras_internet,
                vl_internet,
                vl_faculdade,
                vl_energia,
                vl_gas,
                vl_racao,
                vl_spotify,
                vl_netflix,
                vl_internet_movel
            FROM
                despesa
        """)

        # Check if the query executed successfully
        if not query.exec_():
            QMessageBox.critical(self, "Database Error", query.lastError().text())
            return

        # Populate the lists with data from the query
        while query.next():
            vls_ganhos.append(query.value(0))
            vls_totais_gastos.append(query.value(1))
            vls_combustiveis_carro.append(query.value(2))
            vls_combustiveis_moto.append(query.value(3))
            vls_alimentacoes.append(query.value(4))
            vls_fast_foods.append(query.value(5))
            vls_shoppings.append(query.value(6))
            vls_compras_internet.append(query.value(7))
            vls_internet.append(query.value(8))
            vls_faculdade.append(query.value(9))
            vls_energia.append(query.value(10))
            vls_gas.append(query.value(11))
            vls_racao.append(query.value(12))
            vls_spotify.append(query.value(13))
            vls_netflix.append(query.value(14))
            vls_internet_movel.append(query.value(15))

        # Calculate the number of rows
        num_rows = len(vls_totais_gastos)  # Assuming all columns have the same number of rows

        if num_rows == 0:
            # Handle the case where there are no rows
            QMessageBox.warning(self, "Error", "No data found in the table.")
            return

        # Calculate the average for each column
        media_de_vls_ganhos = sum(vls_ganhos) / num_rows
        media_de_vls_totais_gastos = sum(vls_totais_gastos) / num_rows
        media_de_vls_combustiveis_carro = sum(vls_combustiveis_carro) / num_rows
        media_de_vls_combustiveis_moto = sum(vls_combustiveis_moto) / num_rows
        media_de_vls_alimentacoes = sum(vls_alimentacoes) / num_rows
        media_de_vls_fast_foods = sum(vls_fast_foods) / num_rows
        media_de_vls_shoppings = sum(vls_shoppings) / num_rows
        media_de_vls_compras_internet = sum(vls_compras_internet) / num_rows
        media_de_vls_internet = sum(vls_internet) / num_rows
        media_de_vls_faculdade = sum(vls_faculdade) / num_rows
        media_de_vls_energia = sum(vls_energia) / num_rows
        media_de_vls_gas = sum(vls_gas) / num_rows
        media_de_vls_racao = sum(vls_racao) / num_rows
        media_de_vls_spotify = sum(vls_spotify) / num_rows
        media_de_vls_netflix = sum(vls_netflix) / num_rows
        media_de_vls_internet_movel = sum(vls_internet_movel) / num_rows

        # Data for plotting
        categories = ['Ganhos', 'Total Gastos', 'Combustível Carro', 'Combustível Moto', 'Alimentações',
                      'Fast Foods', 'Shoppings', 'Compras Internet', 'Internet', 'Faculdade',
                      'Energia', 'Gás', 'Ração', 'Spotify', 'Netflix', 'Internet Móvel']
        averages = [media_de_vls_ganhos, media_de_vls_totais_gastos, media_de_vls_combustiveis_carro,
                    media_de_vls_combustiveis_moto, media_de_vls_alimentacoes, media_de_vls_fast_foods,
                    media_de_vls_shoppings, media_de_vls_compras_internet, media_de_vls_internet,
                    media_de_vls_faculdade, media_de_vls_energia, media_de_vls_gas, media_de_vls_racao,
                    media_de_vls_spotify, media_de_vls_netflix, media_de_vls_internet_movel]



        
        # Normalize the averages for color mapping
        norm = Normalize(vmin=min(averages), vmax=max(averages))
        colormap = cm.get_cmap('Greens')

        # Get colors based on the normalized values
        colors = [colormap(norm(value)) for value in averages]


        # Clear the figure and create the bar graph
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.bar(categories, averages, color=colors)
        ax.set_xlabel('Categorias')
        ax.set_ylabel('Média dos Valores')
        ax.set_title('Média dos Valores das Despesas por Categoria')
        ax.set_xticklabels(categories, rotation=45, ha='right')

        # Draw the canvas
        self.canvas.draw()


    def estilo(self):

        self.setStyleSheet("""
        QWidget {
            background-color: #C1D0B5;
        }
        
        QLabel {
            color: #000000;
            font-size: 14px;
            border-radius: 5px;
        }
        
        QLineEdit, QComboBox, QDateEdit, QPushButton {
            background-color: #D6E8DB;
            color: #000000;
            border: 1px solid #99A98F;
            border-radius: 5px;
            padding: 5px;
        }
        
        QTableWidget {
            background-color: #C1D0B5;
            color: #555555;
            border: 1px solid #C1D0B5;
            selection-background-color: #99A98F;
            border-radius: 5px;
        }
        
        QPushButton {
            background-color: #D6E8DB;
            color: #99A98F;
            border-radius: 5px;
            border: 1px solid #99A98F;
            padding: 8px 16px;
            font-size: 14px;
            
        }
        
        QPushButton:hover {
            background-color: #99A98F;
            color: #000000
        }
    """)
        figure_color = "#99A98F"
        self.figure.patch.set_facecolor(figure_color)
        self.canvas.setStyleSheet(f"background-color:{figure_color};")
        self.canvas.draw()

        if self.dark_mode.isChecked():
            self.setStyleSheet("""
        QWidget {
            background-color: #344C64;
        }
        
        QLabel {
            color: #000000;
            font-size: 14px;
            border-radius: 5px;
        }
        
        QLineEdit, QComboBox, QDateEdit, QPushButton {
            background-color: #577B8D;
            color: #000000;
            border: 1px solid #240750;
            border-radius: 5px;
            padding: 5px;
        }
        
        QTableWidget {
            background-color: #577B8D;
            color: #ffffff;
            border: 1px solid #240750;
            selection-background-color: #57A6A1;
            border-radius: 5px;
        }
        
        QPushButton {
            background-color: #577B8D;
            color: #333333;
            border-radius: 5px;
            border: 1px solid #240750;
            padding: 8px 16px;
            font-size: 14px;
            
        }
        
        QPushButton:hover {
            background-color: #57A6A1;
            color: #ffffff
        }
        """)
            figure_color2 = "#57A6A1"
            self.figure.patch.set_facecolor(figure_color2)
            self.canvas.setStyleSheet(f"background-color:{figure_color2};")
            self.canvas.draw()
            

    def toggle_dark_mode(self):
        self.estilo()


    def reset(self):
        self.date_box.setDate(QDate.currentDate())
        self.vl_ganho.clear()
        self.vl_abastecimento_carro.clear()
        self.vl_abastecimento_moto.clear()
        self.vl_mercado.clear()
        self.vl_fast_food.clear()
        self.vl_shopping.clear()
        self.vl_compras_internet.clear()
        self.vl_internet.clear()
        self.vl_faculdade.clear()
        self.vl_energia.clear()
        self.vl_gas.clear()
        self.vl_racao.clear()
        self.vl_spotify.clear()
        self.vl_netflix.clear()
        self.vl_internet_movel.clear()
        self.figure.clear()
        self.canvas.draw()


    

# criar banco de dados SQLite nativo do programa 

db = QSqlDatabase.addDatabase("QSQLITE")
db.setDatabaseName("despesa.db")

if not db.open():
    QMessageBox.critical(None, "ERROR", "Can not open the database")
    exit(2)

query = QSqlQuery()
query.exec_("""
    CREATE TABLE IF NOT EXISTS despesa (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            data TEXT, 
            vl_ganho REAL ,
            Vl_total_gasto REAL ,
            vl_combustivel_carro REAL ,
            vl_combustivel_moto REAL , 
            vl_alimentacao REAL ,
            vl_fast_food REAL ,
            vl_shopping REAL,
            vl_compras_internet REAL ,
            vl_internet REAL ,
            vl_faculdade REAL ,
            vl_energia REAL ,
            vl_gas REAL , 
            vl_racao REAL ,
            vl_spotify REAL, 
            vl_netflix REAL,
            vl_internet_movel REAL
            )
""")



if __name__ == "__main__":
    app = QApplication([])
    main = despesas()
    main.show()
    app.exec_()
