import cv2
import mediapipe as mp

mp_selfie_segmentation = mp.solutions.selfie_segmentation
segment = mp_selfie_segmentation.SelfieSegmentation(model_selection=1)

cap = cv2.VideoCapture('test.mov')
bg_image = cv2.imread('test_bg.jpeg')

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    
    frame = cv2.resize(frame, (640, 480))
    bg_image_resized = cv2.resize(bg_image, (640, 480))
    
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = segment.process(rgb_frame)
    
    mask = results.segmentation_mask > 0.5
    mask = mask.astype("uint8") * 255
    
    mask_imv = cv2.bitwise_not(mask)
    fg = cv2.bitwise_and(frame, frame, mask=mask)
    bg = cv2.bitwise_and(bg_image_resized, bg_image_resized, mask=mask_imv)
    output = cv2.add(fg, bg)
    
    cv2.imshow('Output',output)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()