#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import ast
import math
import time
import numpy as np

class LaserModel(object):

    def __init__(self, angle_min, angle_max, range_min, range_max):

        #here the basic settings of your laser are defined
        self.angle_min = angle_min
        self.angle_max = angle_max
        self.range_min = range_min
        self.range_max = range_max
        self.angle_inc = 0

        #some more member variables that we use during execution
        self.scan_data = []
        self.laser_read_cycle = -1


    '''
    Method to simulate a laserdata stream, you don't have to change anything here
    '''
    def update_laserdata(self,laserdata_file):
        file = open(laserdata_file, "r")
        laserdata_raw = file.read()
        scan_data_raw = ast.literal_eval(laserdata_raw)

        self.scan_data = scan_data_raw[self.laser_read_cycle%len(scan_data_raw)]
        self.laser_read_cycle+=1

    '''
    Setter and getter methods for some member variables
    '''
    def set_angle_inc(self,angle_inc):
        self.angle_inc = angle_inc

    def get_angle_inc(self):
        return self.angle_inc

    def get_scan_length(self):
        return len(self.scan_data)

    '''
    TODO: calculate the angle increment
    '''
    def calc_angle_inc(self):
        self.angle_inc = ((self.angle_max-self.angle_min)/len(self.scan_data))
        return self.angle_inc
    '''
    TODO: port your code from previous exercise
    '''
    def calc_index_of_closest_point(self):
        m = min(i for i in self.scan_data if i > 0)
        self.index_min_dist = self.scan_data.index(m)
        return self.index_min_dist

    '''
    TODO: port your code from previous exercise
    '''
    def calc_angle_of_closest_point(self):
        self.angle_min_dist = self.angle_min+(self.index_min_dist*self.angle_inc)
        return self.angle_min_dist

    '''
    core method for your function calls etc
    '''
    def run(self):
        self.update_laserdata("laser-testdata/laser-testdata_2")
        #print current results
        print("-"*20+
            str("\nCurrent cycle: {0}"+
            "\nIndex of closest point: {1}"+
            "\nAngle of closest point: {2}"
            ).format(self.laser_read_cycle,self.calc_index_of_closest_point(),self.calc_angle_of_closest_point())
        )

if __name__ == '__main__':

    #instantiate the class and set some parameters
    app = LaserModel(-math.pi/2, math.pi/2, 2.0, 30.0)
    app.update_laserdata("laser-testdata/laser-testdata_2")
    app.set_angle_inc(app.calc_angle_inc())

    print("-"*20+
        str("\nAngle increment: {}"+
        "\nLenght of scan data: {}"
        ).format(app.get_angle_inc(),app.get_scan_length())
    )

    #run the script in an infite loop to continously read and process laserdata
    while(True):
        app.run()
        time.sleep(1)
