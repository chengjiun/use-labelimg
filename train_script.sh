conda activate labelImg-tools
# train epoch 1
# python yolov5/train.py --img 640 --batch 12 --epochs 60 --data yolov5-img1.yaml --weights yolov5l.pt --device 0,1 --quad
# mv yolov5/runs/train/exp yolov5/runs/train/img1-v5l-1

# train epoch 2
python yolov5/train.py --img 640 --batch 12 --epochs 60 --data yolov5-img2.yaml --weights yolov5/runs/train/img1-v5l-1/weights/best.pt --device 0 --quad
mv yolov5/runs/train/exp yolov5/runs/train/img2-v5l-2
