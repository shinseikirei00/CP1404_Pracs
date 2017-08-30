# based on the state_names prac
# hex_colours prac by: Jan Crooks

COLOUR_CODE = {"AliceBlue": "#f0f8ff", "AntiqueWhite1": "#ffefdb", "AntiqueWhite3": "#cdc0b0",
               "aquamarine1": "#7fffd4", "aquamarine4": "#458b74", "azure2": "#e0eeee",
               "azure4": "#838b8b", "bisque1": "#ffe4c4", "bisque3": "#cdb79e", "black": "#000000",
               "blue1": "#0000ff", "blue4": "#00008b", "brown": "#a52a2a", "brown2": "#ee3b3b"}

colour_name = input("Enter a colour name: ")
while colour_name != "":
    print("The code for } is {}".format(colour_name, COLOUR_CODE.get(colour_name)))
    colour_name = input("Enter a colour name: ")
