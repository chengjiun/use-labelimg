conda activate labelImg-tools
# train epoch 1
cd yolov5
# python train.py --img 640 --batch 12 --epochs 60 --data ../yolov5-img1.yaml --weights yolov5l.pt --device 0,1 --quad
# mv runs/train/exp runs/train/img1-v5l-1

# train epoch 2
python train.py --img 640 --batch 12 --epochs 60 --data ../yolov5-img2.yaml --weights runs/train/img1-v5l-1/weights/best.pt --device 0 --quad
mv runs/train/exp runs/train/img2-v5l-2

cd ../
