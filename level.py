from level_builder import LevelBuilder
from pacman import Pacman
from ghost.blinky.blinky import Blinky
from ghost.pinky.pinky import Pinky
from ghost.ghost_controller import GhostController
from pacman_input import PacmanInput
from pygame.sprite import Group
from pygame.mixer import Sound


class Level(object):

    START = 0
    PLAY = 1
    END = 2

    def __init__(self, screen_width, screen_height):
        self.sprites = Group()
        self.ghosts = Group()
        self.debug_group = Group()
        self.__initialize_level(screen_width, screen_height)
        self.__initialize_actors()
        self.input = PacmanInput()
        self.state = self.START
        self.intro_time = 0
        self.transistions = {
            self.START: self.intro,
            self.PLAY: self.playing,
            self.END: self.ending
        }
        self.intro_music = Sound('resources/sounds/game_start.wav')
        self.intro_music.play()

    def update(self, time):
        func = self.transistions.get(self.state, lambda: 'Invalid level state')
        func(time)

    def intro(self, time):
        self.intro_time += time
        if self.intro_time > 4000:
            self.state = self.PLAY
            self.intro_time = 0

    def ending(self, time):
        pass

    def playing(self, time):
        if not self.player.alive and \
                self.player.death_completed():
            self.reset_after_death()

        self.player.set_direction(
            self.input.get_direction(
                self.player.motion.dir
            )
        )
        self.player.update(time)
        self.ghost_controller.control(time)
        self.ghosts.update(time)

    def render(self, surface):
        self.__render_background(surface)
        # Draw sprites to surface
        self.sprites.draw(surface)

    def render_debug(self, surface):
        self.__render_background(surface)
        # Draw helper platforms
        self.builder.get_platforms().draw(surface)
        # Draw sprites to surface
        self.sprites.draw(surface)
        self.debug_group.draw(surface)

    def reset_after_death(self):
        self.reset()
        self.__initialize_actors()
        self.state = self.START

    def reset(self):
        self.player.kill()
        for g in self.ghosts:
            g.kill()

    def completed(self):
        return len(self.builder.get_dots()) == 0

    def __render_background(self, surface):
        # Draw background to surface
        surface.blit(self.builder.get_background(), (0, 0))
        # draw dots
        self.builder.get_dots().draw(surface)

    def __initialize_level(self, screen_width, screen_height):
        self.builder = LevelBuilder(
            "resources/levels/level1.json",
            (screen_width, screen_height)
        )
        self.builder.build()

    def __initialize_actors(self):
        '''
        Load actors
        '''
        self.player = Pacman(
            (112, 212),
            self.builder.get_platforms(),
            self.builder.get_dots(),
            self.ghosts,
            self.sprites,
            self.debug_group
        )
        self.blinky = Blinky(
            self.player,
            self.builder.get_platforms(),
            self.sprites,
            self.ghosts,
            self.debug_group
        )
        self.pinky = Pinky(
            self.player,
            self.builder.get_platforms(),
            self.sprites,
            self.ghosts,
            self.debug_group
        )
        self.ghost_controller = GhostController(self.ghosts)
