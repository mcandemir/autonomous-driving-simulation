import cv2
import numpy as np


class LeftCam:
    def __init__(self):
        self.h = None
        self.w = None
        self.m = None
        self.avg_y = None
        self.true_y = None

    def process(self, img):
        # image processing
        greyscaled = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        ret, threshold = cv2.threshold(greyscaled, 235, 255, cv2.THRESH_BINARY)
        lines = cv2.HoughLinesP(threshold, 1, np.pi / 180, 50, np.array([]), minLineLength=100, maxLineGap=5)
        lines_avg = self.average_lines(lines)
        avg_line_drawed = self.draw_lines(img, lines_avg)
        avg_true_line_drawed = self.true_line(avg_line_drawed)

        # attributes
        self.m = self.get_m(lines_avg)
        self.avg_y, self.true_y = self.get_y(lines_avg)

        # command prompt output
        self.info(self.avg_y, self.true_y)

        return avg_true_line_drawed

    def draw_lines(self, img, lines):
        # mask = np.zeros_like(img)
        if lines is not None:
            for x1, y1, x2, y2 in lines:
                cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 2)
            # combined = cv2.addWeighted(img, 0.8, mask, 1, 1)
            return img
        return img

    def average_lines(self, lines):
        if lines is not None:
            line_fit = []
            for line in lines:
                x1, y1, x2, y2 = line.reshape(4)
                line_fit.append((np.array((x1, y1, x2, y2))))
            line_fit = np.average(line_fit, axis=0)
            line_fit = [int(i) for i in line_fit]
            return np.array([line_fit])

    def true_line(self, img):
        self.h = img.shape[0]
        self.w = img.shape[1]
        cv2.line(img, (0, int(self.h / 2)), (self.w, int(self.h / 2)), color=(0, 255, 0), thickness=2)
        return img

    def get_m(self, line):
        if line is not None:
            return (line[0][3] - line[0][1]) / (line[0][2] - line[0][0])

    def get_y(self, line):
        if line is not None:
            avg_y = int((line[0][1] + line[0][3]) / 2)
            true_y = int(self.h / 2)
            return avg_y, true_y
        return None, None

    def info(self, *args):
        print('============LEFT CAM===============')
        for i in args:
            print(i)

