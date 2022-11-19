# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character("Python", color="#306998")
define j = Character("JavaScript", color="#F0DB4F")
define s = Character("Scratch", color= "#f6ab3c")
define u = Character("You")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    
    scene bg CompSciCafe
    with Dissolve(.5)
    "You take the last sip of your coffee, You're at Durhack"
    "Maybe that was a bit to much caffine, you start to feel wierd....."
    
    scene bg black
    with Dissolve(.5)
    "You Wake Up"
    scene bg Outside 1
    with Dissolve(.5)
    "You feel something warm touching your face your face"
    show scratch happy
    "s""Meow"
    hide scratch Happy
    "The cat (guy?) dashes off, huh, guess you should follow them"
    scene bg CompSciCafe
    with Dissolve(.5)
    show py happy at right
    show js at left
    "There are two people in the MCS cafe currently, Who do you want to talk to?"
    menu:
        "The Girl":
            jump js_coffee#Intro_js
        
        "The Guy":
            jump py_coffee#Intro_py

    label Intro_py:
        hide js
        show py happy at center
        "p""Hi, I'm python, Welcome to MCS, What is your name?"
        python:
            name = renpy.input("")
        "p""[name], that's a nice name!"


        
    label Intro_js:
        hide py happy
        show js at center
        "j""Sup."



label js_coffee:
    scene bg MCSTill
    show js neutral at right
    "j""sup"
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


label py_coffee:
    scene bg MCSTill
    show py happy at right
    "p""Lets get a drink!"
    



    # This ends the game.

    return
