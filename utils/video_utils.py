import cv2 # read and save videos

# opens connection to the video and reads the video
def read_video(video_path):
    cap = cv2.VideoCapture(video_path)
    frames = []
    while True:
        # reads frame by frame of the video till there are no more frames
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)

    # closes the connection to the video
    cap.release()
    return frames

# Save video
def save_video(output_video_frames, output_video_path):
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    out = cv2.VideoWriter(output_video_path, fourcc, 24, (output_video_frames[0].shape[1], output_video_frames[0].shape[0]))
    for frame in output_video_frames:
        out.write(frame)
    out.release()