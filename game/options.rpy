define config.name = "Дубль два"
define gui.show_name = True
define config.version = "v0.01pa"
define gui.about = _("Описание\nСледующая строчка")
define build.name = "secondshotru"
define config.has_sound = True
define config.has_music = True
define config.has_voice = False
define config.main_menu_music = None
define config.enter_transition = Dissolve(.2)
define config.exit_transition = Dissolve(.2)
define config.after_load_transition = None
define config.end_game_transition = Dissolve(.5)
define config.window = "auto"
define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)
default preferences.text_cps = 50
default preferences.afm_time = 15
default preferences.music_volume = 0.75
default preferences.sfx_volume = 0.75
define config.save_directory = "SecondShot"
define config.window_icon = "gui/window_icon.png"
define config.allow_skipping = True
define config.has_autosave = False
define config.autosave_on_quit = False
define config.autosave_slots = 0
define config.rollback_enabled = config.developer
define config.layers = [ 'master', 'transient', 'screens', 'overlay', 'front' ]
define config.image_cache_size = 64
define config.predict_statements = 50
define config.menu_clear_layers = ["front"]
define config.gl_test_image = "white"

init python:
    if len(renpy.loadsave.location.locations) > 1: del(renpy.loadsave.location.locations[1])
    renpy.game.preferences.pad_enabled = False
    def replace_text(s):
        s = s.replace('--', u'\u2014')
        s = s.replace(' - ', u'\u2014')
        return s
    config.replace_text = replace_text
    def game_menu_check():
        if quick_menu: renpy.call_in_new_context('_game_menu')

    config.game_menu_action = game_menu_check

    def force_integer_multiplier(width, height):
        if float(width) / float(height) < float(config.screen_width) / float(config.screen_height):
            return (width, float(width) / (float(config.screen_width) / float(config.screen_height)))
        else:
            return (float(height) * (float(config.screen_width) / float(config.screen_height)), height)

init python:
    build.package("DDLCUniversal", 'zip', 'windows linux mac renpy mod',
        description="DDLC Universal by Tetyastan")

    build.archive("scripts", 'mod')
    build.archive("audio", 'mod')
    build.archive("images", 'mod')

    build.renpy_patterns.remove(('renpy.py', ['all']))
    build.classify_renpy("renpy.py", "renpy all")
    
    build.early_base_patterns.remove(('*.sh', None))
    build.classify("game/**.rpyc", "scripts all")
    build.classify("game/images/**", "images all")
    build.classify("game/gui/**", "images all")
    build.classify("game/audio/**", "audio all")
    build.classify("game/core/**", "scripts all")

    build.classify_renpy("renpy/WOW", "renpy all")

    build.include_old_themes = False
