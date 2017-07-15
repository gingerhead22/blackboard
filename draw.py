import cv2
import numpy as np 

def nothing(x):
	pass

draw=False
ix,iy=-1,-1

img=np.zeros((512,512,3),np.uint8)
cv2.namedWindow('Blackboard')

cv2.createTrackbar('R','Blackboard',0,255,nothing)
cv2.createTrackbar('G','Blackboard',0,255,nothing)
cv2.createTrackbar('B','Blackboard',0,255,nothing)

cv2.createTrackbar('Radius','Blackboard',1,20,nothing)

def draw_circle(event,x,y,flags,param):
	global draw, ix,iy,r,g,b,radius

	if event==cv2.EVENT_LBUTTONDOWN:
		draw=True
		ix,iy=x,y
	elif event==cv2.EVENT_MOUSEMOVE:
		if draw:
			cv2.circle(img,(x,y),radius,(b,g,r),-1)
	elif event==cv2.EVENT_LBUTTONUP:
		draw=False
		cv2.circle(img,(x,y),radius,(b,g,r),-1)

cv2.setMouseCallback('Blackboard',draw_circle)

while(1):
	cv2.imshow('Blackboard',img)
	k=cv2.waitKey(1) & 0xFF
	if k==27:
		break
	r=cv2.getTrackbarPos('R','Blackboard')
	g=cv2.getTrackbarPos('G','Blackboard')
	b=cv2.getTrackbarPos('B','Blackboard')
	radius=cv2.getTrackbarPos('Radius','Blackboard')

cv2.destroyAllWindows()

