import cv2
import numpy as np

# Load the two images
img1 = cv2.imread('image3.jpg')  # replace with your first image name
img2 = cv2.imread('image2.jpg')  # replace with your second image name

# Resize images to the same height for horizontal stacking
height = min(img1.shape[0], img2.shape[0])
img1_resized = cv2.resize(img1, (int(img1.shape[1] * height / img1.shape[0]), height))
img2_resized = cv2.resize(img2, (int(img2.shape[1] * height / img2.shape[0]), height))

# Join images horizontally
horizontal = np.hstack((img1_resized, img2_resized))

# OR Join images vertically (same width needed)
# width = min(img1.shape[1], img2.shape[1])
# img1_resized = cv2.resize(img1, (width, int(img1.shape[0] * width / img1.shape[1])))
# img2_resized = cv2.resize(img2, (width, int(img2.shape[0] * width / img2.shape[1])))
# vertical = np.vstack((img1_resized, img2_resized))

# Show and save the result
cv2.imshow('Joined Image', horizontal)  # or use 'vertical'
cv2.imwrite('joined_output.jpg', horizontal)  # or vertical

cv2.waitKey(0)
cv2.destroyAllWindows()

