# -*- coding: utf-8 -*-
# @File  : editor_deluxe.py
# @Author: deeeeeeeee
# @Date  : 2018/6/18

import sys
import os
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QApplication, QAction, QMainWindow, QFileDialog, QTextEdit


class Editor(QMainWindow):

    def __init__(self):
        super().__init__()
        self.history = ''
        self.initUI()

    def initUI(self):
        self.text = QTextEdit()
        self.text.hide()
        self.setCentralWidget(self.text)
        self.initMenuBar()

        self.setGeometry(500, 300, 1000, 600)
        self.setWindowTitle('Editor Deluxe Edition')
        self.show()

    def initMenuBar(self):
        menu_bar = self.menuBar()
        write_menu = menu_bar.addMenu("pyWrite")
        file_menu = menu_bar.addMenu("File")
        edit_menu = menu_bar.addMenu("Edit")
        format_menu = menu_bar.addMenu("Format")
        window_menu = menu_bar.addMenu("Window")

        # fill format_menu
        bold_act = QAction('Bold', self)
        bold_act.setShortcut('Ctrl+B')
        bold_act.triggered.connect(lambda: self.text.setFontWeight(75))
        italic_act = QAction('Italic', self)
        italic_act.setShortcut('Ctrl+I')
        italic_act.triggered.connect(lambda: self.text.setFontItalic(True))
        underlined_act = QAction('Underlined_act', self)
        underlined_act.setShortcut('Ctrl+U')
        underlined_act.triggered.connect(lambda: self.text.setFontUnderline(True))
        note_act = QAction('Note_act', self)
        ommit_act = QAction('Ommit_act', self)
        add_pb_act = QAction('Add Page Break', self)
        add_pb_act.setShortcut('Ctrl+Enter')
        add_tp_act = QAction('Add Tilte Page', self)
        format_menu.addActions([bold_act, italic_act, underlined_act])
        format_menu.addSeparator()
        format_menu.addActions([note_act, ommit_act])
        format_menu.addSeparator()
        format_menu.addActions([add_pb_act, add_tp_act])

        # fill file_menu
        new_act = QAction(QIcon("new_file.png"), "New File", self)
        new_act.setShortcut("Ctrl+N")
        new_act.triggered.connect(self.new_file)
        open_act = QAction(QIcon("open_file.png"), 'Open', self)
        open_act.setShortcut("Ctrl+O")
        open_act.triggered.connect(self.open_file)
        save_act = QAction(QIcon("save.png"), 'Save', self)
        save_act.setShortcut("Ctrl+S")
        save_act.triggered.connect(self.save_file)
        save_as_act = QAction(QIcon("save_as.png"), 'Save As', self)
        save_as_act.setShortcut("Ctrl+Shift+S")
        save_as_act.triggered.connect(self.save_as_file)
        save_as_html = QAction(QIcon("save_origin_as.png"), "Save Origin As", self)
        save_as_html.setShortcut("Ctrl+Alt+S")
        save_as_html.triggered.connect(lambda: self.save_as_file(False))
        file_menu.addActions([new_act, open_act, save_act, save_as_act, save_as_html])

        # fill edit_menu
        undo_act = QAction(QIcon("undo.png"), 'Undo', self)
        undo_act.setShortcut("Ctrl+Z")
        undo_act.triggered.connect(self.text.undo)
        redo_act = QAction(QIcon("redo.png"), 'Redo', self)
        redo_act.setShortcut("Ctrl+Shift+Z")
        redo_act.triggered.connect(self.text.redo)
        copy_act = QAction(QIcon("copy.png"), 'Copy', self)
        copy_act.setShortcut("Ctrl+C")
        copy_act.triggered.connect(self.text.copy)
        paste_act = QAction(QIcon("paste.png"), 'Paste', self)
        paste_act.setShortcut("Ctrl+V")
        paste_act.triggered.connect(self.text.paste)
        cut_act = QAction(QIcon("cut.png"), 'Cut', self)
        cut_act.setShortcut("Ctrl+X")
        cut_act.triggered.connect(self.text.undo)
        edit_menu.addActions([undo_act, redo_act, copy_act, paste_act, cut_act])

    def new_file(self):
        self.text.show()
        self.filename = os.getcwd() + "\\Untitled.txt"
        print(self.filename)

    def open_file(self):
        self.filename, filetype = QFileDialog.getOpenFileName(self, '打开', '.', "Text Files (*.txt);;All Files (*)")
        if self.filename:
            with open(self.filename, "rt") as file:
                self.text.setText(file.read())
            self.text.show()
            self.statusBar().showMessage('open file: {}'.format(self.filename))

    def save_file(self):
        if self.filename:
            with open(self.filename, 'w') as file:
                file.write(self.text.toPlainText())
            self.statusBar().showMessage('save at: {}'.format(self.filename))

    def save_as_file(self, origin: bool = True):
        filename, filetype = QFileDialog.getSaveFileName(self, "另存为", '.', "Text Files (*.txt);;All Files (*)")
        if filename:
            self.filename = filename
            if self.filename:
                with open(self.filename, 'w') as file:
                    if origin:
                        file.write(self.text.toHtml())
                    else:
                        file.write(self.text.toPlainText())
                self.statusBar().showMessage('save at: {}'.format(self.filename))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    editor = Editor()
    qss_file = open('editor.qss').read()
    editor.setStyleSheet(qss_file)
    sys.exit(app.exec_())
