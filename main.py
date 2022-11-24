#Importy Kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

import screens.summary_screen
# Importy ekranów
from screens.TestScreen import TestScreen
from screens.quesion_screen import QuestionScreen
from screens.CorrectAnswersScreen import CorrectAnswersScreen
from screens.summary_screen import SummaryScreen
from screens.DifficultyScreen import DifficultyScreen
from screens.CategoryScreen import CategoryScreen
from screens.MainScreen import MainScreen


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
        sm.add_widget(QuestionScreen())
        sm.add_widget(MainScreen())
        sm.add_widget(CorrectAnswersScreen())
        sm.add_widget(SummaryScreen())
        sm.add_widget(DifficultyScreen())
        sm.add_widget(CategoryScreen())

        return sm


if __name__ == '__main__':
    QuizApp().run()