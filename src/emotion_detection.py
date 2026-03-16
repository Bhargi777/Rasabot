import cv2
from fer.fer import FER

class EmotionDetection:
    def __init__(self):
        self.emotion_detector = FER(mtcnn=True)

    def detect_emotion(self):
        cap = cv2.VideoCapture(0)
        _, frame = cap.read()
        cap.release()

        result = self.emotion_detector.detect_emotions(frame)
        if result:
            emotion = max(result[0]['emotions'], key=result[0]['emotions'].get)
            return emotion
        return None