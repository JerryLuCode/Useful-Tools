"""
Camera Capture and Image Saver

This script allows users to capture images from a camera and save them to a specified directory.

Usage:
    python3 image_capture.py [-c CAMERA_INDEX] [-s SAVE_DIRECTORY]

Arguments:
    -c CAMERA_INDEX   Camera index to use (default: 0)
    -s SAVE_DIRECTORY   Directory to save captured images (default: './images')

Controls:
    's' key     Save the current frame as an image
    'q' key     Quit the program

Examples:
    1. Use default camera and save location:
       python3 image_capture.py

    2. Use a specific camera (e.g., camera index 1):
       python3 image_capture.py -c 1

    3. Specify a custom save directory:
       python3 image_capture.py -s my_captures

    4. Use a specific camera and custom save directory:
       python3 image_capture.py -c 2 -s custom_folder

Note: Ensure the specified camera is available on your system.
"""

import cv2
import os
import argparse

def capture_and_save_images(camera_index, save_dir):
    cap = cv2.VideoCapture(camera_index)

    if not cap.isOpened():
        raise IOError(f"Error: Could not open camera {camera_index}.")

    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    img_counter = 1

    print("Press 's' to save an image, 'q' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Can't receive frame. Exiting ...")
            break

        cv2.imshow('Camera', frame)

        key = cv2.waitKey(1) & 0xFF

        if key == ord('s'):
            img_name = os.path.join(save_dir, f"{img_counter:02d}.jpg")
            cv2.imwrite(img_name, frame)
            print(f"{img_name} saved!")
            img_counter += 1
        elif key == ord('q'):
            print("Quitting...")
            break

    cap.release()
    cv2.destroyAllWindows()

def main():
    parser = argparse.ArgumentParser(description="Capture images from camera and save them.")
    parser.add_argument("-c", "--camera", type=int, default=0, help="Camera index to use (default: 0)")
    parser.add_argument("-s", "--save_dir", type=str, default="./images", help="Directory to save captured images (default: 'images')")
    args = parser.parse_args()

    try:
        capture_and_save_images(args.camera, args.save_dir)
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
