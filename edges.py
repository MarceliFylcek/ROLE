import cv2
import numpy as np

def add_mask_edges(mask, edges):
	contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	cv2.drawContours(edges, contours, -1, (255), thickness=1)

teeth_mask = "masks/00001.png"
drop_mask = "Output_label/00001.png"

binary_mask_drop = cv2.imread(drop_mask, cv2.IMREAD_GRAYSCALE)
binary_mask_drop = cv2.convertScaleAbs(binary_mask_drop)

binary_mask_teeth = cv2.imread(teeth_mask, cv2.IMREAD_GRAYSCALE)
binary_mask_teeth = cv2.convertScaleAbs(binary_mask_teeth)

width = binary_mask_drop.shape[1]
height = binary_mask_drop.shape[0]
dim = (width, height)

binary_mask_teeth = cv2.resize(binary_mask_teeth, dim, interpolation = cv2.INTER_AREA)

edges = np.zeros_like(binary_mask_teeth)

add_mask_edges(binary_mask_teeth, edges)
add_mask_edges(binary_mask_drop, edges)

cv2.imshow('Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()