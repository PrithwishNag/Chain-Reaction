import pygame
import sys
pygame.init()
#for 7x7 board
Cube_Size=8
#Grid size
Box_w=50
Box_h=50
#Screen size
Swidth=Cube_Size*Box_w
Sbreath=Cube_Size*Box_h
SIwidth=390
SIbreath=390
#Colours
grey=(195,195,195)
lightgrey=(225,225,225)
Green=(0,200,0)
Red=(200,0,0)
Red2=(140,0,0)
Green2=(0,140,0)
black=(0,0,0)
gap=5#gap between the grids
counter=0#counter for no. of mouse inputs
backgrid=[[0 for i in range(0,Cube_Size)] for i in range(0,Cube_Size)]
gbg=[[0 for i in range(0,Cube_Size)] for i in range(0,Cube_Size)]
rbg=[[0 for i in range(0,Cube_Size)] for i in range(0,Cube_Size)]
screenIntro=pygame.display.set_mode((SIwidth,SIbreath))
bg=pygame.image.load("CHAIN.png").convert()
patch=pygame.image.load("GreyBack.png").convert()
greenball=pygame.image.load("OGB1.png")
redball=pygame.image.load("ORB1.png")
doublegreenball=pygame.image.load("DGB1.png")
doubleredball=pygame.image.load("DRB1.png")
triplegreenball=pygame.image.load("TGB1.png")
tripleredball=pygame.image.load("TRB1.png")
Quadgreenball=pygame.image.load("QGB1.png")
Quadredball=pygame.image.load("QRB1.png")
Pentagreenball=pygame.image.load("PGB1.png")
Pentaredball=pygame.image.load("PRB1.png")
Hexagreenball=pygame.image.load("HGB!.png")
Hexaredball=pygame.image.load("HRB1.png")
Heptagreenball=pygame.image.load("GB7.png")
Heptaredball=pygame.image.load("RB7.png")
Rules=pygame.image.load("Rules.png")
RR=pygame.image.load("RulesNReg.png")
background=pygame.image.load("Background.png").convert()
backgroundlite=pygame.image.load("Backgroundlite.png").convert()
Startscreen=pygame.image.load("StartGame.png").convert()
Startbutton=pygame.image.load("StartButton2.png").convert()
WinnerRed=pygame.image.load("red_won.png")
WinnerGreen=pygame.image.load("green_won1.png")
#Sound
pygame.mixer.init()
Click_Sound=pygame.mixer.Sound("Select.wav")
Click_Sound1=pygame.mixer.Sound("Select2.wav")
pygame.mixer.music.load("BGSound.mp3")
pygame.display.set_caption("Chain Reaction")
game_over=False
N_count=0
#Making Background sprite
class BackBlock(pygame.sprite.Sprite):
	def __init__(self, color=grey, w=Box_w,h=Box_h):
		super(BackBlock, self).__init__()
		self.image = background
		self.rect=self.image.get_rect()
class BackBlockLight(pygame.sprite.Sprite):
	def __init__(self, color=lightgrey, w=Box_w,h=Box_h):
		super(BackBlockLight, self).__init__()
		self.image = backgroundlite
		self.rect=self.image.get_rect()
#Making Patch Grid
class PatchGreyClass(pygame.sprite.Sprite):
	def __init__(self):
		super(PatchGreyClass, self).__init__()
		self.image=patch
		self.rect=self.image.get_rect()
#Making One Green Ball Sprite
class OneGreenBallClass(pygame.sprite.Sprite):
	def __init__(self):
		super(OneGreenBallClass, self).__init__()
		self.image=greenball
		self.image.set_colorkey(black)
		self.rect=self.image.get_rect()
#Making One Red Ball Sprite 
class OneRedBallClass(pygame.sprite.Sprite):
	def __init__(self):
		super(OneRedBallClass, self).__init__()
		self.image=redball
		self.image.set_colorkey(black)
		self.rect=self.image.get_rect()
#Making double Green Ball Sprite
class DoubleGreenBallClass(pygame.sprite.Sprite):
	def __init__(self):
		super(DoubleGreenBallClass, self).__init__()
		self.image=doublegreenball
		self.image.set_colorkey(black)
		self.rect=self.image.get_rect()
#Making double Red Ball Sprite 
class DoubleRedBallClass(pygame.sprite.Sprite):
	def __init__(self):
		super(DoubleRedBallClass, self).__init__()
		self.image=doubleredball
		self.image.set_colorkey(black)
		self.rect=self.image.get_rect()
#Making triple Green Ball Sprite
class TripleGreenBallClass(pygame.sprite.Sprite):
	def __init__(self):
		super(TripleGreenBallClass, self).__init__()
		self.image=triplegreenball
		self.image.set_colorkey(black)
		self.rect=self.image.get_rect()
#Making triple Red Ball Sprite 
class TripleRedBallClass(pygame.sprite.Sprite):
	def __init__(self):
		super(TripleRedBallClass, self).__init__()
		self.image=tripleredball
		self.image.set_colorkey(black)
		self.rect=self.image.get_rect()
#Making Quad Green Ball Sprite
class QuadGreenBallClass(pygame.sprite.Sprite):
	def __init__(self):
		super(QuadGreenBallClass, self).__init__()
		self.image=Quadgreenball
		self.image.set_colorkey(black)
		self.rect=self.image.get_rect()
#Making Quad Red Ball Sprite 
class QuadRedBallClass(pygame.sprite.Sprite):
	def __init__(self):
		super(QuadRedBallClass, self).__init__()
		self.image=Quadredball
		self.image.set_colorkey(black)
		self.rect=self.image.get_rect()
