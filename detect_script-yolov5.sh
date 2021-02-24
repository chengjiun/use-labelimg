# conda env pytorch17
conda activate labelImg-tools
# prelabel - epoch1
#CUDA_VISIBLE_DEVICES=0 python detect.py --source data/samples/ --weights yolov5m.pt --conf 0.5 --save-txt
# for testing
# CUDA_VISIBLE_DEVICES=0 python detect.py --source ../data/val1-test/ --weights runs/train/exp/weights/best.pt --save-txt

# prelabel - epoch2
# MODEL_DIR='./runs/train/img1-v5l-1/weights'
# CUDA_VISIBLE_DEVICES=0 python detect.py --source data/samples/ --weights $MODEL_DIR/best.pt --conf 0.5 --save-txt --project ../data/ --name samples-train1

MODEL_DIR='./runs/train/img2-v5l-2/weights'
CUDA_VISIBLE_DEVICES=0 python detect.py --source data/samples/ --weights $MODEL_DIR/best.pt --conf 0.5 --save-txt --project ../data/ --name   samples-train2

