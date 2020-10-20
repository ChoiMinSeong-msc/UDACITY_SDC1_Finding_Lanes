#%%
import numpy as np
import cv2

image = cv2.imread('test_images/solidYellowCurve2.jpg')
gray = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)   

cv2.imwrite('(1)gray.jpg',gray)
     
#Define a kernel size and apply Gaussian smoothing
kernel_size = 5 
blur_gray = cv2.GaussianBlur(gray,(kernel_size, kernel_size),0)
cv2.imwrite('(2)blur_gray.jpg',blur_gray)

#Define our parameters for Canny and Apply
low_threshold = 50
high_threshold = 150
edges = cv2.Canny(blur_gray, low_threshold, high_threshold)
cv2.imwrite('(3)Cannyedges.jpg',edges)

#Create masked edges image using cv2.fillPoly()
mask = np.zeros_like(edges)
ignore_mask_color = 255
        
#Define four-side polygon to mask
imshape = image.shape
vertices = np.array([[(0,imshape[0]),(imshape[1]//2-10,imshape[0]//2+47),
              (imshape[1]//2+10,imshape[0]//2+47), (imshape[1],imshape[0])]], dtype=np.int32)
cv2.fillPoly(mask, vertices, ignore_mask_color)
masked_edges = cv2.bitwise_and(edges, mask)   
cv2.imwrite('(4)masked_edges.jpg',masked_edges)

# Define the Hough transform parameters
rho = 1                       # distance resolution in pixels of the Hough grid
theta = np.pi/180             # angular resolution in radians of the Hough grid
threshold = 1                 # minimum number of votes (intersections in Hough grid cell)
min_line_length = 152          # minimum number of pixels making up a line
max_line_gap = 100             # maximum gap in pixels between connectable line segments
line_image = np.copy(image)*0 # creating a blank to draw lines on

# Hough Transform on masked_edges
lines = cv2.HoughLinesP(masked_edges, rho, theta, threshold, np.array([]), min_line_length, max_line_gap)

# Draw Hough Transformed line on blank image
for line in lines:
    for x1,y1,x2,y2 in line:
        cv2.line(line_image,(x1,y1),(x2,y2),(255,0,0),5)
cv2.imwrite('(5)line_image.jpg',line_image)
        
# Create a "color" binary image to combine with line image
color_edges = np.dstack((edges, edges, edges))


# Add line image on original image
result = cv2.add(image,line_image)
cv2.imwrite('(6)result.jpg',result)
        

