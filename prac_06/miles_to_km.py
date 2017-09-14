from kivy.app import App
from kivy.lang import Builder

class MilesToKm(App):
    def build(self):
        self.title = "Convert Miles to Kilometers "
        self.root = Builder.load_file('miles_to_km.kv')
        return self.root

    def handle_calculate(self, value):
        """Handle calculation (could be button press or other call),
        output result to label widget."""
        # if self.root.ids.input_miles.text.isnumeric() == True:
        try:
            result = int(self.root.ids.input_miles.text) * 1.60934
            self.root.ids.output_label.text = str("{:.3f}".format(result))

        except ValueError:
            self.root.ids.input_miles.text = '0'
        # elif self.root.ids.input_miles.text == "":
        #     self.root.ids.input_miles.text = '0'
        # # else:
        # #     self.root.ids.output_label.text = '0.000'


    def increment_value(self, value, input_value):
        result = int(input_value) + value
        self.root.ids.input_miles.text = str("{}".format(result))


MilesToKm().run()