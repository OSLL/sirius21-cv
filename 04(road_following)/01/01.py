from gym_duckietown.tasks.task_solution import TaskSolution
import numpy as np
import cv2


def get_pose(env):
	global dist, angle
	pose = env.get_lane_pos2(env.cur_pos, env.cur_angle)
	dist = pose.dist
	angle = pose.angle_rad


def dist_stab(env):
	global dist, angle

	if dist > 0.02:
		while dist > -0.02:
			env.step([0.3, 1])
			get_pose(env)

	elif dist < -0.02:
		while dist < 0.02:
			env.step([0.3, -1])
			get_pose(env)

	else:
		env.step([1, 0])


def angle_stab(env):
	global dist, angle

	if angle > 0.02:
		while angle > -0.02:
			env.step([0, 1])
			get_pose(env)

	elif angle < -0.02:
		while angle < 0.02:
			env.step([0, -1])
			get_pose(env)

	else:
		env.step([1, 0])


dist = 0
angle = 0


class LfChallengeNoCvTaskSolution(TaskSolution):
	def __init__(self, generated_task):
		super().__init__(generated_task)

	def solve(self):
		env = self.generated_task['env']
		while True:
			get_pose(env)
			# Требуется по положению робота в полосе определить линейную и угловые скорости

			dist_stab(env)
			angle_stab(env)

			env.render()
