import cv2

def play_video(video_path,speed=1):
    cap = cv2.VideoCapture("C:/Users/ACER/Downloads/11700405-uhd_3840_2160_30fps.mp4")

    if not cap.isOpened():
        print("Cannot open video")
        return

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        cv2.imshow("Video", frame)

        # Higher speed -> smaller delay -> faster playback
        if cv2.waitKey(int(30 / speed)) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Normal speed
play_video("video.mp4", 1)

# Fast playback
# play_video("video.mp4", 2)

# Slow playback
# play_video("video.mp4", 0.5)
