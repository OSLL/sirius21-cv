from gym_duckietown.tasks.task_solution import TaskSolution
import numpy as np
import cv2

class LfChallengeNoCvTaskSolution(TaskSolution):
    def __init__(self, generated_task):
        super().__init__(generated_task)


    def solve(self):
        env = self.generated_task['env']
        while True:
            speed = 1
            kv = 1
            kw = 3 * (speed * 10)
            kd = 20 * (speed * 10)
            steering = 0
            print('kv=', kv, 'kw=', kw, 'kd=', kd)
            print('speed=', speed, 'steering=', steering)
            lane_pose = env.get_lane_pos2(env.cur_pos, env.cur_angle)
            print('env.cur_pos=', env.cur_pos, 'env.cur_angle=', env.cur_angle)
            distance_to_road_center = lane_pose.dist
            print('distance_to_road_center=', distance_to_road_center)
            angle_from_straight_in_rads = lane_pose.angle_rad
            print('angle_from_straight_in_rads=', angle_from_straight_in_rads)
            # Требуется по положению робота в полосе определить линейную и угловые скорости
            steering = 0 + kw * angle_from_straight_in_rads + kd * distance_to_road_center
            if(steering > 1):
                steering = 1
            if(steering < -1):
                steering = -1
            speed = 1 - abs(steering * kv)
            if(speed < 0):
                speed = 0

            print('speed=', speed, 'steering=', steering)
            print('distance_to_road_center=', distance_to_road_center, 'angle_from_straight_in_rads=', angle_from_straight_in_rads)
            env.step([speed, steering])
            env.render()
