# "position very interesting position" - levi rozeman
init:
    transform buttonStory:
        zoom 0.2
        xpos 300
        ypos 675
    transform buttonSkip:
        zoom 0.2
        xpos 400
        ypos 675
    transform buttonSave:
        zoom 0.2
        xpos 500
        ypos 675
    transform buttonLoad:
        zoom 0.2
        xpos 600
        ypos 675
    transform buttonKnigga:
        zoom 0.2
        xpos 700
        ypos 675
    transform buttonOptions:
        zoom 0.2
        xpos 800
        ypos 675

#трусториёбан
image quick button story idle = im.MatrixColor("gui/quickmenu/truestoryepta.png",im.matrix.colorize("#fff", "#000"))

image quick button story hover = im.MatrixColor("gui/quickmenu/truestoryepta.png",im.matrix.colorize("#f00", "#000"))

image quick button story insensitive = im.MatrixColor("gui/quickmenu/truestoryepta.png",im.matrix.colorize("#444","#000"))

#скипёпта
image quick button skip idle = im.MatrixColor("gui/quickmenu/skipepta.png", im.matrix.colorize("#fff", "#000"))

image quick button skip hover = im.MatrixColor("gui/quickmenu/skipepta.png", im.matrix.colorize("#f00", "#000"))

image quick button skip insensitive = im.MatrixColor("gui/quickmenu/skipepta.png", im.matrix.colorize("#444", "#000"))

#сейвёпта
image quick button save idle = im.MatrixColor("gui/quickmenu/savepta.png",im.matrix.colorize("#fff", "#000"))

image quick button save hover = im.MatrixColor("gui/quickmenu/savepta.png",im.matrix.colorize("#f00", "#000"))

image quick button save insensitive = im.MatrixColor("gui/quickmenu/savepta.png",im.matrix.colorize("#444", "#000"))

#лоадёпта
image quick button load idle = im.MatrixColor("gui/quickmenu/loadepta.png",im.matrix.colorize("#fff", "#000"))

image quick button load hover = im.MatrixColor("gui/quickmenu/loadepta.png",im.matrix.colorize("#f00", "#000"))

image quick button load insensitive = im.MatrixColor("gui/quickmenu/loadepta.png",im.matrix.colorize("#444", "#000"))

#спизженный с сп глоссарий ёпта
image quick button knigger idle = im.MatrixColor("gui/quickmenu/kniggaepta.png",im.matrix.colorize("#fff", "#fff"))

image quick button knigger hover = im.MatrixColor("gui/quickmenu/kniggaepta.png",im.matrix.colorize("#f00", "#f00"))

image quick button knigger insensitive = im.MatrixColor("gui/quickmenu/kniggaepta.png",im.matrix.colorize("#444", "#000"))

#нутупанастройки свэг 228
image quick button options idle = im.MatrixColor("gui/quickmenu/optionsepta.png",im.matrix.colorize("#fff", "#fff"))

image quick button options hover = im.MatrixColor("gui/quickmenu/optionsepta.png",im.matrix.colorize("#f00", "#f00"))

image quick button options insensitive = im.MatrixColor("gui/quickmenu/optionsepta.png",im.matrix.colorize("#444", "#000"))

init 100:
    screen quick_menu():
        zorder 100

        

        default tt = Tooltip("")

        if quick_menu:
            vbox:
                #xalign 0.5
                #yalign 1.0

                if (tt.value != ""):
                    text tt.value

                hbox:
                    #ТРУСТОРИ ёпта
                    imagebutton:
                        idle "quick button story idle"
                        hover "quick button story hover"
                        insensitive "quick button story insensitive"
                        #hovered tt.Action("Показать историю")
                        at buttonStory
                        action ShowMenu('history')

                    #пролетаю пау пау пау
                    imagebutton:
                        idle "quick button skip idle"
                        hover "quick button skip hover"
                        insensitive "quick button skip insensitive"
                        #hovered tt.Action("Пропустить")
                        at buttonSkip
                        action Skip() alternate Skip(fast=True, confirm=True)

                    #сохраниться - ебаться в рот
                    imagebutton:
                        idle "quick button save idle"
                        hover "quick button save hover"
                        insensitive "quick button save insensitive"
                        #hovered tt.Action("Сохранить")
                        at buttonSave
                        action ShowMenu('save')

                    #загрузиться - ебаться в сраку
                    imagebutton:
                        idle "quick button load idle"
                        hover "quick button load hover"
                        insensitive "quick button load insensitive"
                        #hovered tt.Action("Загрузить")
                        at buttonLoad
                        action ShowMenu('load')

                    #спизженный напрочь у сп глоссарий
                    imagebutton:
                        idle "quick button knigger idle"
                        hover "quick button knigger hover"
                        insensitive "quick button knigger insensitive"
                        #hovered tt.Action("Словарь")
                        at buttonKnigga
                        action ShowMenu('glossary')

                    #настройи (чёреально?)
                    imagebutton:
                        idle "quick button options idle"
                        hover "quick button options hover"
                        insensitive "quick button options insensitive"
                        #hovered tt.Action("Настройки")
                        at buttonOptions
                        action ShowMenu('preferences')
