import PySide2
import pyqtgraph
from PySide2 import *
from PySide2 import QtWidgets
from PySide2.QtCore import QTimer
from pynput import keyboard
from mainwindow import Ui_MainWindow
import sys

data = {
    "a": 0,
    "b": 0,
    "c": 0,
    "d": 0,
    "e": 0,
    "f": 0,
    "g": 0,
    "h": 0,
    "i": 0,
    "j": 0,
    "k": 0,
    "l": 0,
    "m": 0,
    "n": 0,
    "o": 0,
    "p": 0,
    "q": 0,
    "r": 0,
    "s": 0,
    "t": 0,
    "u": 0,
    "v": 0,
    "w": 0,
    "x": 0,
    "y": 0,
    "z": 0,
}

def read_data():
    global data
    try:
        with open("datasheet.txt", "r") as file:
            file_reader = file.read()
            file_splitter = file_reader.split(" ")
            if file_reader != "":
                for x in file_splitter:
                    splitter_data = x.split(":")
                    if splitter_data != ['']:
                        data[splitter_data[0]] = int(splitter_data[1])
    except FileNotFoundError:
        file = open("datasheet.txt", "w")
        file.close()

def write_data():
    global data
    with open("datasheet.txt", "w") as file:
        for k, v in data.items():
            file.write(f"{k}:{v} ")

class MainGUI(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainGUI, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.timer = QTimer()
        self.timer.setInterval(3600000)
        self.timer.timeout.connect(write_data)
        self.timer.start()

        y = list(data.values())
        self.graph = pyqtgraph.BarGraphItem(x=range(26), height=y, width=0.6)
        self.ui.graphicsView.addItem(self.graph)

        self.update_gui()
    def closeEvent(self, event):
        write_data()

    def update_gui(self):
        global data
        self.ui.key_Q.setText(
            f"<html><head/><body><p>Q</p><p>{data['q']}</p></body></html>")
        self.ui.key_W.setText(
            f"<html><head/><body><p>W</p><p>{data['w']}</p></body></html>")
        self.ui.key_E.setText(
            f"<html><head/><body><p>E</p><p>{data['e']}</p></body></html>")
        self.ui.key_R.setText(
            f"<html><head/><body><p>R</p><p>{data['r']}</p></body></html>")
        self.ui.key_T.setText(
            f"<html><head/><body><p>T</p><p>{data['t']}</p></body></html>")
        self.ui.key_Y.setText(
            f"<html><head/><body><p>Y</p><p>{data['y']}</p></body></html>")
        self.ui.key_U.setText(
            f"<html><head/><body><p>U</p><p>{data['u']}</p></body></html>")
        self.ui.key_I.setText(
            f"<html><head/><body><p>I</p><p>{data['i']}</p></body></html>")
        self.ui.key_O.setText(
            f"<html><head/><body><p>O</p><p>{data['o']}</p></body></html>")
        self.ui.key_P.setText(
            f"<html><head/><body><p>P</p><p>{data['p']}</p></body></html>")
        self.ui.key_A.setText(
            f"<html><head/><body><p>A</p><p>{data['a']}</p></body></html>")
        self.ui.key_S.setText(
            f"<html><head/><body><p>S</p><p>{data['s']}</p></body></html>")
        self.ui.key_D.setText(
            f"<html><head/><body><p>D</p><p>{data['d']}</p></body></html>")
        self.ui.key_F.setText(
            f"<html><head/><body><p>F</p><p>{data['f']}</p></body></html>")
        self.ui.key_G.setText(
            f"<html><head/><body><p>G</p><p>{data['g']}</p></body></html>")
        self.ui.key_H.setText(
            f"<html><head/><body><p>H</p><p>{data['h']}</p></body></html>")
        self.ui.key_J.setText(
            f"<html><head/><body><p>J</p><p>{data['j']}</p></body></html>")
        self.ui.key_K.setText(
            f"<html><head/><body><p>K</p><p>{data['k']}</p></body></html>")
        self.ui.key_L.setText(
            f"<html><head/><body><p>L</p><p>{data['l']}</p></body></html>")
        self.ui.key_Z.setText(
            f"<html><head/><body><p>Z</p><p>{data['z']}</p></body></html>")
        self.ui.key_X.setText(
            f"<html><head/><body><p>X</p><p>{data['x']}</p></body></html>")
        self.ui.key_C.setText(
            f"<html><head/><body><p>C</p><p>{data['c']}</p></body></html>")
        self.ui.key_V.setText(
            f"<html><head/><body><p>V</p><p>{data['v']}</p></body></html>")
        self.ui.key_B.setText(
            f"<html><head/><body><p>B</p><p>{data['b']}</p></body></html>")
        self.ui.key_N.setText(
            f"<html><head/><body><p>N</p><p>{data['n']}</p></body></html>")
        self.ui.key_M.setText(
            f"<html><head/><body><p>M</p><p>{data['m']}</p></body></html>")
        y = list(data.values())
        self.graph.setOpts(x=range(26), height=y)


def on_press(key):
    try:
        if str(key.char).isalpha():
            z = str(key.char).lower()
            if data.get(z) is None:
                data[z] = 0
            data[z] += 1
            global main_gui
            main_gui.update_gui()
    except AttributeError:
        return


read_data()
app = QtWidgets.QApplication(sys.argv)
main_gui = MainGUI()


def main():
    global main_gui, app
    main_gui.show()
    listener = keyboard.Listener(on_press=on_press)
    PySide2.QtGui.QFontDatabase.addApplicationFont(":/font/arial.ttf")
    app.setFont(PySide2.QtGui.QFont("Arial Rounded MT Bold",20,5))
    listener.start()
    app.exec_()

main()
