from level_builder import LevelBuilder
from pacman import Pacman
from ghost.blinky.blinky import Blinky
from ghost.pinky.pinky import Pinky
from ghost.inky.inky import Inky
from ghost.ghost_controller import GhostController
from pacman_input import PacmanInput
from pygame.sprite import Group
from timer import Timer


class Level(object):

    START = 0  # When level starts for 1st time
    PLAY = 1  # Playing lthe level
    LOSE = 2  # When pacman animate lose state
    LOST = 3  # When a ghost ate pacman
    RESTART = 4  # Restart after life lost

    def __init__(self, screen_width, screen_height):
        self.sprites = Group()
        self.ghosts = Group()
        self.debug_group = Group()
        self.__initialize_level(screen_width, screen_height)
        self.__initialize_actors()
        self.input = PacmanInput()
        self.state = self.START
        self.intro_time = Timer(1000)
        self.lost_time = Timer(1000)
        self.reset_losing_time = Timer(1000)
        self.restart_time = Timer(800)
        self.transistions = {
            self.START: self.intro,
            self.PLAY: self.playing,
            self.LOST: self.lost,
            self.LOSE: self.losing,
            self.RESTART: self.restarting
        }

    def update(self, time):
        func = self.transistions.get(self.state, lambda: 'Invalid level state')
        func(time)

    def intro(self, time):
        if self.intro_time.completed(time):
            self.state = self.PLAY

    def lost(self, time):
        self.ghosts.update(time)
        if self.lost_time.looped(time):
            self.reset_ghosts()
            self.state = self.LOSE

    def losing(self, time):
        if self.player.lose_completed():
            self.reset_player()
            if self.reset_losing_time.looped(time):
                self.reset_after_lose()
            return
        self.player.update(time)

    def restarting(self, time):
        if (self.restart_time.looped(time)):
            self.state = self.PLAY

    def playing(self, time):
        if not self.player.alive:
            self.state = self.LOST

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

    def reset_after_lose(self):
        self.__initialize_actors()
        self.state = self.RESTART

    def reset_actors(self):
        self.reset_player()
        self.reset_ghosts()

    def reset_player(self):
        self.player.kill()

    def reset_ghosts(self):
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
            self.debug_group,
            self.builder.get_doors()
        )
        self.pinky = Pinky(
            self.player,
            self.builder.get_platforms(),
            self.sprites,
            self.ghosts,
            self.debug_group,
            self.builder.get_doors()
        )
        self.inky = Inky(
            self.player,
            self.blinky,
            self.builder.get_platforms(),
            self.sprites,
            self.ghosts,
            self.debug_group,
            self.builder.get_doors()
        )
        self.ghost_controller = GhostController(self.ghosts)
