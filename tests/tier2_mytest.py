#!/usr/bin/env python#
# -*- coding: utf-8 -*-

def func(x):
  return x + 1

def test_works():
  assert func(3) == 4

def test_fails():
  assert func(5) == 6

import tier2_main_class as tier2_class
import math


class Test:

	def setup(self):
		self.app = tier2_class.LaserModel(-math.pi/2, math.pi/2, 0.0, 7.0)
		self.app.update_laserdata("laser-testdata/laser-testdata_2")
		self.app.set_angle_inc(self.app.calc_angle_inc())
		#self.app.laser_read_cycle = 0

	def test_calc_angle_of_closest_point(self):
		angle_min= -1.57079637051
		angle_max= 1.53938043118
		assert (angle_min + self.app.calc_index_of_closest_point()*self.app.calc_angle_inc()) > -1.57079637051
		assert (angle_min + self.app.calc_index_of_closest_point()*self.app.calc_angle_inc()) < 1.53938043118

