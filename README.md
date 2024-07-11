# Invisibility Cloak using Python and OpenCV

This Python script uses computer vision techniques with OpenCV to create an "invisibility cloak" effect, inspired by the concept from Harry Potter.

## Requirements

- Python 3.x
- OpenCV (`pip install opencv-python`)

## How it Works

The script captures video from your webcam and detects a specified color (blue by default) to create the invisibility effect:

1. **Capture Background**: The script captures a background image without the object (cloak) present.
   
2. **Detect Color**: It detects the specified color (blue in this case) in each frame of the video feed.

3. **Create Mask**: Using OpenCV, it creates a binary mask where the detected color appears as white (255) and everything else as black (0).

4. **Segmentation**: It segments the color (cloak) out of the frame using bitwise operations.

5. **Replace Background**: It replaces the segmented area with the previously captured background image, creating the illusion of invisibility.

## Usage

1. Clone this repository:
   git clone https://github.com/anigam075/Invisibility_cloak
   cd invisibility_cloak

2. Install dependencies:
    pip install opencv-python

3. Run the script:
    python main.py

4. To exit the program, press 'q' on the keyboard.

## Customization
Adjust Color Detection: Modify lower_blue and upper_blue values in invisibility_cloak.py to detect different shades of blue or other colors.

Improve Performance: Experiment with different morphological operations (like opening and dilation) to refine the mask and improve detection accuracy.

## Notes
Ensure good lighting conditions for better color detection and background segmentation.
The effectiveness of the invisibility effect may vary based on the cloth or object used.
Enjoy experimenting with your invisibility cloak script! 🧙‍♂️✨
