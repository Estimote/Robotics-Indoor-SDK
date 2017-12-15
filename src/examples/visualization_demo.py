#!/usr/bin/env python

#Before starting this demo:
# 1. Log in to cloud.estimote.com
# 2. In a separate tab go to https://cloud.estimote.com/v1/indoor/locations/YOUR_LOCATION_IDENTIFIER
# 3. Save the raw json to a location.json file locatet above the examples directory
# 4. Make sure that Robotics-Indoor-SDK is alread up and running
# 5. Run visualization_demo.py from the examples directory
# 6. Enjoy a simple positioning visualization 

import pygame, sys, json, time, rospy
from pygame.locals import *
from std_msgs.msg import String

WINDOW_WIDTH = 480
WINDOW_HEIGTH = 480
COORDINATES_MULTIPLIER = 50

BLACK_COLOR = (0, 0, 0)
BLUE_COLOR = (0, 0, 255)
WHITE_COLOR = (255, 255, 255)

WALLS_THICKNESS = 4

LOCATION_PATH = "../location.json"

# Convert coordinates into pygame coordinates (lower left => top left)
def to_pygame_coordinates(coordinates):
	print coordinates[0]
	print coordinates[1]
	return (int(COORDINATES_MULTIPLIER * round(float(coordinates[0]))), int(WINDOW_HEIGTH - (COORDINATES_MULTIPLIER * round(float(coordinates[1])))))

def main():
	pygame.init()

	#POSITION_IMAGE = pygame.transform.scale(pygame.image.load('position_image.jpg', (COORDINATES_MULTIPLIER, COORDINATES_MULTIPLIER))
	DISPLAY = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGTH), 0, 32)

	pygame.display.set_caption('Robotics Indoor SDK - visualization demo')
	
	location_json = []
	with open(LOCATION_PATH, 'r') as file:
		location_json = json.load(file)
	
	def prepare_drawable_walls():
		location_json_walls = location_json['walls']
		walls = []
		for wall in location_json_walls:
			wall_start = to_pygame_coordinates((wall['x1'], wall['y1']))
			wall_end = to_pygame_coordinates((wall['x2'], wall['y2']))
			walls.append((wall_start, wall_end))
		return walls
	DRAWABLE_WALLS = prepare_drawable_walls()
		
	def draw_location():
		for wall in DRAWABLE_WALLS:
			wall_start = wall[0]
			wall_end = wall[1]
			pygame.draw.line(DISPLAY, BLACK_COLOR, wall_start, wall_end, WALLS_THICKNESS)

	DISPLAY.fill(WHITE_COLOR)
	draw_location()
	pygame.display.update()

	def draw_tracked_object(coordinates):
		DISPLAY.fill(WHITE_COLOR)
		draw_location()

		#DISPLAY.blit(POSITION_IMAGE, to_pygame_coordinates(coordinates))
		pygame.draw.circle(DISPLAY, BLUE_COLOR, to_pygame_coordinates(coordinates), 10, 0)
		pygame.display.update()
 
	#LISTEN TO ROS MESSAGES
	def estimote_position_callback(data):
		rospy.loginfo(rospy.get_caller_id() + " [Robotics Indoor SDK] x, y = %s", data.data)
		coordinates = tuple(data.data.replace(" ", "").split(','))
		draw_tracked_object(coordinates)

	def listen_for_position_messages():
		rospy.init_node('listener', anonymous = True)
		rospy.Subscriber("estimote_position", String, estimote_position_callback)
		rospy.spin()
	listen_for_position_messages()

if __name__ == "__main__":
	main()

