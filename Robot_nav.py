#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.media.ev3dev import SoundFile, ImageFile
import time
from math import pi


WHEEL_DIAMETER = 56 #mm
CIRCUMFERENCE_WHEEL = pi * WHEEL_DIAMETER # 3.14 * 56
SPEED = 300 # degrees/second
TURN_SPEED = 150 # degrees/second
ROBOT_WIDTH = 114 # mm


def calculateTime(distance, speed):

    # Distance to travel (mm) / circumference of wheel = number of rotations needed
    no_rotations = distance / CIRCUMFERENCE_WHEEL

    # (number of rotations * 360) + error = degree of rotation 
    #no_degrees = (no_rotations * 360) + ROTATION_ERROR
    no_degrees = (no_rotations * 360)

    # time needed for motor to run at SPEED to achieve required rotation = degrees / speed
    rotation_time = no_degrees/speed

    return rotation_time


def drive_distance_forward(distance):

    # calculate time motor needs to run to travel given distance
    motor_time = calculateTime(distance, SPEED)
    left_motor.run(SPEED)
    right_motor.run(SPEED)
    time.sleep(motor_time)
    left_motor.brake()
    right_motor.brake()

    ev3.speaker.beep()
    time.sleep(0.5)


def drive_distance_backward(distance):

    # calculate time motor needs to run to travel given distance backward
    motor_time = calculateTime(distance, SPEED)
    left_motor.run(-SPEED)
    right_motor.run(-SPEED)
    time.sleep(motor_time)
    left_motor.brake()
    right_motor.brake()

    ev3.speaker.beep()


def turn_left_angle(angle):
    # distance wheels need to travel to rotate at point between axle.
    # Here width * pi gives circumference because we rotate both wheels, one forward and other backwards 
    distance = (ROBOT_WIDTH*pi)/(360/angle)

    # get time for motor to run
    motor_time = calculateTime(distance, TURN_SPEED)

    left_motor.run(TURN_SPEED)
    right_motor.run(-TURN_SPEED)
    time.sleep(motor_time)
    left_motor.brake()
    right_motor.brake()

    ev3.speaker.beep()
    time.sleep(0.5)


def turn_right_angle(angle):
    # distance wheels need to travel to rotate at point between axle.
    # Here width * pi gives circumference because we rotate both wheels, one forward and other backwards 
    distance = (ROBOT_WIDTH*pi)/(360/angle)

    # get time for motor to run
    motor_time = calculateTime(distance, TURN_SPEED)

    left_motor.run(-TURN_SPEED)
    right_motor.run(TURN_SPEED)
    time.sleep(motor_time)
    left_motor.brake()
    right_motor.brake()

    ev3.speaker.beep()

    time.sleep(0.5)


if __name__ == "__main__":

    # Initialize the EV3 Brick.
    ev3 = EV3Brick()

    # Connect two motors on output ports B and C
    left_motor = Motor(Port.B)
    right_motor = Motor(Port.C)

    #ev3.speaker.beep()

    drive_distance_forward(300)
    turn_left_angle(90)
    drive_distance_forward(300)
    turn_right_angle(90)
    drive_distance_forward(700)
    turn_right_angle(90)
    drive_distance_forward(600)
    turn_right_angle(90)
    drive_distance_forward(700)
    turn_right_angle(90)
    drive_distance_forward(300)
    turn_left_angle(90)

    ev3.speaker.beep()


