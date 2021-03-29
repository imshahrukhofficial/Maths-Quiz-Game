from tkinter import *
import tkinter.messagebox as tm
root = Tk()
root.geometry("900x900")
root.title("Math Quiz Game")
root.configure(background="grey")
                                        # all buttons
def b1():
    global l1, l2, l3, l4
    l.destroy()
    wi.destroy()
    p.destroy()
    aa.destroy()
    # vl.destroy()
    l1 = Button(text="Simple calculations\n(+ , - , * , /)", command=b2, font="Forte 20 bold")
    l1.grid(pady=100, row=1, column=2, padx=80)
    l2 = Button(text="        BODMAS       \n           ", command=b3, font="Forte 20 bold")
    l2.grid(pady=100, row=1, column=8, padx=60)
    l3 = Button(text="    MATHS Formula   \n                ", command=b4, font="Forte 20 bold")
    l3.grid(pady=70, row=2, column=2, padx=80)
    l4 = Button(text="  Logical Question   \n             ", command=b5, font="Forte 20 bold")
    l4.grid(pady=70, row=2, column=8, padx=60)
                                   # questions of simple calculations
q= [
    "solve : 3 + 4",
    "solve : 10 + 5",
    "solve : 10 X 2",
    "solve : 4 X 7",
    "solve : 13 - 4",
    "solve : 10 - 5",
    "solve : 10 / 2",
    "solve : 40 / 5",
    "solve : Square of  15 (15*15)",
    "solve : Square of 12 (12*12)",
    ]
                                    # options of simple calculations
options =[
    ["7","8","9","6"],#1
    ["24","13","50","15"],#2
    ["10","20","30","40"],#3
    ["15","60","28","20"],#4
    ["9","17","5","8"],#5
    ["3","5","7","15"],#6
    ["3","1","0","5"],#7
    ["3","7","8","6"],#8
    ["169","144","225","100"],#9
    ["110","144","122","224"],#10

]
                                    # answers of simple calculations
a = [1,4,2,3,1,2,4,3,3,2]
                                           #questions of bodmas
q1= [
    "solve : 7 x (15 + 5)",
    "solve : 6 + 3 of 7 - 5",
    "solve : 22 + 21/ 3 x 2",
    "solve : 17 + (8 - 5) x 5",
    "solve : 25 - 48 /6 + 12 x 2",
    "solve : 78 -[5 + 3 of(25 - 2 x 10)]",
    "solve : 52 - 4 of(17 - 12) + 4 x 7",
    "solve : 20 -(10 - 3 + 2)",
    "solve : 50 -[20 +{30 -(20 - 5)}]",
    "solve : 100 - 3[20 + 10]",
    ]
                                           # options of bodmas
options1 =[
    ["140","114","110","160"],
    ["14","23","22","26"],
    ["18","34","33","43"],
    ["23","18","13","32"],
    ["41","31","24","17"],
    ["50","53","58","56"],
    ["40","60","30","56"],
    ["11","12","10","9"],
    ["15","16","10","20"],
    ["20","15","13","10"]
]
                                          # answers of bodmas
a1 = [1,3,2,4,1,3,2,1,1,4]
                                        # questions of maths formula
q2= [
    "solve : (a + b)^2",#1
    "solve : (a - b)^2",#2
    "solve : (a - b)(a + b)",#3
    "solve : (a + b)^3",#4
    "Area of Square",#5
    "Area of rectangle",#6
    "perimeter of square",#7
    "Perimeter of rectangle",#8
    "Perimeter of triangle",#9
    "Simple Interest",#10

    ]
                                         # options of math formula
