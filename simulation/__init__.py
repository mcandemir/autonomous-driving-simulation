from FrontCam import FrontCam
from LeftCam import LeftCam
from RightCam import RightCam
import cv2
import numpy as np
from PIL import ImageGrab
from SetScreen import set_pos
from CarController import CarController


class Simulation:
    def __init__(self, mode):
        self.mode = mode
        self.cam_pos1 = None
        self.cam_pos2 = None
        self.LeftCam = LeftCam()
        self.RightCam = RightCam()
        self.FrontCam = FrontCam()
        self.carcontroller = CarController()
        self.set_view()

    def set_view(self):
        if self.mode == 'side':
            self.cam_pos1 = set_pos()
            self.cam_pos2 = set_pos()

    def run(self):
        while True:
            if self.mode == 'side':
                cam_img1 = ImageGrab.grab(self.cam_pos1)
                cam_img2 = ImageGrab.grab(self.cam_pos2)

                cam_img1 = cv2.cvtColor(np.array(cam_img1), cv2.COLOR_RGB2BGR)
                cam_img2 = cv2.cvtColor(np.array(cam_img2), cv2.COLOR_RGB2BGR)

                cam_img1 = self.LeftCam.process(cam_img1)
                cam_img2 = self.RightCam.process(cam_img2)

                # todo: completed controller 10/8
                m1 = self.LeftCam.m
                m2 = self.RightCam.m
                avg_y1 = self.LeftCam.avg_y
                true_y1 = self.LeftCam.true_y
                avg_y2 = self.RightCam.avg_y
                true_y2 = self.RightCam.true_y

                self.controller(m1, m2, avg_y1, true_y1, avg_y2, true_y2)

                cv2.imshow('left', cam_img1)
                cv2.imshow('right', cam_img2)
                q = cv2.waitKey(1)

                if q == 27:
                    cv2.destroyAllWindows()
                    return

    # todo: optimize controller
    def controller(self, m1, m2, avg_y1, true_y1, avg_y2, true_y2):
        # : None None
        self.carcontroller.go()
        if m1 is None and m2 is None:
            self.carcontroller.go_straight()
        # : v None
        elif m2 is None and m1 is not None:
            if m1 < -0.005:
                self.carcontroller.go_left()
            elif m1 > 0.005:
                self.carcontroller.go_right()
            elif -0.005 < m1 < 0.005:
                self.carcontroller.go_straight()
        # : None v
        elif m1 is None and m2 is not None:
            if m2 < -0.005:
                self.carcontroller.go_left()
            elif m2 > 0.005:
                self.carcontroller.go_right()
            elif -0.005 < m2 < 0.005:
                self.carcontroller.go_straight()
        # : v v
        elif m1 is not None and m2 is not None:
            if m1 < -0.005 and m2 < -0.005:
                self.carcontroller.go_left()
            elif m1 > 0.005 and m2 > 0.005:
                self.carcontroller.go_right()
            elif -0.005 < m1 < 0.005 and -0.005 < m2 < 0.005:
                self.carcontroller.go_straight()
                # todo: implement self.carcontroller.center()




























    # def controller(self, m1, m2, avg_y1, true_y1, avg_y2, true_y2):
    #     # : None None
    #     self.keyboard.press('w')
    #     if m1 is None and m2 is None:
    #         self.keyboard.release('d')
    #         self.keyboard.release('a')
    #     # : v None
    #     elif m2 is None and m1 is not None:
    #         if m1 < -0.005:
    #             self.keyboard.release('d')
    #             self.keyboard.press('a')
    #         elif m1 > 0.005:
    #             self.keyboard.release('a')
    #             self.keyboard.press('d')
    #     # : None v
    #     elif m1 is None and m2 is not None:
    #         if m2 < -0.005:
    #             self.keyboard.release('d')
    #             self.keyboard.press('a')
    #         elif m2 > 0.005:
    #             self.keyboard.release('a')
    #             self.keyboard.press('d')
    #     # : v v
    #     elif m1 is not None and m2 is not None:
    #         if m1 < -0.005 or m2 < -0.005:
    #             self.keyboard.release('d')
    #             self.keyboard.press('a')
    #         elif m1 > 0.005 or m2 > 0.005:
    #             self.keyboard.release('a')
    #             self.keyboard.press('d')


sim = Simulation(mode='side')
sim.run()
