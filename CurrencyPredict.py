import cv2
from ultralytics import YOLO
import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed of speech


def give_voice_command(command):
    engine.say(command)
    engine.runAndWait()


model = YOLO('runs/detect/currency/weights/best.pt')  # Use YOLOv8n for better performance on smaller devices

# Define the class IDs for detection (Person, Bicycle, Car as examples)
class_ids = [0,1,2,3,4,5,6]  # Person, Bicycle, Car

# Class names for COCO dataset
class_names = ['10', '100', '20', '200', '2000', '50', '500']

# Open webcam (change to video path if using a video file)
cap = cv2.VideoCapture(0)  # Use 'video.mp4' or another file instead of 0 for videos
d10 = 0
d100 = 0
d20 = 0
d200 = 0
d2000 = 0
d50 = 0
d500 = 0


if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        break

    # Perform detection
    results = model(frame,conf=0.3)

    # Filter detections for the specified class IDs
    for result in results:
        for box in result.boxes:
            if int(box.cls) in class_ids:  # Check if the detected class is in the list
                class_id = int(box.cls)
                label = class_names[class_ids.index(class_id)]  # Get class label
                x1, y1, x2, y2 = map(int, box.xyxy[0])  # Bounding box coordinates
                confidence = box.conf.item()  # Convert tensor to float

                # Draw bounding box and label
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, f'{label} {confidence:.2f}', (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

                # Get frame dimensions
                #frame_width = frame.shape[1]

                frame_height, frame_width = frame.shape[:2]  # Ensure this gives correct dimensions
                frame_center_x = frame_width // 2

                bounding_box_center_x = (x1 + x2) // 2  # Center x-coordinate of the bounding box

                if label =='10':
                    d10 += 1


                    d100 = 0
                    d20 = 0
                    d200 = 0
                    d2000 = 0
                    d50 = 0
                    d500 = 0

                    if d10 == 20:
                        d10 = 0
                        give_voice_command("detected Currency  '" + label + "' Rupee.")

                if label =='100':
                    d100 += 1

                    d10 = 0

                    d20 = 0
                    d200 = 0
                    d2000 = 0
                    d50 = 0
                    d500 = 0
                    if d100 == 20:
                        d100= 0
                        give_voice_command("detected Currency  '" + label + "' Rupee.")

                if label =='20':
                    d20 += 1
                    d10 = 0
                    d100 = 0

                    d200 = 0
                    d2000 = 0
                    d50 = 0
                    d500 = 0
                    if d20 == 20:
                        d20 = 0
                        give_voice_command("detected Currency  '" + label + "' Rupee.")

                if label =='200':
                    d200 += 1

                    d10 = 0
                    d100 = 0
                    d20 = 0
                    d2000 = 0
                    d50 = 0
                    d500 = 0
                    if d200 == 20:
                        d200 = 0
                        give_voice_command("detected Currency  '" + label + "' Rupee.")

                if label =='2000':
                    d2000 += 1

                    d10 = 0
                    d100 = 0
                    d20 = 0
                    d200 = 0
                    d50 = 0
                    d500 = 0
                    if d2000 == 20:
                        d2000 = 0
                        give_voice_command("detected Currency  '" + label + "' Rupee.")

                if label =='50':
                    d50 += 1
                    d10 = 0
                    d100 = 0
                    d20 = 0
                    d200 = 0
                    d2000 = 0

                    d500 = 0
                    if d50 == 20:
                        d50 = 0
                        give_voice_command("detected Currency  '" + label + "' Rupee.")

                if label =='500':
                    d500 += 1
                    d10 = 0
                    d100 = 0
                    d20 = 0
                    d200 = 0
                    d2000 = 0
                    d50 = 0

                    if d500 == 20:
                        d500 = 0
                        give_voice_command("detected Currency  '" + label + "' Rupee.")









    # Show the frame
    cv2.imshow(' Detection', frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close windows
cap.release()
cv2.destroyAllWindows()