#Making Penta Green Ball Sprite
class PentaGreenBallClass(pygame.sprite.Sprite):
	def __init__(self):
		super(PentaGreenBallClass, self).__init__()
		self.image=Pentagreenball
		self.image.set_colorkey(black)
		self.rect=self.image.get_rect()
#Making Penta Red Ball Sprite 
class PentaRedBallClass(pygame.sprite.Sprite):
	def __init__(self):
		super(PentaRedBallClass, self).__init__()
		self.image=Pentaredball
		self.image.set_colorkey(black)
		self.rect=self.image.get_rect()
#Making Hexa Green Ball Sprite
class HexaGreenBallClass(pygame.sprite.Sprite):
	def __init__(self):
		super(HexaGreenBallClass, self).__init__()
		self.image=Hexagreenball
		self.image.set_colorkey(black)
		self.rect=self.image.get_rect()
#Making Hexa Red Ball Sprite 
class HexaRedBallClass(pygame.sprite.Sprite):
	def __init__(self):
		super(HexaRedBallClass, self).__init__()
		self.image=Hexaredball
		self.image.set_colorkey(black)
		self.rect=self.image.get_rect()
#Making Hepta Green Ball Sprite
class HeptaGreenBallClass(pygame.sprite.Sprite):
	def __init__(self):
		super(HeptaGreenBallClass, self).__init__()
		self.image=Heptagreenball
		self.image.set_colorkey(black)
		self.rect=self.image.get_rect()
#Making Hepta Red Ball Sprite 
class HeptaRedBallClass(pygame.sprite.Sprite):
	def __init__(self):
		super(HeptaRedBallClass, self).__init__()
		self.image=Heptaredball
		self.image.set_colorkey(black)
		self.rect=self.image.get_rect()
class RulesClass(pygame.sprite.Sprite):
	def __init__(self):
		super (RulesClass, self).__init__()
		self.image=Rules
		self.rect=self.image.get_rect()
class RulesNRegClass(pygame.sprite.Sprite):
	def __init__(self):
		super (RulesNRegClass, self).__init__()
		self.image=RR
		self.rect=self.image.get_rect()
class StartGameIntro(pygame.sprite.Sprite):
	def __init__(self):
		super(StartGameIntro, self).__init__()
		self.image=Startscreen
		self.rect=self.image.get_rect()
class StartButton(pygame.sprite.Sprite):
	def __init__(self):
		super(StartButton, self).__init__()
		self.image=Startbutton
		self.rect=self.image.get_rect()

class WinnerRedClass(pygame.sprite.Sprite):
	def __init__(self):
		super(WinnerRedClass, self).__init__()
		self.image=WinnerRed
		self.rect=self.image.get_rect()
class WinnerGreenClass(pygame.sprite.Sprite):
	def __init__(self):
		super(WinnerGreenClass, self).__init__()
		self.image=WinnerGreen
		self.rect=self.image.get_rect()

#Intro of the Game
def Gameintro(sg,startgame,sb,startbutton):
	x=112.5
	y=300
	xr=100
	yr=240
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		sg.rect.x=0
		sg.rect.y=0
		startgame.draw(screenIntro)
		sb.rect.x=x
		sb.rect.y=y
		startbutton.draw(screenIntro)
		RulesB.rect.x=xr
		RulesB.rect.y=yr
		RulesGroup.draw(screenIntro)
		if event.type == pygame.MOUSEBUTTONDOWN:
			mx,my=pygame.mouse.get_pos()
			if x+164>mx>x and y+30>my>y:
				pygame.mixer.Sound.play(Click_Sound)
				break
			if xr+200>mx>xr and yr+50>my>yr:
				pygame.mixer.Sound.play(Click_Sound)
				RulesFun()
				break
		pygame.display.update() 
#For Rules Section
def RulesFun():
	x=112.5
	y=310
	mx=0
	my=0
	RR.rect.x=0
	RR.rect.y=0
	RRGroup.draw(screenIntro)
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			if event.type == pygame.MOUSEBUTTONDOWN:
				mx,my=pygame.mouse.get_pos()
				
			SB.rect.x=x
			SB.rect.y=y
			StartBGroup.draw(screenIntro)
		if x+164>mx>x and y+30>my>y:
			pygame.mixer.Sound.play(Click_Sound)
			break
		pygame.display.update() 
