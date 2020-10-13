from SideCam import SideCam
import cv2
import numpy as np
from PIL import ImageGrab
from SetScreen import set_pos
from pynput.keyboard import Controller


class Simulation:
    def __init__(self, mode):
        self.mode = mode
        self.cam_pos1 = None
        self.cam_pos2 = None
        self.LeftCam = SideCam('left')
        self.RightCam = SideCam('right')
        self.keyboard = Controller()
        self.set_view()

    def set_view(self):
        """
        sets the screen to monitor
        """
        if self.mode == 'side':
            self.cam_pos1 = set_pos()
            self.cam_pos2 = set_pos()

    def run(self):
        while True:
            if self.mode == 'side':
                """take screenshots"""
                cam_img1 = ImageGrab.grab(self.cam_pos1)
                cam_img2 = ImageGrab.grab(self.cam_pos2)

                """convert into numpy form"""
                cam_img1 = cv2.cvtColor(np.array(cam_img1), cv2.COLOR_RGB2BGR)
                cam_img2 = cv2.cvtColor(np.array(cam_img2), cv2.COLOR_RGB2BGR)

                """do required processings"""
                cam_img1 = self.LeftCam.process(cam_img1)
                cam_img2 = self.RightCam.process(cam_img2)

                """avg_y: average height of line, true_y: height of true line"""
                self.controller()

                """monitoring processing"""
                cv2.imshow('left', cam_img1)
                cv2.imshow('right', cam_img2)
                q = cv2.waitKey(1)

                if q == 27:
                    cv2.destroyAllWindows()
                    return

    # todo: optimize controller
    def controller(self):
        self.keyboard.press('w')

        """avg_y: average height of line, true_y: height of true line"""
        avg_y1 = self.LeftCam.avg_y
        true_y1 = self.LeftCam.true_y
        avg_y2 = self.RightCam.avg_y
        true_y2 = self.RightCam.true_y

        # if left is open
        if avg_y1:
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

        # if right is open
        elif avg_y2:
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

        # if lost
        else:
            self.keyboard.release('w')
            self.keyboard.release('a')
            self.keyboard.release('d')


sim = Simulation(mode='side')
sim.run()
