import tkinter as tk
import mediapipe as mp
import cv2
from PIL import Image, ImageTk

def create_gui():
    # Create the main window
    main_window_instance = tk.Tk()
    main_window_instance.title("iFrame")
    main_window_instance.geometry("1000x500")
    main_window_instance.resizable(False, False)

    # Label for the viewing window
    label_1 = tk.Label(main_window_instance, text=" Viewing window:", fg="red")
    label_1.pack(anchor="w")

    # Canvas for displaying video frames
    canvas_form = tk.Canvas(main_window_instance, width="750", height="450", bd=1, relief="raised", highlightbackground="blue", highlightthickness=2, bg="gray")
    canvas_form.pack(anchor="w", padx=5)

    # Button to start video streaming
    button_start = tk.Button(main_window_instance, text="Start", command=start_video_flow)
    button_start.pack()

    # Status bar with information about the program
    status_bar = tk.Label(main_window_instance, bd=1, text=" The program is in beta mode. In general, it works, but there are drawbacks.", relief=tk.SUNKEN, anchor=tk.W, fg="blue")
    status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    return main_window_instance, canvas_form

def start_video_flow():
    global flow_pictures
    # Start video streaming if not already running
    if 'flow_pictures' not in globals() or not flow_pictures.isOpened():
        flow_pictures = cv2.VideoCapture(url)
        update()

def click_mouse(event):
    # Trigger video streaming on mouse click
    start_video_flow()

def update():
    if 'flow_pictures' in globals() and flow_pictures.isOpened():
        # Read a frame from the video stream
        ret, frame = flow_pictures.read()

        # Convert and resize the frame for display
        format_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        format_rgb = cv2.resize(format_rgb, (750, 450))
        images = Image.fromarray(format_rgb)
        images_tkinter = ImageTk.PhotoImage(image=images)

        # Display the frame on the Canvas
        canvas_form.img = images_tkinter
        canvas_form.create_image(canvas_form.winfo_width() // 2, canvas_form.winfo_height() // 2, anchor=tk.CENTER, image=images_tkinter)

        # Update the main window after a delay
        main_window_instance.after(10, update)

# URL for the video stream
url = "http://192.168.1.127:4747/video"

# Create the GUI components
main_window_instance, canvas_form = create_gui()

# Bind the mouse click event to start video streaming
canvas_form.bind("<Button-1>", click_mouse)

# Run the Tkinter main loop
main_window_instance.mainloop()
