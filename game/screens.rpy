init offset = -1
define -2 text_outline_color = "#4b4248"

style default:
    font gui.default_font
    size gui.text_size
    color gui.text_color
    outlines [(2, "#000000aa", 0, 0)]
    line_overlap_split 1
    line_spacing 1

style normal is default:
    xpos gui.text_xpos
    xanchor gui.text_xalign
    xsize gui.text_width
    ypos gui.text_ypos

    text_align gui.text_xalign
    layout ("subtitle" if gui.text_xalign else "tex")

style input:
    color gui.accent_color

style splash_text:
    size 24
    color "#000"
    font gui.default_font
    text_align 0.5
    outlines []

style poemgame_text:
    yalign 0.5
    font "gui/font/BordersDivideButHeartsShall.ttf"
    size 30
    color "#000"
    outlines []

    hover_xoffset -3
    hover_outlines [(3, "#fef", 0, 0), (2, "#fcf", 0, 0), (1, "#faf", 0, 0)]

style gui_text:
    font gui.interface_font
    color gui.interface_text_color
    size gui.interface_text_size

style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.button_text_properties("button")
    yalign 0.5


style label_text is gui_text:
    color gui.accent_color
    size gui.label_text_size

style prompt_text is gui_text:
    color gui.text_color
    size gui.interface_text_size

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style bar:
    ysize 18
    base_bar Frame("gui/scrollbar/horizontal_poem_bar.png", tile=False)
    thumb Frame("gui/scrollbar/horizontal_poem_thumb.png", top=6, right=6, tile=True)

style scrollbar:
    ysize 18
    base_bar Frame("gui/scrollbar/horizontal_poem_bar.png", tile=False)
    thumb Frame("gui/scrollbar/horizontal_poem_thumb.png", top=6, right=6, tile=True)
    unscrollable "hide"
    bar_invert True

style vscrollbar:
    xsize 18
    base_bar Frame("gui/scrollbar/vertical_poem_bar.png", tile=False)
    thumb Frame("gui/scrollbar/vertical_poem_thumb.png", left=6, top=6, tile=True)
    unscrollable "hide"
    bar_invert True

style slider:
    ysize 18
    base_bar Frame("gui/scrollbar/horizontal_poem_bar.png", tile=False)
    thumb "gui/slider/horizontal_hover_thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        text what id "what"

        if who is not None:

            window:
                style "namebox"
                text who id "who"

    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0

    use quick_menu

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label

style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Transform("gui/textbox.png", xalign=0.5, yalign=1.0)

style window_monika is window:
    background Transform("gui/textbox_monika.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    color gui.accent_color
    font gui.name_font
    size gui.name_text_size
    xalign gui.name_xalign
    yalign 0.5
    outlines [(3, text_outline_color, 0, 0), (1, text_outline_color, 1, 1)]

style say_dialogue:
    xpos gui.text_xpos
    xanchor gui.text_xalign
    xsize gui.text_width
    ypos gui.text_ypos

    text_align gui.text_xalign
    layout ("subtitle" if gui.text_xalign else "tex")

image ctc:
    xalign 0.81 yalign 0.98 xoffset -5 alpha 0.0 subpixel True
    "gui/ctc.png"
    block:
        easeout 0.75 alpha 1.0 xoffset 0
        easein 0.75 alpha 0.5 xoffset -5
        repeat

image input_caret:
    Solid("#b59")
    size (2,25) subpixel True
    block:
        linear 0.35 alpha 0
        linear 0.35 alpha 1
        repeat

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xpos gui.text_xpos
            xanchor 0.5
            ypos gui.text_ypos

            text prompt style "input_prompt"
            input id "input"


style input_prompt is default

style input_prompt:
    xmaximum gui.text_width
    xalign gui.text_xalign
    text_align gui.text_xalign

style input:
    caret "input_caret"
    xmaximum gui.text_width
    xalign 0.5
    text_align 0.5

screen choice(items):
    style_prefix "choice"

    vbox:

        for i in items:
            
            if "kwargs=" in i.caption:

                $ kwarg = i.caption.split("(kwargs=")[-1].replace(")", "")
                $ caption = i.caption.replace(" (kwargs=" + kwarg + ")", "")

                if "#" in kwarg:
                    
                    $ kwarg = kwarg.replace(", ", ",").split(",")
                    
                    if len(kwarg) == 1:
                        $ kwarg.append('#ffe6f4')
                    
                    $ arg1 = kwarg[0]
                    $ arg2 = kwarg[-1]
                    
                    textbutton caption:
                        idle_background Frame(im.MatrixColor(im.MatrixColor("gui/button/choice_idle_background.png", im.matrix.desaturate() * im.matrix.contrast(1.29) * im.matrix.colorize("#00f", "#fff") * im.matrix.saturation(120)), 
                            im.matrix.desaturate() * im.matrix.colorize(arg1, arg2)), gui.choice_button_borders)
                        hover_background Frame(im.MatrixColor(im.MatrixColor("gui/button/choice_hover_background.png", im.matrix.desaturate() * im.matrix.contrast(1.29) * im.matrix.colorize("#00f", "#fff") * im.matrix.saturation(120)), 
                            im.matrix.desaturate() * im.matrix.colorize(arg1, "#fff")), gui.choice_button_borders)
                        action i.action

                else:

                    textbutton caption:
                        style kwarg
                        action i.action

            else:

                textbutton i.caption action i.action

define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 270
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound
    idle_background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders)
    hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders)

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")
    outlines []

