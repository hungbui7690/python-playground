"""
TKINTER CURSORS

\\\\\\\\\\\\\\\\\\\\\

Changing cursor for widgets

- All ttk widgets have the cursor parameter that allows you to change the cursor when the mouse hovers them.
- For example, if you want to change the cursor of a button, you can set the cursor name using the cursor parameter as follows:

    from tkinter import ttk

    #...
    button = ttk.Button(cursor=cursor_name)

- The cursor name can be one of the following values:

    arrow                   man
    based_arrow_down	    middlebutton
    based_arrow_up	        mouse
    boat	                pencil
    bogosity                pirate
    bottom_left_corner      plus
    bottom_right_corner     question_arrow
    bottom_side             right_ptr
    bottom_tee              right_side
    box_spiral              right_tee
    center_ptr	            rightbutton
    circle                  rtl_logo
    clock                   sailboat
    coffee_mug              sb_down_arrow
    cross	                sb_h_double_arrow
    cross_reverse           sb_left_arrow
    crosshair	            sb_right_arrow
    diamond_cross	        sb_up_arrow
    dot	                    sb_v_double_arrow
    dotbox	                shuttle
    double_arrow	        sizing
    draft_large	            spider
    draft_small	            spraycan
    draped_box	            star
    exchange                target
    fleur                   tcross
    gobbler	                top_left_arrow
    gumby	                top_left_corner
    hand1	                top_right_corner
    hand2	                top_side
    heart                   top_tee
    icon	                trek
    iron_cross	            ul_angle
    left_ptr	            umbrella
    left_side	            ur_angle
    left_tee	            watch
    leftbutton	            xterm
    ll_angle                X_cursor
    lr_angle	
    
- To change the cursor of the root window, you can:

    First, create a new Frame.
    Second, place it on the root window and expand it 100%.
    Third, set the cursor on the frame.

"""


# The following program allows you to change the cursor by selecting it in a combobox:

from tkinter import ttk
import tkinter as tk

root = tk.Tk()

# config the root window
root.geometry("600x400")
root.resizable(False, False)
root.title("Tkinter Cursors")

frame = ttk.Frame(root)


# label
label = ttk.Label(frame, text="Cursor:")
label.pack(fill=tk.X, padx=5, pady=5)

# cursor list
selected_cursor = tk.StringVar()
cursor_list = ttk.Combobox(frame, textvariable=selected_cursor, cursor="arrow")
cursors = [
    "arrow",
    "man",
    "based_arrow_down",
    "middlebutton",
    "based_arrow_up",
    "mouse",
    "boat",
    "pencil",
    "bogosity",
    "pirate",
    "bottom_left_corner",
    "plus",
    "bottom_right_corner",
    "question_arrow",
    "bottom_side",
    "right_ptr",
    "bottom_tee",
    "right_side",
    "box_spiral",
    "right_tee",
    "center_ptr",
    "rightbutton",
    "circle",
    "rtl_logo",
    "clock",
    "sailboat",
    "coffee_mug",
    "sb_down_arrow",
    "cross",
    "sb_h_double_arrow",
    "cross_reverse",
    "sb_left_arrow",
    "crosshair",
    "sb_right_arrow",
    "diamond_cross",
    "sb_up_arrow",
    "dot",
    "sb_v_double_arrow",
    "dotbox",
    "shuttle",
    "double_arrow",
    "sizing",
    "draft_large",
    "spider",
    "draft_small",
    "spraycan",
    "draped_box",
    "star",
    "exchange",
    "target",
    "fleur",
    "tcross",
    "gobbler",
    "top_left_arrow",
    "gumby",
    "top_left_corner",
    "hand1",
    "top_right_corner",
    "hand2",
    "top_side",
    "heart",
    "top_tee",
    "icon",
    "trek",
    "iron_cross",
    "ul_angle",
    "left_ptr",
    "umbrella",
    "left_side",
    "ur_angle",
    "left_tee",
    "watch",
    "leftbutton",
    "xterm",
    "ll_angle",
    "X_cursor",
    "lr_angle",
]
cursor_list["values"] = cursors
cursor_list["state"] = "readonly"


cursor_list.pack(fill=tk.X, padx=5, pady=5)

frame.pack(expand=True, fill=tk.BOTH)


# bind the selected value changes
def cursor_changed(event):
    frame.config(cursor=selected_cursor.get())


cursor_list.bind("<<ComboboxSelected>>", cursor_changed)

root.mainloop()


# Summary
# The root window has only two cursors: normal ("") and busy ("watch").
# The widget has many cursors with fixed names.
# Use the cursor parameter to change the cursor for the root window or a widget.
