import settings as st
import objects as ob
import pygame
import sys
from random import randrange

class Game:
	#win = pygame.display.set_mode((st.screenwidth, st.screenheight))
	win = st.win
	def __init__(self):
		self.Allies = []
		self.Enemies = []
		self.Collectibles = []
		self.Stages = []

		pygame.display.set_caption("Rabbit Run by Ashardalon78 version 1.0")
		self.clock = pygame.time.Clock()
		
		self.bg_img = pygame.image.load("Images/Bg_1.png").convert()
		self.bg_img = pygame.transform.scale(self.bg_img, (st.screenwidth,st.screenheight*3))
		
		self.rabbit_ui_img = pygame.image.load("Images/rabbit_ui.png").convert()
		self.rabbit_ui_img.set_colorkey((255,255,255))
		
		self.menu_sel_img = pygame.image.load("Images/rabbit_ui.png").convert()
		self.menu_sel_img.set_colorkey((255,255,255))
		
		self.collect_sound = pygame.mixer.Sound('Sounds/collect.wav')
		self.move_arrow_sound = pygame.mixer.Sound('Sounds/move_arrow.wav')
		self.death_sound = pygame.mixer.Sound('Sounds/death.wav')
		self.stage_end_sound = pygame.mixer.Sound('Sounds/stage_end.wav')
		self.transform_sound = pygame.mixer.Sound('Sounds/transform.ogg')
		
		self.start_screen()
		
	def start_screen(self):
		color = (127,63,0)
		titletext1 = st.font_huge1.render('BIH ZAYCYA', True, color)
		titletext2 = st.font_huge1.render('BEG ZAYCA', True, color)
		titletext3 = st.font_huge1.render('RABBIT RUN', True, color)
		y_start_ini = 4
		y_start = y_start_ini
		y_inc = self.menu_sel_img.get_height()
		items = ('Start Game', 'Toggle Fullscreen', 'Instructions', 'Exit')
		run = True
		while run:
			self.clock.tick(st.menu_framerate)
			self.events()
			
			self.win.blit(self.bg_img, (0, 0))
			self.win.blit(titletext1, (st.screenwidth // 4, st.screenheight // 16))
			self.win.blit(titletext2, (st.screenwidth // 4, st.screenheight // 16 + 80))
			self.win.blit(titletext3, (st.screenwidth // 4, st.screenheight // 16 + 160))
			
			for no, item in enumerate(items):
				y = y_inc * (no + y_start_ini +1)
				text = st.font_large1.render(item, True, (255,0,0))
				self.win.blit(text, (st.screenwidth // 3, y))
				
			y_sel = (y_start + 1) * y_inc
			self.win.blit(self.menu_sel_img, (st.screenwidth // 4, y_sel - y_inc//2))
			
			if self.keys[pygame.K_UP] and y_start > y_start_ini: 
				self.move_arrow_sound.play()
				y_start -= 1
			if self.keys[pygame.K_DOWN] and y_start < len(items) + y_start_ini - 1:
				self.move_arrow_sound.play()
				y_start += 1
			if self.keys[pygame.K_SPACE]:
				self.collect_sound.play()
				if y_start == y_start_ini:
					run = False
					self.new_game()
				elif y_start == y_start_ini + 1:
					if self.win.get_flags() and pygame.FULLSCREEN: pygame.display.set_mode((st.screenwidth,st.screenheight))
					else: pygame.display.set_mode((st.screenwidth,st.screenheight),pygame.FULLSCREEN)					
				elif y_start == y_start_ini + 2:
					run = False
					self.instructions_screen()				
				elif y_start == len(items) + y_start_ini - 1:
					run = False
					pygame.quit()
					sys.exit()						
			
			pygame.display.update()
		
	def instructions_screen(self):
		color = (127,63,0)
		
		text_items = [('The rabbits have been turned into evil wolves.', 'Avoid the wolves and collect carrots. When having',\
			'5 or more carrots, you can turn a wolf', 'back into a rabbit. Saved rabbits assist you',\
			'for some time, they will start blinking', 'before they disappear. When teaming up with other',\
			'rabbits (touching them), you can', 'convince wolves of their rabbit-nature', 'when they attack. They will give', 'you a carrot and disappear.',\
			'You can see that you are teamed up', 'when your rabbit turns green.', 'You win a stage when you transform', '5 wolves back into rabbits.'),\
			('Controls (Keyboard only)', 'Menu controls: Up/down arrows', 'Menu Select: Space', 'Control Rabbit: Up/down/left/right arrows', 'Transform wolf: Space',\
			'Pause: Enter ')] 
		
		i = 0
		run = True
		while run:
			self.clock.tick(st.menu_framerate)
			self.events()
						
			self.win.blit(self.bg_img, (0, 0))
										
			for j, line in enumerate(text_items[i]):
				text = st.font_large1.render(line, True, color)
				self.win.blit(text, (st.screenwidth//2 - text.get_width()//2, (j+1)*st.font_large1.size('a')[1]+st.screenheight//8))
			
			if self.keys[pygame.K_SPACE]:
				i += 1
			if i >= len(text_items):
				run = False
				self.start_screen()
			
			pygame.display.update()
			
	def pause(self):
		color = (255,255,255)
		y_start_ini = 1
		y_start = y_start_ini
		y_inc = self.menu_sel_img.get_height()
		items = ('Continue', 'End Game')
		run = True
		while run:
			self.clock.tick(st.menu_framerate)
			self.events()
			self.win.fill((0,0,0))
			
			for no, item in enumerate(items):
				y = y_inc * (no + y_start_ini +1)
				text = st.font_large1.render(item, True, color)
				self.win.blit(text, (st.screenwidth // 3, y))
				
			y_sel = (y_start + 1) * y_inc
			self.win.blit(self.menu_sel_img, (st.screenwidth // 4, y_sel - y_inc//2))
			
			if self.keys[pygame.K_UP] and y_start > y_start_ini: 
				self.move_arrow_sound.play()
				y_start -= 1
			if self.keys[pygame.K_DOWN] and y_start < len(items) + y_start_ini - 1:
				self.move_arrow_sound.play()
				y_start += 1
			if self.keys[pygame.K_SPACE]:
				self.collect_sound.play()
				if y_start == y_start_ini: run = False								
				elif y_start == len(items) + y_start_ini - 1:
					run = False
					self.start_screen()						
			
			pygame.display.update()			
		
	def new_game(self):
		self.Player1 = ob.Player(*st.start_coords)
		self.start_stage(0)
		
	def start_stage(self, i_stage, starttext=True):
		self.Allies.clear()
		self.Enemies.clear()
		self.Collectibles.clear()
				
		self.frame_counter = 0
		self.scroll_v = 1
		self.Player1.rect.center = st.start_coords
		
		self.randomness = (4 - i_stage) * 20
		self.i_stage = i_stage
		
		if starttext: 		
			run = True
			while run:
				self.clock.tick(st.menu_framerate)
				self.events()
				if self.keys[pygame.K_SPACE]: 
					run = False
					self.game_loop()
					
				self.win.blit(self.bg_img, (0, 0))
				#textstruct = ()
				if i_stage == 0:
					textstruct = ('Stage 1', 'In this stage wolves', 'move only vertically.', 'Get ready!', '(Press Space to continue)')
				elif i_stage == 1:
					textstruct = ('Stage 2', 'The wolves are becoming', 'more dangerous! Now they', 'also move horizontally!', 'Be careful!',\
					'(Press Space to continue)')
				elif i_stage == 2:
					textstruct = ('Final Stage', 'Now the wolves are', 'extrmely dangerous!', 'They move longer', 'horizontal distances!', 'Extreme Caution!',\
					'(Press Space to continue)')
				
				color = (127,63,0)
				for i, line in enumerate(textstruct):
					text = st.font_huge1.render(line, True, color)
					self.win.blit(text, (st.screenwidth//2 - text.get_width()//2, (i+1)*st.font_huge1.size('a')[1]+st.screenheight//8))
				
				pygame.display.update()
		else: self.game_loop()
		
	def game_loop(self):
		run = True
		bgy = 0
		bgheight = self.bg_img.get_height()
		bgy2 = -bgheight
		
		while run:
			self.clock.tick(st.game_framerate)	
			self.frame_counter += 1			
			if (self.frame_counter / st.game_framerate) % 10 == 0 and self.scroll_v <= 5: self.scroll_v += 1			
			
			
			self.events()
			if self.keys[pygame.K_LEFT] and self.Player1.rect.left > self.Player1.vel: self.Player1.walk(-1,0)
			if self.keys[pygame.K_RIGHT] and self.Player1.rect.right < st.screenwidth  - self.Player1.vel: self.Player1.walk(1,0)
			if self.keys[pygame.K_UP] and self.Player1.rect.top > self.Player1.vel: self.Player1.walk(0,-1)
			if self.keys[pygame.K_DOWN] and self.Player1.rect.bottom < st.screenheight - self.Player1.vel: self.Player1.walk(0,1)
			if self.keys[pygame.K_SPACE]: self.Player1.transform_monster(self.Enemies, self.Allies, self.transform_sound)
			if self.keys[pygame.K_RETURN]: self.pause()
					
			if not self.keys[pygame.K_LEFT] and not self.keys[pygame.K_RIGHT] \
			and not self.keys[pygame.K_UP] and not self.keys[pygame.K_DOWN]: self.Player1.moving = False 
		
			
			#end stage here
			
			#Background		
			bgy +=self.scroll_v
			bgy2 +=self.scroll_v
			if bgy > bgheight: bgy = -bgheight
			if bgy2 > bgheight: bgy2 = -bgheight
				 
			self.win.blit(self.bg_img,(0,bgy))
			self.win.blit(self.bg_img,(0,bgy2))
			
			self.draw_ui()
			
			#move Enemies here
			for ene in self.Enemies:
				ene.rect.centery += self.scroll_v
				ene.walk(0,1)
				if ene.rect.centerx - self.Player1.rect.centerx < self.i_stage*75\
				and ene.rect.centerx - self.Player1.rect.centerx >0 and not self.Player1.invulnerable: ene.walk(-1,0)
				elif ene.rect.centerx - self.Player1.rect.centerx > -self.i_stage*75\
				and ene.rect.centerx - self.Player1.rect.centerx <0 and not self.Player1.invulnerable: ene.walk(1,0)
				
				ene.draw(self.win)
				
			for al in self.Allies:
				al.time_exist += 1
				if al.time_exist == 15*st.game_framerate: self.Allies.pop(self.Allies.index(al))
				if al.time_exist < 12*st.game_framerate: subset = (0,4)
				else: subset = None
				al.draw(self.win, subset=subset)
				
			for col in self.Collectibles:
				col.rect.centery += self.scroll_v
				col.draw(self.win)
			
						
			if self.Player1.invulnerable: subset = (4,8)
			else: subset = (0,4)
			self.Player1.draw(self.win, subset = subset)
			
			
			#move Projectiles (if any)
			
			#check and handle collisions
			self.Player1.invulnerable = False
			for al in self.Allies:				
				if al.rect.colliderect(self.Player1.rect):
					self.Player1.invulnerable = True
			
			for ene in self.Enemies:
				if ene.rect.colliderect(self.Player1.rect):
					if self.Player1.invulnerable:
						self.transform_sound.play()
						x, y = ene.rect.centerx, ene.rect.centery
						self.Enemies.pop(self.Enemies.index(ene))
						self.Collectibles.append(ob.Carrot(x,y-20))
					else: self.playerdeath()
			
			for al in self.Allies:
				for ene in self.Enemies:		
					if ene.rect.colliderect(al.rect):
						if al.rect.colliderect(self.Player1.rect):
							self.transform_sound.play()
							x, y = ene.rect.centerx, ene.rect.centery
							self.Enemies.pop(self.Enemies.index(ene))
							self.Collectibles.append(ob.Carrot(x,y-20))
					
			for col in self.Collectibles:
				if col.rect.colliderect(self.Player1.rect):
					self.Collectibles.pop(self.Collectibles.index(col))
					self.Player1.carrots += col.value
					self.collect_sound.play()
									
			#Garbage collection
			
			#Spawn Objects
			if randrange(self.randomness) == 0:
				self.Enemies.append(ob.Wolf(randrange(st.screenwidth//8,st.screenwidth//8*7),0))
			if randrange(120) == 0:
				self.Collectibles.append(ob.Carrot(randrange(st.screenwidth//8,st.screenwidth//8*7),0))
			
			#Reloads
			
			if self.Player1.wolves_turned >= 5:
				run = False
				self.end_stage()
			
			pygame.display.update()
	
	def end_stage(self):
		self.stage_end_sound.play()
		color = (127,63,0)
		text1 = st.font_huge1.render('Congratulations!', True, color)
		text2 = st.font_huge1.render('You have finished Stage ' + str(self.i_stage+1) + '!', True, color)
		self.win.blit(text1, (st.screenwidth//2 - text1.get_width()//2, st.font_huge1.size('a')[1]+st.screenheight//8))
		self.win.blit(text2, (st.screenwidth//2 - text2.get_width()//2, 2*st.font_huge1.size('a')[1]+st.screenheight//8))
		pygame.display.update()
		pygame.time.wait(2000)
		
		if self.i_stage >= 2: self.end_game()
		else:
			self.i_stage +=1
			self.carrots = 0
			self.Player1.wolves_turned = 0
			self.start_stage(self.i_stage)			
		
	def end_game(self):
		color = (127,63,0)
		run = True
		while run:
			self.clock.tick(st.menu_framerate)
			self.events()
			if self.keys[pygame.K_SPACE]: 
				run = False
				self.start_screen()
				
			self.win.blit(self.bg_img, (0, 0))
			textstruct = ('You have been successful!', 'You have lifted the curse and', 'saved the rabbit nation!', 'From now on, rabbits and',\
			'wolves will live together', 'peacefully forever!')
			
			for i, line in enumerate(textstruct):
				text = st.font_huge1.render(line, True, color)
				self.win.blit(text, (st.screenwidth//2 - text.get_width()//2, (i+1)*st.font_huge1.size('a')[1]+st.screenheight//8))
			
			pygame.display.update()	
	
	def draw_ui(self):
		self.win.blit(self.rabbit_ui_img,(st.screenwidth//64,st.screenheight//64))
		text = st.font_normal1.render('Carrots: ' + str(self.Player1.carrots), True, (0,0,0))
		self.win.blit(text,(st.screenwidth//12,st.screenheight//32))
		
		text = st.font_normal1.render('Rabbits Saved: ' + str(self.Player1.wolves_turned), True, (0,0,0))
		self.win.blit(text,(st.screenwidth//12,st.screenheight//32 + st.font_normal1.size('a')[1]))
		
		text = st.font_normal1.render('Lives: ' + str(self.Player1.lives), True, (0,0,0))
		self.win.blit(text,(st.screenwidth//12,st.screenheight//32 + 2*st.font_normal1.size('a')[1]))
		
		
	def playerdeath(self):
		self.death_sound.play()
		text = st.font_huge1.render("You got caught", True, (63,127,255))
		self.win.blit(text,(st.screenwidth//4,st.screenheight//2))
		pygame.display.update()
		pygame.time.wait(2000)
		if self.Player1.lives >=1:
			self.Player1.lives -=1
			self.start_stage(self.i_stage, starttext=False)
		else:
			self.win.fill((0,0,0))
			text = st.font_huge1.render("Game Over", True, (255,0,0))
			self.win.blit(text,(st.screenwidth//2 - text.get_width()//2,st.screenheight//2))
			pygame.display.update()
			pygame.time.wait(2000)
			self.start_screen()
		
	
	def events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
		self.keys = pygame.key.get_pressed()
				

if __name__ == '__main__':
	Session1 = Game()