#Draws Board
def draw(n,w,h,bbe,back_group,bbl,bblg,grid):
	mx,my=pygame.mouse.get_pos()
	grid[my//h][mx//w]=1
	x=0
	y=0
	for row in grid:
		for col in row:
			bbe.rect.x=x
			bbe.rect.y=y
			back_group.draw(screen)
			x=x+w
		x=0
		y=y+h
	#Light Effect
	for i in range(0,Cube_Size):
		for j in range(0,Cube_Size):
			if grid[i][j]==1:
				x=i*w
				y=j*h
				bbl.rect.x=y
				bbl.rect.y=x
				bblg.draw(screen)
				grid[i][j]=0
			x=0
			y=0
	#If clicked then no light effect
	if event.type==pygame.MOUSEBUTTONDOWN:
		for row in grid:
			for col in row:
				bbe.rect.x=x
				bbe.rect.y=y
				back_group.draw(screen)
				x=x+w
			x=0
			y=y+h
	
	RedLine()
#First click for green 
def firstclickGreen(OneGBall,OneGBallGroup,c):
	if event.type==pygame.MOUSEBUTTONDOWN:
		pygame.mixer.Sound.play(Click_Sound1)
		mx,my=pygame.mouse.get_pos()
		gbg[my//Box_h][mx//Box_w]+=1
	for i in range(0,Cube_Size):
		for j in range(0,Cube_Size):
			if gbg[i][j]==1:
				c+=1
	return c
#First click for red
def firstclickRed(OneRBall,OneRBallGroup,c):
	if event.type==pygame.MOUSEBUTTONDOWN:
		pygame.mixer.Sound.play(Click_Sound1)
		mx,my=pygame.mouse.get_pos()
		rbg[my//Box_h][mx//Box_w]+=1
	for i in range(0,Cube_Size):
		for j in range(0,Cube_Size):
			if rbg[i][j]==1:
				c=+1
	return c 
def secondclickGreen():
#Corner	
	for i in range(0,Cube_Size):
		for j in range(0,Cube_Size):
			if gbg[i][j]==2:
				if [i,j] == [0,0]:
					gbg[i+1][j]+=1+rbg[i+1][j]
					gbg[i][j+1]+=1+rbg[i][j+1]
					gbg[i][j]=0
					rbg[i+1][j]=0
					rbg[i][j+1]=0
				if [i,j] == [0,Cube_Size-1]:
					gbg[i+1][j]+=1+rbg[i+1][j]
					gbg[i][j-1]+=1+rbg[i][j-1]
					gbg[i][j]=0
					rbg[i+1][j]=0
					rbg[i][j-1]=0
				if [i,j] == [Cube_Size-1,0]:
					gbg[i-1][j]+=1+rbg[i-1][j]
					gbg[i][j+1]+=1+rbg[i][j+1]
					gbg[i][j]=0
					rbg[i-1][j]=0
					rbg[i][j+1]=0
				if [i,j] == [Cube_Size-1,Cube_Size-1]:
					gbg[i-1][j]+=1+rbg[i-1][j]
					gbg[i][j-1]+=1+rbg[i][j-1]
					gbg[i][j]=0
					rbg[i-1][j]=0
					rbg[i][j-1]=0

			if gbg[i][j]>2:
				if [i,j] == [0,0]:
					gbg[i+1][j]+=1+rbg[i+1][j]
					gbg[i][j+1]+=1+rbg[i][j+1]
					gbg[i][j]=1
					rbg[i+1][j]=0
					rbg[i][j+1]=0
				if [i,j] == [0,Cube_Size-1]:
					gbg[i+1][j]+=1+rbg[i+1][j]
					gbg[i][j-1]+=1+rbg[i][j-1]
					gbg[i][j]=1
					rbg[i+1][j]=0
					rbg[i][j-1]=0
				if [i,j] == [Cube_Size-1,0]:
					gbg[i-1][j]+=1+rbg[i-1][j]
					gbg[i][j+1]+=1+rbg[i][j+1]
					gbg[i][j]=1
					rbg[i-1][j]=0
					rbg[i][j+1]=0
				if [i,j] == [Cube_Size-1,Cube_Size-1]:
					gbg[i-1][j]+=1+rbg[i-1][j]
					gbg[i][j-1]+=1+rbg[i][j-1]
					gbg[i][j]=1
					rbg[i-1][j]=0
					rbg[i][j-1]=0
	#Edges
	for i in range(0,Cube_Size):
		for j in range(0,Cube_Size):
			if gbg[i][j]==3:
				#Left most edges
				if j==0 and i in list(range(1,Cube_Size-1)):
					gbg[i+1][j]+=1+rbg[i+1][j]
					gbg[i-1][j]+=1+rbg[i-1][j]
					gbg[i][j+1]+=1+rbg[i][j+1]
					gbg[i][j]=0
					rbg[i+1][j]=0
					rbg[i-1][j]=0
					rbg[i][j+1]=0
				#Right most edges
				if j==Cube_Size-1 and i in list(range(1,Cube_Size-1)):
					gbg[i+1][j]+=1+rbg[i+1][j]
					gbg[i-1][j]+=1+rbg[i-1][j]
					gbg[i][j-1]+=1+rbg[i][j-1]
					gbg[i][j]=0
					rbg[i+1][j]=0
					rbg[i-1][j]=0
					rbg[i][j-1]=0
				#Top most edges
				if i==0 and j in list(range(1,Cube_Size-1)):
					gbg[i][j+1]+=1+rbg[i][j+1]
					gbg[i][j-1]+=1+rbg[i][j-1]
					gbg[i+1][j]+=1+rbg[i+1][j]
					gbg[i][j]=0
					rbg[i][j+1]=0
					rbg[i][j-1]=0
					rbg[i+1][j]=0
				#Bottom most edges
				if i==Cube_Size-1 and j in list(range(1,Cube_Size-1)):
					gbg[i][j+1]+=1+rbg[i][j+1]
					gbg[i][j-1]+=1+rbg[i][j-1]
					gbg[i-1][j]+=1+rbg[i-1][j]
					gbg[i][j]=0
					rbg[i][j+1]=0
					rbg[i][j-1]=0
					rbg[i-1][j]=0
			if gbg[i][j]>3:
				#Left most edges
				if j==0 and i in list(range(1,Cube_Size-1)):
					gbg[i+1][j]+=1+rbg[i+1][j]
					gbg[i-1][j]+=1+rbg[i-1][j]
					gbg[i][j+1]+=1+rbg[i][j+1]
					gbg[i][j]=1
					rbg[i+1][j]=0
					rbg[i-1][j]=0
					rbg[i][j+1]=0
				#Right most edges
				if j==Cube_Size-1 and i in list(range(1,Cube_Size-1)):
					gbg[i+1][j]+=1+rbg[i+1][j]
					gbg[i-1][j]+=1+rbg[i-1][j]
					gbg[i][j-1]+=1+rbg[i][j-1]
					gbg[i][j]=1
					rbg[i+1][j]=0
					rbg[i-1][j]=0
					rbg[i][j-1]=0
				#Top most edges
				if i==0 and j in list(range(1,Cube_Size-1)):
					gbg[i][j+1]+=1+rbg[i][j+1]
					gbg[i][j-1]+=1+rbg[i][j-1]
					gbg[i+1][j]+=1+rbg[i+1][j]
					gbg[i][j]=1
					rbg[i][j+1]=0
					rbg[i][j-1]=0
					rbg[i+1][j]=0
				#Bottom most edges
				if i==Cube_Size-1 and j in list(range(1,Cube_Size-1)):
					gbg[i][j+1]+=1+rbg[i][j+1]
					gbg[i][j-1]+=1+rbg[i][j-1]
					gbg[i-1][j]+=1+rbg[i-1][j]
					gbg[i][j]=1
					rbg[i][j+1]=0
					rbg[i][j-1]=0
					rbg[i-1][j]=0
	#Center
	for i in range(1,Cube_Size-1):
		for j in range(1,Cube_Size-1):
			#Checking for 4 clicks in cells other than extreme center
			if gbg[i][j]==4:
				if (i,j) not in (((Cube_Size/2)-1,(Cube_Size/2)-1),((Cube_Size/2),(Cube_Size/2)),((Cube_Size/2),(Cube_Size/2)-1),((Cube_Size/2)-1,(Cube_Size/2))):					
					gbg[i][j+1]+=1+rbg[i][j+1]
					gbg[i][j-1]+=1+rbg[i][j-1]
					gbg[i+1][j]+=1+rbg[i+1][j]
					gbg[i-1][j]+=1+rbg[i-1][j]
					gbg[i][j]=0
					rbg[i][j+1]=0
					rbg[i][j-1]=0
					rbg[i+1][j]=0
					rbg[i-1][j]=0
			#Checking for 4 clicks in cells other than extreme center
			if gbg[i][j]>4:	
				if (i,j) not in (((Cube_Size/2)-1,(Cube_Size/2)-1),((Cube_Size/2),(Cube_Size/2)),((Cube_Size/2),(Cube_Size/2)-1),((Cube_Size/2)-1,(Cube_Size/2))):				
					gbg[i][j+1]+=1+rbg[i][j+1]
					gbg[i][j-1]+=1+rbg[i][j-1]
					gbg[i+1][j]+=1+rbg[i+1][j]
					gbg[i-1][j]+=1+rbg[i-1][j]
					gbg[i][j]=1
					rbg[i][j+1]=0
					rbg[i][j-1]=0
					rbg[i+1][j]=0
					rbg[i-1][j]=0
			#Extreme center condition check
			if gbg[i][j]==8:
					gbg[i+1][j+1]+=1+rbg[i+1][j+1]
					gbg[i+1][j-1]+=1+rbg[i+1][j-1]
					gbg[i-1][j+1]+=1+rbg[i-1][j+1]
					gbg[i-1][j-1]+=1+rbg[i-1][j-1]
					gbg[i][j+1]+=1+rbg[i][j+1]
					gbg[i][j-1]+=1+rbg[i][j-1]
					gbg[i+1][j]+=1+rbg[i+1][j]
					gbg[i-1][j]+=1+rbg[i-1][j]
					gbg[i][j]=0
					rbg[i][j+1]=0
					rbg[i][j-1]=0
					rbg[i+1][j]=0
					rbg[i-1][j]=0
					rbg[i+1][j+1]=0
					rbg[i+1][j-1]=0
					rbg[i-1][j+1]=0
					rbg[i-1][j-1]=0

			if gbg[i][j]>8:
				gbg[i+1][j+1]+=1+rbg[i+1][j+1]
				gbg[i+1][j-1]+=1+rbg[i+1][j-1]
				gbg[i-1][j+1]+=1+rbg[i-1][j+1]
				gbg[i-1][j-1]+=1+rbg[i-1][j-1]
				gbg[i][j+1]+=1+rbg[i][j+1]
				gbg[i][j-1]+=1+rbg[i][j-1]
				gbg[i+1][j]+=1+rbg[i+1][j]
				gbg[i-1][j]+=1+rbg[i-1][j]
				gbg[i][j]=1
				rbg[i][j+1]=0
				rbg[i][j-1]=0
				rbg[i+1][j]=0
				rbg[i-1][j]=0
				rbg[i+1][j+1]=0
				rbg[i+1][j-1]=0
				rbg[i-1][j+1]=0
				rbg[i-1][j-1]=0

def secondclickRed():
#Corners
	for i in range(0,Cube_Size):
		for j in range(0,Cube_Size):
			if rbg[i][j]==2:
				if [i,j] == [0,0]:
					rbg[i+1][j]+=1+gbg[i+1][j]
					rbg[i][j+1]+=1+gbg[i][j+1]
					rbg[i][j]=0
					gbg[i+1][j]=0
					gbg[i][j+1]=0
					x=i*(Box_w)
					y=j*(Box_h)
				if [i,j] == [0,Cube_Size-1]:
					rbg[i+1][j]+=1+gbg[i+1][j]
					rbg[i][j-1]+=1+gbg[i][j-1]
					rbg[i][j]=0
					gbg[i+1][j]=0
					gbg[i][j-1]=0
				if [i,j] == [Cube_Size-1,0]:
					rbg[i-1][j]+=1+gbg[i-1][j]
					rbg[i][j+1]+=1+gbg[i][j+1]
					rbg[i][j]=0
					gbg[i-1][j]=0
					gbg[i][j+1]=0
				if [i,j] == [Cube_Size-1,Cube_Size-1]:
					rbg[i-1][j]+=1+gbg[i-1][j]
					rbg[i][j-1]+=1+gbg[i][j-1]
					rbg[i][j]=0
					gbg[i-1][j]=0
					gbg[i][j-1]=0

			if rbg[i][j]>2:
				if [i,j] == [0,0]:
					rbg[i+1][j]+=1+gbg[i+1][j]
					rbg[i][j+1]+=1+gbg[i][j+1]
					rbg[i][j]=1
					gbg[i+1][j]=0
					gbg[i][j+1]=0
					x=i*(Box_w)
					y=j*(Box_h)

				if [i,j] == [0,Cube_Size-1]:
					rbg[i+1][j]+=1+gbg[i+1][j]
					rbg[i][j-1]+=1+gbg[i][j-1]
					rbg[i][j]=1
					gbg[i+1][j]=0
					gbg[i][j-1]=0
					
				if [i,j] == [Cube_Size-1,0]:
					rbg[i-1][j]+=1+gbg[i-1][j]
					rbg[i][j+1]+=1+gbg[i][j+1]
					rbg[i][j]=1
					gbg[i-1][j]=0
					gbg[i][j+1]=0
					
				if [i,j] == [Cube_Size-1,Cube_Size-1]:
					rbg[i-1][j]+=1+gbg[i-1][j]
					rbg[i][j-1]+=1+gbg[i][j-1]
					rbg[i][j]=1
					gbg[i-1][j]=0
					gbg[i][j-1]=0
	#Edges
	for i in range(0,Cube_Size):
		for j in range(0,Cube_Size):
			#Checking for 3 clicks on edges
			if rbg[i][j]==3:
				#Left most edges
				if j==0 and i in list(range(1,Cube_Size-1)):
					rbg[i+1][j]+=1+gbg[i+1][j]
					rbg[i-1][j]+=1+gbg[i-1][j]
					rbg[i][j+1]+=1+gbg[i][j+1]
					rbg[i][j]=0
					gbg[i+1][j]=0
					gbg[i-1][j]=0
					gbg[i][j+1]=0
				#Right most edges	
				if j==Cube_Size-1 and i in list(range(1,Cube_Size-1)):
					rbg[i+1][j]+=1+gbg[i+1][j]
					rbg[i-1][j]+=1+gbg[i-1][j]
					rbg[i][j-1]+=1+gbg[i][j-1]
					rbg[i][j]=0
					gbg[i+1][j]=0
					gbg[i-1][j]=0
					gbg[i][j-1]=0
				#Top most edges
				if i==0 and j in list(range(1,Cube_Size-1)):
					rbg[i][j+1]+=1+gbg[i][j+1]
					rbg[i][j-1]+=1+gbg[i][j-1]
					rbg[i+1][j]+=1+gbg[i+1][j]
					rbg[i][j]=0
					gbg[i][j+1]=0
					gbg[i][j-1]=0
					gbg[i+1][j]=0
				#Bottom most edges
				if i==Cube_Size-1 and j in list(range(1,Cube_Size-1)):
					rbg[i][j+1]+=1+gbg[i][j+1]
					rbg[i][j-1]+=1+gbg[i][j-1]
					rbg[i-1][j]+=1+gbg[i-1][j]
					rbg[i][j]=0
					gbg[i][j+1]=0
					gbg[i][j-1]=0
					gbg[i-1][j]=0	

			if rbg[i][j]>3:
				#Left most edges
				if j==0 and i in list(range(1,Cube_Size-1)):
					rbg[i+1][j]+=1+gbg[i+1][j]
					rbg[i-1][j]+=1+gbg[i-1][j]
					rbg[i][j+1]+=1+gbg[i][j+1]
					rbg[i][j]=1
					gbg[i+1][j]=0
					gbg[i-1][j]=0
					gbg[i][j+1]=0
				#Right most edges
				if j==Cube_Size-1 and i in list(range(1,Cube_Size-1)):
					rbg[i+1][j]+=1+gbg[i+1][j]
					rbg[i-1][j]+=1+gbg[i-1][j]
					rbg[i][j-1]+=1+gbg[i][j-1]
					rbg[i][j]=1
					gbg[i+1][j]=0
					gbg[i-1][j]=0
					gbg[i][j-1]=0
				#Top most edges
				if i==0 and j in list(range(1,Cube_Size-1)):
					rbg[i][j+1]+=1+gbg[i][j+1]
					rbg[i][j-1]+=1+gbg[i][j-1]
					rbg[i+1][j]+=1+gbg[i+1][j]
					rbg[i][j]=1
					gbg[i][j+1]=0
					gbg[i][j-1]=0
					gbg[i+1][j]=0
				#Bottom most edges
				if i==Cube_Size-1 and j in list(range(1,Cube_Size-1)):
					rbg[i][j+1]+=1+gbg[i][j+1]
					rbg[i][j-1]+=1+gbg[i][j-1]
					rbg[i-1][j]+=1+gbg[i-1][j]
					rbg[i][j]=1
					gbg[i][j+1]=0
					gbg[i][j-1]=0
					gbg[i-1][j]=0
	#Center
	for i in range(1,Cube_Size-1):
		for j in range(1,Cube_Size-1):
			#Checking 4 clicks
			if rbg[i][j]==4:
				
				if (i,j) not in (((Cube_Size/2)-1,(Cube_Size/2)-1),((Cube_Size/2),(Cube_Size/2)),((Cube_Size/2),(Cube_Size/2)-1),((Cube_Size/2)-1,(Cube_Size/2))):
					rbg[i][j+1]+=1+gbg[i][j+1]
					rbg[i][j-1]+=1+gbg[i][j-1]
					rbg[i+1][j]+=1+gbg[i+1][j]
					rbg[i-1][j]+=1+gbg[i-1][j]
					rbg[i][j]=0
					gbg[i][j+1]=0
					gbg[i][j-1]=0
					gbg[i+1][j]=0
					gbg[i-1][j]=0

			if rbg[i][j]>4:
				if (i,j) not in (((Cube_Size/2)-1,(Cube_Size/2)-1),((Cube_Size/2),(Cube_Size/2)),((Cube_Size/2),(Cube_Size/2)-1),((Cube_Size/2)-1,(Cube_Size/2))): 
					rbg[i][j+1]+=1+gbg[i][j+1]
					rbg[i][j-1]+=1+gbg[i][j-1]
					rbg[i+1][j]+=1+gbg[i+1][j]
					rbg[i-1][j]+=1+gbg[i-1][j]
					rbg[i][j]=1
					gbg[i][j+1]=0
					gbg[i][j-1]=0
					gbg[i+1][j]=0
					gbg[i-1][j]=0
				#Extreme center check
				if rbg[i][j]==8:
					rbg[i+1][j+1]+=1+gbg[i+1][j+1]
					rbg[i+1][j-1]+=1+gbg[i+1][j-1]
					rbg[i-1][j+1]+=1+gbg[i-1][j+1]
					rbg[i-1][j-1]+=1+gbg[i-1][j-1]
					rbg[i][j+1]+=1+gbg[i][j+1]
					rbg[i][j-1]+=1+gbg[i][j-1]
					rbg[i+1][j]+=1+gbg[i+1][j]
					rbg[i-1][j]+=1+gbg[i-1][j]
					rbg[i][j]=0
					gbg[i][j+1]=0
					gbg[i][j-1]=0
					gbg[i+1][j]=0
					gbg[i-1][j]=0
					gbg[i+1][j+1]=0
					gbg[i+1][j-1]=0
					gbg[i-1][j+1]=0
					gbg[i-1][j-1]=0

				if rbg[i][j]>8:
					rbg[i+1][j+1]+=1+gbg[i+1][j+1]
					rbg[i+1][j-1]+=1+gbg[i+1][j-1]
					rbg[i-1][j+1]+=1+gbg[i-1][j+1]
					rbg[i-1][j-1]+=1+gbg[i-1][j-1]
					rbg[i][j+1]+=1+gbg[i][j+1]
					rbg[i][j-1]+=1+gbg[i][j-1]
					rbg[i+1][j]+=1+gbg[i+1][j]
					rbg[i-1][j]+=1+gbg[i-1][j]
					rbg[i][j]=1
					gbg[i][j+1]=0
					gbg[i][j-1]=0
					gbg[i+1][j]=0
					gbg[i-1][j]=0
					gbg[i+1][j+1]=0
					gbg[i+1][j-1]=0
					gbg[i-1][j+1]=0
					gbg[i-1][j-1]=0
#Printing Green Balls
def PatchyGreen():
	for i in range(0,Cube_Size):
		for j in range(0,Cube_Size):
			if gbg[i][j]==0:
				x=i*(Box_w)
				y=j*(Box_h)
				pg.rect.x=y
				pg.rect.y=x
				pg_group.draw(screen)
def PatchyRed():
	for i in range(0,Cube_Size):
		for j in range(0,Cube_Size):
			if rbg[i][j]==0:
				x=i*(Box_w)
				y=j*(Box_h)
				pg.rect.x=y
				pg.rect.y=x
				pg_group.draw(screen)
def ImagePrintGreen():
	x=0
	y=0
	for i in range(0,Cube_Size):
		for j in range(0,Cube_Size):
			if gbg[i][j]==1:
				x=i*Box_w
				y=j*Box_h
				OneGBall.rect.x=y
				OneGBall.rect.y=x
				OneGBallGroup.draw(screen)
			if gbg[i][j]==2:
				x=i*Box_w
				y=j*Box_h
				TwoGBall.rect.x=y
				TwoGBall.rect.y=x
				TwoGBallGroup.draw(screen)
			if gbg[i][j]==3:
				x=i*Box_w
				y=j*Box_h
				ThreeGBall.rect.x=y
				ThreeGBall.rect.y=x
				ThreeGBallGroup.draw(screen)
			if gbg[i][j]==4:
				x=i*Box_w
				y=j*Box_h
				QuadGBall.rect.x=y
				QuadGBall.rect.y=x
				QuadGBallGroup.draw(screen)
			if gbg[i][j]==5:
				x=i*Box_w
				y=j*Box_h
				PentaGBall.rect.x=y
				PentaGBall.rect.y=x
				PentaGBallGroup.draw(screen)
			if gbg[i][j]==6:
				x=i*Box_w
				y=j*Box_h
				HexaGBall.rect.x=y
				HexaGBall.rect.y=x
				HexaGBallGroup.draw(screen)
			if gbg[i][j]==7:
				x=i*Box_w
				y=j*Box_h
				HeptaGBall.rect.x=y
				HeptaGBall.rect.y=x
				HeptaGBallGroup.draw(screen)
			x=0
			y=0
def RedLine():
	for i in range(0,Cube_Size):
		for j in range(0,Cube_Size):
			pygame.draw.line(screen,Red,[i*Box_h,j*Box_w],[i*Box_h,Sbreath],3)
			pygame.draw.line(screen,Red,[i*Box_w,j*Box_h],[Swidth,j*Box_h],3)
			pygame.draw.line(screen,Red2,[(Cube_Size/2-1)*Box_h,(Cube_Size/2-1)*Box_h],[(Cube_Size/2-1)*Box_w,(Cube_Size/2+1)*Box_w],3)
			pygame.draw.line(screen,Red2,[(Cube_Size/2-1)*Box_h,(Cube_Size/2-1)*Box_h],[(Cube_Size/2+1)*Box_w,(Cube_Size/2-1)*Box_w],3)
			pygame.draw.line(screen,Red2,[(Cube_Size/2+1)*Box_h,(Cube_Size/2+1)*Box_h],[(Cube_Size/2+1)*Box_w,(Cube_Size/2-1)*Box_w],3)
			pygame.draw.line(screen,Red2,[(Cube_Size/2+1)*Box_h,(Cube_Size/2+1)*Box_h],[(Cube_Size/2-1)*Box_w,(Cube_Size/2+1)*Box_w],3)
#Printing Red Balls
def ImagePrintRed():
	x=0
	y=0
	for i in range(0,Cube_Size):
		for j in range(0,Cube_Size):
			if rbg[i][j]==1:
				x=i*Box_w
				y=j*Box_h
				OneRBall.rect.x=y
				OneRBall.rect.y=x
				OneRBallGroup.draw(screen)
			if rbg[i][j]==2:
				x=i*Box_w
				y=j*Box_h
				TwoRBall.rect.x=y
				TwoRBall.rect.y=x
				TwoRBallGroup.draw(screen)
			if rbg[i][j]==3:
				x=i*Box_w
				y=j*Box_h
				ThreeRBall.rect.x=y
				ThreeRBall.rect.y=x
				ThreeRBallGroup.draw(screen)
			if rbg[i][j]==4:
				x=i*Box_w
				y=j*Box_h
				QuadRBall.rect.x=y
				QuadRBall.rect.y=x
				QuadRBallGroup.draw(screen)
			if rbg[i][j]==5:
				x=i*Box_w
				y=j*Box_h
				PentaRBall.rect.x=y
				PentaRBall.rect.y=x
				PentaRBallGroup.draw(screen)
			if rbg[i][j]==6:
				x=i*Box_w
				y=j*Box_h
				HexaRBall.rect.x=y
				HexaRBall.rect.y=x
				HexaRBallGroup.draw(screen)
			if rbg[i][j]==7:
				x=i*Box_w
				y=j*Box_h
				HeptaRBall.rect.x=y
				HeptaRBall.rect.y=x
				HeptaRBallGroup.draw(screen)
			x=0
			y=0
def GreenLine():
	for i in range(0,Cube_Size):
		for j in range(0,Cube_Size):
			pygame.draw.line(screen,Green,[i*Box_h,j*Box_w],[i*Box_h,Sbreath],3)
			pygame.draw.line(screen,Green,[i*Box_w,j*Box_h],[Swidth,j*Box_h],3)
			pygame.draw.line(screen,Green2,[(Cube_Size/2-1)*Box_h,(Cube_Size/2-1)*Box_h],[(Cube_Size/2-1)*Box_w,(Cube_Size/2+1)*Box_w],3)
			pygame.draw.line(screen,Green2,[(Cube_Size/2-1)*Box_h,(Cube_Size/2-1)*Box_h],[(Cube_Size/2+1)*Box_w,(Cube_Size/2-1)*Box_w],3)
			pygame.draw.line(screen,Green2,[(Cube_Size/2+1)*Box_h,(Cube_Size/2+1)*Box_h],[(Cube_Size/2+1)*Box_w,(Cube_Size/2-1)*Box_w],3)
			pygame.draw.line(screen,Green2,[(Cube_Size/2+1)*Box_h,(Cube_Size/2+1)*Box_h],[(Cube_Size/2-1)*Box_w,(Cube_Size/2+1)*Box_w],3)
def WinGame(GER,GEG):
	countG=0
	countR=0
	for i in range(Cube_Size):
		for j in range(Cube_Size):
			if gbg[i][j]==0:
				countG+=1
	for i in range(Cube_Size):
		for j in range(Cube_Size):
			if rbg[i][j]==0:
				countR+=1
	if countG==Cube_Size*Cube_Size:
		print("Red won")
		GER()
	if countR==Cube_Size*Cube_Size:
		print("Green won")
		GEG()
def GameEndRed():
	pygame.mixer.music.stop()
	pygame.mixer.music.load("Thug.mp3")
	pygame.mixer.music.play(1)
	pygame.time.delay(2000)
	screenEnd=pygame.display.set_mode((395,395))
	WinnerRed=pygame.image.load("red_won.png") 
	WR.rect.x=0
	WR.rect.y=0
	WinnerRedGroup.draw(screenEnd)
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		pygame.display.update()
def GameEndGreen():
	pygame.mixer.music.stop()
	pygame.mixer.music.load("Thug.mp3")
	pygame.mixer.music.play(1)
	pygame.time.delay(2000)
	screenEnd=pygame.display.set_mode((395,395))
	WinnerGreen=pygame.image.load("green_won.png")
	WG.rect.x=0
	WG.rect.y=0
	WinnerGreenGroup.draw(screenEnd)
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		pygame.display.update()
def WrongRedClick(checkG,counter,i,j):
	if rbg[j][i]>0 and gbg[j][i]>0:
		rbg[j][i]-=1
		counter-=1
	return counter
def WrongGreenClick(checkR,counter,i,j):
	if gbg[j][i]>0 and checkR[j][i]>0:
		gbg[j][i]-=1
		counter-=1
	return counter
#Making Corner board
back_group=pygame.sprite.Group()
bb=BackBlock()
back_group.add(bb)
#Patch Background
pg_group=pygame.sprite.Group()
pg=PatchGreyClass()
pg_group.add(pg)
#calling One Green ball
OneGBallGroup=pygame.sprite.Group()
OneGBall=OneGreenBallClass()
OneGBallGroup.add(OneGBall)
#calling One Red ball
OneRBallGroup=pygame.sprite.Group()
OneRBall=OneRedBallClass()
OneRBallGroup.add(OneRBall)
#calling Double Green ball
TwoGBallGroup=pygame.sprite.Group()
TwoGBall=DoubleGreenBallClass()
TwoGBallGroup.add(TwoGBall)
#calling Double Red ball
TwoRBallGroup=pygame.sprite.Group()
TwoRBall=DoubleRedBallClass()
TwoRBallGroup.add(TwoRBall)
#calling Triple Green ball
ThreeGBallGroup=pygame.sprite.Group()
ThreeGBall=TripleGreenBallClass()
ThreeGBallGroup.add(ThreeGBall)
#calling Triple Red ball
ThreeRBallGroup=pygame.sprite.Group()
ThreeRBall=TripleRedBallClass()
ThreeRBallGroup.add(ThreeRBall)
#calling Quad Green ball
QuadGBallGroup=pygame.sprite.Group()
QuadGBall=QuadGreenBallClass()
QuadGBallGroup.add(QuadGBall)
#calling Quad Red ball
QuadRBallGroup=pygame.sprite.Group()
QuadRBall=QuadRedBallClass()
QuadRBallGroup.add(QuadRBall)
#calling Penta Green ball
PentaGBallGroup=pygame.sprite.Group()
PentaGBall=PentaGreenBallClass()
PentaGBallGroup.add(PentaGBall)
#calling Penta Red ball
PentaRBallGroup=pygame.sprite.Group()
PentaRBall=PentaRedBallClass()
PentaRBallGroup.add(PentaRBall)
#calling Hexa Green ball
HexaGBallGroup=pygame.sprite.Group()
HexaGBall=HexaGreenBallClass()
HexaGBallGroup.add(HexaGBall)
#calling Hexa Red ball
HexaRBallGroup=pygame.sprite.Group()
HexaRBall=HexaRedBallClass()
HexaRBallGroup.add(HexaRBall)
#calling Hepta Green ball
HeptaGBallGroup=pygame.sprite.Group()
HeptaGBall=HeptaGreenBallClass()
HeptaGBallGroup.add(HeptaGBall)
#calling Hepta Red ball
HeptaRBallGroup=pygame.sprite.Group()
HeptaRBall=HeptaRedBallClass()
HeptaRBallGroup.add(HeptaRBall)
#calling Light Effect
BBLGroup=pygame.sprite.Group()
BBL=BackBlockLight()
BBLGroup.add(BBL)
#Start game screen
StartGroup=pygame.sprite.Group()
SG=StartGameIntro()
StartGroup.add(SG)
#Start Button
StartBGroup=pygame.sprite.Group()
SB=StartButton()
StartBGroup.add(SB)
#Rules Button
RulesGroup=pygame.sprite.Group()
RulesB=RulesClass()
RulesGroup.add(RulesB)
#Rules And Regulations
RRGroup=pygame.sprite.Group()
RR=RulesNRegClass()
RRGroup.add(RR)

#Winner Sprite
#Red
WinnerRedGroup=pygame.sprite.Group()
WR=WinnerRedClass()
WinnerRedGroup.add(WR)
#Green
WinnerGreenGroup=pygame.sprite.Group()
WG=WinnerGreenClass()
WinnerGreenGroup.add(WG)

#Calling Game Intro Screen
Gameintro(SG,StartGroup,SB,StartBGroup)
screen=pygame.display.set_mode((Swidth,Sbreath))
#Clock
clock=pygame.time.Clock()
pygame.mixer.music.play(-1)
while not game_over:
	#Updating Second click
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		#So that Draw doesnt overwrite
		if N_count==0:
			draw(Cube_Size,Box_w,Box_h,bb,back_group,BBL,BBLGroup,backgrid)
			
		#If odd then green and if even then redif counter%2!=0:
		if event.type == pygame.MOUSEBUTTONDOWN:
			mx,my=pygame.mouse.get_pos()
			i=mx//Box_w
			j=my//Box_h
			if counter%2!=0:	
				checkR = rbg
				N_count=firstclickGreen(OneGBall,OneGBallGroup,counter)
				counter=WrongGreenClick(checkR,counter,i,j)
			elif counter%2==0: 
				checkG = gbg
				N_count=firstclickRed(OneRBall,OneRBallGroup,counter)
				counter=WrongRedClick(checkG,counter,i,j)	
		#Checking winner
		if counter>2:
			#Using Call Back
			WinGame(GameEndRed,GameEndGreen)
		if event.type == pygame.MOUSEBUTTONDOWN:
			counter+=1
			
	if counter>0:
		if counter%2!=0:
			PatchyGreen()
			GreenLine()
		elif counter%2==0: 
			PatchyRed()
			RedLine()
	secondclickGreen()
	secondclickRed()
	ImagePrintGreen()
	ImagePrintRed()
	#update
	pygame.display.update()
