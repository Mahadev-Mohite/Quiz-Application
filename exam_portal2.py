import tkinter
import tkinter as tk
from tkinter.ttk import Separator
from tkinter.messagebox import showinfo
from tkinter import*
import random,sys
root = Tk()
root.geometry('1500x800')
root.title("Application")
root.configure(bg="pink")
s=Separator(root).place(x=0,y=140,relwidth=2)


def getDetails():
    global Name,Roll,mainWindow,Name,Roll
    Name=name.get()
    Roll=roll.get()
    root.deiconify()
    timeshow()
    mainWindow.destroy()

def attendance():
    global name,roll,mainWindow
    
   
exam_name="MAHATMA GANDHI MITION COLLEGE OF ENGINEERING, NANDED"
lbl_exam=tk.Label(root,text=exam_name)
lbl_exam.configure(bg="pink",fg="black",font=("Times New Roman",24,"bold"))
lbl_exam.place(x=70,y=20)

lbl_fname=tk.Label(root,text="Name")
lbl_fname.configure(bg="pink",fg="black",font=("Times New Roman",20,"bold"))
lbl_fname.place(x=400,y=200)

lbl_Mname=tk.Label(root,text="Roll No")
lbl_Mname.configure(bg="pink",fg="black",font=("Times New Roman",20,"bold"))
lbl_Mname.place(x=400,y=300)

lbl_prn=tk.Label(root,text="PRN No")
lbl_prn.configure(bg="pink",fg="black",font=("Times New Roman",20,"bold"))
lbl_prn.place(x=400,y=400)


#ENTRY FOR MAINWINDOW


e1=Entry()
e1.configure(bg="white",fg="black",font="Helvetica,18",width=30,bd=4)
e1.place(x=500,y=200)
e2=Entry()
e2.configure(bg="white",fg="black",font="Helvetica,18",width=30,bd=4)
e2.place(x=500,y=300)
e3=Entry()
e3.configure(bg="white",fg="black",font="Helvetica,18",width=30,bd=4)
e3.place(x=500,y=400)


##############################################

questions ={'Who is the founder of python ?':'Gudio van Rossum',
            
            'What is the output of 13//3  ?':'4.0',
            
            ' In which language python is created  ?':'C language',
            
            'In which year python is started?':'1990',
            
            'What is output of 2**3 ?':'8',
            
            'In which year C language ?':'1972'
            }
#----------separate questions and answer from questions variable------------------------------------#

que = []
ans = []
for key,value in questions.items():
    que.append(key)
    ans.append(value)
#-----------coresponding answer with answer including at randon-----------------------------------#


options =[
    ['van neuman',ans[0],'james gosling','gudo van rosom'],
    [ans[1],'4','4.5','Error'],
    ['Java','c++',ans[2],'HTML'],
    ['1980','1982',ans[3],'1995'],
    ['6','12','16',ans[4]],
    ['1978','1990',ans[5],'1960']

    ]
#-----------------------------------------------------------#


currentQ =''
queNo=None
currentA=''
score = 0
qn = 1
var =StringVar()

def quit_function():
    answer=showinfo("Congrats","good luck For your Future...\n We'll contact soon.")
    if answer=='ok':
        sys.exit(root.destroy())


def desableAllButton():
    option1.config(state=DISABLED)
    option2.config(state=DISABLED)
    option3.config(state=DISABLED)
    option4.config(state=DISABLED)
#===========enable All button============

def enableAllButton():
    option1.config(state=NORMAL)
    option2.config(state=NORMAL)
    option3.config(state=NORMAL)
    option4.config(state=NORMAL)


def result():
    global score,Name,Roll
    root.withdraw()
    top=Toplevel(root)
    top.geometry('200x100')
    top.resizable(0,0)
    top.title('Quiz rersult')
    top.config(bg='blue')
    top.protocol('WM_DELET_WINDOW',quit_function)
    
    label=Label(top,text='Quiz Over...\n Score: '+str(score),font=30,fg='white',bg='blue').place(x=50,y=25)
    exitBtn = Button(top,text='Exit',width=10,bg='black',fg='red',command=quit_function).place(x=50,y=70)
    top.mainloop()



