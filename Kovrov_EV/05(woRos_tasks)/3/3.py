from gym_duckietown.tasks.task_solution import TaskSolution


class LaneCenterTaskSolution(TaskSolution):
    def __init__(self, generated_task):
        super().__init__(generated_task)

    def solve(self):
        env = self.generated_task['env']
        x, y, z = env.cur_pos
        ang = env.cur_angle

        while ang > 0:
            env.step([0, -1])

            ang = env.cur_angle
            print(ang)
