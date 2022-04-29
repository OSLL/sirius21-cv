from gym_duckietown.tasks.task_solution import TaskSolution
import numpy as np
import cv2


class DontCrushDuckieTaskSolution(TaskSolution):
    def __init__(self, generated_task):
        super().__init__(generated_task)

    def solve(self):
        env = self.generated_task['env']
        # getting the initial picture
        img, _, _, _ = env.step([0, 0])

        condition = True
        while condition:
            img, reward, done, info = env.step([1, 0])
            # img in RGB
            # add here some image processing
            hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            yellow_lower = np.array([20, 100, 100])
            yellow_upper = np.array([30, 255, 255])
            mask_yellow = cv2.inRange(hsv, yellow_lower, yellow_upper)
            yellow_ratio = (cv2.countNonZero(mask_yellow)) / (img.size / 3)
            res = np.round(yellow_ratio * 100, 2)
            if res > 17.59:
                condition = False
            env.render()