def _start():
    #submit.destroy()
    instr.destroy()
    
    global currentQ,currentA,queNo,score,i,var,qn
    global q2
    i=0
    # till last question is left----------
    
    if len(que)>0:
        currentQ = random.choice(que)
        print(currentQ)
        q = Label(root,text="Que"+str(qn),font=('arial',20))
        q.configure(bg='pink',fg='black')
        q.place(x=15,y=220)
        q2=Label(root,text= currentQ,font=('arial',20))
        q2.configure(bg='pink',fg='black')
        q2.place(x=100,y=220)
        
        qn+=1
        queNo=que.index(currentQ)
        print(options[queNo])
        currentA = questions[currentQ]
        #first change caption of question

        

        
        option1=Radiobutton(root,text='',bg='white',font=20,width=20,relief=FLAT,
                    indicator=0,value=1,variable=var,bd=0)
        option1.place(x=350,y=300)
        option2=Radiobutton(root,text='',bg='white',font=20,width=20,relief=FLAT,
                    indicator=0,value=2,variable=var,bd=0)
        option2.place(x=700,y=300)
        option3=Radiobutton(root,text='',bg='white',font=20,width=20,relief=FLAT,
                    indicator=0,value=3,variable=var,bd=0)
        option3.place(x=350,y=350)
        option4=Radiobutton(root,text='',bg='white',font=20,width=20,relief=FLAT,
                    indicator=0,value=4,variable=var,bd=0)
        option4.place(x=700,y=350)


        #----------------------------------------------------#
        '''hour_tf= Entry(root, width=3, font=f,textvariable=hour)

        hour_tf.place(x=80,y=20)

        mins_tf= Entry(root, width=3, font=f,textvariable=minute)

        mins_tf.place(x=130,y=20)

        sec_tf = Entry(root, width=3, font=f,textvariable=second)

        sec_tf .place(x=180,y=20)'''


        #enableAllButton()

        option1.config(text=options[queNo][0],bg='sky blue',value=options[queNo][0],bd=1,command=answer)
        option2.config(text=options[queNo][1],bg='sky blue',value=options[queNo][1],bd=1,command=answer)
        option3.config(text=options[queNo][2],bg='sky blue',value=options[queNo][2],bd=1,command=answer)
        option4.config(text=options[queNo][3],bg='sky blue',value=options[queNo][3],bd=1,command=answer)
        
        
        que.remove(currentQ)
       # ans.remove(currentA)
        options.remove(options[queNo])
    elif len(que)==0:
        result()
        

        
def answer():
    global currenQ,currentA,score
    # -----------print select radioButton#
    a = var.get()
    if currentA==str(a):
        score+=100
        desableAllButton()
    else:
        desableAllButton()
       
        
################################
def _next():
    lbl_fname.destroy()
    lbl_Mname.destroy()
    lbl_prn.destroy()
    e1.destroy()
    e2.destroy()
    e3.destroy()
    submit.destroy()
    
    #lbl_exam.destroy()
    instruction="1. THIS EXAM CONTAINS 10 QUESTIONS.\n \n               2. ONLY ONE TIMES YOU CAN SELECT A OPTION \n\n 3. EACH QUESTION CONTAINS 5 MARKS \n\n4. SOLVE A QUESTIONS IN 30 MIN\n\nBEST OF LUCK ....👍👍"
    
    
    


    
    global instr
    
    instr=tk.Label(root,text=instruction)
    instr.configure(bg="pink",fg="green",font=("Times New Roman",16,"bold"))
    instr.place(x=350,y=200)
    
    
    submit2 = Button(root,text='START EXAM..',fg='white',
                bg='red',width=15,font=('impact',15),command=_start)
    submit2.place(x=700,y=600)
    submit2.configure(text="NEXT")
    
    
        



   
submit = Button(root,text='START EXAM',fg='white',
                bg='red',width=15,font=('impact',15),command=_next)
submit.place(x=600,y=450)                                   

######################################



root.mainloop()

