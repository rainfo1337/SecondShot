## Работать, сука!
label start:
    $ chapter = 0
    $ _dismiss_pause = config.developer
    $ quick_menu = True
    $ style.say_dialogue = style.normal
    $ in_sayori_kill = None
    $ allow_skipping = True
    $ config.allow_skipping = True

    ## ...
    "I was here, and my only name is JOHN CENA!"
    m "Чего?"

label endgame(pause_length=4.0):
    $ quick_menu = False
    stop music fadeout 2.0
    scene black
    show image "gui/end.png"
    with dissolve_scene_full
    pause pause_length
    $ quick_menu = True
    return
