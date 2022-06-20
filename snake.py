import pygame
import time
import random

pygame.init()
# өнгө
# program
white = (255, 255, 255)
# score
yellow = (255, 255, 102)
# snake
black = (0, 0, 0)
# lost
red = (213, 50, 80)
# apple
green = (0, 255, 0)
# bg
blue = (50, 153, 213)

# board design
dis_width = 600
dis_height = 400
# board зурж бн
dis = pygame.display.set_mode((dis_width, dis_height))
# header title
pygame.display.set_caption('Snake Game by zombie')
# тоглоомын нийт цаг бидэнд тогойн хөдөлгббнийг хугцааны агшин бүрт өөрчлөхөд хэрэг болно оо.
clock = pygame.time.Clock()
# нэг могойн урт
snake_block = 10
# хөдөлгөөн
snake_speed = 15
# font design
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# тоолуур params(тухайн агшины утгыг авна)


def Your_score(score):
    # оноог дэлгэцэннд хэвлэхэд бэлдэнэ params(хэвлэх text, дэлгэцэнд хэвлэх эсэх, өнгө)
    value = score_font.render("Your Score: " + str(score), True, yellow)
    # дэлгэцэнд хэвлэнэ
    dis.blit(value, [0, 0])

# могойн урт params (нэг блокын урт болон могойн идсэн блокуудын лист)


def our_snake(snake_block, snake_list):

    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

# ямар нэгэн зүйл болохол msg гаргах хэсэг


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

# ерөнхий хэсэг


def gameLoop(snake_speed):
    # тоглоом дуусах эсвэл тоглоомоос гарах эсэхийг шийдэх утагууд
    game_over = False
    game_close = False

    # эхлэх цэг
    x1 = dis_width / 2
    y1 = dis_height / 2
    # өөрчлөлтийг илэрхийлх утагууд
    x1_change = 0
    y1_change = 0
    # могойн биеийг илэрхийлэх параметрүүд
    snake_List = []
    Length_of_snake = 1
    # ногоон алимийг санамсаргүйгээр гаргаж ирэх хэсэг
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
    # Тоглоом дуусаагүй байхад ажиллах func
    while not game_over:
        # Тоглоом дууссан байвал ажиллах хэсэг
        while game_close == True:
            dis.fill(blue)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            # толгойн утгыг хасч оноог явуулж байна
            Your_score(Length_of_snake - 1)
            # тоглоомийн бүх зүйлийг шинэчлэх func ыг дуудаж байна
            pygame.display.update()
            # гараас ямар нэгэн товч дарвал биелүүлэх кодууд
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        # шууд гаргах хэсэг
                        game_over = True
                        # while дуусгах хэсэг
                        game_close = False
                    if event.key == pygame.K_c:
                        #  тоглоомын дахин эхлүүлэх хэсэг
                        gameLoop()
        # Тоглоомын удирдах хэсэг
        for event in pygame.event.get():
            # гарах товчыг дарах үед гаргах хэсэг
            if event.type == pygame.QUIT:
                game_over = True
            #  өөр ямар нэгэн товч дарах үед
            if event.type == pygame.KEYDOWN:
                #  =>
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                #  <=
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                # ^
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                # down
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
                # x1 y1 change нь x боолн y ын утагуудыг өөрчөл параметрүүд юм
        # дэлгэцэээс гарсанэ тохиолдолд шууд тоглоомыг зогсоох хэсэг
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        # өөрчлөгдсөн утгуудаар шууд x1 болон y1 өгнө
        x1 += x1_change
        y1 += y1_change
        # board ад өнгө өгж байна
        dis.fill(blue)
        # Алимийг зурж бн params(хаана хэвлэх, ямар өнгөтэй, [x y байрлал болон блокын өргөн өндөрийг авна])
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        # могойн толгой энэ утгыг цаашдаа могойн бие болож өөрчилнө
        snake_Head = []
        # append нь өмнөх утгыг дарж утга оноож байна могойг хөдөлж байгаа юм шиг харагдуулна
        snake_Head.append(x1)
        snake_Head.append(y1)
        #  могойн биений утгыг дарж утга олгож байна
        snake_List.append(snake_Head)
        #  могойн хөдөлгөөн хийх бүрт хамгийн сүүлийн утгыг арилгаж байна
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
        # өөрийгөө идсэн тохиолдолд үхнэ
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
        #  өөрчилнө утгуудаар update хийх хэсэг
        pygame.display.update()

        # идсэн тохиолдолд могойн уртыг нэмэх болоод дараагийн алимийг гаргах хэсэг
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(
                0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(
                0, dis_height - snake_block) / 10.0) * 10.0
            # могойн уртыг нэмнэ
            Length_of_snake += 1
        # могойн хурдныг агшин бүрт өөрчилны delay үүсгэнэ
        if Length_of_snake > 5:
            snake_speed = 100
        clock.tick(snake_speed)
    #  нэг бүтэн үйлдэл хийж дуусна
    pygame.quit()
    #  тоглоом дуусна
    quit()


# тоглоом ажиллаж эхлэх хэсэг
gameLoop(snake_speed)
