from cv2 import cv2
import face_recognition as fr

# Upload Images
control_picture = fr.load_image_file('FotoA.jpg')
trial_picture = fr.load_image_file('FotoB.jpg')

# Pictures to RGB
control_picture = cv2.cvtColor(control_picture, cv2.COLOR_BGR2RGB)
trial_picture = cv2.cvtColor(trial_picture, cv2.COLOR_BGR2RGB)

# Location Control Face
location_face_A = fr.face_locations(control_picture)[0]
processed_face_A = fr.face_encodings(control_picture)[0]

# Location Trial Face
location_face_B = fr.face_locations(trial_picture)[0]
processed_face_B = fr.face_encodings(trial_picture)[0]

# Show Rectangle on Face
cv2.rectangle(control_picture,
              (location_face_A[3], location_face_A[0]),
              (location_face_A[1], location_face_A[2]),
              (0, 255, 0),
              2)

cv2.rectangle(trial_picture,
              (location_face_B[3], location_face_B[0]),
              (location_face_B[1], location_face_B[2]),
              (0, 255, 0),
              2)

# Show Images
cv2.imshow('Control Picture', control_picture)
cv2.imshow('Trial Picture', trial_picture)

# Keep the Image Alive
cv2.waitKey(0)




