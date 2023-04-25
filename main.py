from tkinter import *
from settings import *
from utils import *
from cell import Cell

root = Tk()

# PENCERE AYARLARININ YAPILMASI
root.configure(bg="black")
root.geometry(f"{WIDTH}x{HEIGHT}")
root.resizable(False,False)
root.title("Minesweeper")


# FRMELERİN AYARLANMASI
topFrame = Frame(
    root,
    bg = "black",
    width = WIDTH,
    height = oran(HEIGHT,25) 
)
topFrame.place(x=0, y=0)

gameTitle = Label(
    topFrame,
    bg="black",
    fg="White",
    text="Minesweeper",
    font=("", 36)    
)
gameTitle.place(x=0,y=0)

leftFrame = Frame(
    root,
    bg= "black",
    width= oran(WIDTH,25),
    height= oran(HEIGHT,75)
)
leftFrame.place(x=0,y=oran(HEIGHT,25))

centerFrame = Frame(
    root,
    bg= "black",
    width=oran(WIDTH,75),
    height=oran(HEIGHT,75)
)
centerFrame.place(x=oran(WIDTH,25),y=oran(HEIGHT,25))


# CELL'LERİN AYARLANMASI
for i in range(CELL_COUNT):
    x = i%GRID_SIZE
    y = i//GRID_SIZE
    
    cell = Cell(x,y)
    cell.create_btn_object(centerFrame)
    cell.cell_btn_object.grid(row=y, column=x)

Cell.randomize_mines()


# OYUN DETAYLARINI YAZDIR
Cell.create_cell_count_label(leftFrame)
Cell.cell_count_label_object.place(x=0,y=0)



# PENCEREYİ ÇALIŞTIR
root.mainloop()
