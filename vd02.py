import cv2

def play_video():
    cap = cv2.VideoCapture(0)
    speed_factor = 1.0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow("Webcam", frame)

        key = cv2.waitKey(int(30 / speed_factor)) & 0xFF

        if key == ord('+'):
            speed_factor += 0.5
        elif key == ord('-'):
            speed_factor = max(0.5, speed_factor - 0.5)
        elif key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

play_video()
