from tkinter import *


THEME_COLOR = "#311432"

class QuizUi:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quiz")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        self.canvas = Canvas(height=250,width=300, bg="white")
        true_img = PhotoImage(file="images/true.png")
        false_img= PhotoImage(file="images/false.png")
        self.quiz_question = self.canvas.create_text(150, 125, text="Question here", font=("Ariel", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady = 50)

    

        self.quiz_score = Label(text= "Score: 0", fg="white", highlightthickness=0, bg=THEME_COLOR)
        self.quiz_score.grid(row=0, column=1)

        self.true = Button(image=true_img, highlightthickness=0)
        self.true.grid(row=2, column=0)

        self.false = Button(image=false_img, highlightthickness=0)
        self.false.grid(row=2, column=1)

        
        

        self.window.mainloop()