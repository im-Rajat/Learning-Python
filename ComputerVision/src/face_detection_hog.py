import dlib
import cv2


video_capture = cv2.VideoCapture(0)
flag = 0

face_detect = dlib.get_frontal_face_detector()

while True:

    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rects = face_detect(gray, 1)

    for (i, rect) in enumerate(rects):

        # (x, y, w, h) = face_utils.rect_to_bb(rect)
        x = rect.left()
        y = rect.top()
        w = rect.right() - x
        h = rect.bottom() - y

        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()