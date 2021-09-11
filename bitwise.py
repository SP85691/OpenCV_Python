import cv2 as cv
import numpy as np

blank = np.zeros((400,400), dtype= "uint8")

rect = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)

cv.imshow("Rectangle", rect)
cv.imshow("Circle", circle)

# ----------------- BITWISE OPERATOR --------------------- #

# Bitwise And  --> Intersecting Region
bitwise_and = cv.bitwise_and(rect,circle)
cv.imshow("Bitwise_AND", bitwise_and)

# Bitwise OR  --> Intersecting and Non-Intersecting Regions
bitwise_or = cv.bitwise_or(rect,circle)
cv.imshow("OR Opretor", bitwise_or)

# Bitwise XOR --> Non-Intersecting Region
bitwise_xor = cv.bitwise_xor(rect,circle)
cv.imshow("BITWISE_XOR",bitwise_xor)

# Bitwise NOT  
bitwise_not = cv.bitwise_not(rect)
cv.imshow("NOT Operator", bitwise_not)

bitwise_not = cv.bitwise_not(circle)
cv.imshow("NOT Circle Operator", bitwise_not)

cv.waitKey(0)