./darknet detector valid cfg/coco-train.data cfg/yolov3-tiny.cfg models/yolov3-tiny.weights -out coco -thresh 0.001

#./darknet detector valid cfg/coco-train.data cfg/yolov3-tiny.cfg backup/yolov3-tiny-train_400000.weights -out coco -thresh 0.001

python evaluate_coco.py

