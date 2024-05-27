from kivymd.uix.bottomnavigation.bottomnavigation import MDScreen 
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang import Builder 
from kivymd.uix.screenmanager import MDScreenManager 
from kivymd.uix.screen import MDScreen 
from kivy.app import App

class Primeiratela(MDApp):
    pass

class telalogin(MDScreen):
    pass

class segundatela(MDApp): 
    pass



class Aplicativo(MDApp):
    
    Window.size = (360, 600)
    
    def build(self):
        
        Window.clearcolor = (0, 0, 0, 1)
        
        return 
    
Aplicativo().run()
    
    

