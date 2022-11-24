from kivy.uix.screenmanager import Screen

class QuestionScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.name = "QuestionScreen"
