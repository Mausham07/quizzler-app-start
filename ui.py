from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#311432"

class QuizUi:
    def __init__(self, quiz_question:QuizBrain):
        self.quiz = quiz_question

        self.window = Tk()
        self.window.title("QUIZ - TRUE || FALSE")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        self.canvas = Canvas(height=250,width=300, bg="white")
        true_img = PhotoImage(file="images/true.png")
        false_img= PhotoImage(file="images/false.png")
        self.quiz_question = self.canvas.create_text(150, 125, width=280, text="Question here", font=("Ariel", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady = 50)

    

        self.quiz_score = Label(text= "Score: 0", fg="white", highlightthickness=0, bg=THEME_COLOR)
        self.quiz_score.grid(row=0, column=1)

        self.true = Button(image=true_img, highlightthickness=0, command= self.check_true)
        self.true.grid(row=2, column=0)

        self.false = Button(image=false_img, highlightthickness=0, command= self.check_false)
        self.false.grid(row=2, column=1)

        self.question()
        

        self.window.mainloop()
    
    def question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.quiz_score.config(text=f"Score: {self.quiz.score}")

            question = self.quiz.next_question()
            self.canvas.itemconfig(self.quiz_question, text=question)
        
        else:
            self.canvas.config(bg="white")
            self.quiz_score.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.quiz_question, text=f"You have reached the end of question. You got {self.quiz.score} correct answers out of 10.")
            self.true.config(state="disabled")
            self.false.config(state="disabled")

    def check_true(self):
        choice = "True"
        check = self.quiz.check_answer(choice)
        self.feedback(check)

    def check_false(self):
        choice = "False"
        check = self.quiz.check_answer(choice)
        self.feedback(check)

    def feedback(self, check):
        self.check = check
        if self.check:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        
        self.window.after(1000, self.question)