from pynput.keyboard import Controller


class CarController:
    def __init__(self):
        self.keyboard = Controller()
        self.turning_left = None
        self.turning_right = None

    def go_left(self):
        self.keyboard.release('d')
        self.keyboard.press('a')

    def go_right(self):
        self.keyboard.release('a')
        self.keyboard.press('d')

    def go_straight(self):
        self.keyboard.release('a')
        self.keyboard.release('d')

    def go(self):
        self.keyboard.release('s')
        self.keyboard.press('w')

    def stop(self):
        self.keyboard.release('w')

    def center(self, m1, m2, avg_y, true_y):
        # todo
        pass
