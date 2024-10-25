"""
release 4 - FINAL
(releas1 & releas2 & releas3 & new idea )

"""


from tkinter import *
from random import *

number = randint(1, 6)
k = 3
#напишемо функцію для нової гри
def new_game():
    global k
    global namber
    k = 3
    number = randint(1, 6)
    label2.config(text=" ", bg="#FED700")
    entry.config(state=NORMAL) # поле для введення стає доступне
    button.config(state=NORMAL) # кнопка стає доступна
    entry.delete(0, END)

# напишемо функцію - процес гри
def one_click():
  global k
  if k-1<=0: 
      entry.config(state=DISABLED) # поле для введення стає недоступне
      button.config(state=DISABLED) # кнопка стає недоступна

  
  a=int(entry.get())
  if a<number: 
    k -= 1
    label2.config(text=f" залишилось спроб - {k}  \n спробуй більше ")
    
  elif a>number:
    k -= 1
    label2.config(text=f" залишилось спроб- {k}   \n спробуй менше ")
    
   
  else:
    k -= 1
    new_window = Toplevel(root) #нове вікно new_window  клас  Toplevel - вікно верхнього рівня
    new_window.title("Нове Top-Level Вікно") 
    new_window.geometry("300x300")
    label3 = Label(new_window, text=f"залишилось спроб- {k}\n Вгадав!\n Вітаю!  ", font="Arial 15",bg="#FF0000")
    label3.pack()
    close_new_window = Button(new_window, text="close", command=new_window.destroy)#Метод .destroy() - закриття вікна
    close_new_window.pack()
    

  entry.delete(0, END)
  

root =Tk()  
root.title("Вгадай число!") 
root.geometry("400x400")
root.configure(bg="#FED700")
root.resizable(False, False)



label1 = Label(root, text="Введи число число від 1 до 6", bg="#FED700",font="Arial 10")
label1.pack()


entry = Entry(root, width=15)
entry.place(x=155,y=100)



photo = PhotoImage(file="1.files/cube.png")
button = Button(root,image=photo,  width=107, height=100, bd=1, command=one_click)
button.place(x=145,y=230)


label2 = Label(root, text=" ", font="Arial 18",bg="#FED700")
label2.place(x=90,y=150)

#створимо кнопку new_game
new_game_button = Button(root, text="New Game", command=new_game)
new_game_button.place(x=170, y=350)



root.mainloop()
