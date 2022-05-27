from gym_duckietown.tasks.task_solution import TaskSolution
import math


class RoundtripTaskSolution(TaskSolution):
    def __init__(self, generated_task):
        super().__init__(generated_task)

    def solve(self):
        env = self.generated_task['env']
        sx, sy, sz = env.cur_pos
        gx, gy, gz = self.generated_task['target_coordinates'][0]
        print("Starting!!!!")
        print(sx, sy, sz)
        print(gx, gy, gz)
        print(env.cur_angle)

        cos = (sx * gx + sz * gz) / (math.sqrt(sx * sx + sz * sz) * math.sqrt(gx * gx + gz * gz))
        angle = math.acos(cos)
        if sx > gx:
            angle = (math.pi + angle) % (2 * math.pi)
        print("Rotating")
        print(angle)
        while env.cur_angle > angle: env.step([0, -0.1])
        print(env.cur_angle)
        dist = math.hypot(abs(gx - sx), abs(gz - sz))
        x, y, z = env.cur_pos
        print("Running")
        print(dist)
        travelled = math.hypot(abs(sx - x), abs(sz - z))
        while travelled < dist:
            env.step([0.5, 0])
            x, y, z = env.cur_pos
            travelled = math.hypot(abs(sx - x), abs(sz - z))
            print(travelled, "debug", x, y, z)
        print("Good")

        cos = (gx * sx + gz * sz) / (math.sqrt(gx * gx + gz * gz) * math.sqrt(sx * sx + sz * sz))
        angle = math.acos(cos)
        if sx > gx:
            angle = (math.pi + angle) % (2 * math.pi)
        print("Rotating")
        print(angle)
        while env.cur_angle > angle: env.step([0, -0.1])
        dist = math.hypot(abs(gx - sx), abs(gz - sz))
        x, y, z = env.cur_pos
        print("Running")
        print(dist)
        travelled = math.hypot(abs(gx - x), abs(gz - z))
        while travelled < dist:
            env.step([0.5, 0])
            x, y, z = env.cur_pos
            travelled = math.hypot(abs(sx - x), abs(sz - z))
            print(travelled, "debug", x, y, z)
        print("Good")
