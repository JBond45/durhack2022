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
define console = Character('Console', color="#FFFFFF")

init python:
    def checkStr(given):
        if given[0] == given[-1] and (given[0] == '''"''' or given[0] == "'"):
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
                        p("Umm... I asked for {0}.".format(given))
                else:
                    done = True

            else:
                p("hmm... you started talking but never opened your mouth. Did you use print(x) and write the variable name in the brackets?")

    def consoleInput(inp, given = ""):
        done = False
        while not done:
            inp = renpy.input("Can you put that in the console so I can hear you? Try using console.log(x); and put the name of the variable you just defined in the brackets.;")
            if inp[:12] == "console.log(" and inp[-2:] == ");":
                if len(given) > 0:
                    if inp[12:-2] == given:
                        done = True

                    else:
                        j("Umm... I asked for {0}.;".format(given))
                else:
                    done = True

            else:
                j("hmm... you started talking but never opened your mouth.;")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    
    scene bg hallway
    with Dissolve(.5)
    "You take the last sip of your 50th cup of coffee, You're at Durhack"
    "Maybe that was a bit too much caffine, you start to feel weird....."
    
    scene bg black
    with Dissolve(.5)
    "This doesn't feel like a normal nap... In fact it feels like a whole new world. Will you say hello to this world?"
    menu:
        "answer = True":
            console "print(answer)"
            $ renpy.input("", default="Hello world.")
        "answer = False":
            console "print(answer)"

    
    scene bg onground
    with Dissolve(.5)
    "You wake up."
    "Someone is standing over you."
    play music "music/scratch.wav"

    show scratch happy
    s "Meow"
    scene bg offground
    "The cat (guy?) dashes off, huh, guess you should follow them back into the MCS cafe. Maybe they've started serving the food."
    scene bg compscicafe
    with Dissolve(.5)
    play music 'music/coffeeDate.wav'
    show py happy at right
    show js normal at left
    "This is definitely the Cafe you know and love, but where were all the people? There's only two here, and they both look like they've jumped out of Coolors.com."
    "They've both noticed you, maybe noticed that you don't quite belong."
    show js displeased at left
    "The girl looks at you and points to her hair - oh, yikes! You've got a leaf in your hair, how did that get there?"
    show js bashful at left
    "The guy discretely points out you also have mud on your face. You should have really expected this after waking up on a path."
    "Who do you want to talk to?"
    menu:
        "let answer = 'The Girl';":
            jump Intro_js
        
        "answer = 'The Guy'":
            jump Intro_py

    label Intro_py:
        hide js normal
        show py happy at center
        
        python:
            global met_py
            met_py = True
        p "Hi, I'm python, Welcome to MCS, What is your name?"
        "{i}(Python? Like the programming language? WHAT HAPPENED?!){/i}"
        python:
            name = renpy.input("")
        p "[name], that's a nice name!"
        p "Would you like to come get a coffee with me?"
        menu:
            "answer = 'yes'":
                console "print(answer)"
                jump py_coffee
            "answer = 'no, in fact I wanna go with the girl over there'":
                console "print(answer)"
                p "That's alright! You'll have a chance to meet me properly soon enough anyway."
                jump firstjs_coffee


        
    label Intro_js:
        hide py happy
        show js normal at center
        j "Sup. What's ya name variable?;"
        python:
            name = renpy.input("")
        j "[name], huh, I'm JavaScript;"
        "{i}(JavaScript? Like the programming language? WHAT HAPPENED?!){/i}"
        j "Wanna get a drink?;"
        menu:
            "let answer = 'yes';":
                console "console.log(answer);"
                jump js_coffee
            "let answer = 'no, in fact I wanna go with the guy over there';":
                show js displeased at center
                console "console.log(answer);"
                j "Oh... okay. It's not like I was going to ask you to give me a list of your favourite webpage coffee attributes or anything.;"
                jump Firstpy_coffee



label firstjs_coffee:
    hide py happy at center
    show js normal at center
    j "Sup. What's ya name variable?;"
    python:
        name = renpy.input("")
    j "[name], huh, I'm JavaScript;"
    "{i}(JavaScript? Like the programming language? WHAT HAPPENED?!){/i}"

