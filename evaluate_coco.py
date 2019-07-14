# this script uses python 2.7
import sys
sys.path.append("/home/ubuntu/cocoapi/PythonAPI")

import matplotlib.pyplot as plt
from pycocotools.coco import COCO
from pycocotools.cocoeval import COCOeval
import numpy as np
import skimage.io as io
import pylab
pylab.rcParams['figure.figsize'] = (10.0, 8.0)

annType = ['segm','bbox','keypoints']
annType = annType[1]      #specify type here
prefix = 'person_keypoints' if annType=='keypoints' else 'instances'
print 'Running demo for *%s* results.'%(annType)


#initialize COCO ground truth api
#dataDir='../'
#dataType='val2014'
annFile = '/media/sdf/COCO/2014/annotations/instances_val2014.json'
#annFile = '/media/sdf/COCO/2014/annotations/instances_minival2014.json'
cocoGt=COCO(annFile)

#initialize COCO detections api
resFile='/home/ubuntu/yolo-v3/results/coco.json'
# resFile = resFile%(dataDir, prefix, dataType, annType)
cocoDt=cocoGt.loadRes(resFile)

# imgIds=sorted(cocoGt.getImgIds())
# imgIds=imgIds[0:100]
# imgId = imgIds[np.random.randint(100)]

import json
dts = json.load(open(resFile,'r'))
imgIds = [imid["image_id"] for imid in dts]
imgIds = sorted(list(set(imgIds)))
del dts
# print(imgIds)

# running evaluation
cocoEval = COCOeval(cocoGt,cocoDt,annType)
cocoEval.params.imgIds  = imgIds
cocoEval.evaluate()
cocoEval.accumulate()
cocoEval.summarize()
