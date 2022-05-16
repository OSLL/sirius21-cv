from gym_duckietown.tasks.task_solution import TaskSolution
import numpy as np
import cv2


class LfChallengeNoCvTaskSolution(TaskSolution):
	def __init__(self, generated_task):
		super().__init__(generated_task)

	def solve(self):
		env = self.generated_task['env']
		while True:
			lane_pose = env.get_lane_pos2(env.cur_pos, env.cur_angle)
			distance_to_road_center = lane_pose.dist
			angle_from_straight_in_rads = lane_pose.angle_rad

			steering = distance_to_road_center * 30 + angle_from_straight_in_rads * 20
			speed = 1 - abs(steering) * 0.8

			if speed < 0:
				speed = 0

			env.step([speed, steering])
			env.render()
