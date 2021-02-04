from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
img1 = ""
img2 = ""


class UI:

    def __init__(self, quizBrain: QuizBrain):
        self.window = Tk()
        self.window.title("Quizzler App")
        self.window.minsize(width=400, height=500)
        self.window.config(bg=THEME_COLOR, pady=50)
        self.brain = quizBrain
        self.scoreLabel()
        self.questionArea()
        self.trueAndFalse()
        self.window.mainloop()

    def questionArea(self):
        self.canv = Canvas(width=300, height=200, bg="white", highlightthickness=0)
        self.canv.grid(row=2, column=1, columnspan=2, padx=50, pady=30)
        self.question_text = self.canv.create_text(150, 100, width=280, font=("Arial", 15, "italic"), text="")
        self.goToNextQuestion()

    def scoreLabel(self):
        self.scoreLabel = Label(text=f"Score: {self.brain.score}", font=("Arial", 20, "normal"), bg=THEME_COLOR, fg="white")
        self.scoreLabel.grid(row=1, column=2)

    def truePressed(self):
        if self.brain.check_answer("True"):
            self.turnGreen()
        else:
            self.turnRed()

    def falsePressed(self):
        if self.brain.check_answer("False"):
            self.turnGreen()
        else:
            self.turnRed()

    def turnGreen(self):
        self.canv.config(bg="green")
        self.window.after(1000, self.goToNextQuestion)

    def turnRed(self):
        self.canv.config(bg="red")
        self.window.after(1000, self.goToNextQuestion)

    def goToNextQuestion(self):
        question = self.brain.next_question()
        self.canv.config(bg="white")
        self.scoreLabel.config(text=f"Score: {self.brain.score}")
        if question is not None:
            self.canv.itemconfig(self.question_text, text=question)
        else:
            self.canv.itemconfig(self.question_text, text=f"You have completed the quiz!\nYour score is {self.brain.score}/{len(self.brain.question_list)}")

    def trueAndFalse(self):
        global img1, img2
        img1 = PhotoImage(file="images/true.png")
        self.trueButton = Button(image=img1, command=self.truePressed)
        self.trueButton.grid(row=3, column=2)
        img2 = PhotoImage(file="images/false.png")
        self.falseButton = Button(image=img2, command=self.falsePressed)
        self.falseButton.grid(row=3, column=1)