options2 =[
    ["(a^2 + b^2 + 2ab)","(a^2 + b^2 + ab)","(a^2 + b^2 - 2ab)","(2a + 2b + ab)"],#1
    ["(a^2 + b^2 + 2ab)","(a^2 + b^2 - 2ab)","(a + b + 2ab)","(a^2 + b^2 + ab)"],#2
    ["(a^2 + b^2)","(2ab)","(a^2 + 2ab)","(a^2 - b^2)"],#3
    ["(a^3 + b^3 + 3(a^2)b + 3a(b^2)","(a^3 + b^3 - 3(a^2)b - 3a(b^2)","(a^3 + b^3","(3(a^2)b + 3a(b^2)"],#4
    ["(side)^2","(side)^3","2*side","4*side"],#5
    ["2(length*breadth)","2(length + breadth)","(length*breadth)","2+(length*breadth)"],#6
    ["(side)^2","(side)*3","side","4*side"],#7
    ["2(length*breadth)","(length*breadth)","2(length + breadth)","2+(length)"],#8
    ["side*side*side","2*side","side+side+side","side^2"],#9
    ["(P*R*T)","(P*R*T)/100","(P+R+T)/100","(P+R+T)"]
]
                                          # answers of math formula
a2 = [1,2,4,1,1,3,4,3,3,2]
                                        #questions of logical question
q3 =["Q1. Look at this series:36,34,30,28,24...\n what number should come next",
     "Q2. Look at this series:7,10,8,11,9,12...\n what number should come next",
     "Q3. Look at this series:80,10,70,15,60...\n what number should come next",
     "Q4. Which word is the odd man out?",
     "Q5. Which word is the odd man out?",
     "Q6. CUP : LIP :: BIRD : ?",
     "Q7. PAW : CAT :: HOOF : ?",
     "Q8. SCD, TEF, UGH, _____, WKL",
     "Q9. FAG, GAF, HAI, IAH,_____",
     "Q10. CMM, EOO, GQQ, ______,KUU",
     ]
#options of logical questions
options3 =[
             ["22","26","23","20"],
             ["7","12","10","13"],
             ["20","25","30","50"],
             ["hate","fondness","liking","attachment"],
             ["just","fair","equitable","biased"],
             ["GRASS","FOREST","BEAK","BUSH"],
             ["LAMB","HORSE","ELEPHANT","TIGER"],
             ["CMN","UJI","VIJ","IJT"],
             ["JAK","HAL","HAK","JAI"],
             ["GRR","GSS","ISS","ITT"],

           ]
#answers of logical questions
a3=[1,3,1,1,4,3,2,3,1,3]
                                        # simple calculations function
def b2():
    l1.destroy()
    l2.destroy()
    l3.destroy()
    l4.destroy()

    class quiz:
        def __init__(self, master):
            self.opt_selected = IntVar()
            self.qn = 0
            self.correct = 0
            self.ques = self.create_q(master, self.qn)
            self.opts = self.create_options(master, 4)
            self.display_q(self.qn)
            self.button = Button(master, text="  Close  ", command=quit, font=" aerial 30 bold")
            self.button.pack(side=BOTTOM)
            self.button = Button(master, text="   Next   ", command=self.next_btn, font=" aerial 30 bold")
            self.button.pack(side=BOTTOM, pady=10)

        def create_q(self, master, qn):
            w = Label(master, text=q[qn], font="aerial 30 bold", bg="grey")
            w.pack(side=TOP)
            return w

        def create_options(self, master, n):
            b_val = 0
            b = []
            while b_val < n:
                btn = Radiobutton(master, text="foo", font="aerial 20 bold", bg="grey", borderwidth="10",
                                  variable=self.opt_selected, value=b_val + 1)
                b.append(btn)
                btn.pack(side=TOP, anchor="w")
                b_val = b_val + 1
            return b

        def display_q(self, qn):
            b_val = 0
            self.opt_selected.set(0)
            self.ques['text'] = q[qn]
            for op in options[qn]:
                self.opts[b_val]['text'] = op
                b_val = b_val + 1

        def check_q(self, qn):
            if self.opt_selected.get() == a[qn]:
                return True
            return False

        def print_results(self):
            print("score: ", self.correct, "/", len(q))

        def back_btn(self):
            print("go back")

        def next_btn(self):
            if self.check_q(self.qn):
                print("correct")
                self.correct += 1
            else:
                print("wrong")
                self.qn = self.qn + 1
            if self.qn >= len(q):
                self.print_results()
            if self.qn == len(q):
                value = tm.askokcancel("SCORE", f"score: {self.correct} / {len(q)}")
                print(value)
                if value == "ok":
                    quit()
                else:
                    quit()

            else:
                self.display_q(self.qn)

    app = quiz(root)
                                              # bodmas function
