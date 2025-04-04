from collections import defaultdict

from PySide6.QtWidgets import (
    QMainWindow,
    QTableWidgetItem,
    QMessageBox,
)
from matplotlib import pyplot as plt

from term_editor_dialog import TermEditor
from ui.ui_mainWindow import Ui_MainWindow


class GraphEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.max_value_input.valueChanged.connect(self.generate_membership_functions)
        self.ui.build_graph_button.clicked.connect(self.plot_graph)
        self.ui.points_table.setHorizontalHeaderLabels(["X1 (0)", "X2 (1)", "X3 (1)", "X4 (0)"])
        self.ui.points_table.itemChanged.connect(self.on_table_value_changed)

        editor_dialog = TermEditor()
        if not editor_dialog.exec():
            return

        self.var_name = editor_dialog.ui.var_name.text()
        self.term_names = editor_dialog.term_names

        self.setWindowTitle(f"График для {self.var_name}")

        self.term_points = []

        self.generate_membership_functions()

    def on_table_value_changed(self, item: QTableWidgetItem):
        row_index = item.row()
        col_index = item.column()

        previous_value = self.term_points[row_index][col_index][0]
        new_value = int(item.text())

        if new_value < 0 or new_value > self.ui.max_value_input.value():
            QMessageBox.warning(
                self,
                "Ошибка полноты покрытия",
                str("Недопустимое значение x!"),
            )
            item.setText(str(self.term_points[row_index][col_index][0]))
            return
        self.term_points[row_index][col_index][0] = new_value

        sums = defaultdict(int)
        for segment in self.term_points:
            for point in segment:
                if point is not None:
                    x, y = point
                    sums[x] += y

        for key, value in sums.items():
            if value != 1:
                QMessageBox.warning(
                    self,
                    "Ошибка полноты покрытия",
                    str(f"Внимание! Для x={key} сумма функций принадлежности не равна 1.",),
                )
                self.term_points[row_index][col_index][0] = previous_value
                item.setText(str(self.term_points[row_index][col_index][0]))
                return

    def generate_membership_functions(self):
        terms_count = len(self.term_names)
        max_val = self.ui.max_value_input.value()

        if terms_count < 2:
            raise ValueError("Количество термов должно быть минимум 2.")

        step = max_val // (2 * terms_count)

        self.term_points.clear()

        for i in range(terms_count):
            if i == 0:
                x2 = 0
                x3 = step
                x4 = step * 2
                term_points = [
                    None,
                    [x2, 1],
                    [x3, 1],
                    [x4, 0],
                ]
            elif i == terms_count - 1:
                x1 = step * (2 * i - 1)
                x2 = step * (2 * i)
                x3 = step * (2 * i + 1)
                term_points = [
                    [x1, 0],
                    [x2, 1],
                    [x3, 1],
                    None,
                ]
            else:
                x1 = step * (2 * i - 1)
                x2 = step * (2 * i)
                x3 = step * (2 * i + 1)
                x4 = step * (2 * i + 2)
                term_points = [
                    [x1, 0],
                    [x2, 1],
                    [x3, 1],
                    [x4, 0],
                ]

            self.term_points.append(term_points)
        self.fill_points_table()

    def fill_points_table(self):
        self.ui.points_table.setRowCount(0)

        for i, points in enumerate(self.term_points):
            row = self.ui.points_table.rowCount()
            self.ui.points_table.insertRow(row)
            if i == 0:
                self.ui.points_table.setItem(row, 2, QTableWidgetItem(str(points[2][0])))
                self.ui.points_table.setItem(row, 3, QTableWidgetItem(str(points[3][0])))
            elif i == len(self.term_points) - 1:
                self.ui.points_table.setItem(row, 0, QTableWidgetItem(str(points[0][0])))
                self.ui.points_table.setItem(row, 1, QTableWidgetItem(str(points[1][0])))
            else:
                self.ui.points_table.setItem(row, 0, QTableWidgetItem(str(points[0][0])))
                self.ui.points_table.setItem(row, 1, QTableWidgetItem(str(points[1][0])))
                self.ui.points_table.setItem(row, 2, QTableWidgetItem(str(points[2][0])))
                self.ui.points_table.setItem(row, 3, QTableWidgetItem(str(points[3][0])))


    def plot_graph(self):
        plt.figure()

        for i, term in enumerate(self.term_points):
            term = [i for i in term if i]
            x, y = zip(*term)

            plt.plot(x, y, marker='o', label=f"Терм {i + 1}")

        plt.xlabel("Предметная шкала")
        plt.ylabel("Функция принадлежности")
        plt.legend()
        plt.grid(True)
        plt.show()
