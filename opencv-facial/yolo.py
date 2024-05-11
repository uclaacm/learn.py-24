import cv2
import numpy as np

# Load the YOLOv3 model and its configuration and weights files
net = cv2.dnn.readNetFromDarknet("yolov3.cfg", 'yolov3.weights')

# Load the class labels file
classes = []
with open('coco.names', 'r') as f:
    classes = [line.strip() for line in f.readlines()]

# Set the input and output layers of the network
output_layers = net.getUnconnectedOutLayersNames()
input_layer = net.getLayerNames()[0]

# Load an image file
img = cv2.imread('image.jpg')

# Resize the image to the input size of the network
blob = cv2.dnn.blobFromImage(img, scalefactor=1/255.0, size=(416, 416), swapRB=True, crop=False)

# Set the input to the network
net.setInput(blob)

# Forward pass through the network to get the output
outputs = net.forward(output_layers)

# Process the output to get the bounding boxes, class IDs, and confidence scores
boxes = []
class_ids = []
confidences = []
for output in outputs:
  for detection in output:
    scores = detection[5:]
    class_id = np.argmax(scores)
    confidence = scores[class_id]
    if confidence > 0.5:
       center_x = int(detection[0] * img.shape[1])
       center_y = int(detection[1] * img.shape[0])
       width = int(detection[2] * img.shape[1])
       height = int(detection[3] * img.shape[0])
       left = int(center_x - width/2)
       top = int(center_y - height/2)
       boxes.append([left, top, width, height])
       class_ids.append(class_id)
       confidences.append(float(confidence))

# Apply non-max suppression to remove overlapping bounding boxes
indices = cv2.dnn.NMSBoxes(boxes, confidences, score_threshold=0.5, nms_threshold=0.4)

# Draw the bounding boxes and class labels on the image
colors = np.random.uniform(0, 255, size=(len(classes), 3))
for i in indices.flatten():
  x, y, w, h = boxes[i]
  label = classes[class_ids[i]]
  confidence = max(confidences)

  # Draw the bounding box
  color = colors[class_ids[i]]
  cv2.rectangle(img, (x, y), (x+w, y+h), color, thickness=2)

  # Draw the class label and confidence score
  label = f"{label}: {confidence:.2f}"
  cv2.putText(img, label, (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, thickness=2)

# Show the result
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
