import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.con = sqlite3.connect("coffee.sqlite")
        cur = self.con.cursor()
        self.comboBox.addItems(
            [item[0] for item in cur.execute("SELECT roasting_name FROM roasting").fetchall()])
        self.comboBox_2.addItems(
            [item[0] for item in cur.execute("SELECT ground_name FROM ground").fetchall()])
        self.comboBox_3.addItems(
            [item[0] for item in cur.execute("SELECT pack_name FROM pack").fetchall()])
        self.pushButton.clicked.connect(self.filter)
        self.pushButton_2.clicked.connect(self.filter_2)
        self.pushButton_3.clicked.connect(self.filter_3)
        self.pushButton_4.clicked.connect(self.filter_4)

    def filter_2(self):
        cur = self.con.cursor()
        self.result = cur.execute(f"""
                            SELECT DISTINCT
                                coffee_sort.sort_name,
                                roasting.roasting_name,
                                ground_name,
                                coffee_sort.taste,
                                coffee_sort.price,
                                pack_name
                            FROM
                                coffee_sort,
                                roasting,
                                ground,
                                pack
                            JOIN
                                coffee_sort_roasting,
                                coffee_sort_ground,
                                coffee_sort_pack
                            ON
                                coffee_sort.id = coffee_sort_roasting.id_coffee_sort AND
                                   roasting.id = coffee_sort_roasting.id_roasting AND
                                coffee_sort.id = coffee_sort_ground.id_coffee_sort AND
                                     ground.id = coffee_sort_ground.id_ground AND
                                coffee_sort.id = coffee_sort_pack.id_coffee_sort AND
                                       pack.id = coffee_sort_pack.id_pack
                            WHERE id_roasting = {self.comboBox.currentIndex() + 1}
                            """).fetchall()
        self.make_table()

    def filter_3(self):
        cur = self.con.cursor()
        self.result = cur.execute(f"""
                            SELECT DISTINCT
                                coffee_sort.sort_name,
                                roasting.roasting_name,
                                ground_name,
                                coffee_sort.taste,
                                coffee_sort.price,
                                pack_name
                            FROM
                                coffee_sort,
                                roasting,
                                ground,
                                pack
                            JOIN
                                coffee_sort_roasting,
                                coffee_sort_ground,
                                coffee_sort_pack
                            ON
                                coffee_sort.id = coffee_sort_roasting.id_coffee_sort AND
                                   roasting.id = coffee_sort_roasting.id_roasting AND
                                coffee_sort.id = coffee_sort_ground.id_coffee_sort AND
                                     ground.id = coffee_sort_ground.id_ground AND
                                coffee_sort.id = coffee_sort_pack.id_coffee_sort AND
                                       pack.id = coffee_sort_pack.id_pack
                            WHERE id_ground = {self.comboBox_2.currentIndex() + 1}
                            """).fetchall()
        self.make_table()

    def filter_4(self):
        cur = self.con.cursor()
        self.result = cur.execute(f"""
                            SELECT DISTINCT
                                coffee_sort.sort_name,
                                roasting.roasting_name,
                                ground_name,
                                coffee_sort.taste,
                                coffee_sort.price,
                                pack_name
                            FROM
                                coffee_sort,
                                roasting,
                                ground,
                                pack
                            JOIN
                                coffee_sort_roasting,
                                coffee_sort_ground,
                                coffee_sort_pack
                            ON
                                coffee_sort.id = coffee_sort_roasting.id_coffee_sort AND
                                   roasting.id = coffee_sort_roasting.id_roasting AND
                                coffee_sort.id = coffee_sort_ground.id_coffee_sort AND
                                     ground.id = coffee_sort_ground.id_ground AND
                                coffee_sort.id = coffee_sort_pack.id_coffee_sort AND
                                       pack.id = coffee_sort_pack.id_pack
                            WHERE id_pack = {self.comboBox_3.currentIndex() + 1}
                            """).fetchall()
        self.make_table()

    def filter(self):
        cur = self.con.cursor()
        self.result = cur.execute(f"""
                            SELECT DISTINCT
                                coffee_sort.sort_name,
                                roasting.roasting_name,
                                ground_name,
                                coffee_sort.taste,
                                coffee_sort.price,
                                pack_name
                            FROM
                                coffee_sort,
                                roasting,
                                ground,
                                pack
                            JOIN
                                coffee_sort_roasting,
                                coffee_sort_ground,
                                coffee_sort_pack
                            ON
                                coffee_sort.id = coffee_sort_roasting.id_coffee_sort AND
                                   roasting.id = coffee_sort_roasting.id_roasting AND
                                coffee_sort.id = coffee_sort_ground.id_coffee_sort AND
                                     ground.id = coffee_sort_ground.id_ground AND
                                coffee_sort.id = coffee_sort_pack.id_coffee_sort AND
                                       pack.id = coffee_sort_pack.id_pack
                            WHERE id_roasting = {self.comboBox.currentIndex() + 1} AND
                                id_ground = {self.comboBox_2.currentIndex() + 1} AND 
                                id_pack = {self.comboBox_3.currentIndex() + 1}

                            """).fetchall()
        if self.result:
            self.make_table()
        else:
            self.result = [('-', '-', '-', '-', '-', '-',)]
            self.make_table()

    def make_table(self):
        self.tableWidget.setRowCount(len(self.result))
        self.tableWidget.setColumnCount(len(self.result[0]))
        for n, text in enumerate(
                ["Сорт кофе", "Степень обжарки", "Молотый/в зернах", "Вкус", "Цена, руб", "Объем упаковки"]):
            item = QTableWidgetItem()
            item.setText(text)
            self.tableWidget.setHorizontalHeaderItem(n, item)
        for i, elem in enumerate(self.result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
