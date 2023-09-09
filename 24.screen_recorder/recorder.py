import cv2
import pyautogui
import numpy as np

screen_size = (1920, 1080)  # Set the screen size according to your needs
output_file = 'screen_recording.mp4'  # Set the output file name
fps = 30  # Set the frames per second for the recording

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_file, fourcc, fps, screen_size)

while True:
       # Capture the screen frame
       img = pyautogui.screenshot()
       frame = np.array(img)

       # Convert the frame color from BGR to RGB
       frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

       # Write the frame to the output file
       out.write(frame)

       # Display the resulting frame (optional)
       cv2.imshow('Screen Recording', frame)

       # Stop the recording when 'q' is pressed
       if cv2.waitKey(1) == ord('q'):
           break
       
out.release()
cv2.destroyAllWindows()