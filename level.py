from level_builder import LevelBuilder
from pacman import Pacman
from ghost.blinky.blinky import Blinky
from ghost.pinky.pinky import Pinky
from ghost.ghost_controller import GhostController
from pacman_input import PacmanInput
from pygame.sprite import Group


class Level(object):

    def __init__(self, screen_width, screen_height):
        self.sprites = Group()
        self.ghosts = Group()
        self.debug_group = Group()
        self.__initialize_level(screen_width, screen_height)
        self.__initialize_actors()
        self.input = PacmanInput()

    def update(self, time):
        self.player.set_direction(self.input.get_direction(self.player.motion.dir))
        self.player.update()
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
            self.sprites
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
