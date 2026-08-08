import numpy as np
import cv2

def order_points(pts): #34an n define el coordinates bta3 el rectangle.
	
	rectangle = np.zeros((4, 2), dtype = "float32") # this line creates a 2D array consisting of 4 rows and 2 columns, filled with zeros. (34an el rectangle)
	
	s = pts.sum(axis = 1)
	rectangle[0] = pts[np.argmin(s)] #top-left
	rectangle[2] = pts[np.argmax(s)] #bottom-right
	diff = np.diff(pts, axis = 1)
	rectangle[1] = pts[np.argmin(diff)] #top-right
	rectangle[3] = pts[np.argmax(diff)] #bottom-left
	
	return rectangle

def four_point_transform(image, pts):
	
	rect = order_points(pts)
	(tl, tr, br, bl) = rect
	# compute the width of the new image, using the distance formula 3ady.
	widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
	widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
	maxWidth = max(int(widthA), int(widthB))# da by estimate it bas .
	# compute the height of the new image, using the distance formula bardo.
	heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
	heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
	maxHeight = max(int(heightA), int(heightB))
	
	dst = np.array([
		[0, 0],
		[maxWidth - 1, 0],
		[maxWidth - 1, maxHeight - 1],
		[0, maxHeight - 1]], dtype = "float32") #ana hena badelo el destination elly ydawar feha 3la el image elly 3ayez ygeeb el bird eye view bta3ha.
	# compute the perspective transform matrix 
	M = cv2.getPerspectiveTransform(rect, dst)
	warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))
	return warped