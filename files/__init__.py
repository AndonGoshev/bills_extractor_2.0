# import tkinter as tk
# from tkinter import filedialog
#
# def browse_file():
#     file_path = filedialog.askopenfilename()
#     if file_path:
#         directory = os.path.dirname(file_path)
#         entry_var.set(directory)
#
# # Create the main window
# root = tk.Tk()
# root.title("File Directory Entry")
#
# # Create and place the Entry widget
# entry_var = tk.StringVar()
# entry = tk.Entry(root, textvariable=entry_var, width=40)
# entry.pack(pady=10)
#
# # Create and place the Button widget
# button = tk.Button(root, text="Browse", command=browse_file)
# button.pack()
#
# # Run the Tkinter event loop
# root.mainloop()