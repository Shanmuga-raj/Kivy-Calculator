import kivy
from kivy.core import window
kivy.require("2.0.0")                                       # Version below than this will not run
from kivy.app import App                                    # Base class of CalculatorApp inherits from App class
from kivy.lang import Builder                               # To link the kivy design file
from kivy.uix.widget import Widget                          # Base class of MyLayout inherits from Widget class
from kivy.core.window import Window                         # To Set Default Window Size


# Find and Load our .kv Design File:
Builder.load_file("Calculator.kv")

# Set the App Window Size
Window.size = (400, 600)


class MyLayout(Widget):
    
    # Clear the Input Field:
    def clear(self):
        self.ids.calc_input.text = ""


    # Create a Button Press:
    def button_press(self, button):
        previous = self.ids.calc_input.text

        if "Error" in previous:
            previous = ""

        elif previous == "":
            self.ids.calc_input.text = f"{button}"

        else:
            self.ids.calc_input.text = f"{previous}{button}"


    def dot(self):
        previous = self.ids.calc_input.text
        num_list = previous.split("+")

        if "+" in previous and "." not in num_list[-1]:
            self.ids.calc_input.text = f"{previous}."

        elif "." in previous:
            pass

        else:
            self.ids.calc_input.text = f"{previous}."


    def backspace(self):
        previous = self.ids.calc_input.text
        self.ids.calc_input.text = previous[:-1]


    def equal_to(self):
        previous = self.ids.calc_input.text

        try:
            self.ids.calc_input.text = str(eval(previous))

        except:
            self.ids.calc_input.text =  "Error"


    def change_sign(self):
        previous = self.ids.calc_input.text

        if "-" in previous:
            self.ids.calc_input.text = f'{previous.replace("-","")}'
        
        else:
            self.ids.calc_input.text = f'-{previous}'


class CalculatorApp(App):    

    def build(self):
        return MyLayout()


if __name__ == "__main__":
    CalculatorApp().run()