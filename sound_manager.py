from pygame.mixer import Sound
from timer import Timer


class SoundManager(object):
    def __init__(self):
        self.intro_music = Sound('resources/sounds/game_start.wav')
        self.munch1 = Sound('resources/sounds/munch_1.wav')
        self.munch2 = Sound('resources/sounds/munch_2.wav')
        self.death_sound = Sound('resources/sounds/death_1.wav')
        self.t = 0
        self.s = {
            1: self.play_munch1,
            2: self.play_munch2
        }

    def play_intro(self):
        self.intro_music.play()

    def play_munch(self, time):
        self.t += 1
        if self.t > 2:
            self.t = 1
        func = self.s.get(self.t)
        func()

    def play_munch1(self):
        return self.munch1.play()

    def play_munch2(self):
        return self.munch2.play()

    def play_lose(self):
        return self.death_sound.play()