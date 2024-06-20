import carla
import math
import numpy as np

import csv

# def save_waypoints_to_csv(waypoints, filename='waypoints.txt'):
#     with open(filename, mode='w', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow(['x', 'y', 'z'])  # Header
#         for waypoint in waypoints:
#             writer.writerow(waypoint)

# def save_boundary_to_csv(boundary, filename='boundary.txt'):
#     with open(filename, mode='w', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow(['left_x', 'left_y', 'left_z', 'right_x', 'right_y', 'right_z'])  # Header
#         for left, right in zip(boundary[0], boundary[1]):
#             # print(boundary[0], boundary[1])
#             left_location = left.transform.location
#             right_location = right.transform.location
#             writer.writerow(["(" + str(left_location.x), str(left_location.y)+")","(" + 
#                              str(right_location.x), str(right_location.y)+")"])


# def save_obstacles_to_csv(filtered_obstacles, filename='obstacles.csv'):
#     with open(filename, mode='w', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow(['id', 'x', 'y', 'z'])  # Header
#         for obstacle in filtered_obstacles:
#             obstacle_id = obstacle.id
#             obstacle_transform = obstacle.get_transform()
#             obstacle_location = obstacle_transform.location
#             writer.writerow([obstacle_id, obstacle_location.x, obstacle_location.y, obstacle_location.z])


def get_speed(velocity):
    velocity = math.sqrt(velocity.x**2 + velocity.y**2 + velocity.z**2)
    print(velocity)
    return velocity

class Agent():
    def __init__(self, vehicle=None, L=2.875):
        self.vehicle = vehicle
        self.L = L  # Wheelbase of the vehicle
        # all_filtered_obstacles = []

    def longitudinal_controller(self, curr_x, curr_y, curr_vel, curr_yaw, future_unreached_waypoints):
        straight_speed = 0.8
        turn_speed = 0.3
        if len(future_unreached_waypoints) >= 2:
            first_waypoint = future_unreached_waypoints[0]
            second_waypoint = future_unreached_waypoints[1]
            angle = math.atan2(second_waypoint[1] - first_waypoint[1], second_waypoint[0] - first_waypoint[0])
            # Ensure the angle is within the range [0, 2*pi]
            angle = (angle + 2 * math.pi) % (2 * math.pi)
        else:
            angle = 0.0
        angle_error = abs(math.degrees(curr_yaw) - math.degrees(angle))
        angle_error = angle_error % 360
        if 340 > angle_error > 10: 
            target_velocity = turn_speed
        else:
            target_velocity = straight_speed
        # print(target_velocity,math.degrees(angle),math.degrees(curr_yaw),angle_error)
        return target_velocity

    def pure_pursuit_lateral_controller(self, curr_x, curr_y, curr_yaw, waypoints):
        lookahead_distance = 5.0
        lookahead_point = None

        # Find the first waypoint that is at least lookahead_distance away
        for waypoint in waypoints:
            if math.dist((curr_x, curr_y), waypoint[:2]) > lookahead_distance:
                lookahead_point = waypoint
                break

        if lookahead_point is None:
            return 0.0  # No steering if no lookahead point is found

        # Calculate the angle to the lookahead point
        angle_to_waypoint = math.atan2(lookahead_point[1] - curr_y, lookahead_point[0] - curr_x)

        # Calculate the target steering angle using the pure pursuit formula
        target_steering = np.arctan(2 * self.L * np.sin(angle_to_waypoint - curr_yaw) / lookahead_distance)
        # print(target_steering)
        return target_steering

    def run_step(self, filtered_obstacles, waypoints, vel, transform, boundary):
        
        # save_waypoints_to_csv(waypoints)
        # save_boundary_to_csv(boundary)

        # Get the current velocity in m/s
        # print(vel)
        current_velocity = get_speed(vel)
        # print(current_velocity)
        # Determine the target velocity
        # target_velocity = self.longitudinal_controller(current_velocity, target_velocity)

        

        # Get the current position and orientation
        curr_x = transform.location.x
        curr_y = transform.location.y
        curr_yaw = math.radians(transform.rotation.yaw)

        # Calculate the steering angle
        target_velocity = self.longitudinal_controller(curr_x, curr_y, current_velocity, curr_yaw, waypoints)
        steer = self.pure_pursuit_lateral_controller(curr_x, curr_y, curr_yaw, waypoints)

        # Create the control command
        control = carla.VehicleControl()
        control.throttle = target_velocity
        # control.throttle = 0.0
        control.steer = steer
        control.brake = 0  # Set the brake to 0 for now

        # save_to_csv(filtered_obstacles, 'filtered_obstacles.csv')
        # Return the control command
        return control
