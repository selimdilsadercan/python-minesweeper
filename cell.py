from tkinter import Button, Label
import random
from settings import *
import ctypes
import sys

class Cell:
    all = []
    cell_count = CELL_COUNT
    cell_count_label_object = None

    def __init__(self, x, y, is_mine = False):
        self.is_opened = False
        self.is_mine = is_mine
        self.is_flagged = False
        self.cell_btn_object = None
        self.x = x
        self.y = y

        Cell.all.append(self)


    def create_btn_object(self, location):
        btn = Button(
            location,
            width= 12,
            height= 4,
        )        
        btn.bind("<Button-1>", self.left_click_actions)
        btn.bind("<Button-3>", self.right_click_actions)

        self.cell_btn_object = btn
        

    @staticmethod    
    def create_cell_count_label(location):
        lbl = Label(
            location,
            text= f"Kalan Kutu Sayısı: {Cell.cell_count}",
            bg="black",
            fg="white",
            width= 20,
            font=("",16),
            height= 4
        )
        Cell.cell_count_label_object = lbl

    def left_click_actions(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            if self.etraftaki_mine_olan_cells_count == 0:
                for etraftaki_cell in self.etraftaki_cells:
                    etraftaki_cell.show_cell()
            self.show_cell()

        self.cell_btn_object.unbind("<Button-1>")
        self.cell_btn_object.unbind("<Button-3>")


    def right_click_actions(self, event):
        if not self.is_flagged:
            self.cell_btn_object.configure(bg="yellow")
            self.is_flagged = True
        else:
            self.cell_btn_object.configure(bg="SystemButtonFace")
            self.is_flagged = False


    def show_cell(self):
        if self.is_opened == False:
            Cell.cell_count -= 1
            self.cell_btn_object.configure(text= self.etraftaki_mine_olan_cells_count)
            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(text= f"Kalan Kutu Sayısı: {Cell.cell_count}")
            self.is_opened = True


    @property
    def etraftaki_cells(self):
        cells = [
            self.get_cell_by_axis(self.x-1,self.y-1),
            self.get_cell_by_axis(self.x-1,self.y),
            self.get_cell_by_axis(self.x-1,self.y+1),
            self.get_cell_by_axis(self.x,self.y-1),
            self.get_cell_by_axis(self.x+1,self.y-1),
            self.get_cell_by_axis(self.x+1,self.y-1),
            self.get_cell_by_axis(self.x+1,self.y),
            self.get_cell_by_axis(self.x+1,self.y+1),
            self.get_cell_by_axis(self.x,self.y+1),

        ]

        cells = [cell for cell in cells if cell is not None]
        return cells


    @property
    def etraftaki_mine_olan_cells_count(self):
        counter = 0
        for cell in self.etraftaki_cells:
            if cell.is_mine:
                counter += 1

        return counter


    def get_cell_by_axis(self,x,y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell
    

    def show_mine(self):
        self.cell_btn_object.configure(bg="red")
        ctypes.windll.user32.MessageBoxW(0,"Patladın","Game Over",0)


    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(Cell.all, MINES_COUNT)
        
        for picked_cell in picked_cells:
            picked_cell.is_mine = True
        

    def __repr__(self):
        return f'Cell({self.x}, {self.y})'
