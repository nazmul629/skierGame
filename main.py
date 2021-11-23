import  pygame

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
print(markers)

def draw_markers():
	x_pos = 0
	for x in markers:
		y_pos = 0
		for y in x:
			if y == 1:
				pygame.draw.line(screen, red, (x_pos * 100 + 15, y_pos * 100 + 15), (x_pos * 100 + 85, y_pos * 100 + 85), line_wigth)
				pygame.draw.line(screen, red, (x_pos * 100 + 85, y_pos * 100 + 15), (x_pos * 100 + 15, y_pos * 100 + 85), line_wigth)
			if y == -1:
				pygame.draw.circle(screen, green, (x_pos * 100 + 50, y_pos * 100 + 50), 38, line_wigth)
			y_pos += 1
		x_pos += 1	



    
 

run = True
while run:

    draw_grid()
    draw_markers()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
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

    pygame.display.update()        
pygame.quit()