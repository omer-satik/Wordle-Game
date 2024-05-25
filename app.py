import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from gui import Ui_MainWindow
from words import Words
import random


class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.num_letters = 0
        self.chosen_word_list = []

        self.words = Words()
        words_set = self.words.words_set

        word_list_4 = list(filter(lambda x: len(x) == 4, words_set))
        word_list_5 = list(filter(lambda x: len(x) == 5, words_set))
        word_list_6 = list(filter(lambda x: len(x) == 6, words_set))
        self.word_list_4 = [i.upper() for i in word_list_4]
        self.word_list_5 = [i.upper() for i in word_list_5]
        self.word_list_6 = [i.upper() for i in word_list_6]

        self.win_word = ""
        self.win_word1 = ""
        self.win_word2 = ""
        self.win_word3 = ""
        self.win_word4 = ""
        self.win_words = []

        self.win_word_is_found = False
        self.win_word1_is_found = False
        self.win_word2_is_found = False
        self.win_word3_is_found = False
        self.win_word4_is_found = False
        self.game_over = False  # indicates if the guess rights are over

        self.game_mode = ""
        self.mode_w = False  # wordle mode
        self.mode_q = False  # quordle mode

        # Rows of wordle modes
        self.row1 = []
        self.row2 = []
        self.row3 = []
        self.row4 = []
        self.row5 = []
        self.row6 = []
        self.row7 = []
        #

        # Rows of quordle modes
        self.row1_1 = []
        self.row1_2 = []
        self.row1_3 = []
        self.row1_4 = []

        self.row2_1 = []
        self.row2_2 = []
        self.row2_3 = []
        self.row2_4 = []

        self.row3_1 = []
        self.row3_2 = []
        self.row3_3 = []
        self.row3_4 = []

        self.row4_1 = []
        self.row4_2 = []
        self.row4_3 = []
        self.row4_4 = []

        self.row5_1 = []
        self.row5_2 = []
        self.row5_3 = []
        self.row5_4 = []

        self.row6_1 = []
        self.row6_2 = []
        self.row6_3 = []
        self.row6_4 = []

        self.row7_1 = []
        self.row7_2 = []
        self.row7_3 = []
        self.row7_4 = []

        self.row8_1 = []
        self.row8_2 = []
        self.row8_3 = []
        self.row8_4 = []

        self.row9_1 = []
        self.row9_2 = []
        self.row9_3 = []
        self.row9_4 = []

        self.row10_1 = []
        self.row10_2 = []
        self.row10_3 = []
        self.row10_4 = []

        self.row11_1 = []
        self.row11_2 = []
        self.row11_3 = []
        self.row11_4 = []
        #

        # Keyboard buttons
        self.keyboard = [self.ui.a, self.ui.b, self.ui.c, self.ui.d, self.ui.e, self.ui.f,
                         self.ui.g, self.ui.h, self.ui.i, self.ui.j, self.ui.k, self.ui.l,
                         self.ui.m, self.ui.n, self.ui.o, self.ui.p, self.ui.q, self.ui.r,
                         self.ui.s, self.ui.t, self.ui.u, self.ui.v, self.ui.w, self.ui.x, self.ui.y, self.ui.z]

        self.row_dict = {}  # Dictionary of wordle mode rows
        self.rows_dict = {}  # Dictionary of quordle mode rows
        self.counter = 1

        self.texter()
        self.open_page1()
        self.ui.four_letters_mode.clicked.connect(self.open_page2)
        self.ui.five_letters_mode.clicked.connect(self.open_page3)
        self.ui.six_letters_mode.clicked.connect(self.open_page4)
        self.ui.four_letters_mode_q.clicked.connect(self.open_page5)
        self.ui.five_letters_mode_q.clicked.connect(self.open_page6)
        self.ui.six_letters_mode_q.clicked.connect(self.open_page7)
        self.ui.back_home.clicked.connect(self.clean_buttons)
        self.ui.back_home.clicked.connect(self.open_page1)
        self.ui.play_again.clicked.connect(self.refresh)
        self.ui.quit_game.clicked.connect(QApplication.quit)

    def determine_row_dict(self, num_letters):  # creates the dictionary that stores the rows of the respective gamemode
        if num_letters == 4:
            if self.mode_w:
                self.row1 = [self.ui.b1_1, self.ui.b1_2, self.ui.b1_3, self.ui.b1_4]
                self.row2 = [self.ui.b2_1, self.ui.b2_2, self.ui.b2_3, self.ui.b2_4]
                self.row3 = [self.ui.b3_1, self.ui.b3_2, self.ui.b3_3, self.ui.b3_4]
                self.row4 = [self.ui.b4_1, self.ui.b4_2, self.ui.b4_3, self.ui.b4_4]
                self.row5 = [self.ui.b5_1, self.ui.b5_2, self.ui.b5_3, self.ui.b5_4]
                self.row_dict = {1: self.row1, 2: self.row2, 3: self.row3, 4: self.row4, 5: self.row5}

            elif self.mode_q:
                self.row1_1 = [self.ui.e1_1_1, self.ui.e1_1_2, self.ui.e1_1_3, self.ui.e1_1_4] # eg: row1 of 1st guess block
                self.row1_2 = [self.ui.e2_1_1, self.ui.e2_1_2, self.ui.e2_1_3, self.ui.e2_1_4]
                self.row1_3 = [self.ui.e3_1_1, self.ui.e3_1_2, self.ui.e3_1_3, self.ui.e3_1_4]
                self.row1_4 = [self.ui.e4_1_1, self.ui.e4_1_2, self.ui.e4_1_3, self.ui.e4_1_4]

                self.row2_1 = [self.ui.e1_2_1, self.ui.e1_2_2, self.ui.e1_2_3, self.ui.e1_2_4] # eg: row2 of 2nd guess block
                self.row2_2 = [self.ui.e2_2_1, self.ui.e2_2_2, self.ui.e2_2_3, self.ui.e2_2_4]
                self.row2_3 = [self.ui.e3_2_1, self.ui.e3_2_2, self.ui.e3_2_3, self.ui.e3_2_4]
                self.row2_4 = [self.ui.e4_2_1, self.ui.e4_2_2, self.ui.e4_2_3, self.ui.e4_2_4]

                self.row3_1 = [self.ui.e1_3_1, self.ui.e1_3_2, self.ui.e1_3_3, self.ui.e1_3_4]
                self.row3_2 = [self.ui.e2_3_1, self.ui.e2_3_2, self.ui.e2_3_3, self.ui.e2_3_4]
                self.row3_3 = [self.ui.e3_3_1, self.ui.e3_3_2, self.ui.e3_3_3, self.ui.e3_3_4]
                self.row3_4 = [self.ui.e4_3_1, self.ui.e4_3_2, self.ui.e4_3_3, self.ui.e4_3_4]

                self.row4_1 = [self.ui.e1_4_1, self.ui.e1_4_2, self.ui.e1_4_3, self.ui.e1_4_4]
                self.row4_2 = [self.ui.e2_4_1, self.ui.e2_4_2, self.ui.e2_4_3, self.ui.e2_4_4]
                self.row4_3 = [self.ui.e3_4_1, self.ui.e3_4_2, self.ui.e3_4_3, self.ui.e3_4_4]
                self.row4_4 = [self.ui.e4_4_1, self.ui.e4_4_2, self.ui.e4_4_3, self.ui.e4_4_4]

                self.row5_1 = [self.ui.e1_5_1, self.ui.e1_5_2, self.ui.e1_5_3, self.ui.e1_5_4]
                self.row5_2 = [self.ui.e2_5_1, self.ui.e2_5_2, self.ui.e2_5_3, self.ui.e2_5_4]
                self.row5_3 = [self.ui.e3_5_1, self.ui.e3_5_2, self.ui.e3_5_3, self.ui.e3_5_4]
                self.row5_4 = [self.ui.e4_5_1, self.ui.e4_5_2, self.ui.e4_5_3, self.ui.e4_5_4]

                self.row6_1 = [self.ui.e1_6_1, self.ui.e1_6_2, self.ui.e1_6_3, self.ui.e1_6_4]
                self.row6_2 = [self.ui.e2_6_1, self.ui.e2_6_2, self.ui.e2_6_3, self.ui.e2_6_4]
                self.row6_3 = [self.ui.e3_6_1, self.ui.e3_6_2, self.ui.e3_6_3, self.ui.e3_6_4]
                self.row6_4 = [self.ui.e4_6_1, self.ui.e4_6_2, self.ui.e4_6_3, self.ui.e4_6_4]

                self.row7_1 = [self.ui.e1_7_1, self.ui.e1_7_2, self.ui.e1_7_3, self.ui.e1_7_4]
                self.row7_2 = [self.ui.e2_7_1, self.ui.e2_7_2, self.ui.e2_7_3, self.ui.e2_7_4]
                self.row7_3 = [self.ui.e3_7_1, self.ui.e3_7_2, self.ui.e3_7_3, self.ui.e3_7_4]
                self.row7_4 = [self.ui.e4_7_1, self.ui.e4_7_2, self.ui.e4_7_3, self.ui.e4_7_4]

                self.rows_dict = {1: [self.row1_1, self.row1_2, self.row1_3, self.row1_4],
                                  2: [self.row2_1, self.row2_2, self.row2_3, self.row2_4],
                                  3: [self.row3_1, self.row3_2, self.row3_3, self.row3_4],
                                  4: [self.row4_1, self.row4_2, self.row4_3, self.row4_4],
                                  5: [self.row5_1, self.row5_2, self.row5_3, self.row5_4],
                                  6: [self.row6_1, self.row6_2, self.row6_3, self.row6_4],
                                  7: [self.row7_1, self.row7_2, self.row7_3, self.row7_4]}

        elif num_letters == 5:
            if self.mode_w:
                self.row1 = [self.ui.c1_1, self.ui.c1_2, self.ui.c1_3, self.ui.c1_4, self.ui.c1_5]
                self.row2 = [self.ui.c2_1, self.ui.c2_2, self.ui.c2_3, self.ui.c2_4, self.ui.c2_5]
                self.row3 = [self.ui.c3_1, self.ui.c3_2, self.ui.c3_3, self.ui.c3_4, self.ui.c3_5]
                self.row4 = [self.ui.c4_1, self.ui.c4_2, self.ui.c4_3, self.ui.c4_4, self.ui.c4_5]
                self.row5 = [self.ui.c5_1, self.ui.c5_2, self.ui.c5_3, self.ui.c5_4, self.ui.c5_5]
                self.row6 = [self.ui.c6_1, self.ui.c6_2, self.ui.c6_3, self.ui.c6_4, self.ui.c6_5]
                self.row_dict = {1: self.row1, 2: self.row2, 3: self.row3, 4: self.row4, 5: self.row5, 6: self.row6}

            elif self.mode_q:
                self.row1_1 = [self.ui.f1_1_1, self.ui.f1_1_2, self.ui.f1_1_3, self.ui.f1_1_4, self.ui.f1_1_5]
                self.row1_2 = [self.ui.f2_1_1, self.ui.f2_1_2, self.ui.f2_1_3, self.ui.f2_1_4, self.ui.f2_1_5]
                self.row1_3 = [self.ui.f3_1_1, self.ui.f3_1_2, self.ui.f3_1_3, self.ui.f3_1_4, self.ui.f3_1_5]
                self.row1_4 = [self.ui.f4_1_1, self.ui.f4_1_2, self.ui.f4_1_3, self.ui.f4_1_4, self.ui.f4_1_5]

                self.row2_1 = [self.ui.f1_2_1, self.ui.f1_2_2, self.ui.f1_2_3, self.ui.f1_2_4, self.ui.f1_2_5]
                self.row2_2 = [self.ui.f2_2_1, self.ui.f2_2_2, self.ui.f2_2_3, self.ui.f2_2_4, self.ui.f2_2_5]
                self.row2_3 = [self.ui.f3_2_1, self.ui.f3_2_2, self.ui.f3_2_3, self.ui.f3_2_4, self.ui.f3_2_5]
                self.row2_4 = [self.ui.f4_2_1, self.ui.f4_2_2, self.ui.f4_2_3, self.ui.f4_2_4, self.ui.f4_2_5]

                self.row3_1 = [self.ui.f1_3_1, self.ui.f1_3_2, self.ui.f1_3_3, self.ui.f1_3_4, self.ui.f1_3_5]
                self.row3_2 = [self.ui.f2_3_1, self.ui.f2_3_2, self.ui.f2_3_3, self.ui.f2_3_4, self.ui.f2_3_5]
                self.row3_3 = [self.ui.f3_3_1, self.ui.f3_3_2, self.ui.f3_3_3, self.ui.f3_3_4, self.ui.f3_3_5]
                self.row3_4 = [self.ui.f4_3_1, self.ui.f4_3_2, self.ui.f4_3_3, self.ui.f4_3_4, self.ui.f4_3_5]

                self.row4_1 = [self.ui.f1_4_1, self.ui.f1_4_2, self.ui.f1_4_3, self.ui.f1_4_4, self.ui.f1_4_5]
                self.row4_2 = [self.ui.f2_4_1, self.ui.f2_4_2, self.ui.f2_4_3, self.ui.f2_4_4, self.ui.f2_4_5]
                self.row4_3 = [self.ui.f3_4_1, self.ui.f3_4_2, self.ui.f3_4_3, self.ui.f3_4_4, self.ui.f3_4_5]
                self.row4_4 = [self.ui.f4_4_1, self.ui.f4_4_2, self.ui.f4_4_3, self.ui.f4_4_4, self.ui.f4_4_5]

                self.row5_1 = [self.ui.f1_5_1, self.ui.f1_5_2, self.ui.f1_5_3, self.ui.f1_5_4, self.ui.f1_5_5]
                self.row5_2 = [self.ui.f2_5_1, self.ui.f2_5_2, self.ui.f2_5_3, self.ui.f2_5_4, self.ui.f2_5_5]
                self.row5_3 = [self.ui.f3_5_1, self.ui.f3_5_2, self.ui.f3_5_3, self.ui.f3_5_4, self.ui.f3_5_5]
                self.row5_4 = [self.ui.f4_5_1, self.ui.f4_5_2, self.ui.f4_5_3, self.ui.f4_5_4, self.ui.f4_5_5]

                self.row6_1 = [self.ui.f1_6_1, self.ui.f1_6_2, self.ui.f1_6_3, self.ui.f1_6_4, self.ui.f1_6_5]
                self.row6_2 = [self.ui.f2_6_1, self.ui.f2_6_2, self.ui.f2_6_3, self.ui.f2_6_4, self.ui.f2_6_5]
                self.row6_3 = [self.ui.f3_6_1, self.ui.f3_6_2, self.ui.f3_6_3, self.ui.f3_6_4, self.ui.f3_6_5]
                self.row6_4 = [self.ui.f4_6_1, self.ui.f4_6_2, self.ui.f4_6_3, self.ui.f4_6_4, self.ui.f4_6_5]

                self.row7_1 = [self.ui.f1_7_1, self.ui.f1_7_2, self.ui.f1_7_3, self.ui.f1_7_4, self.ui.f1_7_5]
                self.row7_2 = [self.ui.f2_7_1, self.ui.f2_7_2, self.ui.f2_7_3, self.ui.f2_7_4, self.ui.f2_7_5]
                self.row7_3 = [self.ui.f3_7_1, self.ui.f3_7_2, self.ui.f3_7_3, self.ui.f3_7_4, self.ui.f3_7_5]
                self.row7_4 = [self.ui.f4_7_1, self.ui.f4_7_2, self.ui.f4_7_3, self.ui.f4_7_4, self.ui.f4_7_5]

                self.row8_1 = [self.ui.f1_8_1, self.ui.f1_8_2, self.ui.f1_8_3, self.ui.f1_8_4, self.ui.f1_8_5]
                self.row8_2 = [self.ui.f2_8_1, self.ui.f2_8_2, self.ui.f2_8_3, self.ui.f2_8_4, self.ui.f2_8_5]
                self.row8_3 = [self.ui.f3_8_1, self.ui.f3_8_2, self.ui.f3_8_3, self.ui.f3_8_4, self.ui.f3_8_5]
                self.row8_4 = [self.ui.f4_8_1, self.ui.f4_8_2, self.ui.f4_8_3, self.ui.f4_8_4, self.ui.f4_8_5]

                self.row9_1 = [self.ui.f1_9_1, self.ui.f1_9_2, self.ui.f1_9_3, self.ui.f1_9_4, self.ui.f1_9_5]
                self.row9_2 = [self.ui.f2_9_1, self.ui.f2_9_2, self.ui.f2_9_3, self.ui.f2_9_4, self.ui.f2_9_5]
                self.row9_3 = [self.ui.f3_9_1, self.ui.f3_9_2, self.ui.f3_9_3, self.ui.f3_9_4, self.ui.f3_9_5]
                self.row9_4 = [self.ui.f4_9_1, self.ui.f4_9_2, self.ui.f4_9_3, self.ui.f4_9_4, self.ui.f4_9_5]

                self.rows_dict = {1: [self.row1_1, self.row1_2, self.row1_3, self.row1_4],
                                  2: [self.row2_1, self.row2_2, self.row2_3, self.row2_4],
                                  3: [self.row3_1, self.row3_2, self.row3_3, self.row3_4],
                                  4: [self.row4_1, self.row4_2, self.row4_3, self.row4_4],
                                  5: [self.row5_1, self.row5_2, self.row5_3, self.row5_4],
                                  6: [self.row6_1, self.row6_2, self.row6_3, self.row6_4],
                                  7: [self.row7_1, self.row7_2, self.row7_3, self.row7_4],
                                  8: [self.row8_1, self.row8_2, self.row8_3, self.row8_4],
                                  9: [self.row9_1, self.row9_2, self.row9_3, self.row9_4]}


        elif num_letters == 6:
            if self.mode_w:
                self.row1 = [self.ui.d1_1, self.ui.d1_2, self.ui.d1_3, self.ui.d1_4, self.ui.d1_5, self.ui.d1_6]
                self.row2 = [self.ui.d2_1, self.ui.d2_2, self.ui.d2_3, self.ui.d2_4, self.ui.d2_5, self.ui.d2_6]
                self.row3 = [self.ui.d3_1, self.ui.d3_2, self.ui.d3_3, self.ui.d3_4, self.ui.d3_5, self.ui.d3_6]
                self.row4 = [self.ui.d4_1, self.ui.d4_2, self.ui.d4_3, self.ui.d4_4, self.ui.d4_5, self.ui.d4_6]
                self.row5 = [self.ui.d5_1, self.ui.d5_2, self.ui.d5_3, self.ui.d5_4, self.ui.d5_5, self.ui.d5_6]
                self.row6 = [self.ui.d6_1, self.ui.d6_2, self.ui.d6_3, self.ui.d6_4, self.ui.d6_5, self.ui.d6_6]
                self.row7 = [self.ui.d7_1, self.ui.d7_2, self.ui.d7_3, self.ui.d7_4, self.ui.d7_5, self.ui.d7_6]
                self.row_dict = {1: self.row1, 2: self.row2, 3: self.row3, 4: self.row4,
                                 5: self.row5, 6: self.row6, 7: self.row7}
            elif self.mode_q:
                self.row1_1 = [self.ui.g1_1_1, self.ui.g1_1_2, self.ui.g1_1_3, self.ui.g1_1_4, self.ui.g1_1_5,
                               self.ui.g1_1_6]
                self.row1_2 = [self.ui.g2_1_1, self.ui.g2_1_2, self.ui.g2_1_3, self.ui.g2_1_4, self.ui.g2_1_5,
                               self.ui.g2_1_6]
                self.row1_3 = [self.ui.g3_1_1, self.ui.g3_1_2, self.ui.g3_1_3, self.ui.g3_1_4, self.ui.g3_1_5,
                               self.ui.g3_1_6]
                self.row1_4 = [self.ui.g4_1_1, self.ui.g4_1_2, self.ui.g4_1_3, self.ui.g4_1_4, self.ui.g4_1_5,
                               self.ui.g4_1_6]

                self.row2_1 = [self.ui.g1_2_1, self.ui.g1_2_2, self.ui.g1_2_3, self.ui.g1_2_4, self.ui.g1_2_5,
                               self.ui.g1_2_6]
                self.row2_2 = [self.ui.g2_2_1, self.ui.g2_2_2, self.ui.g2_2_3, self.ui.g2_2_4, self.ui.g2_2_5,
                               self.ui.g2_2_6]
                self.row2_3 = [self.ui.g3_2_1, self.ui.g3_2_2, self.ui.g3_2_3, self.ui.g3_2_4, self.ui.g3_2_5,
                               self.ui.g3_2_6]
                self.row2_4 = [self.ui.g4_2_1, self.ui.g4_2_2, self.ui.g4_2_3, self.ui.g4_2_4, self.ui.g4_2_5,
                               self.ui.g4_2_6]

                self.row3_1 = [self.ui.g1_3_1, self.ui.g1_3_2, self.ui.g1_3_3, self.ui.g1_3_4, self.ui.g1_3_5,
                               self.ui.g1_3_6]
                self.row3_2 = [self.ui.g2_3_1, self.ui.g2_3_2, self.ui.g2_3_3, self.ui.g2_3_4, self.ui.g2_3_5,
                               self.ui.g2_3_6]
                self.row3_3 = [self.ui.g3_3_1, self.ui.g3_3_2, self.ui.g3_3_3, self.ui.g3_3_4, self.ui.g3_3_5,
                               self.ui.g3_3_6]
                self.row3_4 = [self.ui.g4_3_1, self.ui.g4_3_2, self.ui.g4_3_3, self.ui.g4_3_4, self.ui.g4_3_5,
                               self.ui.g4_3_6]

                self.row4_1 = [self.ui.g1_4_1, self.ui.g1_4_2, self.ui.g1_4_3, self.ui.g1_4_4, self.ui.g1_4_5,
                               self.ui.g1_4_6]
                self.row4_2 = [self.ui.g2_4_1, self.ui.g2_4_2, self.ui.g2_4_3, self.ui.g2_4_4, self.ui.g2_4_5,
                               self.ui.g2_4_6]
                self.row4_3 = [self.ui.g3_4_1, self.ui.g3_4_2, self.ui.g3_4_3, self.ui.g3_4_4, self.ui.g3_4_5,
                               self.ui.g3_4_6]
                self.row4_4 = [self.ui.g4_4_1, self.ui.g4_4_2, self.ui.g4_4_3, self.ui.g4_4_4, self.ui.g4_4_5,
                               self.ui.g4_4_6]

                self.row5_1 = [self.ui.g1_5_1, self.ui.g1_5_2, self.ui.g1_5_3, self.ui.g1_5_4, self.ui.g1_5_5,
                               self.ui.g1_5_6]
                self.row5_2 = [self.ui.g2_5_1, self.ui.g2_5_2, self.ui.g2_5_3, self.ui.g2_5_4, self.ui.g2_5_5,
                               self.ui.g2_5_6]
                self.row5_3 = [self.ui.g3_5_1, self.ui.g3_5_2, self.ui.g3_5_3, self.ui.g3_5_4, self.ui.g3_5_5,
                               self.ui.g3_5_6]
                self.row5_4 = [self.ui.g4_5_1, self.ui.g4_5_2, self.ui.g4_5_3, self.ui.g4_5_4, self.ui.g4_5_5,
                               self.ui.g4_5_6]

                self.row6_1 = [self.ui.g1_6_1, self.ui.g1_6_2, self.ui.g1_6_3, self.ui.g1_6_4, self.ui.g1_6_5,
                               self.ui.g1_6_6]
                self.row6_2 = [self.ui.g2_6_1, self.ui.g2_6_2, self.ui.g2_6_3, self.ui.g2_6_4, self.ui.g2_6_5,
                               self.ui.g2_6_6]
                self.row6_3 = [self.ui.g3_6_1, self.ui.g3_6_2, self.ui.g3_6_3, self.ui.g3_6_4, self.ui.g3_6_5,
                               self.ui.g3_6_6]
                self.row6_4 = [self.ui.g4_6_1, self.ui.g4_6_2, self.ui.g4_6_3, self.ui.g4_6_4, self.ui.g4_6_5,
                               self.ui.g4_6_6]

                self.row7_1 = [self.ui.g1_7_1, self.ui.g1_7_2, self.ui.g1_7_3, self.ui.g1_7_4, self.ui.g1_7_5,
                               self.ui.g1_7_6]
                self.row7_2 = [self.ui.g2_7_1, self.ui.g2_7_2, self.ui.g2_7_3, self.ui.g2_7_4, self.ui.g2_7_5,
                               self.ui.g2_7_6]
                self.row7_3 = [self.ui.g3_7_1, self.ui.g3_7_2, self.ui.g3_7_3, self.ui.g3_7_4, self.ui.g3_7_5,
                               self.ui.g3_7_6]
                self.row7_4 = [self.ui.g4_7_1, self.ui.g4_7_2, self.ui.g4_7_3, self.ui.g4_7_4, self.ui.g4_7_5,
                               self.ui.g4_7_6]

                self.row8_1 = [self.ui.g1_8_1, self.ui.g1_8_2, self.ui.g1_8_3, self.ui.g1_8_4, self.ui.g1_8_5,
                               self.ui.g1_8_6]
                self.row8_2 = [self.ui.g2_8_1, self.ui.g2_8_2, self.ui.g2_8_3, self.ui.g2_8_4, self.ui.g2_8_5,
                               self.ui.g2_8_6]
                self.row8_3 = [self.ui.g3_8_1, self.ui.g3_8_2, self.ui.g3_8_3, self.ui.g3_8_4, self.ui.g3_8_5,
                               self.ui.g3_8_6]
                self.row8_4 = [self.ui.g4_8_1, self.ui.g4_8_2, self.ui.g4_8_3, self.ui.g4_8_4, self.ui.g4_8_5,
                               self.ui.g4_8_6]

                self.row9_1 = [self.ui.g1_9_1, self.ui.g1_9_2, self.ui.g1_9_3, self.ui.g1_9_4, self.ui.g1_9_5,
                               self.ui.g1_9_6]
                self.row9_2 = [self.ui.g2_9_1, self.ui.g2_9_2, self.ui.g2_9_3, self.ui.g2_9_4, self.ui.g2_9_5,
                               self.ui.g2_9_6]
                self.row9_3 = [self.ui.g3_9_1, self.ui.g3_9_2, self.ui.g3_9_3, self.ui.g3_9_4, self.ui.g3_9_5,
                               self.ui.g3_9_6]
                self.row9_4 = [self.ui.g4_9_1, self.ui.g4_9_2, self.ui.g4_9_3, self.ui.g4_9_4, self.ui.g4_9_5,
                               self.ui.g4_9_6]

                self.row10_1 = [self.ui.g1_10_1, self.ui.g1_10_2, self.ui.g1_10_3, self.ui.g1_10_4, self.ui.g1_10_5,
                                self.ui.g1_10_6]
                self.row10_2 = [self.ui.g2_10_1, self.ui.g2_10_2, self.ui.g2_10_3, self.ui.g2_10_4, self.ui.g2_10_5,
                                self.ui.g2_10_6]
                self.row10_3 = [self.ui.g3_10_1, self.ui.g3_10_2, self.ui.g3_10_3, self.ui.g3_10_4, self.ui.g3_10_5,
                                self.ui.g3_10_6]
                self.row10_4 = [self.ui.g4_10_1, self.ui.g4_10_2, self.ui.g4_10_3, self.ui.g4_10_4, self.ui.g4_10_5,
                                self.ui.g4_10_6]

                self.row11_1 = [self.ui.g1_11_1, self.ui.g1_11_2, self.ui.g1_11_3, self.ui.g1_11_4, self.ui.g1_11_5,
                                self.ui.g1_11_6]
                self.row11_2 = [self.ui.g2_11_1, self.ui.g2_11_2, self.ui.g2_11_3, self.ui.g2_11_4, self.ui.g2_11_5,
                                self.ui.g2_11_6]
                self.row11_3 = [self.ui.g3_11_1, self.ui.g3_11_2, self.ui.g3_11_3, self.ui.g3_11_4, self.ui.g3_11_5,
                                self.ui.g3_11_6]
                self.row11_4 = [self.ui.g4_11_1, self.ui.g4_11_2, self.ui.g4_11_3, self.ui.g4_11_4, self.ui.g4_11_5,
                                self.ui.g4_11_6]

                self.rows_dict = {1: [self.row1_1, self.row1_2, self.row1_3, self.row1_4],
                                  2: [self.row2_1, self.row2_2, self.row2_3, self.row2_4],
                                  3: [self.row3_1, self.row3_2, self.row3_3, self.row3_4],
                                  4: [self.row4_1, self.row4_2, self.row4_3, self.row4_4],
                                  5: [self.row5_1, self.row5_2, self.row5_3, self.row5_4],
                                  6: [self.row6_1, self.row6_2, self.row6_3, self.row6_4],
                                  7: [self.row7_1, self.row7_2, self.row7_3, self.row7_4],
                                  8: [self.row8_1, self.row8_2, self.row8_3, self.row8_4],
                                  9: [self.row9_1, self.row9_2, self.row9_3, self.row9_4],
                                  10: [self.row10_1, self.row10_2, self.row10_3, self.row10_4],
                                  11: [self.row11_1, self.row11_2, self.row11_3, self.row11_4]}

    def open_page1(self):  # Page1 is opened at the beginning and whenever "Back to main menu" button is pressed
        self.ui.stackedWidget.setCurrentIndex(0)
        self.win_word = ""
        self.win_word1 = ""
        self.win_word2 = ""
        self.win_word3 = ""
        self.win_word4 = ""
        self.win_words = []

        self.win_word_is_found = False
        self.win_word1_is_found = False
        self.win_word2_is_found = False
        self.win_word3_is_found = False
        self.win_word4_is_found = False

        self.game_mode = ""
        self.mode_w = False
        self.mode_q = False
        self.game_over = False

        self.row1 = []
        self.row2 = []
        self.row3 = []
        self.row4 = []
        self.row5 = []
        self.row6 = []
        self.row7 = []

        self.row1_1 = []
        self.row1_2 = []
        self.row1_3 = []
        self.row1_4 = []

        self.row2_1 = []
        self.row2_2 = []
        self.row2_3 = []
        self.row2_4 = []

        self.row3_1 = []
        self.row3_2 = []
        self.row3_3 = []
        self.row3_4 = []

        self.row4_1 = []
        self.row4_2 = []
        self.row4_3 = []
        self.row4_4 = []

        self.row5_1 = []
        self.row5_2 = []
        self.row5_3 = []
        self.row5_4 = []

        self.row6_1 = []
        self.row6_2 = []
        self.row6_3 = []
        self.row6_4 = []

        self.row7_1 = []
        self.row7_2 = []
        self.row7_3 = []
        self.row7_4 = []

        self.row8_1 = []
        self.row8_2 = []
        self.row8_3 = []
        self.row8_4 = []

        self.row9_1 = []
        self.row9_2 = []
        self.row9_3 = []
        self.row9_4 = []

        self.row10_1 = []
        self.row10_2 = []
        self.row10_3 = []
        self.row10_4 = []

        self.row11_1 = []
        self.row11_2 = []
        self.row11_3 = []
        self.row11_4 = []

        self.keyboard = [self.ui.a, self.ui.b, self.ui.c, self.ui.d, self.ui.e, self.ui.f,
                         self.ui.g, self.ui.h, self.ui.i, self.ui.j, self.ui.k, self.ui.l,
                         self.ui.m, self.ui.n, self.ui.o, self.ui.p, self.ui.q, self.ui.r,
                         self.ui.s, self.ui.t, self.ui.u, self.ui.v, self.ui.w, self.ui.x, self.ui.y, self.ui.z]

        self.row_dict = {}
        self.rows_dict = {}
        self.counter = 1

    def open_page2(self):  # 4-lettered wordle page
        self.game_mode = "w_4letters"
        self.mode_w = True
        self.num_letters, self.chosen_word_list, self.num_rows = 4, self.word_list_4, 5
        self.win_word = random.choice(self.chosen_word_list)
        self.determine_row_dict(4)
        self.ui.stackedWidget.setCurrentIndex(1)

    def open_page3(self):  # 5-lettered wordle page
        self.game_mode = "w_5letters"
        self.mode_w = True
        self.num_letters, self.chosen_word_list, self.num_rows = 5, self.word_list_5, 6
        self.win_word = random.choice(self.chosen_word_list)
        self.determine_row_dict(5)
        self.ui.stackedWidget.setCurrentIndex(2)

    def open_page4(self):  # 6-lettered wordle page
        self.game_mode = "w_6letters"
        self.mode_w = True
        self.num_letters, self.chosen_word_list, self.num_rows = 6, self.word_list_6, 7
        self.win_word = random.choice(self.chosen_word_list)
        self.determine_row_dict(6)
        self.ui.stackedWidget.setCurrentIndex(3)

    def open_page5(self):  # 4-lettered quordle page
        self.game_mode = "q_4letters"
        self.mode_q = True
        self.num_letters, self.chosen_word_list, self.num_rows = 4, self.word_list_4, 7
        while len(set(self.win_words)) != 4:
            self.win_word1 = random.choice(self.chosen_word_list)
            self.win_word2 = random.choice(self.chosen_word_list)
            self.win_word3 = random.choice(self.chosen_word_list)
            self.win_word4 = random.choice(self.chosen_word_list)
            self.win_words = [self.win_word1, self.win_word2, self.win_word3, self.win_word4]

        self.determine_row_dict(4)
        self.ui.stackedWidget.setCurrentIndex(4)

    def open_page6(self):  # 5-lettered quordle page
        self.game_mode = "q_5letters"
        self.mode_q = True
        self.num_letters, self.chosen_word_list, self.num_rows = 5, self.word_list_5, 9
        self.win_words = []
        while len(set(self.win_words)) != 4:
            self.win_word1 = random.choice(self.chosen_word_list)
            self.win_word2 = random.choice(self.chosen_word_list)
            self.win_word3 = random.choice(self.chosen_word_list)
            self.win_word4 = random.choice(self.chosen_word_list)
            self.win_words = [self.win_word1, self.win_word2, self.win_word3, self.win_word4]

        self.determine_row_dict(5)
        self.ui.stackedWidget.setCurrentIndex(5)

    def open_page7(self):  # 6-lettered quordle page
        self.game_mode = "q_6letters"
        self.mode_q = True
        self.num_letters, self.chosen_word_list, self.num_rows = 6, self.word_list_6, 11
        while len(set(self.win_words)) != 4:
            self.win_word1 = random.choice(self.chosen_word_list)
            self.win_word2 = random.choice(self.chosen_word_list)
            self.win_word3 = random.choice(self.chosen_word_list)
            self.win_word4 = random.choice(self.chosen_word_list)
            self.win_words = [self.win_word1, self.win_word2, self.win_word3, self.win_word4]

        self.determine_row_dict(6)
        self.ui.stackedWidget.setCurrentIndex(6)

    def on_button_clicked(self, key, counter):  # MAIN ALGORITHM for receiving on-screen keyboard inputs
        if self.mode_w and not self.win_word_is_found and not self.game_over:
            current_row = self.row_dict[counter]
            if key != "enter":
                column_index = 0
                while column_index in range(self.num_letters):
                    button = current_row[column_index]
                    if button.text() == "" and key != "backspace":  # When a letter input  is received
                        button.setText(key)                # writes the letter in the first blank box on the current row
                        return
                    elif key == "backspace":  # Deletes the last occupied box of the row when backspace is pressed
                            n = 1
                            while current_row[column_index+n].text() != "":
                                if column_index == self.num_letters - 1:
                                    break
                                n += 1
                                if column_index + n > self.num_letters - 1:
                                    break
                            current_row[column_index+n-1].setText("")
                            return
                    column_index += 1

            elif key == "enter":
                for box in current_row:
                    if box.text() == "":
                        QMessageBox.information(self, "Warning!", "Fill the row")
                        return

                guess = ""
                for letter in current_row:
                    guess += letter.text()

                if guess == self.win_word:
                    self.win_word_is_found = True
                    for box in current_row:
                        box.setStyleSheet("background-color: rgb(0,200,0);"
                                          "border: 2px solid black;")
                    QMessageBox.information(self, "Congratulations!", f"You found the word: {self.win_word}")

                elif guess not in self.chosen_word_list:
                    QMessageBox.information(self, "Warning!", f"The word '{guess}' is not valid", )

                elif guess != self.win_word:  # For coloring the boxes to indicate box's situation for the winning word
                    for indx in range(self.num_letters):
                        box = current_row[indx]
                        if box.text() == self.win_word[indx]:
                            box.setStyleSheet("background-color: rgb(0,200,0);"
                                              "border: 2px solid black;")
                            key = self.key_finder(box.text())
                            key.setStyleSheet("background-color: rgb(0,200,0);"
                                              "border: 2px solid black;"
                                              "color: black")
                        elif box.text() != self.win_word[indx] and box.text() in self.win_word:
                            box.setStyleSheet("background-color: rgb(227, 182, 36);"
                                              "border: 2px solid black;")
                            key = self.key_finder(box.text())
                            key.setStyleSheet("background-color: rgb(227, 182, 36);"
                                              "border: 2px solid black;"
                                              "color: black")
                        else:
                            box.setStyleSheet("background-color: gray;"
                                              "border: 2px solid black")
                            key = self.key_finder(box.text())
                            key.setStyleSheet("background-color: gray;"
                                              "border: 2px solid black;"
                                              "color: black")

                    self.counter += 1
                    if self.counter > self.num_rows:
                        self.game_over = True
                        QMessageBox.information(self, "GAME OVER", f"The correct word is {self.win_word}")

        if self.mode_q and not self.game_over and (not self.win_word1_is_found or not self.win_word1_is_found
                                                   or not self.win_word1_is_found or not self.win_word1_is_found):
            current_row_of_1 = self.rows_dict[counter][0]
            current_row_of_2 = self.rows_dict[counter][1]
            current_row_of_3 = self.rows_dict[counter][2]
            current_row_of_4 = self.rows_dict[counter][3]
            if key != "enter":
                column_index = 0
                while column_index in range(self.num_letters):
                    button1 = current_row_of_1[column_index]
                    button2 = current_row_of_2[column_index]
                    button3 = current_row_of_3[column_index]
                    button4 = current_row_of_4[column_index]
                    buttons = [button1, button2, button3, button4]  # current boxes of each guess block

                    if self.win_word1_is_found:  # for avoiding more guesses on the block whose word is found
                        buttons.remove(button1)
                    if self.win_word2_is_found:
                        buttons.remove(button2)
                    if self.win_word3_is_found:
                        buttons.remove(button3)
                    if self.win_word4_is_found:
                        buttons.remove(button4)

                    for b in buttons:
                        if b.text() == "" and key != "backspace":
                            if not self.win_word1_is_found:
                                button1.setText(key)
                            if not self.win_word2_is_found:
                                button2.setText(key)
                            if not self.win_word3_is_found:
                                button3.setText(key)
                            if not self.win_word4_is_found:
                                button4.setText(key)
                            return
                    if key == "backspace":
                        n = 1
                        current_rows = [current_row_of_1, current_row_of_2, current_row_of_3, current_row_of_4]
                        for row in current_rows:
                            if not self.win_word1_is_found:
                                current_row = row
                                break
                            if not self.win_word2_is_found:
                                current_row = row
                                break
                            if not self.win_word3_is_found:
                                current_row = row
                                break
                            if not self.win_word4_is_found:
                                current_row = row
                                break

                        while current_row[column_index + n].text() != "":
                            if column_index == self.num_letters - 1:
                                break
                            n += 1
                            if column_index + n > self.num_letters - 1:
                                break
                        current_row_of_1[column_index + n - 1].setText("")
                        current_row_of_2[column_index + n - 1].setText("")
                        current_row_of_3[column_index + n - 1].setText("")
                        current_row_of_4[column_index + n - 1].setText("")
                        return
                    column_index += 1

            elif key == "enter":
                if not self.win_word1_is_found:
                    for box in current_row_of_1:
                        if box.text() == "":
                            QMessageBox.information(self, "Warning!", "Fill the row(s)")
                            return

                    guess = ""
                    for letter in current_row_of_1:
                        guess += letter.text()

                    if guess == self.win_word1:
                        for box in current_row_of_1:
                                box.setStyleSheet('background-color: rgb(0, 200, 0);'
                                                  'border: 2px solid black;')
                        self.win_word1_is_found = True

                if not self.win_word2_is_found:
                    for box in current_row_of_2:
                        if box.text() == "":
                            QMessageBox.information(self, "Warning!", "Fill the row(s)")
                            return
                    guess = ""
                    for letter in current_row_of_2:
                        guess += letter.text()
                    if guess == self.win_word2:
                        for box in current_row_of_2:
                            box.setStyleSheet('background-color: rgb(0, 200, 0);'
                                              'border: 2px solid black;')
                        self.win_word2_is_found = True

                if not self.win_word3_is_found:
                    for box in current_row_of_3:
                        if box.text() == "":
                            QMessageBox.information(self, "Warning!", "Fill the row(s)")
                            return
                    guess = ""
                    for letter in current_row_of_3:
                        guess += letter.text()
                    if guess == self.win_word3:
                        for box in current_row_of_3:
                            box.setStyleSheet('background-color: rgb(0, 200, 0);'
                                              'border: 2px solid black;')
                        self.win_word3_is_found = True

                if not self.win_word4_is_found:
                    for box in current_row_of_4:
                        if box.text() == "":
                            QMessageBox.information(self, "Warning!", "Fill the row(s)")
                            return
                    guess = ""
                    for letter in current_row_of_4:
                        guess += letter.text()
                    if guess == self.win_word4:
                        for box in current_row_of_4:
                            box.setStyleSheet('background-color: rgb(0, 200, 0);'
                                              'border: 2px solid black;')
                        self.win_word4_is_found = True

                if self.win_word1_is_found and self.win_word2_is_found and self.win_word3_is_found and self.win_word4_is_found:
                    QMessageBox.information(self, "Congratulations!", f"You found the words: {self.win_word1}, "
                                                                      f"{self.win_word2}, {self.win_word3}, "
                                                                      f" {self.win_word4}")

                elif guess not in self.chosen_word_list:
                    QMessageBox.information(self, "Warning!", f"The word '{guess}' is not valid")
                    return

                constant = 0
                for word in self.win_words:
                    if guess == word:
                        constant += 1

                if constant != 4:
                    for indx in range(self.num_letters):
                        box_of_1 = current_row_of_1[indx]
                        box_of_2 = current_row_of_2[indx]
                        box_of_3 = current_row_of_3[indx]
                        box_of_4 = current_row_of_4[indx]
                        boxes = [box_of_1, box_of_2, box_of_3, box_of_4]
                        if self.win_word1_is_found:  # for avoiding coloring the completed block's boxes
                            boxes.remove(box_of_1)
                            if self.win_word1 in self.win_words:
                                self.win_words.remove(self.win_word1)

                        if self.win_word2_is_found:
                            boxes.remove(box_of_2)
                            if self.win_word2 in self.win_words:
                                self.win_words.remove(self.win_word2)

                        if self.win_word3_is_found:
                            boxes.remove(box_of_3)
                            if self.win_word3 in self.win_words:
                                self.win_words.remove(self.win_word3)

                        if self.win_word4_is_found:
                            boxes.remove(box_of_4)
                            if self.win_word4 in self.win_words:
                                self.win_words.remove(self.win_word4)
                        n = 0
                        for box in boxes:
                            if box.text() == self.win_words[n][indx]:
                                box.setStyleSheet('background-color: rgb(0, 200, 0);'
                                                  'border: 2px solid black;')
                                key = self.key_finder(box.text())
                                key_style = key.styleSheet()
                                if box == box_of_1:
                                    key_style += " border-top: 7px solid rgb(0, 200, 0);"
                                elif box == box_of_2:
                                    key_style += " border-right: 12px solid rgb(0, 200, 0);"
                                elif box == box_of_3:
                                    key_style += " border-left: 12px solid rgb(0, 200, 0);"
                                elif box == box_of_4:
                                    key_style += " border-bottom: 7px solid rgb(0, 200, 0);"
                                key.setStyleSheet(key_style)

                            elif box.text() != self.win_words[n][indx] and box.text() in self.win_words[n]:
                                box.setStyleSheet('background-color: rgb(227, 182, 36);'
                                                  'border: 2px solid black;')
                                key = self.key_finder(box.text())
                                key_style = key.styleSheet()
                                if box == box_of_1:
                                    key_style += " border-top: 7px solid rgb(227, 182, 36);"
                                elif box == box_of_2:
                                    key_style += " border-right: 12px solid rgb(227, 182, 36);"
                                elif box == box_of_3:
                                    key_style += " border-left: 12px solid rgb(227, 182, 36);"
                                elif box == box_of_4:
                                    key_style += " border-bottom: 7px solid rgb(227, 182, 36);"
                                key.setStyleSheet(key_style)

                            else:
                                box.setStyleSheet('background-color: gray;'
                                                  'border: 2px solid black;')

                                key = self.key_finder(box.text())
                                key_style = key.styleSheet()
                                if box == box_of_1:
                                    key_style += " border-top: 7px solid gray;"
                                elif box == box_of_2:
                                    key_style += " border-right: 12px solid gray;"
                                elif box == box_of_3:
                                    key_style += " border-left: 12px solid gray;"
                                elif box == box_of_4:
                                    key_style += " border-bottom: 7px solid gray;"
                                key.setStyleSheet(key_style)

                            n += 1
                            if n > 3:
                                break

                    self.counter += 1
                    if self.counter > self.num_rows:
                        self.game_over = True
                        QMessageBox.information(self, "GAME OVER", f"The correct words are  {self.win_word1}, "
                                                                   f"{self.win_word3}, {self.win_word2}, "
                                                                   f"{self.win_word4}")

    def clean_buttons(self):  # for cleaning all the buttons on the game page
        if self.mode_w:
            for k, v in self.row_dict.items():
                for box in v:
                    box.setText("")
                    box.setStyleSheet("background-color: lightgray;"
                                      "border: 2px solid black;")
            for key in self.keyboard:
                key.setStyleSheet("background-color: black;"
                                  "color: white;"
                                  "border: 2px solid white;")
            self.counter = 1
        elif self.mode_q:
            for k, v in self.rows_dict.items():
                for row in v:
                    for box in row:
                        box.setText("")
                        box.setStyleSheet("background-color: lightgray;"
                                          "border: 2px solid black;")
            for key in self.keyboard:
                key.setStyleSheet("background-color: black;"
                                  "color: white;"
                                  "border: 2px solid white;")

    def refresh(self):  # refreshing the current page
        self.win_word_is_found = False
        self.win_word1_is_found = False
        self.win_word2_is_found = False
        self.win_word3_is_found = False
        self.win_word4_is_found = False
        self.game_over = False
        self.clean_buttons()
        self.counter = 1
        if self.game_mode == "w_4letters":
            self.open_page2()
        elif self.game_mode == "w_5letters":
            self.open_page3()
        elif self.game_mode == "w_6letters":
            self.open_page4()
        elif self.game_mode == "q_4letters":
            self.open_page5()
        elif self.game_mode == "q_5letters":
            self.open_page6()
        elif self.game_mode == "q_6letters":
            self.open_page7()

    def texter(self):  # Receives the click signal from on-screen keyboard
        self.ui.enter.clicked.connect(lambda: self.on_button_clicked("enter", self.counter))
        self.ui.backspace.clicked.connect(lambda: self.on_button_clicked("backspace", self.counter))
        self.ui.a.clicked.connect(lambda: self.on_button_clicked("A", self.counter))
        self.ui.b.clicked.connect(lambda: self.on_button_clicked("B", self.counter))
        self.ui.c.clicked.connect(lambda: self.on_button_clicked("C", self.counter))
        self.ui.d.clicked.connect(lambda: self.on_button_clicked("D", self.counter))
        self.ui.e.clicked.connect(lambda: self.on_button_clicked("E", self.counter))
        self.ui.f.clicked.connect(lambda: self.on_button_clicked("F", self.counter))
        self.ui.g.clicked.connect(lambda: self.on_button_clicked("G", self.counter))
        self.ui.h.clicked.connect(lambda: self.on_button_clicked("H", self.counter))
        self.ui.i.clicked.connect(lambda: self.on_button_clicked("I", self.counter))
        self.ui.j.clicked.connect(lambda: self.on_button_clicked("J", self.counter))
        self.ui.k.clicked.connect(lambda: self.on_button_clicked("K", self.counter))
        self.ui.l.clicked.connect(lambda: self.on_button_clicked("L", self.counter))
        self.ui.m.clicked.connect(lambda: self.on_button_clicked("M", self.counter))
        self.ui.n.clicked.connect(lambda: self.on_button_clicked("N", self.counter))
        self.ui.o.clicked.connect(lambda: self.on_button_clicked("O", self.counter))
        self.ui.p.clicked.connect(lambda: self.on_button_clicked("P", self.counter))
        self.ui.q.clicked.connect(lambda: self.on_button_clicked("Q", self.counter))
        self.ui.r.clicked.connect(lambda: self.on_button_clicked("R", self.counter))
        self.ui.s.clicked.connect(lambda: self.on_button_clicked("S", self.counter))
        self.ui.t.clicked.connect(lambda: self.on_button_clicked("T", self.counter))
        self.ui.u.clicked.connect(lambda: self.on_button_clicked("U", self.counter))
        self.ui.v.clicked.connect(lambda: self.on_button_clicked("V", self.counter))
        self.ui.w.clicked.connect(lambda: self.on_button_clicked("W", self.counter))
        self.ui.x.clicked.connect(lambda: self.on_button_clicked("X", self.counter))
        self.ui.y.clicked.connect(lambda: self.on_button_clicked("Y", self.counter))
        self.ui.z.clicked.connect(lambda: self.on_button_clicked("Z", self.counter))

    def key_finder(self, letter):  # for finding the colored box's key on on-screen keyboard
        for key in self.keyboard:
            if key.text() == letter:
                return key


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MyMainWindow()
    mainWindow.show()
    sys.exit(app.exec_())

