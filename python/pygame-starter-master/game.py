import pygame
import random
from settings import Settings
from mit import MIT

class Game():
	def __init__(self):
		self.background = pygame.image.load("images/bg.jpg")
		self.enemy = None
		self.mits = [
    MIT("kaitlen"),
    MIT("bennett"),
    MIT("austin"),
    MIT("rhy rhy"),
    MIT("travis")
        ]
		random.shuffle(self.mits)



	def loop(self, screen):
		clock = pygame.time.Clock()

		if not self.enemy:
			self.enemy = self.mits.pop()

		while True:
			delta_t = clock.tick(Settings.frameRate)

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					return

			screen.fill((0, 0, 0))
			screen.blit(self.background,(0, 0))
			screen.blit(self.enemy.img,(Settings.width - 100,0))

			pygame.display.flip()

	def quit(self):
		pass
