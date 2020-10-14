import cv2
import numpy as np
import json
from PIL import Image


class FrontCam:
    def __init__(self):
        """
        load the signs at the start
        """
        self.signs = None
        self.command = None
        with open('signs_path.json', 'r') as f:
            self.signs = json.load(f)

        for sign, path in self.signs.items():
            self.signs[sign] = cv2.imread(path)

    def process(self, img):
        """
        finds the matched sign
        """
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # for every known sign check if any exist
        for sign, sign_img in self.signs.items():

            # convert to gray
            sign_img = cv2.cvtColor(sign_img, cv2.COLOR_BGR2GRAY)

            # match templates
            res = cv2.matchTemplate(img_gray, sign_img, cv2.TM_CCOEFF_NORMED)

            # check if template (sign) matched
            threshold = 0.8
            flag = False
            if np.amax(res) > threshold:
                flag = True

            # save which sign is matched
            if flag:
                self.detected = sign
                print(f'template found: {sign}')

                # find the location
                w, h = sign_img.shape[:: -1]
                loc = np.where(res >= threshold)
                for pt in zip(*loc[:: -1]):
                    cropped_sign = img[pt[1]: pt[1] + int(h/2), pt[0]: pt[0] + int(w/2)]

                # if it is a traffic light
                if sign == "traffic_light":
                    # apply color detection
                    color = self.color_detection(cropped_sign)

                    if color == "red":
                        self.command = "stop"
                    elif color == "green":
                        self.command = "go"
                    elif color == "yellow":
                        self.command = "go"

            return img

    def color_detection(self, img):
        """if a traffic light detected"""

        # red
        low_red = np.array([0, 0, 160])
        high_red = np.array([130, 130, 255])
        red_threshold = cv2.inRange(img, low_red, high_red)

        # green
        low_green = np.array([0, 120, 0])
        high_green = np.array([90, 255, 90])
        green_threshold = cv2.inRange(img, low_green, high_green)

        # yellow
        low_yellow = np.array([0, 140, 140])
        high_yellow = np.array([150, 255, 255])
        yellow_threshold = cv2.inRange(img, low_yellow, high_yellow)

        count = np.sum(np.nonzero(red_threshold))
        if count == 0:
            print("Not red")
        else:
            print("red")
            return "red"

        count = np.sum(np.nonzero(green_threshold))
        if count == 0:
            print("Not green")
        else:
            print("green")
            return "green"

        count = np.sum(np.nonzero(yellow_threshold))
        if count == 0:
            print("Not yellow")
        else:
            print("yellow")
            return "yellow"





