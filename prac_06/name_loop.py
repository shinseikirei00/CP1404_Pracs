from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Label
from kivy.properties import StringProperty


class name_loop(App):
    def __init__(self, **kwargs):
        """
        Construct main app
        """
        super().__init__(**kwargs)
        self.names = ['Jan', 'Jim', 'Jack', 'Silv', 'Josh', 'Dave']

    def build(self):
        """
        Build the Kivy GUI
        :return: reference to the root Kivy widget
        """
        self.title = "Name Loop Widget"
        self.root = Builder.load_file('name_loop.kv')
        self.create_widgets()
        return self.root


    def create_widgets(self):
        """
        Create buttons from dictionary entries and add them to the GUI
        :return: None
        """
        for name in self.names:
            # create a button for each phonebook entry
            temp_label = Label(text=name)
            # add the button to the "entriesBox" using add_widget()
            self.root.ids.entriesBox.add_widget(temp_label)


    def clear_all(self):
        """
        Clear all of the widgets that are children of the "entriesBox" layout widget
        :return:
        """
        self.root.ids.entriesBox.clear_widgets()



name_loop().run()
