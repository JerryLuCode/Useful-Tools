"""
Video Frame Extractor

This script extracts a specific frame from a video file based on the given time and saves it as an image.

Usage:
    python3 get_frame.py -v VIDEO_PATH -t TIME_IN_SECONDS [-o OUTPUT_DIRECTORY]

Arguments:
    -v, --video VIDEO_PATH      Path to the input video file
    -t, --time TIME_IN_SECONDS  Time in seconds at which to extract the frame
    -o, --output OUTPUT_DIRECTORY   Directory to save the extracted frame (default: current directory)

Example:
    1. Extract frame at 41 seconds and save in the current directory:
       python3 get_frame.py -v path/to/video.mp4 -t 41

    2. Extract frame at 30 seconds and save in a specific directory:
       python3 get_frame.py -v path/to/video.mp4 -t 30 -o path/to/save/directory

Note: Ensure the specified time is within the duration of the video.
"""

import cv2
import argparse
import os

def extract_frame(video_path, desired_time, output_dir):
    video = cv2.VideoCapture(video_path)

    if not video.isOpened():
        raise IOError(f"Error: Could not open video {video_path}")

    fps = video.get(cv2.CAP_PROP_FPS)
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

    frame_number = int(fps * desired_time)

    if frame_number >= total_frames:
        raise ValueError(f"Error: The video is shorter than {desired_time} seconds.")

    video.set(cv2.CAP_PROP_POS_FRAMES, frame_number)

    ret, frame = video.read()
    if not ret:
        raise IOError(f"Error: Could not read frame at {desired_time} seconds.")

    output_image_path = os.path.join(output_dir, f'frame_at_{desired_time}s.jpg')
    cv2.imwrite(output_image_path, frame)

    video.release()

    return output_image_path

def main():
    parser = argparse.ArgumentParser(description="Extract a frame from a video at a specified time.")
    parser.add_argument("-v", "--video", required=True, help="Path to the input video file")
    parser.add_argument("-t", "--time", type=int, required=True, help="Time in seconds at which to extract the frame")
    parser.add_argument("-o", "--output", default=".", help="Directory to save the extracted frame (default: current directory)")
    args = parser.parse_args()

    if not os.path.exists(args.output):
        os.makedirs(args.output)

    try:
        output_path = extract_frame(args.video, args.time, args.output)
        print(f"Frame at {args.time} seconds saved as {output_path}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
