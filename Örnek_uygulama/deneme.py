import cv2
import numpy as np
from pathlib import Path
import argparse
from boxmot import BoTSORT
from ultralytics import YOLO

class ObjectTracker:
    def __init__(self, yolo_model_path, conf, reid_model_path, video_source, tracker_type='botsort'):
        self.detector = YOLOv8Detector(yolo_model_path, conf)
        self.tracker = self.initialize_tracker(tracker_type, reid_model_path)
        self.video_source = video_source

    def initialize_tracker(self, tracker_type, reid_model_path):
        if tracker_type.lower() == 'botsort':
            return BoTSORT(model_weights=Path(reid_model_path), device='cpu', fp16=False)
        else:
            raise ValueError(f"Unknown tracker type: {tracker_type}")

    def run(self):
        vid = cv2.VideoCapture(self.video_source)
        fps = vid.get(cv2.CAP_PROP_FPS)

        while True:
            ret, im = vid.read()
            if not ret:
                break

            # Nesnelerin tespiti
            dets = self.detector.detect_objects(im)

            # Nesne takibi güncelleniyor
            tracked_objects = self.tracker.update(dets, im)

            # Takip sonuçları çiziliyor
            annotated_frame = visualize_tracking_results(im, tracked_objects)

            # Sonuçlar ekranda gösteriliyor
            cv2.imshow('Object Tracking', annotated_frame)

            # q veya space tuşuna basıldığında döngüyü kır
            key = cv2.waitKey(1) & 0xFF
            if key == ord(' ') or key == ord('q'):
                break

        # Video yakalama serbest bırakılıyor
        vid.release()
        # Ekran pencereleri kapatılıyor
        cv2.destroyAllWindows()

class YOLOv8Detector:
    def __init__(self, model_path, conf=0.8):
        self.model = YOLO(model_path)
        self.conf = conf

    def detect_objects(self, frame):
        detections = self._yolo_inference(frame)
        return np.array(detections).reshape(-1, 6)

    def _yolo_inference(self, frame):
        results = self.model(frame)
        boxes = results[0].boxes.xyxy
        confidences = results[0].boxes.conf
        class_indices = results[0].boxes.cls
        detections = [(box[0].item(), box[1].item(), box[2].item(), box[3].item(), conf.item(), cls.item()) for
                      box, conf, cls in zip(boxes, confidences, class_indices) if conf.item() >= self.conf]
        return detections

def visualize_tracking_results(image, detections, trajectories=None):
    for det in detections:
        x_min, y_min, x_max, y_max, obj_id, conf = det[:6]
        cv2.rectangle(image, (int(x_min), int(y_min)), (int(x_max), int(y_max)), (0, 255, 0), 2)
        cv2.putText(image, f"ID: {int(obj_id)}, Conf: {conf:.2f}", (int(x_min), int(y_min) - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

    if trajectories is not None:
        for trajectory in trajectories:
            for i in range(len(trajectory) - 1):
                x1, y1 = int(trajectory[i][0]), int(trajectory[i][1])
                x2, y2 = int(trajectory[i + 1][0]), int(trajectory[i + 1][1])
                cv2.line(image, (x1, y1), (x2, y2), (255, 0, 0), 2)

    return image

def parse_args():
    parser = argparse.ArgumentParser(description="Object Tracking with YOLOv8 and BoTSORT")
    parser.add_argument('--yolo-model', type=str, required=True, help='Path to the YOLOv8 model file.')
    parser.add_argument('--conf', type=float, default=0.5, help='Confidence threshold for YOLO detection.')
    parser.add_argument('--reid-model', type=str, required=True, help='Path to the ReID model file.')
    parser.add_argument('--video-source', type=str, required=True, help='Path to the video file or camera index.')
    parser.add_argument('--tracker', type=str, default='botsort', help='Type of tracker to use (default: botsort).')
    return parser.parse_args()

def main():
    args = parse_args()
    tracker = ObjectTracker(args.yolo_model, args.conf, args.reid_model, args.video_source, args.tracker)
    tracker.run()

if __name__ == "__main__":
    main()
# cmd commed : python object_tracking.py --yolo-model yolov8_sabitkanat.pt --conf 0.5 --reid-model osnet_x1_0_msmt17.pt --video-source ucus6_1.mp4 --tracker botsort