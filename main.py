import cv2
import numpy as np

# Initialize the webcam
cap = cv2.VideoCapture(0)

# Allow the camera to warm up
import time
time.sleep(3)

# Capture the background frame
for i in range(30):
    ret, background = cap.read()

# Flip the background frame
background = np.flip(background, axis=1)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # Flip the current frame
    frame = np.flip(frame, axis=1)
    
    # Convert the frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Define the range for the color of the cloak (blue in this case)
    lower_blue = np.array([100, 150, 0])
    upper_blue = np.array([140, 255, 255])
    
    # Create a mask for the blue color
    mask1 = cv2.inRange(hsv, lower_blue, upper_blue)
    
    # Refine the mask
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_DILATE, np.ones((3, 3), np.uint8))
    
    # Create an inverse mask
    mask2 = cv2.bitwise_not(mask1)
    
    # Segment the cloak out of the frame using bitwise and with the inverse mask
    res1 = cv2.bitwise_and(frame, frame, mask=mask2)
    
    # Create the background from the background image using the mask1
    res2 = cv2.bitwise_and(background, background, mask=mask1)
    
    # Combine the two results to get the final output
    final_output = cv2.addWeighted(res1, 1, res2, 1, 0)
    
    # Display the output
    cv2.imshow("Invisibility Cloak", final_output)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and destroy all windows
cap.release()
cv2.destroyAllWindows()
