from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QSpinBox,
    QLabel,
    QTableWidget,
    QPushButton,
    QTableWidgetItem,
)
from matplotlib import pyplot as plt

from term_editor_dialog import TermEditor


class GraphEditor(QMainWindow):
    def __init__(self):
        super().__init__()

        editor_dialog = TermEditor()
        if not editor_dialog.exec():
            return

        self.var_name = editor_dialog.ui.var_name.text()
        self.terms = editor_dialog.term_names

        self.setWindowTitle(f"График для {self.var_name}")
        self.initUI()


    def initUI(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()

        self.max_value_input = QSpinBox()
        self.max_value_input.setMaximum(1000)
        self.max_value_input.setValue(100)
        self.max_value_input.valueChanged.connect(self.generate_membership_functions)
        self.layout.addWidget(QLabel("Максимальное значение предметной шкалы:"))
        self.layout.addWidget(self.max_value_input)

        self.points_table = QTableWidget()
        self.points_table.setColumnCount(3)
        self.points_table.setHorizontalHeaderLabels(
            [
                "Значение X",
                "Значение принадлежности 1",
                "Значение принадлежности 2",
            ],
        )
        self.layout.addWidget(self.points_table)

        self.build_graph_button = QPushButton("Построить график")
        self.build_graph_button.clicked.connect(self.plot_graph)
        self.layout.addWidget(self.build_graph_button)

        self.central_widget.setLayout(self.layout)
        self.generate_membership_functions()

    def generate_membership_functions(self):
        self.points_table.setRowCount(0)
        max_val = self.max_value_input.value()

        step = max_val / (len(self.terms) * 2)
        x_values = [round(i * step) for i in range(len(self.terms) * 2)]
        y_values_1 = [
            int((i // 2) % 2 == 0) for i, x in enumerate(x_values)
        ]
        y_values_2 = [
            int(not ((i // 2) % 2 == 0)) for i, x in enumerate(x_values)
        ]

        for x, y1, y2 in zip(x_values, y_values_1, y_values_2):
            row = self.points_table.rowCount()
            self.points_table.insertRow(row)
            self.points_table.setItem(row, 0, QTableWidgetItem(str(x)))
            self.points_table.setItem(row, 1, QTableWidgetItem(str(y1)))
            self.points_table.setItem(row, 2, QTableWidgetItem(str(y2)))

        self.x_values = x_values
        self.y_values_1 = y_values_1
        self.y_values_2 = y_values_2

    def plot_graph(self):
        plt.figure()
        # plt.fill_between(self.x_values, self.y_values_1, color="skyblue", alpha=0.4, label="График 1")
        plt.plot(self.x_values, self.y_values_1, marker='o', linestyle='-', color="b", label="График 1")
        # plt.fill_between(self.x_values, self.y_values_2, color="salmon", alpha=0.4, label="График 2")
        plt.plot(self.x_values, self.y_values_2, marker='o', linestyle='-', color="r", label="График 2")
        plt.xlabel("Предметная шкала")
        plt.ylabel("Функция принадлежности")
        plt.legend()
        plt.grid(True)
        plt.show()
