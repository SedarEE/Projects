class ColourChanger:
    def __init__(self):
        self.colour_replacement = {'red': 'black', 'green': 'white'}


    def make_readable(self, colours):
        result = []

        if ('red' in colours or 'Red' in colours) and ('green' in colours or 'Green' in colours):
            for col in colours:
                if col in self.colour_replacement: # Here it checks if color (in lower) is in color_replacement
                    result.append(self.colour_replacement[col])

                elif col.lower() in self.colour_replacement: #If color is not in lower, 
                        #this makes it lower to check if the color is in color_replacement, and then returns it in title 
                    result.append(self.colour_replacement[col.lower()].title())

                else:
                    result.append(col)

            return result
        else: 
            return colours


c = ColourChanger()
print(c.make_readable(['Red', 'green', 'white', 'pink', 'yellow', 'red']))
print(c.make_readable(['red', 'Green']))
print(c.make_readable(['red', 'red', 'yellow', 'Red']))
