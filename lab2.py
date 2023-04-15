#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

wings = 5
frame_size = 256
camera_lines = 8
frames = 64
multiplier = frame_size/2
car_box_size = frame_size / camera_lines
rotation = np.arange(-frames / 2, frames / 2, 1)
resolution = 2137

linspace = np.linspace(0, 2 * np.pi * multiplier, resolution)
fx = lambda x, m: np.sin(wings * x + (m * np.pi /10))


def is_in_carbox(x, y, line_idx):
  carbox_y_start = camera_lines * line_idx - multiplier
  carbox_y_stop = camera_lines * (line_idx + 1) - multiplier
  return (x >= -multiplier and x < multiplier) and (y >= carbox_y_start and y < carbox_y_stop)


def cartesian(x, deg):
  return x * np.cos(deg), x * np.sin(deg)


def gen_line(rotation, carbox_idx):
  x_passed, y_passed = [], []
  x, y = cartesian(fx(linspace, rotation) * multiplier, linspace)
  for i in range(x.size):
    if is_in_carbox(x[i], y[i], carbox_idx):
      x_passed.append(x[i])
      y_passed.append(y[i])
  return x_passed, y_passed


def gen_frame(rotation):
  x_frame, y_frame = [], []
  for carbox_idx in range(int(car_box_size)):
    x_passed, y_passed = gen_line(rotation+carbox_idx, carbox_idx)
    x_frame += x_passed
    y_frame += y_passed
    # print("carbox_idx: ", carbox_idx, "rotation: ", rotation)
    # ax.scatter(x_passed, y_passed, color='blue', s=1)
    # plt.pause(0.1)
  return x_frame, y_frame


fig = plt.figure()
ax = fig.add_subplot()

for i in range(frames):
  ax.clear()
  ax.set_xlim(-multiplier, multiplier)
  ax.set_ylim(-multiplier, multiplier)
  x_frame, y_frame = gen_frame(rotation[i])
  ax.scatter(x_frame, y_frame, color='red', s=2)
  plt.pause(0.01)

plt.show()