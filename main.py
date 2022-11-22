#Importy Kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

# Importy ekranów
from screens.TestScreen import TestScreen

# Rozmiar okna
from kivy.config import Config
Config.set("graphics", "width", "360")
Config.set("graphics", "height", "640")
Config.set("graphics", "resizable", 0)
Config.write()

# Ekran debugowania
class DebugScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.name = "Debug"


# Punkt wejścia
class QuizApp(App):
    def build(self):
        sm = ScreenManager()

        # Tu dodajemy wszystkie ekrany
        sm.add_widget(DebugScreen())
        sm.add_widget(TestScreen())

        return sm


if __name__ == '__main__':
    QuizApp().run()