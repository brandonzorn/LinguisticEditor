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
        self.ui.points_table.setHorizontalHeaderLabels(
            [
                "Значение X",
                "Значение принадлежности 1",
                "Значение принадлежности 2",
            ],
        )
        self.ui.points_table.itemChanged.connect(self.on_table_value_changed)

        editor_dialog = TermEditor()
        if not editor_dialog.exec():
            return

        self.var_name = editor_dialog.ui.var_name.text()
        self.terms = editor_dialog.term_names

        self.setWindowTitle(f"График для {self.var_name}")

        self.x_values = []
        self.y_values_1 = []
        self.y_values_2 = []

        self.generate_membership_functions()

    def on_table_value_changed(self, item: QTableWidgetItem):
        if not self.x_values or not self.y_values_1 or not self.y_values_2:
            return

        new_value = int(item.text())
        row_index = item.row()

        if item.column() == 0:
            try:
                if new_value < 0 or new_value > self.ui.max_value_input.value():
                    raise ValueError("Недопустимое значение x!")
                self.x_values[row_index] = new_value
            except ValueError as e:
                QMessageBox.warning(
                    self,
                    "Ошибка полноты покрытия",
                    str(e),
                )
                item.setText(str(self.x_values[item.row()]))

        elif item.column() == 1:
            try:
                if new_value < 0 or new_value > 1:
                    raise ValueError("Недопустимое значение y1!")
                if new_value + self.y_values_2[row_index] != 1:
                    raise ValueError(
                        f"Внимание! Для x={self.x_values[row_index]} сумма функций принадлежности не равна 1.",
                    )
                self.y_values_1[row_index] = new_value
            except ValueError as e:
                QMessageBox.warning(
                    self,
                    "Ошибка полноты покрытия",
                    str(e),
                )
                item.setText(str(self.y_values_1[item.row()]))
        elif item.column() == 2:
            try:
                if new_value < 0 or new_value > 1:
                    raise ValueError("Недопустимое значение y2!")
                if self.y_values_1[row_index] + new_value != 1:
                    raise ValueError(
                        f"Внимание! Для x={self.x_values[row_index]} сумма функций принадлежности не равна 1.",
                    )
                self.y_values_2[row_index] = new_value
            except ValueError as e:
                QMessageBox.warning(
                    self,
                    "Ошибка полноты покрытия",
                    str(e),
                )
                item.setText(str(self.y_values_2[item.row()]))

    def generate_membership_functions(self):
        self.ui.points_table.setRowCount(0)
        max_val = self.ui.max_value_input.value()

        step = max_val / (len(self.terms) * 2)
        x_values = [round(i * step) for i in range(len(self.terms) * 2)]
        y_values_1 = [
            int((i // 2) % 2 == 0) for i, x in enumerate(x_values)
        ]
        y_values_2 = [
            int(not ((i // 2) % 2 == 0)) for i, x in enumerate(x_values)
        ]

        for x, y1, y2 in zip(x_values, y_values_1, y_values_2):
            row = self.ui.points_table.rowCount()
            self.ui.points_table.insertRow(row)
            self.ui.points_table.setItem(row, 0, QTableWidgetItem(str(x)))
            self.ui.points_table.setItem(row, 1, QTableWidgetItem(str(y1)))
            self.ui.points_table.setItem(row, 2, QTableWidgetItem(str(y2)))

        self.x_values = x_values
        self.y_values_1 = y_values_1
        self.y_values_2 = y_values_2

    def plot_graph(self):
        plt.figure()
        plt.plot(self.x_values, self.y_values_1, marker='o', linestyle='-', color="b", label="График 1")
        plt.plot(self.x_values, self.y_values_2, marker='o', linestyle='-', color="r", label="График 2")
        plt.xlabel("Предметная шкала")
        plt.ylabel("Функция принадлежности")
        plt.legend()
        plt.grid(True)
        plt.show()
