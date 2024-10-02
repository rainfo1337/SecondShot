init:
    transform buttonZoom:
        zoom 0.3

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
image quick button knigger idle = im.MatrixColor("gui/quickmenu/kniggaepta.png",im.matrix.colorize("#fff", "#000"))

image quick button knigger hover = im.MatrixColor("gui/quickmenu/kniggaepta.png",im.matrix.colorize("#f00", "#000"))

image quick button knigger insensitive = im.MatrixColor("gui/quickmenu/kniggaepta.png",im.matrix.colorize("#444", "#000"))

#нутупанастройки свэг 228
image quick button options idle = im.MatrixColor("gui/quickmenu/optionsepta.png",im.matrix.colorize("#fff", "#000"))

image quick button options hover = im.MatrixColor("gui/quickmenu/optionsepta.png",im.matrix.colorize("#f00", "#000"))

image quick button options insensitive = im.MatrixColor("gui/quickmenu/optionsepta.png",im.matrix.colorize("#444", "#000"))

init 100:
    screen quick_menu():
        zorder 100

        

        default tt = Tooltip("")

        if quick_menu:
            vbox:
                xalign 1.0
                yalign 1.0

                if (tt.value != ""):
                    text tt.value

                hbox:
                    #ТРУСТОРИ ёпта
                    imagebutton:
                        idle "quick button story idle"
                        hover "quick button story hover"
                        insensitive "quick button story insensitive"
                        hovered tt.Action("Показать историю")
                        at buttonZoom
                        action ShowMenu('history')

                    #пролетаю пау пау пау
                    imagebutton:
                        idle "quick button skip idle"
                        hover "quick button skip hover"
                        insensitive "quick button skip insensitive"
                        hovered tt.Action("Пропустить")
                        at buttonZoom
                        action Skip() alternate Skip(fast=True, confirm=True)

                    #сохраниться - ебаться в рот
                    imagebutton:
                        idle "quick button save idle"
                        hover "quick button save hover"
                        insensitive "quick button save insensitive"
                        hovered tt.Action("Сохранить")
                        at buttonZoom
                        action ShowMenu('save')

                    #загрузиться - ебаться в сраку
                    imagebutton:
                        idle "quick button load idle"
                        hover "quick button load hover"
                        insensitive "quick button load insensitive"
                        hovered tt.Action("Загрузить")
                        at buttonZoom
                        action ShowMenu('load')

                    #спизженный напрочь у сп глоссарий
                    imagebutton:
                        idle "quick button knigger idle"
                        hover "quick button knigger hover"
                        insensitive "quick button knigger insensitive"
                        hovered tt.Action("Словарь")
                        at buttonZoom
                        action ShowMenu('glossary')

                    #настройи (чёреально?)
                    imagebutton:
                        idle "quick button options idle"
                        hover "quick button options hover"
                        insensitive "quick button options insensitive"
                        hovered tt.Action("Настройки")
                        at buttonZoom
                        action ShowMenu('preferences')