def b3():
    l1.destroy()
    l2.destroy()
    l3.destroy()
    l4.destroy()

    class quiz:
        def __init__(self, master):
            self.opt_selected = IntVar()
            self.qn = 0
            self.correct = 0
            self.ques = self.create_q(master, self.qn)
            self.opts = self.create_options(master, 4)
            self.display_q(self.qn)
            self.button = Button(master, text="  Close  ", command=quit,font=" aerial 30 bold")
            self.button.pack(side=BOTTOM )
            self.button = Button(master, text="   Next   ", command=self.next_btn,font=" aerial 30 bold")
            self.button.pack(side=BOTTOM, pady=10)

        def create_q(self, master, qn):
            w = Label(master, text=q1[qn], font="aerial 30 bold", bg="grey")
            w.pack(side=TOP)
            return w

        def create_options(self, master, n):
            b_val = 0
            b = []
            while b_val < n:
                btn = Radiobutton(master, text="foo", font="aerial 20 bold", bg="grey", borderwidth="10",
                                  variable=self.opt_selected, value=b_val + 1)
                b.append(btn)
                btn.pack(side=TOP, anchor="w")
                b_val = b_val + 1
            return b

        def display_q(self, qn):
            b_val = 0
            self.opt_selected.set(0)
            self.ques['text'] = q1[qn]
            for op in options1[qn]:
                self.opts[b_val]['text'] = op
                b_val = b_val + 1

        def check_q(self, qn):
            if self.opt_selected.get() == a1[qn]:
                return True
            return False

        def print_results(self):
            print("score: ", self.correct, "/", len(q1))

        def back_btn(self):
            print("go back")

        def next_btn(self):
            if self.check_q(self.qn):
                print("correct")
                self.correct += 1
            else:
                print("wrong")
                self.qn = self.qn + 1
            if self.qn >= len(q1):
                self.print_results()
            if self.qn == len(q1):
                value = tm.askokcancel("SCORE", f"score: {self.correct} / {len(q1)}")
                print(value)
                if value == "ok":
                    quit()
                else:
                    quit()

            else:
                self.display_q(self.qn)

    app = quiz(root)
                                             # math formula function
def b4():
    l1.destroy()
    l2.destroy()
    l3.destroy()
    l4.destroy()
    class quiz:
        def __init__(self, master):
            self.opt_selected = IntVar()
            self.qn = 0
            self.correct = 0
            self.ques = self.create_q(master, self.qn)
            self.opts = self.create_options(master, 4)
            self.display_q(self.qn)
            self.button = Button(master, text="  Close  ", command=quit, font=" aerial 30 bold")
            self.button.pack(side=BOTTOM)
            self.button = Button(master, text="   Next   ", command=self.next_btn, font=" aerial 30 bold")
            self.button.pack(side=BOTTOM, pady=10)

        def create_q(self, master, qn):
            w = Label(master, text=q2[qn], font="aerial 30 bold", bg="grey")
            w.pack(side=TOP)
            return w

        def create_options(self, master, n):
            b_val = 0
            b = []
            while b_val < n:
                btn = Radiobutton(master, text="foo", font="aerial 20 bold", bg="grey", borderwidth="10",
                                  variable=self.opt_selected, value=b_val + 1)
                b.append(btn)
                btn.pack(side=TOP, anchor="w")
                b_val = b_val + 1
            return b

        def display_q(self, qn):
            b_val = 0
            self.opt_selected.set(0)
            self.ques['text'] = q2[qn]
            for op in options2[qn]:
                self.opts[b_val]['text'] = op
                b_val = b_val + 1

        def check_q(self, qn):
            if self.opt_selected.get() == a2[qn]:
                return True
            return False

        def print_results(self):
            print("score: ", self.correct, "/", len(q2))

        def back_btn(self):
            print("go back")

        def next_btn(self):
            if self.check_q(self.qn):
                print("correct")
                self.correct += 1
            else:
                print("wrong")
            self.qn = self.qn + 1
            if self.qn >= len(q2):
                self.print_results()
            if self.qn == len(q2):
                value = tm.askokcancel("SCORE", f"score: {self.correct} / {len(q2)}")
                print(value)
                if value == "ok":
                    quit()
                else:
                    quit()

            else:
                self.display_q(self.qn)

    app = quiz(root)
                                           # logical questions function
