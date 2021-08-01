from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.core.clipboard import Clipboard
from kivymd.uix.snackbar import Snackbar
import base64


class decoderlayout(BoxLayout):
    pass


class decoderApp(MDApp):

    data={
        "Encode":"cog-clockwise",
        "Decode":"cog-counterclockwise"
    }

    def callback(self,instance):
        if instance.icon == "cog-clockwise":
            self.encode()
        elif instance.icon == "cog-counterclockwise":
            self.decode()
    

    def build(self):
        root_widget = decoderlayout()
        self.icon = "assets/tinyicon.png"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "DeepPurple"
        self.title = 'B64Decoder'
        return root_widget

    def decode(self):
        try:
            self.root.ids.text_field.text = base64.b64decode(
                self.root.ids.text_field.text.encode('utf-8'))
            try:
                Clipboard.copy(self.root.ids.text_field.text)
                Snackbar(text="Copied to clipboard").open()
            except:
                pass
        except:
            pass

    def encode(self):
        try:
            self.root.ids.text_field.text = base64.b64encode(
                self.root.ids.text_field.text.encode('utf-8'))
            try:
                Clipboard.copy(self.root.ids.text_field.text)
                Snackbar(text="Copied to clipboard").open()
            except:
                pass
        except:
            pass


decoderApp().run()
