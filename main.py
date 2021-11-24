from typing import Collection
import  pygame
from pygame.locals import *
pygame.init()


screen_wigth = 300
screen_hight = 300

screen = pygame.display.set_mode((screen_wigth, screen_hight))
pygame.display.set_caption("TicTacToe")

line_wigth = 5

markers = []
clicked = False
pos = []
player = 1
green = (0,255,0)
red = (255,0,0)
blue = (0,0,255)


winner = 0 
game_over = False
font = pygame.font.SysFont(None,50)
again_rect =Rect(screen_wigth//2 - 80 ,screen_hight//2+10, 220,45)

def draw_grid():
    bg = (255,255,200)
    grid= (50,50,50)
    screen.fill(bg)
    for i in range(1,3):
        pygame.draw.line(screen,grid,(0,i*100),(screen_wigth,i*100),line_wigth)
        pygame.draw.line(screen,grid,(i*100, 0),(i*100,screen_hight),line_wigth)

for x in range(3):
    row = [0]*3
    markers.append(row)
# print(markers)



def draw_markers():
	x_pos = 0
	for x in markers:
		y_pos = 0
		for y in x:
			if y == 1:
				pygame.draw.line(screen, red, (x_pos * 100 + 15, y_pos * 100 + 15), (x_pos * 100 + 85, y_pos * 100 + 85), line_wigth)
               
				pygame.draw.line(screen, red, (x_pos * 100 + 85, y_pos * 100 + 15), (x_pos * 100 + 15, y_pos * 100 + 85), line_wigth)

			if y == -1:
				pygame.draw.circle(screen, green, (x_pos * 100+50, y_pos * 100 + 50), 38, line_wigth)
			y_pos += 1
		x_pos += 1	




def check_winner():
    global winner
    global game_over
    y_pos = 0 
    for x in markers:
        # Check  in Columns
        if sum(x) ==3:
            winner =1
            game_over =True
        if sum(x) == -3:
            winner =2
            game_over =True
        # Check in  Rows
        if markers[0][y_pos] + markers[1][y_pos]+markers[2][y_pos] ==3:
            winner = 1
            game_over =True
        if markers[0][y_pos] + markers[1][y_pos]+markers[2][y_pos] == -3:
            winner = 2
            game_over =True
        y_pos +=1
    # Checking Cross
    if markers[0][0] +markers[1][1]+markers[2][2] ==3 or markers[0][2] +markers[1][1]+markers[2][0] ==3:
        winner = 1
        game_over =True
    if markers[0][0] +markers[1][1]+markers[2][2] == -3 or markers[0][2] +markers[1][1]+markers[2][0] == -3:
        winner = 2
        game_over =True

def draw_winner(winner):
    win_text ="Player"+str(winner) + "Wins!"
    win_img = font.render(win_text,True,blue)
    pygame.draw.rect(screen,green,(screen_wigth//2 -100, screen_hight//2 - 60,230,60))
    screen.blit(win_img,(screen_wigth//2 -100, screen_hight//2 - 50))

    again_play = "Play Again ?"
    again_img = font.render(again_play,True,blue)
    pygame.draw.rect(screen,green,again_rect)
    screen.blit(again_img,(screen_wigth//2 - 80, screen_hight//2 + 10))
    




run = True
while run:

    draw_grid()
    draw_markers()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

# Mouse Click togole 
        if game_over == False:
            if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
                clicked = True
            if event.type == pygame.MOUSEBUTTONDOWN and clicked == True:
                clicked = False
                pos = pygame.mouse.get_pos()
                cell_x = pos[0]
                cell_y = pos[1]

                if markers[cell_x // 100][cell_y // 100] == 0:
                    markers[cell_x // 100][cell_y // 100] = player
                    player *= -1
                    check_winner()
                    
    if game_over ==True:
        draw_winner(winner)
        #check for mouseclick to see if we clicked on Play Again
        if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
            clicked = True
        if event.type == pygame.MOUSEBUTTONUP and clicked == True:
            clicked = False
            pos = pygame.mouse.get_pos()
            print(pos)
            if again_rect.collidepoint(pos):
				#reset variables
                markers = []
                pos=[]
                player = 1
                winner = 0
                game_over = False
				#create empty 3 x 3 list to represent the grid
                for x in range (3):
                    row = [0] * 3
                    markers.append(row)
    pygame.display.update()        
pygame.quit()