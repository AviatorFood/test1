def on_button_pressed_a():
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    music.play_sound_effect(music.create_sound_effect(WaveShape.NOISE,
            500,
            499,
            255,
            0,
            750,
            SoundExpressionEffect.NONE,
            InterpolationCurve.LINEAR),
        SoundExpressionPlayMode.UNTIL_DONE)
    basic.show_leds("""
        # . . . .
                . # . . .
                . . # . .
                . . . # .
                . . . . #
    """)
input.on_button_pressed(Button.B, on_button_pressed_b)
