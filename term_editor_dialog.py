import json

from PySide6.QtWidgets import (
    QDialog,
    QLineEdit,
    QFileDialog,
    QMessageBox,
)

from ui.ui_termDialog import Ui_Dialog


class TermEditor(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.setWindowTitle("Редактор лингвистической переменной")

        self.ui.term_count.valueChanged.connect(self.update_term_inputs)
        self.ui.build_button.clicked.connect(self.open_graph_editor)
        self.ui.save_button.clicked.connect(self.save_to_file)
        self.ui.load_button.clicked.connect(self.load_from_file)

        self.term_names = []

    def update_term_inputs(self):
        self.term_names.clear()
        for i in reversed(range(self.ui.term_inputs.count())):
            self.ui.term_inputs.itemAt(i).widget().deleteLater()
        for i in range(self.ui.term_count.value()):
            term_input = QLineEdit()
            self.term_names.append(term_input)
            self.ui.term_inputs.addWidget(term_input)

    def save_to_file(self):
        var_name = self.ui.var_name.text().strip()
        file_name, _ = QFileDialog.getSaveFileName(
            self,
            "Сохранить как",
            f"{var_name}.json",
            "JSON Files (*.json)",
        )
        if file_name:
            data = {
                "variable": var_name,
                "terms": [
                    term.text().strip() for term in self.term_names if term.text().strip()
                ]
            }
            with open(file_name, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)

    def load_from_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Открыть файл", "", "JSON Files (*.json)")
        if file_name:
            try:
                with open(file_name, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    self.ui.var_name.setText(data.get("variable", ""))
                    self.ui.term_count.setValue(len(data.get("terms", [])))

                    for i, term in enumerate(data.get("terms", [])):
                        term_input = self.ui.term_inputs.itemAt(i).widget()
                        term_input.setText(term)
            except Exception as e:
                QMessageBox.critical(self, "Ошибка", f"Не удалось загрузить данные: {e}")

    def open_graph_editor(self):
        if not self.ui.var_name.text().strip() or len(self.term_names) == 0:
            return
        self.accept()
