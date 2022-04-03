import pygame
import settings as st


class Object(pygame.sprite.Sprite):	
	i_img = 0.01
	def load_images(motionstates, name):
		images = []
		for i in range(motionstates):
			img = pygame.image.load("Images/" + name + "/img" + str(i) + ".png").convert()
			img.set_colorkey((255,255,255))
			images.append(img)
			
		return images

	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.rect = self.images[0].get_rect()
		self.rect.center = x, y
		
	def draw(self, win, subset=None):
		self.i_img += 0.1
		
		if subset: cur_images = self.images[subset[0]:subset[1]]
		else: cur_images = self.images
		
		if self.i_img >= len(cur_images): self.i_img = 0.01
		# pygame.draw.rect(win, (0,0,0),
                          # (self.rect.x, self.rect.y, self.rect.width, self.rect.height))	
		image = cur_images[int(self.i_img)]		
		#win.blit(image, (self.rect.x,self.rect.y))
		win.blit(image, (self.rect.centerx-image.get_width()//2,self.rect.centery-image.get_height()//2))
				

class Creature(Object):	
	def walk(self, xdir, ydir):
		self.moving = True
		self.rect.centerx += xdir * self.vel
		self.rect.centery += ydir * self.vel
	
	
class Player(Creature):
	vel = 5
	carrots = 0
	wolves_turned = 0
	lives = 4
	invulnerable = False
	motionstates = 8
	images = Object.load_images(motionstates, "Player")
	
	def transform_monster(self, Enemies, Allies, Sound):
		if self.carrots >= 5:			
			target = st.get_closest_enemy(Enemies, *self.rect.center)
			if target:
				Sound.play()
				self.carrots -= 5
				x, y = target.rect.centerx, target.rect.centery
				Enemies.pop(Enemies.index(target))
				Allies.append(Rabbit(x,y))
				self.wolves_turned += 1
			
			
class Rabbit(Creature):
	vel = 0
	time_exist = 0
	motionstates = 8
	images = Object.load_images(motionstates, "Rabbit")			


class Wolf(Creature):
	vel = 3
	motionstates = 4
	images = Object.load_images(motionstates, "Wolf")
	

class Carrot(Object):
	value = 1 
	motionstates = 1
	images = Object.load_images(motionstates, "Carrot")