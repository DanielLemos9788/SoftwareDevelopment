from cv2 import *
import face_recognition as fr

# Upload Images
control_picture = fr.load_image_file('FotoA.jpg')
trial_picture = fr.load_image_file('FotoB.jpg')

# Pictures to RGB
control_picture = cv2.cvtColor(control_picture, cv2.COLOR_BGR2RGB)
trial_picture = cv2.cvtColor(trial_picture, cv2.COLOR_BGR2RGB)

# Show Images
cv2.imshow('Control Picture', control_picture)
cv2.imshow('Trial Picture', trial_picture)

# Keep the Image Alive
cv2.waitKey(0)




