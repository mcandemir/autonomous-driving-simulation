from pynput.keyboard import Controller
import time


class CarController:
    def __init__(self):
        self.keyboard = Controller()
        self.moving = None

    def go_left(self, avg_y1, true_y1):
        self.moving = True
        self.keyboard.press('w')
        if true_y1 - 5 <= avg_y1 <= true_y1 + 5:
            self.keyboard.release('a')
            self.keyboard.release('d')
            print('going forward')
        elif avg_y1 < true_y1:
            self.keyboard.release('d')
            self.keyboard.press('a')
            print('steering left')
        elif avg_y1 > true_y1:
            self.keyboard.release('a')
            self.keyboard.press('d')
            print('steering right')

    def go_right(self, avg_y2, true_y2):
        self.moving = True
        self.keyboard.press('w')
        if true_y2 - 5 <= avg_y2 <= true_y2 + 5:
            self.keyboard.release('a')
            self.keyboard.release('d')
            print('going forward')
        elif avg_y2 < true_y2:
            self.keyboard.release('a')
            self.keyboard.press('d')
            print('steering right')
        elif avg_y2 > true_y2:
            self.keyboard.release('d')
            self.keyboard.press('a')
            print('steering left')

    def go_straight(self):
        self.moving = True
        self.keyboard.press('w')
        self.keyboard.release('a')
        self.keyboard.release('d')
        print('going forward')

    def stop(self):
        self.moving = False
        self.keyboard.release('a')
        self.keyboard.release('d')
        self.keyboard.release('w')
        self.keyboard.press('s')
        print('stopping')
        time.sleep(0.60)
        print('stopped')
        self.keyboard.release('s')
