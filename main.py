import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QDialog, QWidget, QVBoxLayout, QLabel


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
        self.item_select = 0
        # self.table_select = 0
        self.pushButton_5.clicked.connect(self.open_dialog_for_change)
        self.pushButton_6.clicked.connect(self.open_dialog_for_new)
        # self.tableWidget.itemChanged.connect(self.show_my_dialog)
        # self.tableWidget.cellClicked.connect(self.show_my_dialog)
        # self.tableWidget.itemClicked.connect(self.show_my_dialog)
        self.tableWidget.itemDoubleClicked.connect(self.open_dialog_for_change)
        self.tableWidget.itemClicked.connect(self.table_selected)
        self.out_stroka_table = []

    def table_selected(self):
        self.item_select = 1

    def open_dialog_for_change(self):
        if self.item_select:
            self.tableWidget.clearContents
            current_row_table = self.tableWidget.currentRow()
            # (current_row_table)
            self.out_stroka_table = [self.tableWidget.item(current_row_table, i).text() for i in range(6)]
            # print(str(self.out_stroka_table))
            self.w = MyDialog(self.out_stroka_table)
            self.w.show()

    def open_dialog_for_new(self, checked):
        self.w = MyDialog([])
        self.w.show()

        # mydialog = QDialog(self)
        # # mydialog.setModal(True)
        # # mydialog.exec()
        # mydialog.show()

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


