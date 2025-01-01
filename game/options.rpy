define config.name = "Дубль два"
define gui.show_name = True
define config.version = "v0.01pa"
define gui.about = _("Описание\nСледующая строчка")
define build.name = "secondshotru"
define config.has_sound = True
define config.has_music = True
define config.has_voice = False
define config.main_menu_music = 'audio/gui/sfx/to-the-moon.mp3'
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
define config.save_directory = None
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

# if renpy.version_tuple >= (8, 1, 0, 23051307):
#     define config.quadratic_volumes = True

init python:
    renpy.game.preferences.pad_enabled = False
    def replace_text(s):
        # s = s.replace('--', u'\u2014')
        s = s.replace(' - ', " – ")
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
