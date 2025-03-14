# boiler plate code to integrate frontend

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.lang import Builder
from kivy.core.clipboard import Clipboard


Builder.load_file('frontend.kv')

# backend
from filesharer import FileSharer
import time
import webbrowser


class CameraScreen(Screen): # acts as webCam object

    def start(self):
        self.ids.camera.play=True
        self.ids.camera_button.text='Stop Camera'
        self.ids.camera.opacity=1

    def stop(self):
        self.ids.camera.play=False
        self.ids.camera_button.text='Start Camera'
        self.ids.camera.texture=None
        self.ids.camera.opacity=0

    def capture(self):
        currentTime = time.strftime('%Y%m%d-%H%M%S')
        filePath = f'files/{currentTime}.png'
        self.ids.camera.export_to_png(filePath)
        self.manager.current='image_screen'
        self.manager.current_screen.ids.img.source=filePath



class ImageScreen(Screen):
    def create_link(self):
        file_path = self.manager.current_screen.ids.img.source
        file_sharer = FileSharer(file_path)
        self.url = file_sharer.share()
        self.ids.link.text=self.url

    def copy_link(self):
        try:
            Clipboard.copy(self.url)
        except:
            self.ids.link.text='Generate Link First'

    def open_link(self):
        try:
            webbrowser.open(self.url)
        except:
            self.ids.link.text='Generate Link First'


class RootWidget(ScreenManager):
    pass

class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()