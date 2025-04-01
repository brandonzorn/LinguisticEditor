from PySide6.QtWidgets import QApplication
import sys

from graph_editor import GraphEditor


if __name__ == "__main__":
    app = QApplication(sys.argv)

    graph_editor = GraphEditor()
    graph_editor.show()

    sys.exit(app.exec())
