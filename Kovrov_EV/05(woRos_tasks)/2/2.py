from gym_duckietown.tasks.task_solution import TaskSolution


class Ride1MTaskSolution(TaskSolution):
    def __init__(self, generated_task):
        super().__init__(generated_task)

    def solve(self):
        env = self.generated_task['env']
        x_start, y, z = env.cur_pos
        x = x_start

        while x - x_start < 1:
            env.step([0.5, 0])
            x, y, z = env.cur_pos

            print(x)
