import cv2
import os

def video_to_selected_images(video_path, output_folder, frame_interval=10):
    # Check if video file exists
    if not os.path.isfile(video_path):
        print(f"Error: Video file '{video_path}' not found.")
        return

    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Open the video file
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error: Could not open video '{video_path}'.")
        return

    # Initialize counters
    frame_count = 0
    saved_count = 0

    # Read frames in a loop
    while True:
        ret, frame = cap.read()  # Read a frame
        if not ret:
            print("Reached the end of the video or encountered a read error.")
            break

        # Save every 'frame_interval' frame as an image
        if frame_count % frame_interval == 0:
            frame_path = os.path.join(output_folder, f"frame_{frame_count:04d}.jpg")
            cv2.imwrite(frame_path, frame)
            saved_count += 1
            print(f"Saved frame {frame_count} as '{frame_path}'")

        frame_count += 1

    # Release resources
    cap.release()
    print(f"Conversion complete. {saved_count} frames saved in '{output_folder}'.")

# Example usage:
video_to_selected_images("SampleVideo_1280x720_5mb.mp4", "output_images", frame_interval=10)
