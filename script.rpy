# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
python:
    global met_js
    global met_py
    met_js = False
    met_py = False

define p = Character('Python', color="#306998")
define j = Character('JavaScript', color="#F0DB4F")
define s = Character('Scratch', color= "#f6ab3c")
define u = Character('You')

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

    def printInput(given = ""):
        done = False
        while not done:
            inp = renpy.input("Could you print that for me?")
            if inp[:6] == "print(" and inp[-1] == ")":
                if len(given) > 0:
                    if inp[6:-1] == given:
                        done = True

                    else:
                        e("Umm... I asked for [given].")
                else:
                    done = True

            else:
                e("hmm... you started talking but never opened your mouth.")

    def consoleInput(inp, given = ""):
        done = False
        while not done:
            inp = renpy.input("Could you console.log that for me?")
            if inp[:12] == "console.log(" and inp[-2:] == ");":
                if len(given) > 0:
                    if inp[12:-2] == given:
                        done = True

                    else:
                        e("Umm... I asked for [given].")
                else:
                    done = True

            else:
                e("hmm... you started talking but never opened your mouth.")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    
    scene bg compscicafe
    with Dissolve(.5)
    "You take the last sip of your coffee, You're at Durhack"
    "Maybe that was a bit to much caffine, you start to feel wierd....."
    
    scene bg black
    with Dissolve(.5)
    "You Wake Up"
    scene bg outside1
    with Dissolve(.5)
    "You feel something warm touching your face your face"
    show scratch happy
    s "Meow"
    hide scratch Happy
    "The cat (guy?) dashes off, huh, guess you should follow them"
    scene bg compscicafe
    with Dissolve(.5)
    show py happy at right
    show js normal at left
    "There are two people in the MCS cafe currently, Who do you want to talk to?"
    menu:
        "The Girl":
            jump Intro_js
        
        "The Guy":
            jump Intro_py

    label Intro_py:
        hide js normal
        show py happy at center
        
        python:
            global met_py
            met_py = True
        p "Hi, I'm python, Welcome to MCS, What is your name?"
        python:
            name = renpy.input("")
        p "[name], that's a nice name!"
        j "Would you like to come get a coffee with me?"
        menu:
            "yes":
                jump py_coffee
            "no, in fact I wanna go with the girl over there":
                jump firstjs_coffee


        
    label Intro_js:
        hide py happy
        show js normal at center
        j "Sup. What's ya name?"
        python:
            name = renpy.input("")
        j "[name], huh, I'm JavaScript"
        j "Wanna get a drink?"
        menu:
            "yes":
                jump js_coffee
            "no, in fact I wanna go with the guy over there":
                jump Firstpy_coffee



label firstjs_coffee:
    scene bg mcstill
    show js normal at right
    j "hey I'm JavaScript.....You want to grab a drink with me? Ok, lets go"
label js_coffee:
    scene bg mcstill
    show js normal at right
    j "Here we are at the front of the queue"
    python:
   
        # javascript asking how much you want to spend
        correctType = False
        while not correctType:
            inp = renpy.input("How much do you have to spend? Tell me in whole numbers, like an integer. No decimals.")
            if inp.isdigit():
                # if is an integer
                correctType = True
            else:
                j("I don't understand - that doesn't sound like the integer I was expecting.")
                
        if int(inp) < 5:
            j("Dont worry... Ill pay for you.")
        else:
            j("Great! Let's get coffee together.")
                # javascript doing lists
        correctType = False
        while not correctType:
            inp = renpy.input("What do you want in your coffee? Make a list called my_list. Milk, sugar, decaf... etc. remember they need to be strings in a list using square brackets!")
            if inp[-2:] == '];':
                if inp[:15] == 'let my_list = [' or inp[:13] == 'let my_list=[':
                    inpList = inp.split("[")[1][:-2]
                    stringList = inpList.split(",")
                    stringChecker = [checkStr(x.strip()) for x in stringList]
                    if False not in stringChecker:
                        consoleInput("my_list")
                        j("Great! \nHi, I'd like a latte, and my friend will have a coffee with {0}".format(inpList))
                        correctType = True
    jump end
    


label Firstpy_coffee:
    scene bg mcstill
    show py happy at right
    p "hey I'm Python.....You want to come sit with me and chat?"
label py_coffee: 
    scene bg mcstill
    show py happy at right
    p "ok, lets grab a drink first!"

    
    



    # This ends the game.
label end:
    return