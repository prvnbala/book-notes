from sys import exit
prompt = "> "


def gold_room():
    print("This room is full of gold. How much do you take?")
    next = input(prompt)
    
    try:
        how_much = int(next)
    except Exception as ex:
        dead("Man, learn to type a number.")
    
    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard!")


def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False
    
    while True:
        print("- take honey")
        print("- taunt bear")
        print("- open door")
        next = input(prompt)
        
        if next == "take honey":
            print("The bear looks at you then slaps your face off.")
        elif next == "taunt bear" and not bear_moved:
            print("The bear has moved from the door. You can go through it now.")
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            print("The bear gets pissed off and chews your leg off.")
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")


def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head.")
    print("- flee? \n- head?")
    next = input(prompt)
    
    if "flee" in next:
        start()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room()


def dead(why):
    print(why, "Good job!")
    exit(0)


def start():
    print("You're in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")
    print("- left")
    print("- right")
    
    next = input(prompt)
    
    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")


start()