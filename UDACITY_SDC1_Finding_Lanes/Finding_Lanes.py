import numpy as np
import cv2


Video = './test_videos/solidYellowLeft.mp4'
cap =  cv2.VideoCapture(Video) #Read Video

# Setting for saving image
fps = 30.0
width = int(cap.get(3))
height = int(cap.get(4))
fcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
out = cv2.VideoWriter('output.avi', fcc, fps, (width,height))


while(cap.isOpened()):
    ret, image = cap.read()


    if ret:
        
        #Read in and grayscale the image
        gray = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)   
        
        #Define a kernel size and apply Gaussian smoothing
        kernel_size = 5
        blur_gray = cv2.GaussianBlur(gray,(kernel_size, kernel_size),0)
        
        #Define our parameters for Canny and Apply
        low_threshold = 50
        high_threshold = 150
        edges = cv2.Canny(blur_gray, low_threshold, high_threshold)
        
        #Create masked edges image using cv2.fillPoly()
        mask = np.zeros_like(edges)
        ignore_mask_color = 255
        
        #Define four-side polygon to mask
        imshape = image.shape
        vertices = np.array([[(0,imshape[0]),(imshape[1]//2-10,imshape[0]//2+47),
                      (imshape[1]//2+10,imshape[0]//2+47), (imshape[1],imshape[0])]], dtype=np.int32)
        cv2.fillPoly(mask, vertices, ignore_mask_color)
        masked_edges = cv2.bitwise_and(edges, mask)   

        
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
        # Create a "color" binary image to combine with line image
        color_edges = np.dstack((edges, edges, edges))

        # Add line image on original image
        result = cv2.add(image,line_image)

        
        # Show results
        cv2.imshow('video',result)

        # Save results in Video
        out.write(result)        


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
    
cap.release()
out.release()
cv2.destroyAllWindows()