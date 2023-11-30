import tkinter as tk
import mediapipe as mp
import cv2
from PIL import Image, ImageTk

def create_gui():
    main_window_instance = tk.Tk()
    main_window_instance.title("iFrame")
    main_window_instance.geometry("1000x500")
    main_window_instance.resizable(False, False)

    label_1 = tk.Label(main_window_instance, text=" Viewing window:", fg="red")
    label_1.pack(anchor="w")

    canvas_form = tk.Canvas(main_window_instance, width="750", height="450", bd=1, relief="raised", highlightbackground="blue", highlightthickness=2, bg="gray")
    canvas_form.pack(anchor="w", padx=5)

    button_start = tk.Button(main_window_instance, text="Start", command=start_video_flow)
    button_start.pack()

    status_bar = tk.Label(main_window_instance, bd=1, text=" The program is in beta mode. In general it works, but there are drawbacks.", relief=tk.SUNKEN, anchor=tk.W, fg="blue")
    status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    return main_window_instance, canvas_form

def start_video_flow():
    global flow_pictures
    if 'flow_pictures' not in globals() or not flow_pictures.isOpened():
        flow_pictures = cv2.VideoCapture(url)
        update()

def click_mouse(event):
    start_video_flow()

def update():
    if 'flow_pictures' in globals() and flow_pictures.isOpened():
        ret, frame = flow_pictures.read()
        format_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        format_rgb = cv2.resize(format_rgb, (750, 450))
        images = Image.fromarray(format_rgb)
        images_tkinter = ImageTk.PhotoImage(image=images)

        canvas_form.img = images_tkinter
        canvas_form.create_image(canvas_form.winfo_width() // 2, canvas_form.winfo_height() // 2, anchor=tk.CENTER, image=images_tkinter)

        main_window_instance.after(10, update)

url = "http://192.168.1.127:4747/video"
main_window_instance, canvas_form = create_gui()
canvas_form.bind("<Button-1>", click_mouse)
main_window_instance.mainloop()
