class Language:
    def __init__(self , which_language):
        self.which_language = which_language

    def which_language_be_known(self):
        if self.which_language == False:
            print("You must learn Kannada")
        elif self.which_language == True:
            print("Then you are a Kannadigaa")
        else:
            print("Invalid")

class Kannada(Language):
    def __init__(self, which_language):
        self.which_language = which_language
        super().__init__(which_language)

x = input("Do you know kannada (True/False)")

y = Kannada(True)
y.which_language_be_known()

