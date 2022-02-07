from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QMainWindow,  QPushButton
from PyQt6.QtGui import QIcon, QFont, QPixmap, QMovie, QRegion, QMouseEvent
from PyQt6.QtCore import Qt
import sys
from ching import Game


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 700, 600)
        self.setWindowTitle("Stone Scissors Paper")

        self.user_label = QLabel("Your Points: ", self)
        self.user_label.move(100, 320)
        self.user_label.setStyleSheet('color:black')

        self.user_counter_label = QLabel("0", self)
        self.user_counter_label.move(200, 320)
        self.user_counter_label.setStyleSheet('color:black')

        self.pc_label = QLabel("PC Points: ", self)
        self.pc_label.move(100, 50)
        self.pc_label.setStyleSheet('color:black')

        self.pc_counter_label = QLabel("0", self)
        self.pc_counter_label.move(200, 50)
        self.pc_counter_label.setStyleSheet('color:black')

        self.user_scissors_btn = QPushButton(self)
        self.user_scissors_btn.setGeometry(100, 380, 100, 100)
        self.user_scissors_btn.setStyleSheet('background-color:white; qproperty-iconSize: 100px')
        self.user_scissors_btn.setIcon(QIcon("scissors.png"))
        self.user_scissors_btn.released.connect(self.scissors_selected)

        self.user_stone_btn = QPushButton(self)
        self.user_stone_btn.setGeometry(300, 380, 100, 100)
        self.user_stone_btn.setStyleSheet('background-color:white; qproperty-iconSize: 100px')
        self.user_stone_btn.setIcon(QIcon("stone.png"))
        self.user_stone_btn.released.connect(self.stone_selected)

        self.user_paper_btn = QPushButton(self)
        self.user_paper_btn.setGeometry(500, 380, 100, 100)
        self.user_paper_btn.setStyleSheet('background-color:white; qproperty-iconSize: 100px')
        self.user_paper_btn.setIcon(QIcon("paper.png"))
        self.user_paper_btn.released.connect(self.paper_selected)

        self.user_selected_move_label = QLabel(self)
        self.user_selected_move_label.setGeometry(300, 250, 100, 100)

        self.pc_selected_move_label = QLabel(self)
        self.pc_selected_move_label.setGeometry(300, 50, 100, 100)

        self.game = Game()

    def scissors_selected(self):
        self.set_pixmap(name='scissors')
        user_move = 2
        pc_move = self.game.user_turn(move=user_move)
        self.update_board(user_move, pc_move)

    def stone_selected(self):
        self.set_pixmap(name='stone')
        user_move = 0
        pc_move = self.game.user_turn(move=user_move)
        self.update_board(user_move, pc_move)

    def paper_selected(self):
        self.set_pixmap(name='paper')
        user_move = 1
        pc_move = self.game.user_turn(move=user_move)
        self.update_board(user_move, pc_move)

    def set_pixmap(self, player='user', name=''):
        pixmap = QPixmap(name+'.png')
        pixmap = pixmap.scaledToWidth(100)
        pixmap = pixmap.scaledToHeight(100)

        if player == 'user':
            self.user_selected_move_label.setPixmap(pixmap)
        else:
            self.pc_selected_move_label.setPixmap(pixmap)

    def update_board(self, user_move, pc_move):
        if pc_move == Game.STONE:
            self.set_pixmap('pc', 'stone')
        elif pc_move == Game.SCISSORS:
            self.set_pixmap('pc', 'scissors')
        else:
            self.set_pixmap('pc', 'paper')

        if user_move == Game.SCISSORS and pc_move == Game.STONE:
            self.pc_counter_label.setText(str(int(self.pc_counter_label.text()) + 1))
        if user_move == Game.SCISSORS and pc_move == Game.PAPER:
            self.user_counter_label.setText(str(int(self.user_counter_label.text()) + 1))
        if user_move == Game.STONE and pc_move == Game.SCISSORS:
            self.user_counter_label.setText(str(int(self.user_counter_label.text()) + 1))
        if user_move == Game.STONE and pc_move == Game.PAPER:
            self.pc_counter_label.setText(str(int(self.pc_counter_label.text()) + 1))
        if user_move == Game.PAPER and pc_move == Game.SCISSORS:
            self.pc_counter_label.setText(str(int(self.pc_counter_label.text()) + 1))
        if user_move == Game.PAPER and pc_move == Game.STONE:
            self.user_counter_label.setText(str(int(self.user_counter_label.text()) + 1))


    def increase_user_points(self):
        self.user_counter_label.setText(str(int(self.user_counter_label.text()) + 1))

    def increase_pc_points(self):
        self.pc_counter_label.setText(str(int(self.pc_counter_label.text()) + 1))


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())