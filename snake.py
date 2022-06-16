import pygame, time, random
pygame.init() #initiate pygame

white = (255, 255, 255) # colors for use
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
purple = (204, 0, 255)
blue = (50, 153, 213)

dis_width = 600
dis_height = 400 #display size

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake') #set window title

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15 #size of snake and its speed

font_style = pygame.font.SysFont("bahnschrift", 25)

def our_snake(snake_block, snake_list): #snake body
    for x in snake_list:
        pygame.draw.rect(dis, purple, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])


def gameLoop(): #game loop for when you fail option to restart
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1
#random placement of food
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
    points = 0

    while not game_over:

        while game_close == True:
            dis.fill(white) #gameLoop menu
            message("You Lost! Press R to Restart or Q to quit", red)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:#quit keybind
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:#Restart keybind
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT: #hitting the close button closes
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a: #keybinds for movement
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_d:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_w:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_s:
                    y1_change = snake_block
                    x1_change = 0
    #Commenting these out becuase these yield game over conditions
        #if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
        #    game_close = True
        if len(snake_List)>0:  # This needs to be found before making the change otherwise mixups might happen.
            x1 = snake_List[-1][0]
            y1 = snake_List[-1][1]
        x1 = (x1+x1_change)% dis_width   #This is the modulus operator ,this ensures that the x1 value is always in display limits.Similar for y1
        
        y1 = (y1+y1_change)% dis_height

        dis.fill(black) #fill background
        pygame.draw.rect(dis, blue, [foodx, foody, snake_block, snake_block])
        #Head flipping
        #print ("Tentative head is at " + str(x1) +"," + str(y1)+". \n")
        if len(snake_List)>0:
        	if [x1,y1] == snake_List[len(snake_List)-2] : # This is to prevent the snake from moving inside its body
        		#Flip the list 
        		x1 = snake_List[0][0]
        		y1 = snake_List[0][1]
        		x1 = (x1+x1_change)% dis_width
        		y1 = (y1+y1_change)% dis_height
        		snake_List.reverse()
        #print ("Chosen head is at " + str(x1) +"," + str(y1)+". \n")		
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
            #Inertia solution . This ensures that the snake's head cannot travel inside its body.OPTION 1 Ignore the input .Comment out if you don't want this one.
        	   
        #Self Hitting 
        for x in snake_List[:-1]:
            if x == snake_Head: #if snake head touches itself game over
                game_close = True
        #print (snake_List)
        our_snake(snake_block, snake_List)


        pygame.display.update()
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
            points += 10

        if points > 0:
            text = font_style.render('Your score: ' + str(points), white, (255, 255, 255))
            dis.blit(text, (50,50)) #render text score once score goes up from zero
        pygame.display.update()


        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameLoop()
