import numpy as np 
import cv2 as cv 

ing = np.zeros((780  ,832,3),np.uint8)


def DrawCircle(XCenter , YCenter , Ri , R , G , B , length) :
    cv.circle(ing #Source_image
            ,(XCenter,YCenter)#center
            ,(Ri)#radiuse
            ,(B,G,R)
            ,length)



#The top 

DrawCircle(415 , 194 , 193 , 255 , 0 ,0 , -1)
DrawCircle(415 , 194 , 78 , 0 , 0 , 0 , -1)

#the Right

DrawCircle( 193, 567 ,193, 0 , 255 , 0 , -1)
DrawCircle(193 , 567 , 78 , 0 , 0 , 0 , -1)

#The big triangle
pts = np.array([[415, 194], [193, 567],
                [635, 567]],np.int32)
isClosed = True
color = (0, 0, 0)
colorB = (55, 33, 12)
thickness = 0
cv.polylines(ing, [pts],isClosed, color, thickness)
cv.fillPoly(ing , [pts],color)

#the left
DrawCircle(635 , 567 , 193 , 0 , 0 , 255 , -1)
DrawCircle(632  , 567 , 78 , 0 , 0 , 0 , -1)

#small Triangel
pts2 = np.array([[526 , 371] , [754 , 371] , [635 , 567]],np.int32)
cv.polylines(ing, [pts2],isClosed, color, 1)
cv.fillPoly(ing , [pts2],color)



cv.imshow("Draw", ing)
cv.waitKey(0)
