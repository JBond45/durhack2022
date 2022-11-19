# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

init python:
    def checkStr(given):
        if given[0] == given[-1] and given[0] == '''"''':
            return True
        return False

    def talkToPy(*options):
        # Usage:
        # python:
        #    ouput = talkToPy("option 1", "option 2")
        #"[output]"
        optionStr = ""
        for option in range(len(options)):
            optionStr = optionStr + "{0} = ".format(chr(option + 65)) + options[option] + "\n"
        optionStr = optionStr + "\nPrint the statement you want to say using the 'print(X)' function."

        reply = renpy.input(optionStr)
        if reply[0:-2] == "print(" and reply[-1] == ")":
            if ord(reply[-2]) - 65 < len(options):
                return options[ord(reply[-2]) - 65]

        return "They stare at you blankly. You started talking but you never opened your mouth."
        


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"
    
    python:
        output = talkToPy("Wow, its so beautiful today...", "I love the colour of this carpet.")
    "[output]"

    # variable tutorial
    python:

        # python asking abt your fav drink
        rightFormat = False
        while not rightFormat:
            inp = renpy.input("What is your favourite drink? Maybe they have it at the cafe downstairs.\n Define a string called 'favourite_drink'.")
            inpList = [x.strip() for x in inp.split("=")]
            # if correct variable name
            if len(inpList) > 1 and inpList[0] == "favourite_drink":
                # if correct quotation marks
                if inpList[1][-1] == inpList[1][0] and inpList[1][0] == '''"''':
                    # defined a variable correctly - end loop
                    output = "Oooo nice, I think {0} is my great aunt C's favourite.".format(inpList[1].strip())
                    rightFormat = True

                else:
                    output = """You started talking but didn't produce any sound... why not try using quotation marks (") around the message?"""

            else:
                output = "Umm... it's nice of you to tell me about {0}".format(inpList[0]) + " but that's not your 'favourite_drink'."

            e(output)

            e("It's really important to name variables with words so that everyone can understand them... or it could get really confusing when you forget what they mean.")

        # javascript asking how much you want to spend
        correctType = False
        while not correctType:
            inp = renpy.input("How much do you have to spend? Tell me in whole numbers, like an integer. No decimals.")
            if inp.isdigit():
                # if is an integer
                correctType = True
            else:
                e("I don't understand - that doesn't sound like the integer I was expecting.")

        e("let spend = [inp]")
        if int(inp) < 5:
            e("Dont worry... Ill pay for you.")
        else:
            e("Great! Let's get coffee together.")

        # javascript doing lists
        correctType = False
        while not correctType:
            inp = renpy.input("What do you want in your coffee? Make a list called my_list. Milk, sugar, decaf... etc. remember they need to be strings in a list using square brackets!")
            if inp[-2:] == '];':
                if inp[:15] == 'let my_list = [' or inp[:13] == 'let my_list = [':
                    inpList = inp.split("[")[1][:-2]
                    stringList = inpList.split(",")
                    stringChecker = [checkStr(x.strip()) for x in stringList]
                    if False not in stringChecker:
                        e("Great! \nHi, I'd like a latte, and my friend will have a coffee with {0}".format(inpList))
                        correctType = True

    return