init python:
    def RigMouse():
        currentpos = renpy.get_mouse_pos()
        targetpos = [640, 345]
        if currentpos[1] < targetpos[1]:
            renpy.display.draw.set_mouse_pos((currentpos[0] * 9 + targetpos[0]) / 10.0, (currentpos[1] * 9 + targetpos[1]) / 10.0)

screen rigged_choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action

    timer 1.0/30.0 repeat True action Function(RigMouse)

screen quick_menu():

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 0.993
            spacing 12

            textbutton _("") action ShowMenu('history') # Feather, U+e939
            textbutton _("") action ShowMenu('glossary') # Feather, U+e923
            if inv_variable:
                textbutton _("") action ShowMenu('investigation') # Feather, U+e958
            textbutton _("") action Skip() alternate Skip(fast=True, confirm=True) # Feather, U+e934
            textbutton _("") action ShowMenu('save') # Feather, U+e955
            textbutton _("") action ShowMenu('load') # Feather, U+e9ef
            textbutton _("") action ShowMenu('preferences') # Feather, U+e9c4

default quick_menu = True

style quick_button:
    properties gui.button_properties("quick_button")
    activate_sound gui.activate_sound

style quick_button_text:
    properties gui.button_text_properties("quick_button")
    outlines []

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.8

        spacing gui.navigation_spacing

        if not persistent.autoload or not main_menu:

            if main_menu:
                textbutton _("Новая игра") action Start()
            else:
                textbutton _("История") action [ShowMenu("history"), SensitiveIf(renpy.get_screen("history") == None)]
            if not main_menu:
                textbutton _("Словарь") action [ShowMenu("glossary"), SensitiveIf(renpy.get_screen("glossary") == None)]
            if inv_variable:
                textbutton _("Дневник") action [ShowMenu("podmost"), SensitiveIf(renpy.get_screen("podmost") == None)]
            if not main_menu:
                textbutton _("Сохранить") action [ShowMenu("save"), SensitiveIf(renpy.get_screen("save") == None)]
            textbutton _("Загрузить") action [ShowMenu("load"), SensitiveIf(renpy.get_screen("load") == None)]
            textbutton _("Настройки") action [ShowMenu("preferences"), SensitiveIf(renpy.get_screen("preferences") == None)]
            if not main_menu:
                textbutton _("Главное меню") action MainMenu()
            textbutton _("Выйти") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")
    font "gui/font/Inconsolata-LGC.otf"
    color "#fff"
    outlines [(4, text_outline_color, 0, 0), (2, text_outline_color, 2, 2)]
    hover_outlines [(4, "#423239", 0, 0), (2, "#423239", 2, 2)]
    insensitive_outlines [(4, "#2b2b2b", 0, 0), (2, "#2b2b2b", 2, 2)]

screen main_menu():
    tag menu
    style_prefix "main_menu"

    add "menu_bg"
    add "menu_art_y"
    frame
    use navigation
    add "menu_logo"

    if gui.show_name:
        vbox:
            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"

    add "menu_fade"

    key "K_ESCAPE" action Quit(confirm=False)

style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text:
    color "#000000"
    size 16
    outlines []

style main_menu_frame:
    xsize 310
    yfill True

    background "menu_nav"

style main_menu_vbox:
    xalign 1.0
    xoffset -20
    xmaximum 800
    yalign 1.0
    yoffset -20

style main_menu_text:
    xalign 1.0

    layout "subtitle"
    text_align 1.0
    color gui.accent_color

style main_menu_title:
    size gui.title_text_size

