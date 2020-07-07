from tkinter import *

#Graphic_Interface class

class Graphic_interface :
       
    def layout(self):
        
        #input1
       
        self.insert_init = Entry(justify= "right", width=17)
        self.insert_init.grid(row=0, column=0,columnspan=3, padx=10, pady=10)
        self.insert_init.configure(font=("Courier",16,"bold"))

        #output
        
        self.display = Label(justify= "right", width=17)
        self.display.grid(row=1, column=4, columnspan=3, padx=10, pady=10)
        self.display.configure(font=("Courier",16,"bold"))

        #input2

        self.insert_end = Entry(justify= "right", width=17)
        self.insert_end.grid(row=0, column=8, columnspan=3, padx=10, pady=10)
        self.insert_end.configure(font=("Courier",16,"bold"))

        #input3
       
        self.insert_init2 = Entry(justify= "right", width=17)
        self.insert_init2.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
        self.insert_init2.configure(font=("Courier",16,"bold"))

        #input4
       
        self.insert_cent = Entry(justify= "right", width=17)
        self.insert_cent.grid(row=0, column=4, columnspan=3, padx=10, pady=10)
        self.insert_cent.configure(font=("Courier",16,"bold"))

        #input5
       
        self.insert_end2 = Entry(justify= "right", width=17)
        self.insert_end2.grid(row=1, column=8, columnspan=3, padx=10, pady=10)
        self.insert_end2.configure(font=("Courier",16,"bold"))


# Input Output class

class IOput(Graphic_interface):
    def __init__(self):
        self.layout()
        self.refresh_disp('0')
        
        
    # clear display

    def clear_disp(self):
        self.insert_init.delete(0,'end')     # 입력값 지우기
        self.insert_init2.delete(0,'end')
        self.insert_end.delete(0,'end')
        self.insert_end2.delete(0,'end')
        self.insert_cent.delete(0,'end')
        
        
    # replace text on display

    def refresh_disp(self, text):
        self.clear_disp()                
        self.insert_init.insert(0, text)    # 입력값 넣기
        self.insert_init2.insert(0, text)
        self.insert_end.insert(0, text)
        self.insert_end2.insert(0, text)
        self.insert_cent.insert(0, text)

    # display the result

    def result_disp(self, text):
        a = str(text)
        self.display.configure(text = '%s' % a)        # 입력값 넣기
        

#Main Class

class Main:


    def initGraphic(self):
        self.interface = IOput()
    

    # detect layer

    def key(self, event):

        #calculate values
        
        
        def average(a, b, c, d, e):
            x = ((e - a)*d + (b - e)*c)/(b-a)
            
            return x

        def result_disp(self, text):
            self.display.insert(0,text)

        a1 = float(self.interface.insert_init.get())
        b1 = float(self.interface.insert_end.get())
        a2 = float(self.interface.insert_init2.get())
        b2 = float(self.interface.insert_end2.get())
        c1 = float(self.interface.insert_cent.get())
        

        c2 = average(a1, b1, a2, b2, c1)

        self.interface.result_disp('%f' % c2)

    #생성자
    
    def __init__(self, master):
        self.master = master
        self.initGraphic()
        master.bind("<Key>", self.key)







#Initialize calculator
 
root = Tk()
root.title("내삽법 계산기")
root.resizable(False,False)             # 화면 크기 고정
Main(root)


root.mainloop()
