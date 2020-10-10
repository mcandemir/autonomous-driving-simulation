from pynput.keyboard import Controller


class CarController:
    def __init__(self):
        self.keyboard = Controller()
        self.turning_left = None
        self.turning_right = None
        self.centering = None

    def steer_left(self):
        self.keyboard.release('d')
        self.keyboard.press('a')

    def steer_right(self):
        self.keyboard.release('a')
        self.keyboard.press('d')

    def go_left(self, avg_y1, true_y1, m1):
        if avg_y1 < true_y1:
            self.keyboard.press('a')
            print('turning left')
        else:
            self.keyboard.release('a')
        if m1 == 0.0:
            self.keyboard.release('a')

    def go_right(self, avg_y2, true_y2, m2):
        if avg_y2 < true_y2:
            self.keyboard.press('d')
            print('turning right')
        else:
            self.keyboard.release('d')
        if m2 == 0.0:
            self.keyboard.release('d')

    def go_straight(self):
        self.keyboard.release('a')
        self.keyboard.release('d')

    def start(self):
        self.keyboard.release('s')
        self.keyboard.press('w')

    def stop(self):
        self.keyboard.release('w')

    def center(self, avg_y1, avg_y2):
        if avg_y1 > avg_y2:
            self.keyboard.press('a')
            self.keyboard.release('a')
        elif avg_y2 > avg_y1:
            self.keyboard.press('d')
            self.keyboard.release('d')
