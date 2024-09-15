from tkinter import Tk, Canvas, Scrollbar, Frame, RIGHT, LEFT, BOTH, Y, Label

def update_scrollregion(canvas):
    canvas.update_idletasks()  # Update the canvas to reflect any changes
    canvas.config(scrollregion=canvas.bbox('all'))  # Update the scrollregion

root = Tk()

# Create and pack the scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# Create the Canvas
canvas = Canvas(root, yscrollcommand=scrollbar.set)
canvas.pack(side=LEFT, fill=BOTH, expand=True)

# Create a Frame and place it inside the Canvas
frame = Frame(canvas, width=100, height=200)
canvas.create_window((0, 0), window=frame, anchor='nw')

# Configure the scrollbar
scrollbar.config(command=canvas.yview)

# Add labels to the Frame
for i in range(1000):
    Label(frame, text=i).pack()

# Update the scroll region after adding all labels
update_scrollregion(canvas)

root.mainloop()
