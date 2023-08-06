from GameMaker.Globals import *

import pygame as pg

Mouse = pg.mouse

class Window():
	def __init__(
			self,
			screen_size: tuple[int,int],
			title: str = "My Game",
			fps: int = 60, 
			background_color: tuple[int,int,int] = (255,255,255),
			no_frame=False,
		):
		pg.init()

		self.RES = self.WIDTH, self.HEIGHT = screen_size
		self.H_WIDTH, self.H_HEIGHT = self.WIDTH // 2, self.HEIGHT // 2

		self.FPS = fps

		self.screen = pg.display.set_mode(self.RES) if not no_frame else pg.display.set_mode(self.RES,pg.NOFRAME)
		self.clock = pg.time.Clock()

		self.title = title
		self.background_color = background_color

		self.RUNNING = True

		self.update_title(self.title)

		self.drawlist = [[],[],[]]
		self.keys_up = []

	def draw(self,item: list,layer: int = FOREGROUND) -> None:
		if type(item) == list:
			for i in item:
				self.drawlist[layer].append(i)
		else:
			self.drawlist[layer].append(item)

	def update_title(self,title: str):
		pg.display.set_caption(title)
		self.title = title

	def keys(self) -> dict[bool]:
		return pg.key.get_pressed()

	def get_key(self,key: int) -> bool:
		return self.keys()[key]

	def update(self) -> None:
		self.keys_up = []

		self.clock.tick(self.FPS)

		for e in pg.event.get():
			if e.type == pg.QUIT:
				pg.quit()
				self.RUNNING = False
				return
			elif e.type == pg.KEYUP:
				self.keys_up.append(e.key)

		self.screen.fill(self.background_color)

		for layer in self.drawlist:
			for item in layer:
				item.draw(self.screen)

		self.drawlist = [[],[],[]]

		pg.display.update()

	def close(self) -> None:
		self.RUNNING = False