#створи тут фоторедактор Easy Editor!
from PyQt5.QtWidgets import QApplication, QListWidget, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFileDialog
import os

app = QApplication([])
main_win = QWidget()
main_win.resize(700,500)
main_win.setWindowTitle('Easy Editor')
lb_image=QLabel('Картинка')
btn_dir =QPushButton('Папка')
main_files = QListWidget()

btn_left = QPushButton('Вліво')
btn_right = QPushButton('Вправо')
btn_flip = QPushButton('Зеркало')
btn_sharp = QPushButton('Різкість')
btn_bw = QPushButton('Ч/Б')

row = QHBoxLayout()
row2 = QHBoxLayout()
col1 = QVBoxLayout()
col2 = QVBoxLayout()
col1.addWidget(btn_dir)
col1.addWidget(main_files)
col2.addWidget(lb_image)
row2.addWidget(btn_left)
row2.addWidget(btn_right)
row2.addWidget(btn_flip)
row2.addWidget(btn_sharp)
row2.addWidget(btn_bw)

col2.addLayout(row2)

row.addLayout(col1)
row.addLayout(col2)
main_win.setLayout(row)

main_win.show()

workdir = ''

def chooseWorkdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()
    
def filter(files, extensions):
    result = []
    for filename in files:
        for ext in extensions:
            if filename.endswith(ext):
                result.append(filename)
    return result        

def showFilenamesList():
    extensions = ['.jpg', '.jpeg', '.png','.gif', '.bmp']
    chooseWorkdir()
    filenames = filter(os.listdir(workdir), extensions)
    main_files.clear()
    for filename in filenames:
        main_files.addItem(filename)

class ImageProcessor():
    def __init__(self):
        self.image = None
        self.dir = None
        self.filename = None
        self.save_dir = "Modified/"
    def loadImage(self, dir, filename):

        self.dir = dir
        self.filename = filename
        image_path = os.path.join(dir, filename)
        self.image = Image.open(image_path)

    def do_bw(self):
        self.image = self.image.convert("L")
        self.saveImage()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.showImage(image_path)
    def saveImage(self):
        path = os.path.join(self.dir, self.save_dir)
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        image_path = os.path.join(path, self.filename)
        self.image.save(image_path)


btn_dir.clicked.connect(showFilenamesList)


app.exec_()