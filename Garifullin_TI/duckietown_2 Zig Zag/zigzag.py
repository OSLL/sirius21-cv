import cv2
import numpy as np
from gym_duckietown.tasks.task_solution import TaskSolution


class DontCrushDuckieTaskSolution(TaskSolution):
    def __init__(self, generated_task):
        super().__init__(generated_task)

    def solve(self):
        env = self.generated_task['env']
        # getting the initial picture
        img, _, _, _ = env.step([0, 0])

        condition = True
        direction = 1
        count = 0
        while condition:
            img, reward, done, info = env.step([0.5, direction])
            lines = findWhiteLine(img)
            count += 1
            if lines is not None and count > 10:
                count = 0
                if not checkLine(lines, 2):
                    direction = -1
                if not checkLine(lines, 1):
                    direction = 1

            # hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            # yellow_lower = np.array([20, 100, 100])
            # yellow_upper = np.array([30, 255, 255])
            # mask_yellow = cv2.inRange(hsv, yellow_lower, yellow_upper)
            # yellow_ratio = (cv2.countNonZero(mask_yellow)) / (img.size / 3)
            # res = np.round(yellow_ratio * 100, 2)

            # if res > 17.59:
            #     condition = False
            env.render()


def checkLine(lines, control_theta):
    for line in lines:
        theta = line[0][1]
        if np.abs(theta - control_theta) < 0.5:
            return True
    return False


def findWhiteLine(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    white_lower = np.array([0, 0, 150])
    white_upper = np.array([255, 10, 255])
    mask = cv2.inRange(hsv, white_lower, white_upper)
    edges = cv2.Canny(mask, 50, 150)
    rho_accuracy = 1
    theta_accuracy = np.pi / 180
    min_length = 70
    lines = cv2.HoughLines(edges, rho_accuracy, theta_accuracy, min_length)
    return lines
