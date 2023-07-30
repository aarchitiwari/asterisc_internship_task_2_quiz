import tkinter as tk
from tkinter import StringVar
import tkinter as Tk
from tkinter import*
from tkinter import messagebox


def handleLogin():
    email = email_input.get()
    password = password_input.get()
    if email == 'abc@gmail.com' and password == '1234':
        messagebox.showinfo('Yayyy', 'Login Successful')
    else:
        messagebox.showerror('Error', 'Login Failed')


root = Tk()

root.title('Login Form')
root.geometry('350x500')
root.configure(bg='#0096DC')

# img = Image.open('pic.jpg')
# resized_img = img.resize((70, 70), Image.LANCZOS)
# img = ImageTk.PhotoImage(resized_img)
# img_label = Label(root, image=img)
# img_label.pack(pady=(10, 10))

text_label = Label(root, text='QUIZ STATION', fg='white', bg='#0096DC')
text_label.pack()
text_label.config(font=('verdana', 24))

email_label = Label(root, text='Enter Email', fg='white', bg='#0096DC')
email_label.pack(pady=(20, 5))
email_label.config(font=('verdana', 12))

email_input = Entry(root, width=50)
email_input.pack(ipady=6, pady=(1, 15))

password_label = Label(root, text='Enter Password', fg='white', bg='#0096DC')
password_label.pack(pady=(20, 5))
password_label.config(font=('verdana', 12))

password_input = Entry(root, width=50)
password_input.pack(ipady=6, pady=(1, 15))

login_btn = Button(root, text='Login Here', bg='white', fg='black', width=10, height=2, command=handleLogin)
login_btn.pack(pady=(10, 20))
login_btn.config(font=('verdana', 10))

root.mainloop()

#-------------------------------------------------------quiz---------------------------------------------------------------

root = tk.Tk()
root.geometry('500x500')

questions = ["Who Developed Python ?","In which Year Python Language was Developed ?","In which Languauge Python was written ?","Which one of the following is correct extension of Python File ?","Which of the following functions is Built-in in python ?"]
options = [['A. Zim Den','B. Niene Stom','C. Guido van Rossum','D. Wick van Rossum','C. Guido van Rossum'],['A. 1995','B. 1989','C. 1972','D. 1981','B. 1989'],
           ['A. English','B. PHP','C. C++','D. C','D. C'],['A. .py','B. .python','C. .p','D. None of these','A. .py'],['A. val()','B. print()','C. prints()','D. None of these','B. print()']]


frame = tk.Frame(root, padx=10, pady=10,bg='#fff')
question_label = tk.Label(frame,height=5, width=28,bg='grey',fg="#fff", 
                          font=('Verdana', 20),wraplength=500)


v1 = StringVar(frame)
v2 = StringVar(frame)
v3 = StringVar(frame)
v4 = StringVar(frame)

option1 = tk.Radiobutton(frame, bg="#fff", variable=v1, font=('Verdana', 20),
                         command = lambda : checkAnswer(option1))
option2 = tk.Radiobutton(frame, bg="#fff", variable=v2, font=('Verdana', 20), 
                         command = lambda : checkAnswer(option2))
option3 = tk.Radiobutton(frame, bg="#fff", variable=v3, font=('Verdana', 20), 
                         command = lambda : checkAnswer(option3))
option4 = tk.Radiobutton(frame, bg="#fff", variable=v4, font=('Verdana', 20), 
                         command = lambda : checkAnswer(option4))

button_next = tk.Button(frame, text='Next',bg='Orange', font=('Verdana', 20), 
                        command = lambda : displayNextQuestion())

frame.pack(fill="both", expand="true")
question_label.grid(row=0, column=0)

option1.grid(sticky= 'W', row=1, column=0)
option2.grid(sticky= 'W', row=2, column=0)
option3.grid(sticky= 'W', row=3, column=0)
option4.grid(sticky= 'W', row=4, column=0)

button_next.grid(row=6, column=0)


index = 0
correct = 0

# create a function to disable radiobuttons
def disableButtons(state):
    option1['state'] = state
    option2['state'] = state
    option3['state'] = state
    option4['state'] = state


# create a function to check the selected answer
def checkAnswer(radio):
    global correct, index
    
    # the 4th item is the correct answer
    # we will check the user selected answer with the 4th item
    if radio['text'] == options[index][4]:
        correct +=1

    index +=1
    disableButtons('disable')


# create a function to display the next question
def displayNextQuestion():
    global index, correct

    if button_next['text'] == 'Restart The Quiz':
        correct = 0
        index = 0
        question_label['bg'] = 'grey'
        button_next['text'] = 'Next'

    if index == len(options):
       question_label['text'] = str(correct) + " / " + str(len(options))
       button_next['text'] = 'Restart The Quiz'
       if correct >= len(options)/2:
           question_label['bg'] = 'green'
       else:
            question_label['bg'] = 'red'





    else:
        question_label['text'] = questions[index]
        
        disableButtons('normal')
        opts = options[index]
        option1['text'] = opts[0]
        option2['text'] = opts[1]
        option3['text'] = opts[2]
        option4['text'] = opts[3]
        v1.set(opts[0])
        v2.set(opts[1])
        v3.set(opts[2])
        v4.set(opts[3])

        if index == len(options) - 1:
            button_next['text'] = 'Check the Results'





displayNextQuestion()

root.mainloop()
