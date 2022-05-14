from gym_duckietown.tasks.task_solution import TaskSolution
import numpy as np
import cv2


def get_pose(env):
	global dist, angle
	pose = env.get_lane_pos2(env.cur_pos, env.cur_angle)
	dist = pose.dist
	angle = pose.angle_rad


def dist_stab(env):
	while dist > 0:
		env.step([0.3, 1])
		get_pose(env)


dist = 0
angle = 0


class LfChallengeNoCvTaskSolution(TaskSolution):
	def __init__(self, generated_task):
		super().__init__(generated_task)

	def solve(self):
		env = self.generated_task['env']

		get_pose(env)

		dist_stab(env)

		while True:
			get_pose(env)
			# Требуется по положению робота в полосе определить линейную и угловые скорости
			k_dist = 1 - dist

			dist_stab(env)
			env.step([0.3 * k_dist, 10 * angle * k_dist])

			print('dist: ' + str(dist))
			print('angle: ' + str(angle))

			env.render()
