# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define hero = Character("????")
define g = Character("Gandalf")


# The game starts here.

label start:

    $ sword = False
    $ bow = False
    $ staff = False

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg mount_dragon

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show gandalf

    # These display lines of dialogue.

    g "Chosen one! Finally you have arrived."

    python:
        name = renpy.input("There isn't much time. Quickly! What should I call you?")
        name = name.strip() or "Hero"

    define hero = Character("[name]")

    g "So it's [name] is it?"

    hero "That's me."

    g "Here, pick a weapon. You'll need it for what's up ahead."

    menu:

        "Sword":
            $ sword = True
            g "Good choice. That should be useful when you're up close."
            jump choice1_done

        "Bow":
            $ bow = True
            g "You've got a keen eye. You can hit enemies from a distance with this."
            jump choice1_done

        "Staff":
            $ staff = True
            g "The staff? I don't think it'll be of much use to you but, well, if that's what you want."
            jump choice1_done

label choice1_done:

    g "There's nothing left for me to give you"

    g "Go now into the mountains. The great lizard awaits you on its peak."

    g "I pray you succeed for the sake of all the worlds."

    hide gandalf

    "Gandalf turns and walks away, fading into the distance."

    "You begin your approach to the mountain and spot a lone goblin not too far away. It hasn't noticed your presence."

    show goblin_far


    if bow:
        menu:
            "Approach the goblin":
                jump close_goblin1

            "Avoid the goblin":
                "You take a different route towards the mountain, circling around the goblin until it leaves your sight."
                hide goblin_far
                "You suddenly hear a quick footsteps approaching. You turn to look back and see the goblin chasing after you."
                jump close_goblin1

            "Shoot the goblin":
                    "Your arrow hits true. The goblin goes down with a *thud*. You approach the goblin."
                    jump dead_goblin1
    else:
        menu:
            "Approach the goblin":
                jump close_goblin1

            "Avoid the goblin":
                "You take a different route towards the mountain, circling around the goblin until it leaves your sight."
                hide goblin_far
                "You suddenly hear a quick footsteps approaching. You turn to look back and see the goblin chasing after you."
                jump close_goblin1

label close_goblin1:
    show goblin_close
    "The goblin glares at you with menace."
    if sword:
        "You take your sword out. The goblin charges at you. You nimbly parry the goblin's dagger and slash through its chest."
        jump dead_goblin1

    elif staff:
        "You take your staff out. The goblin charges at you. You realise you don't know how to use magic and panic."
        "In your moment of hesitation you feel cold steel cut through your chest. You fall to the ground and your vision begins to blur..."
        jump start

    elif bow:
        "Your bow is useless in close range. The goblin charges at you. You panic."
        "In your moment of hesitation you feel cold steel cut through your chest. You fall to the ground and your vision begins to blur..."
        jump start

label dead_goblin1:
    hide goblin_close
    hide goblin_far
    show goblin_dead
    "The goblin lays dead before you."
    "You notice a parchment in its pocket."
    show map_partial
    "It's a map of the mountain. Albeit just a partial map."
    $ partial_map = True
    "You take the map with you"

    # This ends the game.

    return
