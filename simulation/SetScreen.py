import pyautogui
import win32api
import time


def click_coordinates():
    """
        If the key state changes, get the positions
        """
    for pos in range(2):
        state_prev = win32api.GetKeyState(0x01)
        while True:
            state_current = win32api.GetKeyState(0x01)
            if state_current != state_prev:
                pos = pyautogui.position()
                print("**Positions set: ", pos)
                return pos


def set_pos():
    print('\n*Select first corner of the front cam')
    mouse_posX1, mouse_posY1 = click_coordinates()
    time.sleep(0.8)
    print('\n*Select second corner of the front cam')
    mouse_posX2, mouse_posY2 = click_coordinates()
    time.sleep(0.8)
    cam_pos = (mouse_posX1, mouse_posY1, mouse_posX2, mouse_posY2)

    return cam_pos



# def set_cameras(mode):
#     if mode == 'side':
#         print('\n*Select first corner of the left cam')
#         left_mouse_posX1, left_mouse_posY1 = click_coordinates()
#         time.sleep(0.8)
#         print('\n*Select second corner of the left cam')
#         left_mouse_posX2, left_mouse_posY2 = click_coordinates()
#         time.sleep(0.8)
#         left_cam_pos = (left_mouse_posX1, left_mouse_posY1, left_mouse_posX2, left_mouse_posY2)
#
#         print('\n*Select first corner of the right cam')
#         right_mouse_posX1, right_mouse_posY1 = click_coordinates()
#         time.sleep(0.8)
#         print('\n*Select second corner of the right cam')
#         right_mouse_posX2, right_mouse_posY2 = click_coordinates()
#         time.sleep(0.8)
#         right_cam_pos = (right_mouse_posX1, right_mouse_posY1, right_mouse_posX2, right_mouse_posY2)
#
#         return left_cam_pos, right_cam_pos
#
#     elif mode == 'front':
#         print('\n*Select first corner of the front cam')
#         front_mouse_posX1, front_mouse_posY1 = click_coordinates()
#         time.sleep(0.8)
#         print('\n*Select second corner of the front cam')
#         front_mouse_posX2, front_mouse_posY2 = click_coordinates()
#         time.sleep(0.8)
#         front_cam_pos = (front_mouse_posX1, front_mouse_posY1, front_mouse_posX2, front_mouse_posY2)
#
#         return front_cam_pos