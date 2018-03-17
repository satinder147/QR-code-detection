# QR_DETECTION
This is a small little project i made few days back.
It can detect qr codes in the image using opencv-python
The procedure is:

1)We blur the image slightly

2)We dilate the image  , so that after dilation the qr code region becomes a square

3)we errode the image to remove unwated regions.

4)We find contours of the image and these contours and the largest of them is found

5)bounding box is drawn onto the detected qr code

6)The detected qr code is decoded using pyzbar(library to decde barcodes and qrcodes)

7)The url we get is opened in the browser

![screenshot 204](https://user-images.githubusercontent.com/24778913/37554104-135b3170-29fa-11e8-915c-214509fe36e7.png)
