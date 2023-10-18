import random
import pygame

pygame.init()

# Инициализация звуков

sounds = []
sound1 = pygame.mixer.Sound('resources/INTERWORLD_-_METAMORPHOSIS_73761657.mp3')
sound3 = pygame.mixer.Sound('resources/MOONDEITY_X_INTERWORLD_-_ONE_CHANCE_SLOWED_REVERBED_76111378.mp3')
sound4 = pygame.mixer.Sound('resources/nbsplv_-_the_lost_soul_down_X_lost_soul_remix_tiktok_-_slowed_76366392.mp3')

sounds.append(sound1)
sounds.append(sound3)
sounds.append(sound4)

m = random.choice(sounds)
m.play(loops=-1)

# настройки экрана

screen = pygame.display.set_mode((640, 700))
pygame.display.set_caption('Гонки by Ваче')
clock = pygame.time.Clock()

bg = pygame.image.load('resources/15a00e4dca504c6dcb2ac92849ba3378.jpg')
bg = pygame.transform.scale(bg, (640, 700))

# Все машинки

MAin_Car = pygame.image.load('resources/Main_car.png')
MAin_Car = pygame.transform.scale(MAin_Car, (130, 70))
MAin_Car = pygame.transform.rotate(MAin_Car, 90)

MAin_Car_4 = pygame.image.load('resources/fourth.png')
MAin_Car_4 = pygame.transform.scale(MAin_Car_4, (130, 70))
MAin_Car_4 = pygame.transform.rotate(MAin_Car_4, -90)

MAin_Car_3 = pygame.image.load('resources/SecondCar1.png')
MAin_Car_3 = pygame.transform.scale(MAin_Car_3, (130, 70))
MAin_Car_3 = pygame.transform.rotate(MAin_Car_3, -90)

MAin_Car_2 = pygame.image.load('resources/therdCar.png')
MAin_Car_2 = pygame.transform.scale(MAin_Car_2, (130, 70))
MAin_Car_2 = pygame.transform.rotate(MAin_Car_2, -90)

# Остальные изображения

health = pygame.image.load('resources/Haert.png')
health = pygame.transform.scale(health, (50, 50))

# Переменные

fps = 60

run = True

x_change = 0
y_change = 0

car_x = 330
car_y = 450

max_speed = 20

camera_y = 0

score = pygame.font.Font('ofont.ru_Cygre.ttf', 36)

Road_Len = 0

all_y = []

sec_y = []


# функции

def randY():
    y = random.randint(-4000, -200)
    sec_y.append(y)


def retY():
    p = random.randint(-2000, -200)
    return p


randY()
randY()
randY()
randY()

allroad = 0

health_check = 0
# Игровой цикл

while run:

    # Добавление всего на экран

    screen.blit(bg, (0, camera_y))
    screen.blit(bg, (0, camera_y - 700))

    sec2 = screen.blit(MAin_Car_2, (130, sec_y[-1]))
    sec1 = screen.blit(MAin_Car_3, (230, sec_y[-2]))
    sec3 = screen.blit(MAin_Car_4, (330, sec_y[-3]))
    sec4 = screen.blit(MAin_Car_2, (440, sec_y[-4]))

    scoreTXT = score.render('Путь:  ' + str(round(Road_Len)), False, (255, 255, 255))

    screen.blit(scoreTXT, (200, 20))
    # пропадание жизни
    if health_check == 1:
        screen.blit(health, (0, 10))
        screen.blit(health, (0, 60))
        screen.blit(health, (0, 102))
    elif health_check == 2:
        screen.blit(health, (0, 10))
        screen.blit(health, (0, 60))
    elif health_check == 3:
        screen.blit(health, (0, 2))
    elif health_check == 4:
        run = False
    else:
        screen.blit(health, (0, 2))
        screen.blit(health, (0, 52))
        screen.blit(health, (0, 102))
        screen.blit(health, (0, 152))

    # Пропадание машин

    if sec_y[0] >= 800:
        sec_y[0] = retY()
    elif sec_y[1] >= 800:
        sec_y[1] = retY()
    elif sec_y[2] >= 800:
        sec_y[2] = retY()
    elif sec_y[3] >= 800:
        sec_y[3] = retY()

    # Движение зданего фона

    if camera_y >= 700:
        camera_y = 0

    # Запрет отрицательной скорости

    elif y_change <= 0:
        y_change = 0

    # Огарничение максимальной скорости

    elif y_change >= max_speed:
        y_change = max_speed

    camera_y += y_change

    Main = screen.blit(MAin_Car, (car_x, car_y))

    pygame.display.update()

    # Провера нажатий клавиш

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        y_change -= 3

    elif keys[pygame.K_LEFT]:
        x_change = -6

    elif keys[pygame.K_RIGHT]:
        x_change = 6

    # Ограничение по езде игрока

    if car_x >= 440:
        car_x = 440
    elif car_x <= 130:
        car_x = 130
    elif car_y >= 570:
        car_y = 570
    elif car_y <= 0:
        car_y = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                pass
            elif event.key == pygame.K_SPACE:
                y_change += 0.02
            elif event.key == pygame.K_LEFT:
                x_change = 0
            elif event.key == pygame.K_RIGHT:

                x_change = 0
    # Аварии

    if Main.colliderect(sec1):
        if y_change <= 15:
            pass
        else:
            del sec1
            y_change = 0
            health_check += 1
    elif Main.colliderect(sec2):
        if y_change <= 15:
            pass
        else:
            del sec2
            y_change = 0
            health_check += 1
    elif Main.colliderect(sec3):
        if y_change <= 15:
            pass
        else:
            del sec3
            y_change = 0
            health_check += 1
    elif Main.colliderect(sec4):
        if y_change <= 15:
            pass
        else:
            del sec4
            y_change = 0
            health_check += 1

    # Само движение всего

    car_x += x_change
    y_change += 0.06

    Road_Len += y_change / 20

    sec_y[0] += 5
    sec_y[1] += 10
    sec_y[2] += 8
    sec_y[3] += 10

    clock.tick(fps)
