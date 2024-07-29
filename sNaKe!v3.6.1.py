_author_ = "Giacomo"
import pygame,time,sys,random

pygame.init()
main_x = 300
main_y = 300
display_width = 800
display_height = 600
block_size= 15
EnemySize = 20
velox = 8
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("sNaKe!")

img= pygame.image.load("snake.png")
apple = pygame.image.load("mela.png")
icon = pygame.image.load("icona gioco.png")
pygame.display.set_icon(icon)

clock = pygame.time.Clock()
FPS = 30
direction = "right"
smallFont = pygame.font.SysFont("comicsansms",35)
mediumFont = pygame.font.SysFont("comicsansms",50)
largeFont = pygame.font.SysFont("comicsansms",80)
def gameIntro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if  event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro= False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                
        gameDisplay.fill(white)
        messageToScreen("SNAKE",red ,-100,"large")
        messageToScreen("lo scopo del gioco è mangiare più mele possibile",black,-30)
        messageToScreen("più ne mangerai, più ti ingrandirai!",black,10)
        messageToScreen("Ma evita i bordi e te stesso!",black,50)
        messageToScreen("Premi C per giocare,Q per uscire",black,180)
        pygame.display.update()
        clock.tick(FPS)
        
        
def player(snakeList):
    if direction == "right":
        head = pygame.transform.rotate(img,270)
    if direction== "left":
        head = pygame.transform.rotate(img,90)
    if direction== "up":
        head = img
    if direction== "down":
        head = pygame.transform.rotate(img,180)
        
    gameDisplay.blit(head, (snakeList[-1][0], snakeList[-1][1]))
    for XnY in snakeList[:-1]:
       pygame.draw.rect(gameDisplay, verde_scuro, [XnY[0],XnY[1],block_size,block_size])

def textObject(text, color,size):
    if size == "small":
        textSurface = smallFont.render(text ,True,color)
    if size == "medium":
        textSurface = mediumFont.render(text ,True,color)
    if size == "large":
        textSurface = largeFont.render(text ,True,color)
    return textSurface, textSurface.get_rect()
def messageToScreen(msg ,color,margine_y=0,size = "small"):
    textSurface,textRectangle = textObject(msg, color,size)
    textRectangle.center = (display_width/2), (display_height/2)+ margine_y
    gameDisplay.blit(textSurface, textRectangle)
   #text = font.render(msg,True,color)
   #gameDisplay.blit(text,[display_width/2,display_height/2]) 

black =(0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0 ,0,255)
verde_scuro  =(51,104,0)
sfondo=(36,52,39)

def gameLoop():
    global direction
    direction = "right"
    gameExit = False
    gameOver = False 
    
    main_x = display_width/2
    main_y = display_height/2

    
    main_x_change = 10
    main_y_change = 0

    snakeList = [] #inizialmente vuota
    snakeLenght = 1 #lunghezza di partenza
    
    randEnemyX =round( random.randrange(0,display_width-EnemySize)/EnemySize)*EnemySize
    randEnemyY =round(random.randrange(0,display_height-EnemySize)/EnemySize)*EnemySize

    
    while not gameExit:
        while gameOver == True:
            gameDisplay.fill(black)
            messageToScreen("Game Over!",red,-100,"large")
            messageToScreen("-PREMI R PER UNA NUOVA PARITA",blue,60,"small")
  
            messageToScreen("-PREMI Q PER USCIRE DAL GIOCO",blue,100,"small")
            
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_r:
                        gameLoop()
        
       



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if  event.key == pygame.K_LEFT:
                    direction = "left"
                    main_x_change = -velox
                    main_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    direction = "right"
                    main_x_change =velox
                    main_y_change = 0 
                elif event.key == pygame.K_UP:
                    direction = "up"
                    main_y_change =-velox
                    main_x_change = 0
                elif event.key == pygame.K_DOWN:
                    direction = "down"
                    main_y_change = velox
                    main_x_change = 0
        if main_x >= display_width or main_x < 0 or  main_y < 0 or main_y >= display_height:
            gameOver = True 
            
            
            
          
            
        main_x += main_x_change
        main_y += main_y_change
        gameDisplay.fill(black)
        #Enemy
#        pygame.draw.rect(gameDisplay,blue,[randEnemyX, randEnemyY,EnemySize,EnemySize])
        gameDisplay.blit(apple,(randEnemyX,randEnemyY))
        

        head = []
        head.append(main_x)
        head.append(main_y)
        snakeList.append(head)

        if len(snakeList) > snakeLenght:
            del snakeList[0]

        for eachSegment in snakeList[:-1]:
            if eachSegment == head:
                gameOver = True


        player(snakeList)#player
        pygame.display.update()



        if (main_x > randEnemyX)and (main_x < randEnemyX + EnemySize) or (main_x + block_size > randEnemyX) and (main_x + block_size < randEnemyX + EnemySize):
            if main_y >randEnemyY and main_y < randEnemyY + EnemySize or main_y + block_size > randEnemyY and main_y + block_size < randEnemyY + EnemySize:
                   randEnemyX =round( random.randrange(0,display_width-EnemySize)/EnemySize)*EnemySize
                   randEnemyY =round(random.randrange(0,display_height-EnemySize)/EnemySize)*EnemySize
                   snakeLenght += 1
            elif main_y + block_size > randEnemyY and main_y + block_size < randEnemyY + EnemySize:
                    randEnemyX =round( random.randrange(0,display_width-EnemySize)/EnemySize)*EnemySize
                    randEnemyY =round(random.randrange(0,display_height-EnemySize)/EnemySize)*EnemySize
                    snakeLenght += 1             
            
        clock.tick(FPS)
        
    
    pygame.quit()
    quit()
gameIntro()
gameLoop()


