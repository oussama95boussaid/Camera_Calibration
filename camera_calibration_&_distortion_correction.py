# -*- coding: utf-8 -*-
"""camera_calibration_&_distortion_correction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gsA9WN-C57AJ7RtgjWXwbwxFsNDBCFPT

# **Extract Object Points & Image Points**
"""

import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((6*8,3), np.float32)
objp[:,:2] = np.mgrid[0:8, 0:6].T.reshape(-1,2)


# Arrays to store object points and image points from all the images.
objpoints = [] # 3d points in real world space
imgpoints = [] # 2d points in image plane.

# Make a list of calibration images
fname = 'calibration_test.png'
img = cv2.imread(fname)

# Converting an image, imported by cv2 or the glob API, to grayscale:
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Finding chessboard corners (for an 8x6 board):
ret, corners = cv2.findChessboardCorners(gray, (nx, ny), None)

# If found, add object points, image points & draw corners
if ret == True:
  objpoints.append(objp)
  imgpoints.append(corners)
  # Drawing detected corners on an image:
  cv2.drawChessboardCorners(img, (nx, ny), corners, ret)
  plt.imshow(img)

"""# **Camera Calibration & Distortion Correction**

**Note:** If you are reading in an image using mpimg.imread() this will read in an RGB image and you should convert to grayscale using cv2.COLOR_RGB2GRAY, but if you are using cv2.imread() or the glob API, as happens in this video example, this will read in a BGR image and you should convert to grayscale using cv2.COLOR_BGR2GRAY. We'll learn more about color conversions later on in this lesson, but please keep this in mind as you write your own code and look at code examples.

**A note on image shape :** The shape of the image, which is passed into the calibrateCamera function, is just the height and width of the image. One way to retrieve these values is by retrieving them from the grayscale image shape array gray.shape[::-1]. This returns the image width and height in pixel values like (1280, 960).

Another way to retrieve the image shape, is to get them directly from the color image by retrieving the first two values in the color image shape array using img.shape[1::-1]. This code snippet asks for just the first two values in the shape array, and reverses them. Note that in our case we are working with a greyscale image, so we only have 2 dimensions (color images have three, height, width, and depth), so this is not necessary.
"""

import pickle
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


'''
if you want to play with extracting object points and image points,
You can load data from  the distortion pickle file

'''

# Read in the saved objpoints and imgpoints
dist_pickle = pickle.load( open( "wide_dist_pickle.p", "rb" ) )
objpoints = dist_pickle["objpoints"]
imgpoints = dist_pickle["imgpoints"]


# Read in an image
img = cv2.imread('calibration_test.png')

def cal_undistort(img, objpoints, imgpoints) :

  # Converting an image, imported by cv2 or the glob API, to grayscale:
  gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

  # Camera calibration, given object points, image points, and the shape of the grayscale image:
  ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

  #Undistorting a test image:
  undist = cv2.undistort(img, mtx, dist, None, mtx)

  return undist

undistorted = cal_undistort(img, objpoints, imgpoints)

f, (ax1, ax2) = plt.subplots(1, 2, figsize=(24, 9))
f.tight_layout()
ax1.imshow(img)
ax1.set_title('Original Image', fontsize=50)
ax2.imshow(undistorted)
ax2.set_title('Undistorted Image', fontsize=50)
plt.subplots_adjust(left=0., right=1, top=0.9, bottom=0.)
plt.savefig("undistorted.png")