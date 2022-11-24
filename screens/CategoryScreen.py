from kivy.uix.screenmanager import Screen

class CategoryScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.name = "Category"