label js_coffee:
    scene bg compscicafe
    show js normal at right
    j "Here we are at the front of the queue;"
    python:
   
        # javascript asking how much you want to spend
        correctType = False
        while not correctType:
            inp = renpy.input("How much do you have to spend? Tell me in whole numbers, like an integer. No decimals.;")
            if inp.isdigit():
                # if is an integer
                correctType = True
            else:
                j("I don't understand - that doesn't sound like the integer I was expecting.;")
                
        if int(inp) < 5:
            j("Dont worry... I will pay for you.;")
        else:
            j("Great! Let's get coffee together.;")
                # javascript doing lists
        correctType = False
        while not correctType:
            inp = renpy.input('''What do you want in your coffee? Make a list called my_list. "milk", "sugar", "decaf", "etc.. remember they need to be strings in a list using square brackets!;''')
            if inp[-2:] == '];':
                if inp[:15] == 'let my_list = [' or inp[:13] == 'let my_list=[':
                    inpList = inp.split("[")[1][:-2]
                    stringList = inpList.split(",")
                    stringChecker = [checkStr(x.strip()) for x in stringList]
                    if False not in stringChecker:
                        consoleInput("my_list")
                        j("Great! \nHi, I'd like a latte, and my friend will have a coffee with {0}.;".format(inpList))
                        correctType = True
                    else:
                        j("I couldn't hear you? You were mumbling.;")
                else:
                    j("Um, I don't know a variable named like that... did you remember to use 'let' to define a new variable?")

            else:
                j("Did you forget your semicolon?;")

    j "This was nice, but I've got to go now. Durhack waits for no one."

    jump end
    


label Firstpy_coffee:
    scene bg compscicafe
    show py happy at right
    p "Hey I'm Python... You seem a little disorientated. You want to come sit with me and chat?"

label py_coffee: 
    scene bg compscicafe
    show py happy at right
    p "ok, lets grab a drink first!"

    python:
        # python asking abt your fav drink
        rightFormat = False
        while not rightFormat:
            inp = renpy.input("What is your favourite drink? Maybe they have it at the cafe.\n Define a string called 'favourite_drink'.")
            inpList = [x.strip() for x in inp.split("=")]
            # if correct variable name
            if len(inpList) > 1 and inpList[0] == "favourite_drink":
                # if correct quotation marks
                if inpList[1][-1] == inpList[1][0] and inpList[1][0] == '''"''':
                        printInput("favourite_drink")
                        # end of loop
                        output = "Oooo nice, I think {0} is my great aunt C's favourite.".format(inpList[1].strip())
                        rightFormat = True

                else:
                    output = """You started talking but didn't produce any sound... why not try using quotation marks (") around the message?"""

            else:
                output = "Umm... it's nice of you to tell me about {0}".format(inpList[0]) + " but that's not your 'favourite_drink'."

            p(output)
            p("It's really important to name variables with words so that everyone can understand them... or it could get really confusing when you forget what they mean.")
    
        # python doing lists
        correctType = False
        while not correctType:
            inp = renpy.input('''What do you want in your coffee? Make a list called my_list. "milk", "sugar", "decaf", "etc." remember they need to be strings in a list using square brackets!''')
            if inp[-1:] == ']':
                if inp[:11] == 'my_list = [' or inp[:9] == 'my_list=[':
                    inpList = inp.split("[")[1][:-1]
                    stringList = inpList.split(",")
                    stringChecker = [checkStr(x.strip()) for x in stringList]
                    if False not in stringChecker:
                        printInput("my_list")
                        p("Great! \nHi, I'd like a latte, and my friend will have a coffee with {0}".format(inpList))
                        correctType = True

                    else:
                        p("Sorry? You mumbled somewhere in the middle there...")
                else:
                    p("That's not the list I expected, is your syntax alright?")

    hide py happy
    show py sitting:
        xpos 0.65 ypos 0.0
    p "So, have you come here for durhack?"
    menu:
        "answer = 'Yeah, I did?'":
            console "print(answer)"
            p "Nice! I've come here every year since Durhack started."

        "answer = 'No, I came for free food.'":
            console "print(answer)"
            hide py sitting at center
            show py sad at right
            p "Oh... well I suppose that is a noble cause."
            p "You know, maybe you should consider joining in. Even if you've never coded before, there's so many chances here to learn!"
        
    p "The energy is really quite something... So many people coding; creating! Do you know this feeling? This breeze of passion, which has traveled from the innovations towards which I am advancing, gives me a foretaste of those icy logical climes..."
    hide py sitting at center
    show py flustered at center
    p "Inspirited by this wind of promise, my capabilities and compatabilities become more fervent and vivid. I try in vain to be persuaded that the people are the seat of frost and desolation; it ever presents itself to my imagination as the region of beauty and delight."
    p "There, in the people here, the sun is forever visible, its broad disk just skirting the horizon and diffusing a perpetual splendour of coding mania!"
    p "Oh sorry... I got a little carried away there. I'm just really passionate about hackathons I guess."
    show py sad at center
    p "Rattle snakes! Is that the time? I've got to get hacking. I'll see you around."
    hide py sad at center
    with moveoutright

    jump end


    # This ends the game.
label end:
    "Were those programming languages? Am I in the Durhack Universe?! I thought that was a myth!"
    return