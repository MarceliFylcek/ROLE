import cv2

img = cv2.imread("00001.png")

if img is not None:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur before Sobel edge detection
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Sobel edge detection
    sobel_x = cv2.Sobel(blurred, cv2.CV_64F, 1, 0, ksize=5)
    sobel_y = cv2.Sobel(blurred, cv2.CV_64F, 0, 1, ksize=5)
    edges = cv2.magnitude(sobel_x, sobel_y)
    edges = cv2.convertScaleAbs(edges)
    threshold_value = 250  # Adjust this threshold value
    ret, thresholded = cv2.threshold(edges, threshold_value, 255, cv2.THRESH_BINARY)
    cv2.imshow("Thresholded", thresholded)
    cv2.waitKey(0)
else:
    print("Image not found or could not be read.")