#debuging tools
import logging

logging.basicConfig(level=logging.INFO) 


#imports
import pygame
import random
import os
os.environ['SDL_AUDIODRIVER'] = 'dsp'
pygame.init()
pygame.font.init()

#logging.info(pygame.font.get_fonts())

#const var def
WIDTH, HEIGHT = 600,400
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Pong =)")

BG = pygame.transform.scale(pygame.image.load("pongbg.png"), (WIDTH,HEIGHT))

DEBUG_SQU = pygame.Rect(0,0,WIDTH,HEIGHT)


PLAYER_WIDTH = 10
PLAYER_HEIGHT = 70
PLAYER_VEL = 5

BALL_RADI = 10;


FONT = pygame.font.SysFont("Timesnewroman",36)
FONT_BOLD = pygame.font.SysFont("Timesnewroman",36,bold=True)
#FONT.render(f"Time: {round(elapsed_time)}s", 1, "black")

#char displays
def draw(startscreen,start_active,play_active,player,player1,ball,p_score,p1_score):
    
    pygame.draw.rect(WIN,("red"), DEBUG_SQU)
    WIN.blit(BG, (0,0))
    
    
    if startscreen == "Credits":
        credit_text = FONT.render("Made by Rejuvenation_",1,"white")
        WIN.blit(credit_text,((WIDTH-credit_text.get_width())/2,HEIGHT/2))
    
    if startscreen == "Options":
        option_text = FONT.render("nuh uh",1,"white")
        WIN.blit(option_text,((WIDTH-option_text.get_width())/2,HEIGHT/2))
    
    
    if not (startscreen == "1p" or startscreen == "2p"):
        if start_active == 0:
            active_choice_text = FONT.render("Play",1,"white")
        elif start_active == 1:
            active_choice_text = FONT.render("Options",1,"white")
        elif start_active == 2:
            active_choice_text = FONT.render("Quit",1,"white")
        elif start_active == 3:
            active_choice_text = FONT.render("Credits",1,"white")
        else:
            active_choice_text = FONT.render("Null",1,"black")
    
    
    
    if startscreen == "Title":
        title_text = FONT.render("Legally Distinct Pong Game   =D",1,"white")
        WIN.blit(title_text,((WIDTH-title_text.get_width())/2,25))
        WIN.blit(active_choice_text,((WIDTH-active_choice_text.get_width())/2,HEIGHT/2))
        
    if startscreen == "Play":
        
        if play_active == 0:
            play_obt1_text = FONT_BOLD.render("Play 1 Player",1,"white") 
            play_obt2_text = FONT.render("Play 2 Player",1,"white")
        elif play_active == 1:
            play_obt1_text = FONT.render("Play 1 Player",1,"white") 
            play_obt2_text = FONT_BOLD.render("Play 2 Player",1,"white")
        
        WIN.blit(play_obt1_text,(25,(HEIGHT/2)-45))
        WIN.blit(play_obt2_text,(25,(HEIGHT/2)+15))
        
        
        
        
    if not (startscreen == "Title" or startscreen == "1p" or startscreen == "2p"):
        title_text = FONT.render(startscreen,1,"white")
        WIN.blit(title_text,((WIDTH-title_text.get_width())/2,25))    
        
    
    
    
    
    
    if startscreen == "1p" or startscreen == "2p":   
        pygame.draw.rect(WIN,("white"), player)
        pygame.draw.rect(WIN,("white"), player1)
        pygame.draw.rect(WIN,("red"),ball)
        
        p_score_text = FONT.render(f"{p_score}",1,"white")
        WIN.blit(p_score_text,(((WIDTH-p_score_text.get_width())/2)-25,25))
        
        p1_score_text = FONT.render(f"{p1_score}",1,"white")
        WIN.blit(p1_score_text,(((WIDTH-p1_score_text.get_width())/2)+25,25))
    
    
    
    
    
    
    
    
    pygame.display.update()



   
    
#main loop
def main ():
    run = True
