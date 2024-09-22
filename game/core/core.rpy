python early:
    import math
    import datetime
    import random
    import re
    import os
    import subprocess
    import platform
    import urllib.request
    import ssl
    config.atl_start_on_show = False

    class IllegalModLocation(Exception):
        def __str__(self):
            return "Смените местоположение папки с модом."

init -1 python:
    ssl._create_default_https_context = ssl._create_unverified_context
    try:
        from store.achievements import achievementList, Achievement, AchievementCount
    except ModuleNotFoundError:
        pass
    try:
        from store.gallery import GalleryImage, galleryList
    except ModuleNotFoundError:
        pass

init -100 python:
    if renpy.windows:
        onedrive_path = os.environ.get("OneDrive")
        if onedrive_path is not None:
            if onedrive_path in config.basedir:
                raise IllegalModLocation

init python:
    def process_check(stream_list):
        if not renpy.windows:
            for index, process in enumerate(stream_list):
                stream_list[index] = process.replace(".exe", "")
        
        for x in stream_list:
            for y in process_list:
                if re.match(r"^" + x + r"\b", y):
                    return True
        return False

image splash_warning = ParameterizedText(style="splash_text", xalign=0.5, yalign=0.5)

image menu_logo:
    "gui/logo.png"
    subpixel True
    xcenter 240
    ycenter 120
    zoom 0.60

image menu_bg:
    Movie(play="gui/menu_bg.webm")

image game_menu_bg:
    topleft
    Movie(play="gui/menu_bg.webm")

image menu_fade:
    "white"
    menu_fadeout()

image menu_art_y:
    subpixel True
    "gui/menu_art_y.png"
    xcenter 750
    ycenter 695
    zoom 1.12

image menu_nav:
    "gui/overlay/main_menu.png"

transform menu_logo_move:
    subpixel True
    yoffset -300
    time 1.925
    easein_bounce 1.5 yoffset 0

transform menu_nav_move:
    subpixel True
    xoffset -500
    time 1.5
    easein_quint 1 xoffset 0

transform menu_fadeout:
    easeout 0.75 alpha 0

transform menu_art_move(z, x, z2):
    subpixel True
    yoffset 0 + (1200 * z)
    xoffset (740 - x) * z * 0.5
    zoom z2 * 0.75
    time 1.0
    parallel:
        ease 1.75 yoffset 0
    parallel:
        pause 0.75
        ease 1.5 zoom z2 xoffset 0

image intro:
    truecenter
    "white"
    0.5
    "gui/rgsr.webp" with Dissolve(0.5, alpha=True)
    2.5
    "white" with Dissolve(0.5, alpha=True)

image warning:
    truecenter
    "white"
    "splash_warning" with Dissolve(0.5, alpha=True)
    2.5
    "white" with Dissolve(0.5, alpha=True)
    0.5

image tos = "bg/warning.png"
image tos2 = "bg/warning2.png"

default persistent.first_run = True

label splashscreen:
    python:
        for name in ('LOGNAME', 'USER', 'LNAME', 'USERNAME'):
            user = os.environ.get(name)
            if user:
                currentuser = user

    if persistent.first_run:
        $ quick_menu = False
        scene white
        pause 0.5
        scene tos
        with Dissolve(1.0)
        pause 1.0

        "«Дубль два» -- фанатская модификация на игру «Doki Doki Literature Club», никак не связанная с разработчиками игры в лице Team Salvato."
        "Во избежание спойлеров рекомендуем поиграть в оригинальную игру, которую вы можете скачать на официальном сайте или в Steam."
        "Мод, как и игра, не рекомендован к прохождению лицам младше 18 лет и старше 60 лет, лицам со слабым душевным здоровьем и беременным женщинам."

        menu:
            "Играя в «Дубль два» вы подтверждаете то, что ознакомились с предупреждениями, и с тем, что только вы несёте ответственность за возможные последствия."
            "Подтверждаю":
                pass
            "Не подтверждаю":
                $ sys.exit()

        $ persistent.first_run = False
        scene tos2
        with Dissolve(1.5)
        pause 1.0

        scene white

    #if not persistent.special_poems:
    #    python hide:
    #        persistent.special_poems = [0,0,0]
    #        a = list(range(1,12))
    #        for i in range(3):
    #           b = renpy.random.choice(a)
    #            persistent.special_poems[i] = b
    #            a.remove(b)

    $ basedir = config.basedir.replace('\\', '/')

    $ config.allow_skipping = False

    show white
    $ persistent.ghost_menu = False
    $ config.main_menu_music = 'audio/gui/sfx/to-the-moon.mp3'
    $ renpy.music.play(config.main_menu_music)
    show intro with Dissolve(0.5, alpha=True)
    $ pause(2.5)
    hide intro with Dissolve(0.5, alpha=True)
    $ config.allow_skipping = True
    $ quick_menu = True
    return

label warningscreen:
    hide intro
    show warning
    pause 3.0

label before_main_menu:
    $ config.main_menu_music = 'audio/gui/sfx/to-the-moon.mp3'
    return

label quit:
    return
