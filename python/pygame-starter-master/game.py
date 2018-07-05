import pygame
import random
from settings import Settings
from mit import MIT
from button import Button

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


		self.font = pygame.font.SysFont('Comic Sans MS', 30)
		self.buttons = [
			Button(100, Settings.height - 100, 100, 100, "fight"),
			Button(Settings.width - 100, Settings.height - 100, 100, 100, "rest")
		]

	def loop(self, screen):
		clock = pygame.time.Clock()

		if not self.enemy:
			self.enemy = self.mits.pop()
			self.text = self.font.render(self.enemy.name, False, (0,0,0))

		while True:
			delta_t = clock.tick(Settings.frameRate)

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					return

			screen.fill((0, 0, 0))
			screen.blit(self.background,(0, 0))
			screen.blit(self.enemy.img,(Settings.width - 150,50))
			pygame.draw.rect(screen, (0,0,0), (Settings.width - 150, 150, 100, 20))
			pygame.draw.rect(screen, (0,255,0), (Settings.width - 150, 150,(self.enemy.health / 30) * 100, 20))
			screen.blit(self.text, (Settings.width - 150, 150))

			for button in self.buttons:
				pygame.draw.rect(screen, (0,0,225), (button.x, button.y, button.w, button.h))
				screen.blit(button.text, (button.x, button.y))
				
			pygame.display.flip()

	def quit(self):
		pass
