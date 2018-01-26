import cv2
import face_recognition

video_capture = cv2.VideoCapture(0)

names = ["catherine","william",]
images = []
for name in names:
	filename = name +".jpg"
	image = face_recognition.load_image_file(filename)
	images.append(image)

#unknown_image = face_recognition.load_image_file("unknown.jpg")
ret, frame = video_capture.read()
face_encodings = []

for image in images:
	encoding = face_recognition.face_encodings(image)[0]
	face_encodings.append(encoding)
#unknown_face_encodings = face_recognition.face_encodings(unknown_image)
video_encodings = face_recognition.face_encodings(frame)

#face_locations = face_recognition.face_locations(unknown_image)
face_locations = face_recognition.face_locations(frame)

for i in range(len(video_encodings)):
	#video_encoding = unknown_face_encodings[i]
	video_encoding = video_encodings[i]
#for i in range(len(unknown_face_encodings)):
	#unknown_encoding = unknown_face_encodings[i]
	face_location = face_locations[i]
	top, right, bottom, left = face_location
	cv2.rectangle(frame, (left,top), (right, bottom), (0, 255,0), 2)
	results = face_recognition.compare_faces(face_encodings, video_encoding)
	#cv2.rectangle(unknown_image, (left,top), (right, bottom), (0, 255,0), 2)
	#results = face_recognition.compare_faces(face_encodings, unknown_encoding)

	for j in range(len(results)):
		if results[j]:
			name = names[j]
			cv2.putText(frame, name, (left - 10, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
			#unknown_image_rgb = cv2.cvtColor(unknown_image, cv2.COLOR_BGR2RGB)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
			
	#cv2.imshow('Video', frame_rgb)
	
#cv2.imshow("Output", unknown_image_rgb)
# Release handle to the webcam
cv2.imshow('Video', frame_rgb)
video_capture.release()
cv2.destroyAllWindows()