#loop vars
    
    clock = pygame.time.Clock()
    player = pygame.Rect(60,(HEIGHT - PLAYER_HEIGHT)/2, PLAYER_WIDTH,PLAYER_HEIGHT)
    player1 = pygame.Rect(WIDTH-60,(HEIGHT - PLAYER_HEIGHT)/2, PLAYER_WIDTH,PLAYER_HEIGHT)
    
    player_move_u = False
    player_move_d = False
    player1_move_u = False
    player1_move_d = False
    
    
    ball = pygame.Rect((WIDTH-BALL_RADI)/2,(HEIGHT-BALL_RADI)/2,BALL_RADI,BALL_RADI)
    
    p_score = 0
    p1_score = 0
    

#Single Input Shennanigans      
    startscreen = "Title"
    start_active = 0    
    start_changed_L = False
    start_changed_R = False
    start_changed_Enter = True
    
    play_active = 0;
    play_changed_Up = False
    play_changed_Down = False
    play_changed_Enter = True
#ball vel updates as game cont.    
    ball_velx = 5
    ball_vely = random.uniform(-2.0,2.0)
    
   #looping loop 
    while run: 
        clock.tick(60)   
        #logging.info(start_changed_Enter)
    #Quitting
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            
         
        keys = pygame.key.get_pressed()   
        
        
        
        if (startscreen == "Credits" or startscreen == "Options" or startscreen == "Play") and keys[pygame.K_BACKSPACE]:
            startscreen = "Title"
        
        
        
    
        #gameplay    
        if startscreen == "Play":
            
            if not (keys[pygame.K_UP] or keys[pygame.K_w]):
                play_changed_Up = False
            elif play_changed_Up == False:
                play_changed_Up = True
                play_active -= 1    
            if not (keys[pygame.K_DOWN] or keys[pygame.K_s]):
                play_changed_Down = False
            elif play_changed_Down == False:
                play_changed_Down = True
                play_active += 1    
                
            if not (keys[pygame.K_RETURN] or keys[pygame.K_z] or keys[pygame.K_x]):
                play_changed_Enter = False
                    
            elif play_changed_Enter == False:
                play_changed_Enter = True  
                if play_active == 0: 
                    startscreen = "1p"
                elif play_active == 1: 
                    startscreen = "2p"
                    draw(startscreen,start_active,play_active,player,player1,ball,p_score,p1_score)
                    pygame.display.update()
                    pygame.time.delay(300)
                
                
                
                
            if play_active < 0:
                play_active = 1
            if play_active > 1:
                play_active = 0                    
                
    #Title        
        if startscreen == "Title":
            if not (keys[pygame.K_LEFT] or keys[pygame.K_a]):
                start_changed_L = False
            elif start_changed_L == False:
                start_changed_L = True
                start_active -= 1
            
            if not (keys[pygame.K_RIGHT] or keys[pygame.K_d]):
                start_changed_R = False
            elif start_changed_R == False:
                start_changed_R = True
                start_active += 1
        
            if (start_active < 0):
                start_active = 3
            if (start_active > 3):
                start_active = 0     
            
                
            if not (keys[pygame.K_RETURN] or keys[pygame.K_z] or keys[pygame.K_x]):
                start_changed_Enter = False
                    
            elif start_changed_Enter == False:
                start_changed_Enter = True
                if start_active == 0:
                    startscreen = "Play"
                    start_changed_Enter = False
                if start_active == 1:
                    startscreen = "Options"
                if start_active == 2:
                #Quit in Menu
                    run = False
                    break
                if start_active == 3:
                    startscreen = "Credits"
        
        
                
     
     
        
    #Play 2p and 1p
        if startscreen == "2p" or startscreen == "1p":
        #checks if player is moving
            player_move_u = False
            player_move_d = False
            player1_move_u = False
            player1_move_d = False
            #movement
        #the only thing changed b/w 1 and 2p
        
            if startscreen == "1p":
                if (keys[pygame.K_w] or keys[pygame.K_UP]) and player.y - PLAYER_VEL >= 18:
                    player.y -= PLAYER_VEL
                    player_move_u = True
                if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and player.y + PLAYER_VEL + PLAYER_HEIGHT  <= HEIGHT - 26:
                    player.y += PLAYER_VEL
                    player_move_d = True
            
                if ball.y < (player1.y+(PLAYER_HEIGHT/2)) and player1.y - PLAYER_VEL >= 18:
                    player1.y -= PLAYER_VEL
                    player1_move_u = True
                if ball.y > (player1.y+(PLAYER_HEIGHT/2)) and player1.y + PLAYER_VEL + PLAYER_HEIGHT  <= HEIGHT - 26:
                    player1.y += PLAYER_VEL
                    player1_move_d = True
                    
        
            if startscreen == "2p":
                if keys[pygame.K_w] and player.y - PLAYER_VEL >= 18:
                    player.y -= PLAYER_VEL
                    player_move_u = True
                if keys[pygame.K_s] and player.y + PLAYER_VEL + PLAYER_HEIGHT  <= HEIGHT - 26:
                    player.y += PLAYER_VEL
                    player_move_d = True
            
                if keys[pygame.K_UP] and player1.y - PLAYER_VEL >= 18:
                    player1.y -= PLAYER_VEL
                    player1_move_u = True
                if keys[pygame.K_DOWN] and player1.y + PLAYER_VEL + PLAYER_HEIGHT  <= HEIGHT - 26:
                    player1.y += PLAYER_VEL
                    player1_move_d = True
            
            #ball move    
            ball.x += ball_velx
            ball.y += ball_vely

            if ball.colliderect(player) or ball.colliderect(player1):
                #collisions
                if (ball_velx <= PLAYER_WIDTH + BALL_RADI - 1):
                    ball_velx *= -1.1
                else:
                    ball_velx*= -1
                
            if ball.colliderect(player):    
                if player_move_u:
                    ball_vely -= (PLAYER_VEL*1)
                elif player_move_d:
                    ball_vely += (PLAYER_VEL*1)
                else:
                    ball_vely *= 0.5
                    
            if ball.colliderect(player1):        
                if player1_move_u:
                    ball_vely -= (PLAYER_VEL*1)
                elif player1_move_d:
                    ball_vely += (PLAYER_VEL*1)    
                else:
                    ball_vely *= 0.5
            
            
            if ball.y + ball_vely < 18 or ball.y + ball_vely + BALL_RADI > HEIGHT-26:
                ball_vely *= -1
            
            if ball.x < 0 or ball.x > WIDTH: 
                
                if ball.x < 0:
                    p1_score += 1
                    
                if ball.x > WIDTH:
                    p_score += 1
            
                ball.x = (WIDTH-BALL_RADI)/2
                ball.y = (HEIGHT-BALL_RADI)/2
                ball_velx = 5
                ball_vely = random.uniform(-2.0,2.0)
                
                player.x = 60
                player.y = (HEIGHT - PLAYER_HEIGHT)/2
                player1.x = WIDTH-60
                player1.y = (HEIGHT - PLAYER_HEIGHT)/2
                player_move_u = False
                player_move_d = False
                player1_move_u = False
                player1_move_d = False
                draw(startscreen,start_active,play_active,player,player1,ball,p_score,p1_score)
                pygame.display.update()
                pygame.time.delay(300)
            
            
            
            if p_score >= 7:
                lost_text = FONT.render("Player 2  Lost!        Skill Issue lamo",1,"white")
                WIN.blit(lost_text,(WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
                pygame.display.update()
                pygame.time.delay(10000)
                break  
            
            if p1_score >= 7:
                lost_text = FONT.render("Player 1  Lost!        Skill Issue lamo",1,"white")
                WIN.blit(lost_text,(WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
                pygame.display.update()
                pygame.time.delay(10000)
                break  
            
            
    
    
    
        draw(startscreen,start_active,play_active,player,player1,ball,p_score,p1_score)    
    
    
    pygame.quit
        
        
        
        
#Theft Prot. and starting       
if __name__ == "__main__":    
    main()
