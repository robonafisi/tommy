import cv2
from roboflow import Roboflow


def verify_pill_count(target_count):
    pills = 0

    cap = cv2.VideoCapture(0)

    rf = Roboflow(api_key="VFWvWxmvNhcfP4nYZgrm")
    project = rf.workspace().project("pill-detection-llp4r")
    model = project.version(3).model

    while True:
        ret, frame = cap.read()

        if not ret:
                print("Error: Could not read frame.")
                break

        grey = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        small_frame = cv2.resize(frame,dsize=(299,299), interpolation = cv2.INTER_CUBIC)
        print(pills)
        if len(model.predict(small_frame, confidence=40, overlap=30).json()['predictions']) == target_count:
            pills += 1
        else:
            pills = 0

        if pills >= 5:
            break

        cv2.imshow("output", small_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()