import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_face_mesh = mp.solutions.face_mesh

# For static images:
IMAGE_FILES = [r'C:\Users\dell\Desktop\pythonProject\IMG.jpg']
OUTPUT_FILE = r'C:\Users\dell\Desktop\pythonProject\OUTPUT.txt'
OUTPUT_IMAGE = r'C:\Users\dell\Desktop\pythonProject\OUTPUT.jpg'
drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)

with mp_face_mesh.FaceMesh(
        static_image_mode=True,
        max_num_faces=1,
        refine_landmarks=True,
        min_detection_confidence=0.5) as face_mesh:
    for idx, file in enumerate(IMAGE_FILES):
        image = cv2.imread(file)
        output_file = open(OUTPUT_FILE, 'w')
        # Convert the BGR image to RGB before processing.
        results = face_mesh.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

        # Print and draw face mesh landmarks on the image.
        if not results.multi_face_landmarks:
            continue
        annotated_image = image.copy()
        for face_landmarks in results.multi_face_landmarks:
            print(face_landmarks, file=output_file)
            mp_drawing.draw_landmarks(
                image=annotated_image,
                landmark_list=face_landmarks,
                connections=mp_face_mesh.FACEMESH_TESSELATION,
                landmark_drawing_spec=drawing_spec,
                connection_drawing_spec=mp_drawing_styles
                .get_default_face_mesh_tesselation_style())
            mp_drawing.draw_landmarks(
                image=annotated_image,
                landmark_list=face_landmarks,
                connections=mp_face_mesh.FACEMESH_CONTOURS,
                landmark_drawing_spec=drawing_spec,
                connection_drawing_spec=mp_drawing_styles
                .get_default_face_mesh_contours_style())
            mp_drawing.draw_landmarks(
                image=annotated_image,
                landmark_list=face_landmarks,
                connections=mp_face_mesh.FACEMESH_IRISES,
                landmark_drawing_spec=drawing_spec,
                connection_drawing_spec=mp_drawing_styles
                .get_default_face_mesh_iris_connections_style())
        cv2.imwrite(OUTPUT_IMAGE, annotated_image)
    """
    mp_drawing.plot_landmarks(face_landmarks, mp_face_mesh.FACEMESH_TESSELATION)
    mp_drawing.plot_landmarks(face_landmarks, mp_face_mesh.FACEMESH_CONTOURS)
    mp_drawing.plot_landmarks(face_landmarks, mp_face_mesh.FACEMESH_IRISES)
    """
