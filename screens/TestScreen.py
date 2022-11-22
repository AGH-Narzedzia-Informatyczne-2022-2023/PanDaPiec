from kivy.uix.screenmanager import Screen

class TestScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.name = "Test"
