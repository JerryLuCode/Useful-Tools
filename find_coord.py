"""
Image Viewer and Coordinate Marker

This script allows users to view an image, optionally resize it, mark coordinates with mouse clicks,
and save the marked image.

Usage:
    python3 find_coord.py <image_path> [--resize] [--ratio RATIO]

Arguments:
    image_path          Path to the image file
    --resize            Optional flag to resize the image
    --ratio RATIO       Resize ratio (default: 0.5)

Controls:
    Left Mouse Click    Mark a point on the image
    's' key             Save the current marked image
    'q' key             Quit the program

Examples:
    1. View original image:
       python3 find_coord.py path/to/image.jpg

    2. View resized image (50% of original size):
       python3 find_coord.py path/to/image.jpg --resize

    3. View resized image with custom ratio (75% of original size):
       python3 find_coord.py path/to/image.jpg --resize --ratio 0.75

Note: Coordinates displayed are always relative to the original image size.
"""

import cv2
import sys
import argparse
import os

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        # Scale coordinates back to original image size if resized
        if args.resize:
            orig_x = int(x / args.ratio)
            orig_y = int(y / args.ratio)
        else:
            orig_x, orig_y = x, y

        cv2.circle(display_image, (x, y), 5, (0, 0, 255), -1)
        cv2.putText(display_image, f"({orig_x}, {orig_y})", (x, y), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        cv2.imshow("Image", display_image)

def save_image():
    base_name = os.path.splitext(os.path.basename(args.image_path))[0]
    save_path = f"{base_name}_marked.jpg"
    cv2.imwrite(save_path, display_image)
    print(f"Image saved as {save_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Display image and capture click coordinates.")
    parser.add_argument("image_path", help="Path to the image file")
    parser.add_argument("--resize", action="store_true", help="Resize the image")
    parser.add_argument("--ratio", type=float, default=0.5, help="Resize ratio (default: 0.5)")
    args = parser.parse_args()

    image = cv2.imread(args.image_path)
    if image is None:
        sys.exit("Error: Unable to load image.")

    height, width = image.shape[:2]

    if args.resize:
        new_width = int(width * args.ratio)
        new_height = int(height * args.ratio)
        display_image = cv2.resize(image, (new_width, new_height))
    else:
        display_image = image.copy()

    cv2.imshow("Image", display_image)
    cv2.setMouseCallback("Image", click_event)

    while True:
        key = cv2.waitKey(1) & 0xFF
        if key == ord('s'):
            save_image()
        elif key == ord('q'):
            break

    cv2.destroyAllWindows()
