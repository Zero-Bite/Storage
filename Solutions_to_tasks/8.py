class Rainbow:

    def __init__(self, number_of_type=1):

        if number_of_type == 1:
            self.type = 1
        elif number_of_type == 2:
            self.type = 2
        else:
            self.type = 3

    def next_color(self, name):

        # name_of_color = {1: "red",
        #                  2: "orange",
        #                  3: "yellow",
        #                  4: "green",
        #                  5: "light blue",
        #                  6: "blue",
        #                  7: "violet",
        #                  }

        name_of_color = ["red", "orange", "yellow", "green", "light blue", "blue", "violet"]

        if self.type == 1:
            for item in name_of_color.items():
                if item[1] == name and name != 'violet':

        elif self.type == 2:
            pass
        else:
            self.type = 3


tmp = Rainbow(1)
tmp.next_color("blue")
