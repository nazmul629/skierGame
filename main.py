import  pygame

pygame.init()


screen_wigth = 300
screen_hight = 300

screen = pygame.display.set_mode((screen_wigth, screen_hight))
pygame.display.set_caption("TicTacToe")

line_wigth = 5

markers = []
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

run = True
while run:

    draw_grid()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False



    pygame.display.update()        
pygame.quit()