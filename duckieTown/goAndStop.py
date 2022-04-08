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
            if(...)
                condition = False
                img, _, _, _ = env.step([0, 0]) #stop
            env.render()

    class Detector:
        def loadImage(self):
            pass

        def analyze(self):
            pass




