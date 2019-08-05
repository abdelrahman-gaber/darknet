# coco
#./darknet detector train cfg/coco-train.data cfg/yolov3-tiny-train.cfg models/yolov3-tiny.conv.15 | tee "backup/yolov3-tiny-coco.log" 


# wider
#./darknet detector train cfg/wider-train.data cfg/yolov3-tiny-wider-train.cfg models/yolov3-tiny.conv.15 | tee "backup_wider/yolov3-tiny-wider.log"

./darknet detector train cfg/wider-train.data cfg/face-det/Tiny-Yolov3-A-wider-train.cfg models/yolov3-tiny.conv.15 | tee "backup-face-det/Tiny-Yolov3-A-wider/Tiny-Yolov3-A-wider.log"


