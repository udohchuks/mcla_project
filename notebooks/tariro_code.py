import cv2   # importing  for image processing

# Reading image in grayscale 
img = cv2.imread('image.jpg', 0)



identity = img.copy()   # no change ,simply copies the org



sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0)

#  Highlights vertical edges 


sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1)

#  highlights horizontal  edges 


sobel_x = cv2.convertScaleAbs(sobel_x)
sobel_y = cv2.convertScaleAbs(sobel_y)
# converts negative values to range (0- 255)



cv2.imshow("Original", identity)# shows orginal image 


cv2.imshow("Left Sobel (Vertical edges)", sobel_x) 
# shows  the image with highlighted vertical edges 

cv2.imshow("Horizontal edges", sobel_y)
# shows the image with highlighted  horizontal edges


cv2.waitKey(0) # waiting /pausing


cv2.destroyAllWindows() # closing the image window