class MyDialog(QWidget):
    def __init__(self, stroka):
        super().__init__()
        uic.loadUi("addEditCoffeeForm.ui", self)

        if stroka:
            self.pushButton.setVisible(False)
            self.pushButton_2.setVisible(True)

        else:
            self.pushButton.setVisible(True)
            self.pushButton_2.setVisible(False)

        self.pushButton.clicked.connect(self.add_new)
        self.pushButton_2.clicked.connect(self.update_change)
        self.con = sqlite3.connect("coffee.sqlite")
        cur = self.con.cursor()
        self.comboBox.addItems(
            [item[0] for item in cur.execute("SELECT roasting_name FROM roasting").fetchall()])
        self.comboBox_2.addItems(
            [item[0] for item in cur.execute("SELECT ground_name FROM ground").fetchall()])
        self.comboBox_3.addItems(
            [item[0] for item in cur.execute("SELECT pack_name FROM pack").fetchall()])

        # self.tableWidget.itemChanged.connect(self.save_results)

        self.modified = {}
        self.titles = None
        self.in_stroka_tab = stroka
        # print(self.in_stroka_tab)
        self.id_change_coffee = -1
        if self.in_stroka_tab:
            text, text2, text3 = self.in_stroka_tab[0], self.in_stroka_tab[3], self.in_stroka_tab[4]
            self.lineEdit.setText(text)
            self.lineEdit_2.setText(text2)
            self.lineEdit_3.setText(text3)
            self.comboBox.setCurrentIndex(self.comboBox.findText(self.in_stroka_tab[1]))
            self.comboBox_2.setCurrentIndex(self.comboBox_2.findText(self.in_stroka_tab[2]))
            self.comboBox_3.setCurrentIndex(self.comboBox_3.findText(self.in_stroka_tab[5]))
            # self.make_table_for_change()
            cur = self.con.cursor()
            self.id_change_coffee = cur.execute(f"""
                            SELECT DISTINCT
                                coffee_sort.id
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
                            WHERE 
                                coffee_sort.sort_name = ? AND
                                roasting.roasting_name = ? AND
                                ground_name = ? AND
                                coffee_sort.taste = ? AND
                                coffee_sort.price = ? AND
                                pack.pack_name = ?

                            """, (self.in_stroka_tab[0], self.in_stroka_tab[1], self.in_stroka_tab[2],
                                  self.in_stroka_tab[3], int(self.in_stroka_tab[4]), self.in_stroka_tab[5])
                                                ).fetchone()
            self.id_change_coffee = self.id_change_coffee[0]
            # print(self.id_change_coffee)

    def add_new(self):
        cur = self.con.cursor()
        cur.execute(f"""
                    INSERT INTO coffee_sort(sort_name, taste, price)
                    VALUES (?, ?, ?)""", (self.lineEdit.text(), self.lineEdit_2.text(), int(self.lineEdit_3.text())))
        last_add_id = cur.lastrowid
        # print(last_add_id)
        self.con.commit()

        cur = self.con.cursor()
        cur.execute(f"""
                    INSERT INTO coffee_sort_roasting(id_roasting, id_coffee_sort)
                    VALUES (?, ?)""", (self.comboBox.currentIndex() + 1, last_add_id))
        self.con.commit()

        cur = self.con.cursor()
        cur.execute(f"""
                    INSERT INTO coffee_sort_ground(id_ground, id_coffee_sort)
                    VALUES (?, ?)""", (self.comboBox_2.currentIndex() + 1, last_add_id))
        self.con.commit()

        cur = self.con.cursor()
        cur.execute(f"""
                    INSERT INTO coffee_sort_pack(id_pack, id_coffee_sort)
                    VALUES (?, ?)""", (self.comboBox_3.currentIndex() + 1, last_add_id))
        self.con.commit()

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
                            WHERE 
                                coffee_sort.id = {last_add_id}
                            """).fetchone()
        # print(self.result)
        self.make_table_for_new()

    def make_table_for_new(self):
        # print(self.result)
        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(6)
        for n, text in enumerate(
                ["Сорт кофе", "Степень обжарки", "Молотый/в зернах", "Вкус", "Цена, руб", "Объем упаковки"]):
            item = QTableWidgetItem()
            item.setText(text)
            self.tableWidget.setHorizontalHeaderItem(n, item)
        for i, elem in enumerate(self.result):
            self.tableWidget.setItem(0, i, QTableWidgetItem(str(elem)))

    def make_table_for_change(self):
        stroka_for_tab = (
            self.lineEdit.text(), self.comboBox.currentText(), self.comboBox_2.currentText(), self.lineEdit_2.text(),
            int(self.lineEdit_3.text()), self.comboBox_3.currentText(),)
        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(6)
        for n, text in enumerate(
                ["Сорт кофе", "Степень обжарки", "Молотый/в зернах", "Вкус", "Цена, руб", "Объем упаковки"]):
            item = QTableWidgetItem()
            item.setText(text)
            self.tableWidget.setHorizontalHeaderItem(n, item)
        for i, elem in enumerate(stroka_for_tab):
            self.tableWidget.setItem(0, i, QTableWidgetItem(str(elem)))

    def update_change(self):
        # print(self.id_change_coffee)
        if self.id_change_coffee >= 0:
            cur = self.con.cursor()
            cur.execute(f"""
                    UPDATE
                        coffee_sort
                    SET
                        sort_name = ?,
                        taste = ?,
                        price = ?                        
                    WHERE
                        id = ?
                    """, (
                self.lineEdit.text(), self.lineEdit_2.text(), int(self.lineEdit_3.text()), self.id_change_coffee))
            self.con.commit()

            cur = self.con.cursor()
            cur.execute(f"""
                        UPDATE
                         coffee_sort_roasting
                        SET
                         id_roasting = ?
                         WHERE
                          id_coffee_sort = ?
                        """, (self.comboBox.currentIndex() + 1, self.id_change_coffee))
            self.con.commit()

            cur = self.con.cursor()
            cur.execute(f"""
                        UPDATE
                         coffee_sort_ground
                        SET
                         id_ground = ?
                         WHERE
                          id_coffee_sort = ?
                        """, (self.comboBox_2.currentIndex() + 1, self.id_change_coffee))
            self.con.commit()

            cur = self.con.cursor()
            cur.execute(f"""
                        UPDATE
                         coffee_sort_pack
                        SET
                         id_pack = ?
                         WHERE
                          id_coffee_sort = ?
                        """, (self.comboBox_3.currentIndex() + 1, self.id_change_coffee))
            self.con.commit()
        self.make_table_for_change()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