screen game_menu(title, scroll=None):
    add "menu_bg"
    if not main_menu:
        key "mouseup_3" action Return()

    style_prefix "game_menu"

    frame:
        style "game_menu_outer_frame"

        hbox:

            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        yinitial 1.0

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial 1.0

                        scrollbars "vertical"
                        mousewheel True
                        draggable True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("Вернуться"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 30
    top_padding 120

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 280
    yfill True

style game_menu_content_frame:
    left_margin 40
    right_margin 20
    top_margin 10

style game_menu_viewport:
    xsize 920

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 10

style game_menu_label:
    xpos 50
    ysize 120

style game_menu_label_text:
    font "gui/font/Inconsolata-LGC.otf"
    size gui.title_text_size
    color "#fff"
    outlines [(6, text_outline_color, 0, 0), (3, text_outline_color, 2, 2)]
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -30

style about_window is empty
style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    color "#000"
    outlines []
    text_align 0.5
    size gui.label_text_size

style about_text:
    color "#000"
    outlines []
    size gui.text_size
    text_align 0.5
    layout "subtitle"

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    idle_color gui.idle_color
    hover_color gui.hover_color
    hover_underline True

screen save():
    tag menu
    use file_slots(_("Сохранить"))
screen load():
    tag menu
    use file_slots(_("Загрузить"))

screen file_slots(title):
    default page_name_value = FilePageNameInputValue(pattern=_("Страница {}"))
    use game_menu(title):
        fixed:
            order_reverse True
            button:
                style "page_label"
                xalign 0.5
                input:
                    style "page_label_text"
                    value page_name_value
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"
                xalign 0.5
                yalign 0.5
                spacing gui.slot_spacing
                for i in range(gui.file_slot_cols * gui.file_slot_rows):
                    $ slot = i + 1
                    button:
                        action FileAction(slot)
                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%d.%m.%Y, %H:%M:%S"), empty=_("пустой слот")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            
            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing
                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 50
    ypadding 3

style page_label_text:
    color "#000"
    outlines []
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")
    outlines []

style slot_button:
    properties gui.button_properties("slot_button")
    idle_background Frame("gui/button/slot_idle_background.png", gui.choice_button_borders)
    hover_background Frame("gui/button/slot_hover_background.png", gui.choice_button_borders)

style slot_button_text:
    properties gui.button_text_properties("slot_button")
    color "#666"
    outlines []

default preferences.afm_enable = False

screen ddlc_preferences():
    hbox:
        box_wrap True

        if renpy.variant("pc"):

            vbox:
                style_prefix "radio"
                label _("Отображение")
                textbutton _("В окне") action Preference("display", "window")
                textbutton _("На весь экран") action Preference("display", "fullscreen")

        vbox:
            style_prefix "check"
            label _("Пропускать")
            textbutton _("Непрочитанное") action Preference("skip", "toggle")
            textbutton _("После выборов") action Preference("after choices", "toggle")
            textbutton _("В авто-режиме") action Preference("auto-forward", "toggle")
    
    null height (4 * gui.pref_spacing)

    hbox:
        style_prefix "slider"
        box_wrap True

        vbox:
            
            hbox:
                label _("Скорость текста")
                
                null width 5

                text str(preferences.text_cps) style "value_text"

            bar value FieldValue(_preferences, "text_cps", range=180, max_is_zero=False, style="slider", offset=20)

            if preferences.afm_enable == True:
                hbox:
                    label _("Скорость авто-режима")
                
                    null width 5
                
                    text str(round(preferences.afm_time)) style "value_text"

                bar value Preference("auto-forward time")

        vbox:
            
            if config.has_music:
                hbox:
                    label _("Музыка")
                    
                    null width 5
                
                    text str(round(preferences.get_volume("music") * 100)) style "value_text"

                hbox:
                    bar value Preference("music volume")

            if config.has_sound:

                hbox:
                    label _("Звуки")
                    
                    null width 5
                
                    text str(round(preferences.get_volume("sfx") * 100)) style "value_text"

                hbox:
                    bar value Preference("sound volume")

            if config.has_music or config.has_sound:
                null height gui.pref_spacing

                textbutton _("Выключить всё"):
                    action Preference("all mute", "toggle")
                    style "mute_all_button"

screen preferences():

    tag menu

    use game_menu(_("Настройки"), scroll="viewport"):

        vbox:
            xoffset 50

            hbox:
                style_prefix "navigation"
                xoffset 150
                spacing 5
            
            null height 10

            use ddlc_preferences
                            
    text "[config.version]":
        xalign 1.0 yalign 1.0
        xoffset -10 yoffset -10
        style "main_menu_version"

style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 2

style pref_label_text:
    font "gui/font/Inconsolata-LGC.otf"
    size 24
    color "#fff"
    outlines [(3, "#423239", 0, 0), (1, "#423239", 1, 1)]
    yalign 1.0

style pref_vbox:
    xsize 225

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")
    font "gui/font/MotivaSans.otf"
    outlines []

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")
    font "gui/font/MotivaSans.otf"
    outlines []

style slider_slider:
    xsize 350

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 10

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 450

style name_label is pref_label
style name_label_text is pref_label_text

style name_text:
    font "gui/font/Inconsolata-LGC.otf"
    size 24
    color gui.idle_color
    outlines []

style value_text:
    size 18
    color "#000"
    outlines []
    yalign 0.65

default glossary_list = list()

init python:
    class GlossaryItem:
        def __init__(self, name: str, description: str):
            if len(name) > 7:
                raise ValueError("Искомый термин должен быть короче 7 символов.")
            self.name = name
            self.description = description

default inv_variable = 0

screen investigation():
    tag menu
    predict False

    use game_menu(_("Разбор"), scroll=("vpgrid" if gui.history_height else "viewport")):
        style_prefix "history"

        window:
            if inv_variable == 1:
                # vbox:
                label _("Лепер пидорас")
            elif inv_variable == 2:
                # vbox:
                label _("А тролль – молодец")
            else:
                # vbox:
                label _("Разбор ещё не начат.")

screen glossary():
    tag menu
    predict False

    use game_menu(_("Словарь"), scroll=("vpgrid" if gui.history_height else "viewport")):
        style_prefix "history"

        for gl in glossary_list:
            window:
                has fixed:
                    yfit True

                label gl.name:
                    style "history_name"
                    substitute False

                text gl.description:
                    substitute False

        if not glossary_list:
            label _("Словарь пуст.")

screen history():
    tag menu
    
    predict False

    use game_menu(_("История"), scroll=("vpgrid" if gui.history_height else "viewport")):
        style_prefix "history"

        for h in _history_list:
            window:
                has fixed:
                    yfit True

                if h.who:
                    label h.who:
                        style "history_name"
                        substitute False

                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("История пуста.")

define podmost_list = dict()

screen podmost():
    tag menu

    predict False

    use game_menu(_("Дневник"), scroll=("vpgrid" if gui.history_height else "viewport")):
        if podmost_list:
            for pd_text in glossary_list.items():
                vbox:
                    spacing 15
                hbox:
                    text pd_text
                    null width 25
        else:
            vbox:
                text "Дневник пуст."
# так добавляются слова в словарь / $ podmost_list.update({"Вот тут ставишь пробел": "Моего батю замочили в кафе там-то там-то, зацепки такие-то такие-то."})

define gui.history_allow_tags = set()

style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5

screen dialog(message, ok_action):
    modal True
    zorder 200
    style_prefix "confirm"
    add "gui/overlay/confirm.png"
    frame:
        vbox:
            xalign .5
            yalign .5
            spacing 30
            label _(message):
                style "confirm_prompt"
                xalign 0.5
            hbox:
                xalign 0.5
                spacing 100
                textbutton _("ОК") action ok_action

screen confirm(message, yes_action, no_action):
    modal True
    zorder 200
    style_prefix "confirm"
    add "gui/overlay/confirm.png"
    frame:
        vbox:
            xalign .5
            yalign .5
            spacing 30
            label _(message):
                style "confirm_prompt"
                xalign 0.5
            hbox:
                xalign 0.5
                spacing 100
                textbutton _("Да") action yes_action
                textbutton _("Нет") action no_action

style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text
style confirm_frame:
    background Frame("gui/frame.png", gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    color "#000"
    outlines []
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound

style confirm_button_text is navigation_button_text:
    properties gui.button_text_properties("confirm_button")

screen fake_skip_indicator():
    use skip_indicator

screen skip_indicator():
    zorder 100
    style_prefix "skip"
    frame:
        hbox:
            spacing 6
            text _("Пропускаем...")
            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"

transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text message

    timer 3.25 action Hide('notify')

transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    size gui.notify_text_size

screen nvl(dialogue, items=None):

    window:
        style "nvl_window"
        has vbox:
            spacing gui.nvl_spacing

        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0
                use nvl_dialogue(dialogue)

        else:
            use nvl_dialogue(dialogue)
        
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0

screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id

define config.nvl_list_length = 6

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")