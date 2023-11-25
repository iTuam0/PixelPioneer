import tkinter as tk
import mediapipe as mp
import cv2
from PIL import Image, ImageTk

#Start;
def main_window():
      #Basic form;
      main_window = tk.Tk()
      main_window.title("iFrame")

      #Form size;
      main_window.geometry("1000x500")
      main_window.resizable(False, False)

      #Label;
      label_1 = tk.Label(main_window, text=" Viewing window:", fg="red")
      label_1.pack(anchor="w")

      #Convas;
      canvas_form = tk.Canvas(main_window, width="750", height="450", bd=1, relief="raised", highlightbackground="blue", highlightthickness=2)
      canvas_form.pack(anchor="w", padx=5)

      #Create a url with the id from the camera;
      url = "http://192.168.1.127:4747/video"

      #Initialization of mediapipe modules;
      m_faceD = mp.solutions.face_detection
      m_draw = mp.solutions.drawing_utils
      f_detection = m_faceD.FaceDetection()

      #Open the stream coming from the url;
      flow_pictures = cv2.VideoCapture(url)

      #Status bar;
      status_bar = tk.Label(main_window, bd=1, text=" The program is in beta mode. In general it works, but there are drawbacks.", relief=tk.SUNKEN, anchor=tk.W, fg="blue")
      status_bar.pack(side = tk.BOTTOM, fill=tk.X)

      #We'll spam you with updates;
      def update():
            #Reading a stream;
            ret, frame = flow_pictures.read()

            #Convert in from Tkinter-format;
            format_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            format_rgb = cv2.resize(format_rgb, (750, 450))
            images = Image.fromarray(format_rgb)
            images_tkinter_F = ImageTk.PhotoImage(image=images)

            #Displaying an image on Canvas;
            images = Image.fromarray(format_rgb)
            images_tkinter_F = ImageTk.PhotoImage(image=images)

            canvas_form.img = images_tkinter_F
            canvas_form.create_image(canvas_form.winfo_width() // 2, canvas_form.winfo_height() // 2, anchor=tk.CENTER, image=images_tkinter_F)
            
            #Update main_window;
            main_window.after(10, update)

      update()
      
      #End of main_form cycle;
      main_window.mainloop()
#View;
main_window()
