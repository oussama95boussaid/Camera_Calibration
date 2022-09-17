# Camera_Calibration
There are two main steps to this process: use chessboard images to obtain image points and object points, and then use the OpenCV functions cv2.calibrateCamera() and cv2.undistort() to compute the calibration and undistortion.

**Extract Object Points & Image Points**

<img src="FindingCorners.png">


**Camera Calibration & Distortion Correction**

<img src="undistorted.png">

**Undistort and Transform Perspective**

<img src="Undistorted_ Warped.png">
