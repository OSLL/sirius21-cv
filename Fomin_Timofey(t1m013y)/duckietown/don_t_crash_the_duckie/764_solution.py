# 764
from gym_duckietown.tasks.task_solution import TaskSolution
import cv2 as cv
import numpy
cv2 = cv
np = numpy


class DontCrushDuckieTaskSolution(TaskSolution):
    def __init__(self, generated_task):
        super().__init__(generated_task)

    def solve(self):
        env = self.generated_task['env']

        yellow_range_lower, yellow_range_upper = (20, 100, 100), (30, 255, 255)
        yellow_percentage_max = 7.5

        done = False
        moving = True
        while not done:
            if moving:
                img, reward, done, info = env.step([1, 0])
            else:
                img, reward, done, info = env.step([0, 0])
                break

            img_hsv = cv.cvtColor(img, cv.COLOR_RGB2HSV)
            mask_yellow = cv.inRange(img_hsv, yellow_range_lower, yellow_range_upper)
            yellow_nonZero_pixels = cv.countNonZero(mask_yellow)
            yellow_nonZero = yellow_nonZero_pixels / mask_yellow.size
            yellow_percentage = numpy.round(yellow_nonZero * 100, 2)
            moving = yellow_percentage < yellow_percentage_max

            print(f"""yellow_nonZero_pixels: {yellow_nonZero_pixels};
yellow_nonZero: {yellow_nonZero};
yellow_percentage: {yellow_percentage};
yellow_percentage_max: {yellow_percentage_max};
moving: {moving}
-----""")

            env.render()
