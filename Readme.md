Problems:
1) Watermark
2) Skewed image
3) Low resolution

Solution:
1) Watermark:
        a) Reading the image
        b) Changing the contrast and brightness of the image using openCV given:
        g(x)=αf(x)+β

        where
        g(x) is the output image
        α>0 and β are often called the gain and bias parameters
        f(x) is the source image pixels

2) Skewed Image:
        a) Reading the image and converting into Grayscale
        b) Using the canny edge detection algorithm with aperature size 3
        c) We use Hough Line Transform to detect the shape of the page
        d) Rotating the skewed images to make it straight

3) Low Resolution:
        a) Reading the image
        b) Using the Histogram equilization we equilize/improve contrast