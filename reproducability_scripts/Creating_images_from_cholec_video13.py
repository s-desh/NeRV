# #Creating video
# import cv2
# import os


# #for manipulating the number of frames and sequentiality change "max_frames" and "frame_count" accordingly
# def convert_video_to_png(video_path, output_dir, max_frames=100):
#     # Create output directory if it doesn't exist
#     os.makedirs(output_dir, exist_ok=True)

#     # Open the video file
#     cap = cv2.VideoCapture(video_path)
#     if not cap.isOpened():
#         print("Error: Could not open video file.")
#         return

#     # Read frames from the video and save them as PNG images
#     frame_count = 0
#     while frame_count < max_frames:
#         ret, frame = cap.read()
#         if not ret:
#             break

#         # Save frame as PNG image
#         frame_filename = os.path.join(output_dir, f"frame_{frame_count:04d}.png")
#         cv2.imwrite(frame_filename, frame)
#         print(frame_count)
#         frame_count += 1

#     # Release the video capture object
#     cap.release()
#     print(f"Conversion complete. {frame_count} PNG images saved to {output_dir}.")

# # Example usage:
# video_path = "video13.mp4"
# output_dir = "cholec80_13_every_2_frame"
# convert_video_to_png(video_path, output_dir, max_frames=100)

import cv2
import os

def convert_video_to_png(video_path, output_dir, max_frames=100):
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Open the video file
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Could not open video file.")
        return

    # Get the total number of frames in the video
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Calculate the skip interval
    skip_interval = 2

    # Read frames from the video and save every second frame as PNG images
    frame_count = 0
    current_frame = 0
    while frame_count < max_frames and current_frame < total_frames:
        ret, frame = cap.read()
        if not ret:
            break

        # Save frame as PNG image
        frame_filename = os.path.join(output_dir, f"frame_{frame_count:04d}.png")
        cv2.imwrite(frame_filename, frame)

        frame_count += 1
        current_frame += skip_interval

        # Move to the next frame to be read
        cap.set(cv2.CAP_PROP_POS_FRAMES, current_frame)

    # Release the video capture object
    cap.release()
    print(f"Conversion complete. {frame_count} PNG images saved to {output_dir}.")

# Example usage:
video_path = "video13.mp4"
output_dir = "cholec80_13_every_2_frame"
convert_video_to_png(video_path, output_dir, max_frames=100)



