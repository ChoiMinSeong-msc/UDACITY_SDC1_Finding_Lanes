# **Finding Lane Lines on the Road** 

## Writeup Template

### You can use this file as a template for your writeup if you want to submit it as a markdown file. But feel free to use some other method and submit a pdf if you prefer.

---

**Finding Lane Lines on the Road**
The goal of this project is finding lane lines on the road by canny edge & hough transform.
5-step methods are following.
* Gray -> BlurGray 
* Canny Edge Detection
* Mask
* Hough Transform
* Result

[//]: # (Image References)

[image1]: ./(1)gray.jpg "Gray"
[image2]: ./(2)blur_gray.jpg "Blurred Gray"
[image3]: ./(3)Cannyedges.jpg "Canny Edge"
[image4]: ./(4)maskededges.jpg "Canny Edge with Mask"
[image5]: ./(5)line_image.jpg "Line Image with Hough Transform"
[image6]: ./(6)result.jpg "Line Detection Result"


---

### Reflection

### 1.PIPE LINE

1. Get image and change into (blur)gray scale.
   Gaussian Blur function is used.
   
![alt text][image1]
![alt text][image2]

2. Use Canny Edge detection for above blur-gray image.

![alt text][image3]

3. Create four-sided mask and filter the Canny Edge detection image.

![alt text][image4]

4. Run Hough Transform on the Masked Canny Edge detection image.

![alt text][image5]

5. Original Image + Line Image

![alt text][image6]


### 2. Identify potential shortcomings with your current pipeline


The main short comming is 'not Robust'.
We used lots of parameters to tune.
Especially, masking region is always fixed.
If the environment changes, the results will come out bad.
Light change and View change are critical.


### 3. Suggest possible improvements to your pipeline


We need to suggest more robust algorithm.
Maybe using deep learning with lot's of data set would be the one of the solution.


