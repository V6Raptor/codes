import os
import sys
import random
import pygame
from pygame import gfxdraw

class Player(object):
    def __init__(self):
        self.rect = pygame.Rect(17, 256, 9, 9)

    def move(self, dx, dy):
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)

    def move_single_axis(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
        self.collision(dx, dy)

    def collision(self, dx, dy):
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if dx > 0:
                    self.rect.right = wall.rect.left
                if dx < 0:
                    self.rect.left = wall.rect.right
                if dy > 0:
                    self.rect.bottom = wall.rect.top
                if dy < 0:
                    self.rect.top = wall.rect.bottom


class Wall(object):
    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)

def draw_fog(screen, fog_color, player_rect, light_radius):
    fog_surface = pygame.Surface((screen.get_width(), screen.get_height()), pygame.SRCALPHA)
    fog_surface.fill((fog_color[0], fog_color[1], fog_color[2], 255))

    # Draw walls on fog surface
    for wall in walls:
        pygame.draw.rect(fog_surface, (0, 0, 0, 255), wall.rect.move(-camera_offset_x, -camera_offset_y))

    # Draw a small circle for player's light source
    pygame.draw.circle(fog_surface, (0, 0, 0, 0), player_rect.center, light_radius)

    screen.blit(fog_surface, (0, 0))

os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()

pygame.display.set_caption("Get to the red square!")
screen = pygame.display.set_mode((320, 240))

clock = pygame.time.Clock()
walls = []
player = Player()

level = """
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
W            WWW      WWWW                       WWW     W
W WWW WWWWWWWWWW WWWW WWWW WWWWWWWWWWWWWWWWWWWWW WWW WWW W
W WWW WWWWWWWWWW WWWW WWWW WWWWWWWWWWWWWWWWWWWWW WWW WWW W
W WWW            WWWW WWWW                   WWW     WWW W
W WWWWWWWWWWWWWWWWWWW WWWWWWWWW WWWWWWWWWWWW WWWWWWWWWWW W
W WWWWWWWWWWWWWWWWWWW WWWWWWWWW WWWWWWWWWWWW WWWWWWWWWWW W
W            WWW      WWWW               WWW WWWW    WWW W
W WWWWWWWWWWWWWW WWWWWWWWW WWWWWWWW WWWWWWWW WWWW WWWWWW W
W WWWWWWWWWWWWWW WWWWWWWWW WWWWWWWW WWWWWWWW WWWW WWWWWW W
W WWW        WWW      WWWW      WWW          WWWW    WWW W
WWWWW WWWWWWWWWWWWWWW WWWW WWWWWWWWW WWWWWWW WWWWWWW WWW W
WWWWW WWWWWWWWWWWWWWW WWWW WWWWWWWWW WWWWWWW WWWWWWW WWW WWW
WWWWW WWWWWWWWWWWWWWW WWWW WWW           WWW     WWW WWW   EW
W     WWWW       WWWW WWWW WWW WWWWWWWWW WWWWWWWWWWW WWW WWW
W WWWWWWWW WWWWW WWWW WWWW WWW WWWWWWWWW WWWWWWWWWWW WWW W
W WWWWWWWW WWWWW WWWW WWWW WWW WWWWWWWWW WWWWWWW     WWW W
W WWWWWWWW WWWWW WWWW WWWW WWW WWWWWWWWW     WWW WWWWWWW W
W     WWWW WWWWW WWWW WWWW WWW WWWWW     WWWWWWW WWWWWWW W
WWWWW WWWW WWWWW WWWW WWWW WWW WW WW WWWWWWWWWWW WWWWWWW W
WWWWW WWWW WWWWW WWWW WWWW WWW WW WW WWWWWWWWWWW WWWWWWW W
WWWWW WWWW WWWWW WWWW      WWW WW WW             WWWWWWW W
WWWWW WWWW WWWWW WWWWWWWWWWWWW WW WWWWWWWWWWWWWW WWWWWWW W
WWWWW WWWW WWWWW WWWWWWWWWWWWW WW WWWWWWWWWWWWWW WWWWWWW W
W          WWWWW               WW                WWW     W
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
""".splitlines()[1:]

x = y = 1
for row in level:
    for col in row:
        if col == "W":
            Wall((x, y))
        if col == "E":
            end_rect = pygame.Rect(x, y, 10, 10)
        x += 18
    y += 18
    x = 1

running = True
back = pygame.image.load("labyrinthe.jpg")

camera_offset_x, camera_offset_y = 0, 0

# Light parameters
light_radius = 50  # Radius of the player's light source

while running:
    clock.tick(60)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            running = False

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        player.move(-2, 0)
    if key[pygame.K_RIGHT]:
        player.move(2, 0)
    if key[pygame.K_UP]:
        player.move(0, -2)
    if key[pygame.K_DOWN]:
        player.move(0, 2)

    camera_offset_x = max(0, min(player.rect.x - 160, 1050 - 320))
    camera_offset_y = max(0, min(player.rect.y - 120, 480 - 240))

    screen.blit(back, (0 - camera_offset_x, 0 - camera_offset_y))

    draw_fog(screen, (0, 0, 0), player.rect.move(-camera_offset_x, -camera_offset_y), light_radius)

    # Just added this to make it slightly fun ;)
    if player.rect.colliderect(end_rect):
        pygame.quit()
        sys.exit()

    if end_rect is not None:
        pygame.draw.rect(screen, (255, 0, 0), end_rect.move(-camera_offset_x, -camera_offset_y))
    pygame.draw.rect(screen, (255, 200, 0), player.rect.move(-camera_offset_x, -camera_offset_y))

    pygame.display.flip()
    clock.tick(360)

pygame.quit()
