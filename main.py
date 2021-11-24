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


winner = 0 
game_over = False


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


    pygame.display.update()        
pygame.quit()