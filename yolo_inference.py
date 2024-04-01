from ultralytics import YOLO

# importing specific YOLO model
# (yolov8x) is the latest model you can use right now
# argument to yolo is the model that you want to use (can use custom model from .pt file)
# model = YOLO('models/yolov5s_last.pt')
model = YOLO('yolov8x')

# run model on image
# outputs a folder with the prediction of objects in the image with their confidence score
# objects have: 1. boundary box 2. label 3. confidence score

# PREDICT THE OBJECTS PER FRAME
# result = model.predict('input_videos/impage.png', save=True)

# TRACK the objects per frame (gives each object an ID)
# output folder is in /run/detect/track
# result = model.track('input_videos/input_video.mp4', save=True)

# result = model.predict('input_videos/input_video.mp4', conf=0.2 ,save=True)

result = model.predict('input_videos/image.png', conf=0.2 ,save=True)

# predicting result stored in a list of data
print(result)
# printing boundary boxes:
print("boxes: ")
for box in result[0].boxes:
    print(box)


# goal fine tune a the YOLO model to detect SPECIFIC objects better (in this case point out the tennis ball better)