def b5():
    l1.destroy()
    l2.destroy()
    l3.destroy()
    l4.destroy()

    class quiz:
        def __init__(self, master):
            self.opt_selected = IntVar()
            self.qn = 0
            self.correct = 0
            self.ques = self.create_q(master, self.qn)
            self.opts = self.create_options(master, 4)
            self.display_q(self.qn)
            self.button = Button(master, text="  Close  ", command=quit, font=" aerial 30 bold")
            self.button.pack(side=BOTTOM)
            self.button = Button(master, text="   Next   ", command=self.next_btn, font=" aerial 30 bold")
            self.button.pack(side=BOTTOM, pady=10)

        def create_q(self, master, qn):
            w = Label(master, text=q3[qn], font="aerial 30 bold", bg="grey")
            w.pack(side=TOP)
            return w

        def create_options(self, master, n):
            b_val = 0
            b = []
            while b_val < n:
                btn = Radiobutton(master, text="foo", font="aerial 20 bold", bg="grey", borderwidth="10",
                                  variable=self.opt_selected, value=b_val + 1)
                b.append(btn)
                btn.pack(side=TOP, anchor="w")
                b_val = b_val + 1
            return b

        def display_q(self, qn):
            b_val = 0
            self.opt_selected.set(0)
            self.ques['text'] = q3[qn]
            for op in options3[qn]:
                self.opts[b_val]['text'] = op
                b_val = b_val + 1

        def check_q(self, qn):
            if self.opt_selected.get() == a3[qn]:
                return True
            return False

        def print_results(self):
            print("score: ", self.correct, "/", len(q3))

        def back_btn(self):
            print("go back")

        def next_btn(self):
            if self.check_q(self.qn):
                print("correct")
                self.correct += 1
            else:
                print("wrong")
            self.qn = self.qn + 1
            if self.qn >= len(q3):
                self.print_results()
            if self.qn == len(q3):
                value = tm.askokcancel("SCORE", f"score: {self.correct} / {len(q3)}")
                print(value)
                if value == "ok":
                    quit()
                else:
                    quit()

            else:
                self.display_q(self.qn)

    app = quiz(root)

    # front page designing
                                               # front page designing
l=Label(text=" WELCOME   TO    THE    WORLD  \n OF MATHEMATICS" ,font="Forte 28 bold" ,bg="grey",pady="34",relief=GROOVE,borderwidth=8)
l.pack(pady=30)
# photo = PhotoImage(file="q2.png")
# vl = Label(image = photo,width=100,height=105)
# vl.pack()
wi = Button(root,text="START GAME >>",pady="30",fg="black",font="aerial 22 bold",bg="white",command=b1)
wi.pack(pady=30)
p=Label(root,text="Read The Rules And \n Click Start Once You Are Ready",bg="grey",font="Forte 20 bold")
p.pack()
aa=Label(root,text="This quiz contain 4 different type of Question \n each type contain 10 questions \n you will get infinite time to solve a question",bg="black",fg="grey",font="aerial 15 bold")
aa.pack(side=BOTTOM,fill=BOTH)






root.mainloop()