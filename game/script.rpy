label start:
    "Пися попа бобра"
    $ glossary_list.update({"Булки": "Мягкие и хрустящие, а главное -- французские и хороши к чаю"})
    $ glossary_list.update({"Писька": "Твёрдый, а главное -- французский"})
    $ glossary_list.update({"Сиська": "Мягкая, а главное -- женская"})
    $ glossary_list.update({"Собака": "Злая, а главное -- собака"})
    $ glossary_list.update({"Кошка": "Волосатая, а главное -- лысая"})
    na "ракета бомба петарда {a=showmenu:glossary}булка{/a}"
    # call prologue
    # call d0
    # call d1
    # if wanted.scale == 0:
    #     call neutral
    # else:
    #     call d2
    #     call d3
    #     call d4
    #     call d5
    #     call d6
    #     call d7
    #     call d8
    #     if wanted.scale >= 3:
    #         call bad
    #     else:
    #         call good
    return
