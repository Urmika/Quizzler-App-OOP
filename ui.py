from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
FONT = "Arial"
FONT_SIZE = 20
STYLE = "italic"

class QuizzInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        #self.window.minsize(width=200,height=200)
        self.window.config(padx=20,pady=20,background=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300,height=250, bg="white")
        self.question_text = self.canvas.create_text(135,125, width=280,text="Question Text", fill=THEME_COLOR, font=(FONT,20,STYLE))
        self.canvas.grid(column=0, row=1,columnspan=2,pady=50)

        tick_image = PhotoImage(file="images/true.png")
        self.tick = Button(image=tick_image, highlightthickness=0,bd=0, command=self.check_false)
        self.tick.grid(column=0,row=2)

        cross_image = PhotoImage(file="images/false.png")
        self.cross = Button(image=cross_image, highlightthickness=0, bd=0, command=self.check_true)
        self.cross.grid(column=1,row=2)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.button_state(ACTIVE)

        else:
            self.canvas.itemconfig(self.question_text,text="End of the quiz!")
            # self.tick.config(state="disabled")
            # self.cross.config(state="disabled")
            self.button_state(DISABLED)

    def check_true(self):
        ans = self.quiz.check_answer(user_answer="True")
        self.give_feedback(ans)

    def check_false(self):
        ans = self.quiz.check_answer(user_answer="False")
        self.give_feedback(ans)
        #self.get_next_question()

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

    def button_state(self, state:str):
        self.tick.config(state=state)
        self.cross.config(state=state)

