import pygame,sys,random
import os


os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (100,100) #game window position with respect to laptop display

def ball_animation():
    global ball_speed_x,ball_speed_y,player_score,opponent_score,score_time
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        pygame.mixer.Sound.play(wall_hit_sound)
        ball_speed_y *= -1
    if ball.left <= 0:
        pygame.mixer.Sound.play(score_sound)
        player_score += 1
        score_time = pygame.time.get_ticks() # eturns how long game is running from its started

    if ball.right >= screen_width:
        pygame.mixer.Sound.play(score_sound)
        opponent_score += 1
        score_time = pygame.time.get_ticks()


    if ball.colliderect(player) and ball_speed_x > 0:
        pygame.mixer.Sound.play(wall_hit_sound)
        if abs(ball.right - player.left) < 10:
            ball_speed_x *= -1
        elif abs(ball.bottom - player.top) < 10 and ball_speed_y > 0:
            ball_speed_y *= -1
        elif abs(ball.top - player.bottom) < 10 and ball_speed_y < 0:
            ball_speed_y *= -1

    if ball.colliderect(opponent) and ball_speed_x < 0 :
        pygame.mixer.Sound.play(wall_hit_sound)
        if abs(ball.left - opponent.right) < 10:
            ball_speed_x *= -1
        elif abs(ball.bottom - opponent.top) < 10 and ball_speed_y > 0:
            ball_speed_y *= -1
        elif abs(ball.top - opponent.bottom) < 10 and ball_speed_y < 0:
            ball_speed_y *= -1



def ball_restart():
    global ball_speed_x,ball_speed_y,score_time,game_font

    current_time = pygame.time.get_ticks()
    ball.center = (screen_width/2,screen_height/2)

    if current_time - score_time < 700:
        number_three = game_font.render("3",False,orange)
        screen.blit(number_three,(screen_width/2 -10,screen_height/2 -50))
    if 700< current_time - score_time < 1400:
        number_two = game_font.render("2",False,orange)
        screen.blit(number_two,(screen_width/2 - 10,screen_height/2 -50))
    if 1400< current_time-score_time<2100:
        number_one = game_font.render("1", False, orange)
        screen.blit(number_one, (screen_width / 2 - 10, screen_height / 2 - 50))

    if current_time - score_time < 2100:
        ball_speed_x,ball_speed_y = 0,0
    else:
        pygame.mixer.Sound.play(time_counter_sound)
        ball_speed_y = 5*random.choice((1, -1))
        ball_speed_x = 5*random.choice((1, -1))
        score_time = None




def player_animation(): # player la screen madhe thevnya sathi
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

def opponent_ai():
    if opponent.top < ball.centery:
        opponent.top += opponent_speed
    if opponent.bottom > ball.centery:
        opponent.y -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height

def win():
    global player_score,opponent_score,score_time

    player.centery = screen_height/2
    opponent.centery = screen_height/2
    screen.fill(bg_color)  # fill screen with that color
    pygame.draw.rect(screen, (231, 76, 60), player)  # surface,color,object
    pygame.draw.rect(screen, (231, 76, 60), opponent)
    pygame.draw.line(screen, light_grey, (screen_width / 2, 0), (screen_width / 2, screen_height))

    if player_score == 5:
        player_win = game_font.render('You Win.',False,orange)
        screen.blit(player_win,(screen_width/2 - 63,screen_height/2 -10))
    else:
        opponent_win = game_font.render('You Lose.',False,orange)
        screen.blit(opponent_win, (screen_width / 2 - 62, screen_height / 2 - 10))

    info = game_font.render('Press SPACE To Play Again',False,orange)
    screen.blit(info,(screen_width/2 - 205,screen_height/2 + 30))

    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player_score = 0
                    opponent_score = 0
                    score_time = pygame.time.get_ticks()
                    return True
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

def check_win():
    if player_score == 5 or opponent_score == 5:
        win()
        player.centery = screen_height/2
        opponent.centery = screen_height/2

# General setup
pygame.mixer.pre_init(44100,-16,2,512) # reducing sound delay by reducing buffer size
pygame.init()  # for initializing pygame modules
clock = pygame.time.Clock() # requires to control while loop execution speed

# setting up the main window
screen_width = 1080
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Pong by NIKHIL')


#gameIcon = pygame.image.load('media\\icon.png')
#pygame.display.set_icon(gameIcon)
##########################################################

# Game Rectangles
ball = pygame.Rect(screen_width/2 - 15,screen_height/2 - 15,30,30) # x,y,width,height
player = pygame.Rect(screen_width-20,screen_height/2 - 60 ,10,120)
opponent = pygame.Rect(10,screen_height/2 - 60,10,120)

bg_color = pygame.Color('grey12') # asa pn color milavu shakto
light_grey = (200,200,200) # kivva RGB values ne pn milavu shakto
orange = (230, 126, 34)

ball_speed_x = 15* random.choice((1,-1))
ball_speed_y = 15* random.choice((1,-1))
player_speed = 0
opponent_speed = 5

#Text Variables
player_score = 0
opponent_score = 0
game_font = pygame.font.SysFont('calibri',42) #font,size

# score timer
score_time = True

#sounds
wall_hit_sound = pygame.mixer.Sound('Hit_sound.wav')
score_sound = pygame.mixer.Sound('score.wav')
time_counter_sound = pygame.mixer.Sound('time_counter.wav')
#playing background music
pygame.mixer.music.load("background.wav")  # fackt load kelay he music play nahi
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)  # -1 argument mhanje infinitly play karnya sathi
while True:
    #Handling input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed = 5
            if event.key == pygame.K_UP:
                player_speed = -5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                player_speed = 0


    if check_win():
        player.centery = screen_height/2
    ball_animation()
    player_animation()
    opponent_ai()






    #Visuals
    screen.fill(bg_color) #fill screen with that color
    pygame.draw.rect(screen,(231, 76, 60),player) # surface,color,object
    pygame.draw.rect(screen,(231, 76, 60),opponent)
    pygame.draw.ellipse(screen,(41, 128, 185),ball) # width,height rectangle chi same ahe mhanun to circle draw hoil
    pygame.draw.line(screen,light_grey,(screen_width/2,0),(screen_width/2,screen_height))

    if score_time:
        ball_restart()

    player_text = game_font.render(f'{player_score}',False,light_grey) #text,antialiase,color   - ethe basically text surface tayar hoil tyala main surface var taku mg apan
    screen.blit(player_text,(screen_width/2 + 10,20)) #used to put one surface on another - surface,(x,y)

    player_text = game_font.render(f'{opponent_score}', False, light_grey)
    screen.blit(player_text, (screen_width / 2 - 25,20))
    #Updating the window
    pygame.display.update() # to update old screen
    clock.tick(100) # it limits how fast the loop runs/sec