from tkinter import PhotoImage
from PIL import ImageTk
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Label
from SQlpythonProject import DBmain

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(
    r"C:\Users\USER\PycharmProjects\DBProject-Amen-amine-\assets\frame0"
)


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


# ------------------------------------------------------------------------------------------
result = ""
window = Tk()
window.geometry("1920x1080")
window.configure(bg="#FFFFFF")
window.attributes("-fullscreen", True)
# DBmain()
canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=1080,
    width=1920,
    bd=0,
    highlightthickness=0,
    relief="ridge",
)
canvas.place(x=0, y=0)
canvas.create_rectangle(0.0, 0.0, 1920.0, 1080.0, fill="#25323C", outline="")

canvas.create_rectangle(47.0, 117.0, 731.0, 963.0, fill="#1D2731", outline="")

canvas.create_rectangle(848.0, 117.0, 1850.0, 963.0, fill="#1D2831", outline="")

canvas.create_rectangle(0.0, 0.0, 1920.0, 66.0, fill="#2E3D4B", outline="")

canvas.create_rectangle(70.0, 350.0, 707.0, 351.0, fill="#FFFFFF", outline="")

canvas.create_rectangle(70.0, 742.0, 707.0, 743.0, fill="#FFFFFF", outline="")

canvas.create_rectangle(70.0, 539.0, 707.0, 540.0, fill="#FFFFFF", outline="")


# -----------------------------------------------------------------------------
def b(x):
    global result
    result = DBmain(x)
    canvas.create_rectangle(848.0, 117.0, 1850.0, 963.0, fill="#1D2831", outline="")
    canvas.create_text(
        900,
        150,
        anchor="nw",
        text=result,
        fill="#FFFFFF",
        font=("AnekLatin Latin", 18 * -1),
    )


# --------------------------------------buttons----------------------------------------
button_image = ImageTk.PhotoImage(file=relative_to_assets("button.png"))

button_1 = Button(command=lambda: b(1))
button_1.place(x=600, y=238)

button_2 = Button(command=lambda: b(2))
button_2.place(x=600, y=425)

button_3 = Button(command=lambda: b(3))
button_3.place(x=600, y=617)

button_4 = Button(command=lambda: b(4))
button_4.place(x=600, y=816)

# -------------------------------------text--------------------------------------------
canvas.create_text(
    700,
    15,
    anchor="nw",
    text="Pristini Students  Birthday System",
    fill="#FFFFFF",
    font=("AnekLatin Light", 32 * -1),
)
# ---------------------------------buttons text
canvas.create_text(
    210,
    238.0,
    anchor="nw",
    text="Show All Students",
    fill="#FFFFFF",
    font=("AnekLatin Latin", 24 * -1),
)
canvas.create_text(
    210,
    425.0,
    anchor="nw",
    text="Order Students By Age (Ascending)",
    fill="#FFFFFF",
    font=("AnekLatin Latin", 24 * -1),
)
canvas.create_text(
    210,
    617.0,
    anchor="nw",
    text="Order Students By Age (Descending)",
    fill="#FFFFFF",
    font=("AnekLatin Latin", 23 * -1),
)
canvas.create_text(
    210,
    816.0,
    anchor="nw",
    text="Show Students Closest Birthday",
    fill="#FFFFFF",
    font=("AnekLatin Latin", 24 * -1),
)
# window.resizable(False, False)
window.mainloop()