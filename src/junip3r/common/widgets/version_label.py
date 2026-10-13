from PySide6.QtCore import Signal, Qt
from PySide6.QtGui import QCursor
from PySide6.QtWidgets import QLabel, QDialog, QVBoxLayout, QWidget, QSizePolicy

import importlib.metadata
VERSION = importlib.metadata.version("junip3r")


ABOUT_TEXT = """
<p>Designed and developed by Marcel Schmutz at the 3R Hub, ETH Zurich. \u00A9 2026</p>
<p>Testing and feedback: Tom Lorimer, Lukas von Ziegler, Fabienne Rössler</p>
<p>Source code: <a href=\"https://github.com/ETHZ-3Rhub/Junip3R\">https://github.com/ETHZ-3Rhub/Junip3R</a></p>
<p>The source code is released under the <a href=\"https://www.gnu.org/licenses/agpl-3.0.html\">AGPL-3.0 license</a>.</p>
"""


class ClickableLabel(QLabel):
    clicked = Signal()

    def __init__(self, text="", parent=None):
        super().__init__(text, parent)
        self.setCursor(Qt.CursorShape.ArrowCursor)
        self.setStyleSheet("color: grey;")

    def enterEvent(self, event):
        if self.isEnabled():
            self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
            self.setStyleSheet("color: grey; text-decoration: underline;")
        super().enterEvent(event)

    def leaveEvent(self, event):
        self.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.setStyleSheet("color: grey;")
        super().leaveEvent(event)

    def mousePressEvent(self, event):
        if self.isEnabled() and event.button() == Qt.MouseButton.LeftButton:
            self.clicked.emit()
        super().mousePressEvent(event)


class AboutDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("About Junip3R")

        layout = QVBoxLayout(self)

        self.lbl_title = QLabel(f"Junip3R v{VERSION}", self)
        self.lbl_title.setStyleSheet("font-weight: bold; font-size: 16px;")
        layout.addWidget(self.lbl_title)

        self.lbl_about = QLabel(ABOUT_TEXT, self)
        self.lbl_about.setTextFormat(Qt.TextFormat.RichText)
        self.lbl_about.setWordWrap(True)
        self.lbl_about.setOpenExternalLinks(True)
        layout.addWidget(self.lbl_about)

        self.spacer = QWidget(self)
        self.spacer.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        layout.addWidget(self.spacer)


class VersionLabel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        self.lbl_version = ClickableLabel(f"Junip3R v{VERSION} by Marcel Schmutz @ 3R Hub \u00B7 \u00A9 2026", self)
        layout.addWidget(self.lbl_version)

        self.lbl_version.clicked.connect(self._show_about_dialog)

    def _show_about_dialog(self):
        dialog = AboutDialog(self)
        dialog.setWindowModality(Qt.WindowModality.ApplicationModal)
        dialog.show()
