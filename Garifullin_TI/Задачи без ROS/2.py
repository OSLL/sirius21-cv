from gym_duckietown.tasks.task_solution import TaskSolution


class Ride1MTaskSolution(TaskSolution):
    def __init__(self, generated_task):
        super().__init__(generated_task)

    def solve(self):
        env = self.generated_task['env']
        start = env.cur_pos[0]
        while env.cur_pos[0] - start < 1: env.step([0.5, 0])