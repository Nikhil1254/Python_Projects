import pygame
import random
import sys

pygame.init()
pygame.mixer.init()  # music sathi hi libary he module ahe pygame madhe

beep = pygame.mixer.Sound("beep.wav") #sound chya madatine ekavar ek music play karu shakto 'wav' format ch lagto tyala


screen_width = 900
screen_height = 600


#set icon
gameIcon = pygame.image.load('snakes.png')
pygame.display.set_icon(gameIcon)
#colors   rgb chya values varies from 0-255 (r,g,b)
white=(255,255,255)   #sagle colors milun white
red=(255,0,0)
black=(0,0,0)
crimsom=(204,0,102)
light_blue=(204,229,255)
orange = (255,165,0)
# window
gameWindow=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Snake game")  #window title
font = pygame.font.SysFont("comicsansms", 40)
clock = pygame.time.Clock()  # apla frames la time to time update karayla lagta
fps = 60  # frames per second
pygame.display.update()


# game specific variables


def text_screen(text,color,x,y):
    screen_text = font.render(text,True , color)  # (text,antialising,color)  font object cha use karun ani render function vaprun apan ek surface tayar kartoy dilelya string sathi
    gameWindow.blit(screen_text,[int(x),int(y)]) # blit function chya madatine to surface mainscreen valya surface var place kartoy apan

def plot_snake(gameWindow , color ,snake_list,snake_size):
    flag = 0
    for x,y in snake_list:
        pygame.draw.rect(gameWindow,color,[x,y,snake_size,snake_size])

    x,y = snake_list[len(snake_list)-1]
    pygame.draw.rect(gameWindow,orange,[x,y,snake_size,snake_size])    # jo last la ahe na list madhe to sapach head ahe tyala seperate color detoy apan

def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill(white)
        text_screen("Welcome to SNAKES.",black,250,250)
        text_screen("Press SPACEBAR to START",crimsom,200,350)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load("background.mp3")  # fackt load kelay he music play nahi
                    pygame.mixer.music.play(-1)  # -1 argument mhanje infinitly play karnya sathi
                    gameloop()

                if event.key == pygame.K_ESCAPE:
                    sys.exit()

        pygame.display.update()
        clock.tick(60)

#Game loop
def gameloop():
    # game specific variables
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 100
    velocity_x = 0
    velocity_y = 0
    snake_size = 15
    food_x = random.randint(30, screen_width / 1.5)  # 0-screen_width ya range madhun ek random number return karnar.
    food_y = random.randint(80,
                            screen_height / 1.5)  # 0-screen_height ya range madhun ek random number generate karun return karnar.

    score = 0
    init_velocity = 3

    snake_list = []
    snake_length = 1
    with open("HIGHSCORE.txt","r") as f:    # ashi file open keli tar tila aplyala close karaychi garaj nahi padat.deshi tarika
        highscore = f.read()




    while not exit_game:

        if game_over:
            gameWindow.fill(white)
            text_screen("Your Score : "+str(score),black,screen_width/2-150,screen_height/2-200)
            text_screen("Game Over! Press Enter To Contiue", red,screen_width/2-350,screen_height/2-50)
            text_screen("Press Escape to exit.", crimsom,screen_width/2-200,screen_height/1.5)


            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    with open("HIGHSCORE.txt", "w") as f:
                        f.write(str(highscore))
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        pygame.mixer.music.load("background.mp3")  # fackt load kelay he music play nahi
                        pygame.mixer.music.play(-1)
                        gameloop()

                    if event.key ==  pygame.K_ESCAPE:
                        with open("HIGHSCORE.txt","w") as f:
                            f.write(str(highscore))
                        sys.exit()


        else:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:    # QUIT ha event ahe window la band karnarya button var press kel ki occur hoto
                    with open("HIGHSCORE.txt","w") as f:
                        f.write(str(highscore))
                    sys.exit()

                if event.type == pygame.KEYDOWN:   #keyboard var key press keli tya event la KEYDOWN
                    if event.key == pygame.K_ESCAPE :
                        with open("HIGHSCORE.txt", "w") as f:
                            f.write(str(highscore))
                        sys.exit()

                    if event.key == pygame.K_RIGHT:  #mhanje right arrow press kelay
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:  #mhanje right arrow press kelay
                        velocity_x = -init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:  #mhanje right arrow press kelay
                        velocity_y = -init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:  #mhanje right arrow press kelay
                        velocity_y = init_velocity
                        velocity_x = 0

            snake_x += velocity_x
            snake_y += velocity_y

            if abs(snake_x - food_x)<8 and abs(snake_y - food_y)<8:    # food khanyach logic
                beep.play()
                score+=10
                food_x = random.randint(30,screen_width / 1.5)
                food_y = random.randint(80, screen_height / 1.5)
                snake_length += 5
                if score>int(highscore):
                    with open("HIGHSCORE.txt","w") as f:
                        highscore = score
                        f.write(str(highscore))

            gameWindow.fill(light_blue)   # window la kontya color ne fill karaychay.
            text_screen("Score : " + str(score)+"  Highscore: "+str(highscore), crimsom, 5, 5)    # ya saglya goshti white nantar ch havya nahitar changes zalele kalnar nhi screen parat white color ne fill hoil
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size]) # food plot kartoy ethe

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list)>snake_length:    # control kartoy fakt levdi legth ahe snake chi tevdech co-ordinates plot karnya sathi
                del snake_list[0]

            if snake_list.count([snake_x,snake_y])>1:  # swatala tough kel tar out val logic.toch co-ordinate parat ala mhanje touch zalay
                game_over = True
                pygame.mixer.music.load("explosion.mp3")  # fackt load kelay he music play nahi
                pygame.mixer.music.play()

            if snake_x>screen_width or snake_y>screen_height or snake_x<0 or snake_y<0:                  # boundaries la touch kelyavar game over sathi.
                pygame.mixer.music.load("explosion.mp3")  # fackt load kelay he music play nahi
                pygame.mixer.music.play()
                game_over = True

            plot_snake(gameWindow,black,snake_list,snake_size)

        pygame.display.update()  # display madhe changes update karnya sathi
        clock.tick(fps)


if __name__ == '__main__':
    welcome()

pygame.quit()   # pygame la dis_initialize kel
sys.exit()         # program close kela.
