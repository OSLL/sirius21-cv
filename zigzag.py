from gym_duckietown.tasks.task_solution import TaskSolution
import numpy as np
import cv2 as cv


def calc_col(img, low, up):
    img = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    mask_col = cv.inRange(img, low, up)

    col_ratio = (cv.countNonZero(mask_col) / (img.size / 3))
    res = np.round(col_ratio * 100, 2)

    return res


white_lower = np.array([0, 0, 150])
white_upper = np.array([255, 10, 255])

yellow_lower = np.array([20, 100, 100])
yellow_upper = np.array([30, 255, 255])


class DontCrushDuckieTaskSolution(TaskSolution):
    def __init__(self, generated_task):
        super().__init__(generated_task)

    def solve(self):
        env = self.generated_task['env']

        img, _, _, _ = env.step([0, 0])

        condition_straight = True

        while condition_straight:
            img, reward, done, info = env.step([0.5, 1])

            rat = calc_col(img, yellow_lower, yellow_upper)

            if rat <= 1.0:
                condition_straight = False
                img, _, _, _ = env.step([0, 0])

            env.render()
