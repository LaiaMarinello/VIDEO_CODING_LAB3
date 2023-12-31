import tkinter as tk
from tkinter import filedialog
import threading
import os
from Converter import VideoConverter

def create_codec_comparison(input_file1, input_file2, output_file, resolution='720p'):
    # Combine videos side by side
    os.system(f'ffmpeg -i {input_file1} -i {input_file2} -filter_complex hstack=inputs=2 {output_file}')


# Convert button:
def convert_video():
    input_file = entry_path.get()
    conversion_option = var.get().split()[0]  # Extracting the codec from the option

    if not input_file or not conversion_option:
        status_label.config(text="Please fill in all fields.")
        return

    # Function to be executed in a separate thread
    def conversion_thread():
        input_directory, input_filename = os.path.split(input_file)
        custom_name = "converted_video" 
        output_format = "webm" if option == "libvpx (VP8)" in options else "mp4"  # Adjust the format based on the codec
        VideoConverter.convert_resolution_and_codec(input_file, input_directory, 1280, 720, conversion_option, custom_name, output_format) #Function of the other script
        root.after(0, lambda: status_label.config(text="Conversion successful!"))  # Update status_label in the main thread

    # Start the conversion in a separate thread
    threading.Thread(target=conversion_thread).start()

# Compare Button:
def compare_videos():
    input_file1 = entry_path1.get()
    input_file2 = entry_path2.get()
    resolution = resolution_var.get()

    # Output file path based on selected resolution
    output_file = f'comparison_{resolution}.mp4'

    # Call the video comparison function
    create_codec_comparison(input_file1, input_file2, output_file, resolution)
    status_label.config(text=f'Comparison video ({resolution}): {output_file}')

# GUI setup
root = tk.Tk()
root.title("Video Converter and Comparison")

# Input File
tk.Label(root, text="Input Video File:").pack(pady=5)
entry_path = tk.Entry(root, width=40)
entry_path.pack(pady=5)

# Conversion Options
tk.Label(root, text="Conversion Option:").pack(pady=5)
var = tk.StringVar()
var.set("output_resolution")  # Default option
options = ["libvpx (VP8)", "libvpx-vp9 (VP9)", "libx265 (H.265)"]
for option in options:
    tk.Radiobutton(root, text=option, variable=var, value=option).pack()

# Compare Videos Section
tk.Label(root, text="Compare Videos:").pack(pady=5)

# Input File 1
tk.Label(root, text="Input Video File 1:").pack(pady=5)
entry_path1 = tk.Entry(root, width=40)
entry_path1.pack(pady=5)

# Input File 2
tk.Label(root, text="Input Video File 2:").pack(pady=5)
entry_path2 = tk.Entry(root, width=40)
entry_path2.pack(pady=5)

# Resolution Options for the Comparison :
tk.Label(root, text="Select Resolution:").pack(pady=5)
resolutions = ["720p", "480p", "360x240", "160x120"]
resolution_var = tk.StringVar(root)
resolution_var.set(resolutions[0])  # Default resolution
resolution_menu = tk.OptionMenu(root, resolution_var, *resolutions)
resolution_menu.pack(pady=5)

# Convert Button for the Comparison:
tk.Button(root, text="Compare Videos", command=compare_videos).pack(pady=10)

# Convert Button:
tk.Button(root, text="Convert", command=convert_video).pack(pady=10)

# Status Label
status_label = tk.Label(root, text="", fg="green")
status_label.pack()

root.mainloop()
