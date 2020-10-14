from SideCam import SideCam
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
        self.LeftCam = SideCam('left')
        self.RightCam = SideCam('right')
        self.carcontroller = CarController()
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
        """avg_y: average height of line, true_y: height of true line"""
        avg_y1 = self.LeftCam.avg_y
        true_y1 = self.LeftCam.true_y
        avg_y2 = self.RightCam.avg_y
        true_y2 = self.RightCam.true_y

        # if left is open
        if avg_y1:
            self.carcontroller.go_left(avg_y1, true_y1)

        # if right is open
        elif avg_y2:
            self.carcontroller.go_right(avg_y2, true_y2)

        # if lost
        else:
            if self.carcontroller.moving:
                self.carcontroller.stop()


sim = Simulation(mode='side')
sim.run()
