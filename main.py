import pygame
import sys
import random
pygame.init()

# Nastavení obrazovky
screen_width = 820
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

# Barvy
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)  
BROWN = (131, 67, 51)
SUN_COLOR = (255, 255, 0)

# Nastavení poloměrů planet, Slunce a vzdáleností
SUN_RADIUS = 60
PLANET_RADIUS = 15
PLANET_DISTANCE = (screen_width - 2 * SUN_RADIUS) // 9

# Názvy planet Sluneční soustavy
PLANET_NAMES = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

# Barvy planet
PLANET_COLORS = {
    "Mercury": (169, 169, 169),
    "Venus": (255, 165, 0),
    "Earth": (0, 191, 255),
    "Mars": (255, 69, 0),
    "Jupiter": (255, 140, 0),
    "Saturn": (255, 215, 0),
    "Uranus": (173, 216, 230),
    "Neptune": (30, 144, 255)
}

# Fonty
font_planet = pygame.font.SysFont(None, 20)
font_kviz = pygame.font.SysFont(None, 32)


# Class pro planety
class Planet:
    def __init__(self, name, color, position):
        self.name = name
        self.color = color
        self.position = position
        self.rect = pygame.Rect(position[0] - PLANET_RADIUS, position[1] - PLANET_RADIUS, PLANET_RADIUS * 2, PLANET_RADIUS * 2)
        self.clicked = False  # Příznak pro změnu barvy

    def draw(self):
        pygame.draw.circle(screen, self.color, self.position, PLANET_RADIUS)

# Vytvoření Slunce 
sun_position = (SUN_RADIUS, screen_height // 2)
sun = pygame.draw.circle(screen, SUN_COLOR, sun_position, SUN_RADIUS)

# Vytvoření planet
planets = [Planet(name, color, ((i + 1) * (screen_width - 2 * SUN_RADIUS) // 9 + SUN_RADIUS * 2, screen_height // 2)) for i, (name, color) in enumerate(PLANET_COLORS.items())]

# Náhodné zamíchání názvů planet
random.shuffle(PLANET_NAMES)

# Vytvoření názvů planet a jejich rectů
name_surfaces = []
name_rects = []
name_positions = []
for i, name in enumerate(PLANET_NAMES):
    name_surface = font_planet.render(name, True, WHITE)
    name_rect = name_surface.get_rect(center=(random.randint(50, screen_width - 50), random.randint(50, screen_height - 50)))
    name_surfaces.append(name_surface)
    name_rects.append(name_rect)
    name_positions.append(name_rect.center)

# otázky
questions = [
    "Kdo napsal dílo \"Máj\"?",
    "Kdo je autorem díla \"Válka s Mloky\"?",
    "Jak se jmenuje autor knihy Babička?",
    "Kdo působil v Osvobozeném divadle?",
    "V jakém období žil a tvořil Karel Čapek?"
]
# odpovědi
answers = [
    ["a) Svatopluk Čech", "b) Karel Hynek Mácha", "c) Jan Neruda"],
    ["a) Josef Čapek", "b) Karel Čapek", "c) Jaroslav Seifert"],
    ["a) Karel Jaromír Erben", "b) Jaroslav Hašek", "c) Božena Němcová"],
    ["a) Jan Werich", "b) Josef Kajetán Tyl", "c) František Palacký"],
    ["a) Baroko", "b) Renesance", "c) Meziválečné období"]
]
# správné odpovědi
correct_answers = ["b", "b", "c", "a", "c"]

# Funkce pro zobrazení otázek a odpovědí
def display_question_and_answers(question_index):
    screen.fill(WHITE) # Vyplní obrazovku bílou

    # Získání povrchu otázky
    question_surface = font_kviz.render(questions[question_index], True, BLACK)
    question_rect = question_surface.get_rect()

    # Nastavení pozice otázky na horní střed okna
    question_rect.centerx = screen.get_rect().centerx
    question_rect.y = 50

    # Vykreslení otázky
    screen.blit(question_surface, question_rect)

    # Výpočet celkové výšky odpovědí
    total_answer_height = len(answers[question_index]) * 50

    # Pozice první odpovědi
    answer_y = (screen_height - total_answer_height) // 2
    # Vykreslení odpovědí
    for answer in answers[question_index]:
        answer_surface = font_kviz.render(answer, True, BLACK)
        answer_rect = answer_surface.get_rect()
        answer_rect.centerx = screen.get_rect().centerx
        answer_rect.y = answer_y
        screen.blit(answer_surface, answer_rect)
        answer_y += 50  # Zajišťuje posun další odpovědi

# Hlavní funkce literárního kvízu
def literature_quiz():
    question_index = 0
    while question_index < len(questions):
        display_question_and_answers(question_index)
        pygame.display.flip()

        correct_answer = correct_answers[question_index]
        selected_answer = None

        while selected_answer is None:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    for i, answer in enumerate(answers[question_index]):
                        answer_rect = font_kviz.render(answer, True, BLACK).get_rect()
                        answer_rect.centerx = screen.get_rect().centerx
                        answer_rect.y = (screen_height - len(answers[question_index]) * 50) // 2 + i * 50
                        if answer_rect.collidepoint(mouse_pos):
                            selected_answer = answer[0]
                         
                            if selected_answer == correct_answer:
                                question_index += 1
                            


pygame.display.set_caption('Gymnázium Kadaň')
start_button_rect = pygame.Rect(screen_width // 2 - 100, screen_height // 2 - 50, 200, 100)

sprites_right = [pygame.image.load("vpravo_1.png"),
                 pygame.image.load("vpravo_2.png"),
                 pygame.image.load("vpravo_3.png")]
sprites_left = [pygame.image.load("vlevo_1.png"),
                pygame.image.load("vlevo_2.png"),
                pygame.image.load("vlevo_3.png")]
sprites_down = [pygame.image.load("dolu_1.png"),
                pygame.image.load("dolu_2.png"),
                pygame.image.load("dolu_3.png.")]
sprites_up = [pygame.image.load("nahoru_1.png"),
                pygame.image.load("nahoru_2.png"),
                pygame.image.load("nahoru_3.png")]

current_direction = "right"
current_sprites = sprites_right

logogymplu = pygame.image.load('logo.jpg')
logogymplu_rect = logogymplu.get_rect()
pixel_art_map1 = pygame.image.load('venek.png')
pixelartmap_background_rect = pixel_art_map1.get_rect(center = [screen_width//2, screen_height//2])

sprite_rectangle = sprites_right[0].get_rect()
zed1 = pygame.Rect(130, 0, 1, 70)
zed2 = pygame.Rect(130, 68, 580, 1)
zed3 = pygame.Rect(710, 0, 1, 70)
dvere1 = pygame.Rect(80, 68, 30, 1)
dvere2 = pygame.Rect(726, 68, 50, 1)
stromkmen = pygame.Rect(647, 325, 2, 35)
korunastromu = pygame.Rect (638, 285, 19, 20)

sprite_rectangle.x = 360
sprite_rectangle.y = 220

speed = 1

frame_rate = 10

background_x = 0
background_y = 0  

current_frame = 0
texthry1 = font_planet.render('Přiřaď jména k jednotlivým planetám', True, WHITE)
texthry1_rect = texthry1.get_rect(center=(screen_width // 2, 20))

run = True
dragging = False
dragging_name = None
literature_quiz_completed = False
slunecnisoustava_completed = False
game_running = False
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_running:  
            if event.button == 1:  # Levé tlačítko myši
                mouse_pos = pygame.mouse.get_pos()
                if start_button_rect.collidepoint(mouse_pos):
                    game_running = True  
    
    if game_running:
        pygame.draw.rect(pixel_art_map1, (0, 0, 0), zed1)
        pygame.draw.rect(pixel_art_map1, (0, 0, 0), zed2)
        pygame.draw.rect(pixel_art_map1, (0, 0, 0), zed3)
        pygame.draw.rect(pixel_art_map1, (0, 0, 0), dvere1)
        pygame.draw.rect(pixel_art_map1, (0, 0, 0), dvere2)
        pygame.draw.rect(pixel_art_map1, BROWN, stromkmen)
        pygame.draw.rect(pixel_art_map1, (0, 128, 0), korunastromu)

        key = pygame.key.get_pressed()
        if key[pygame.K_a] and sprite_rectangle.x > 50 or sprite_rectangle.colliderect(zed1) or sprite_rectangle.colliderect(stromkmen) or sprite_rectangle.colliderect(korunastromu):
            current_direction = "left"
            current_sprites = sprites_left
            current_frame += 0.2
            sprite_rectangle.x -= speed 
        if key[pygame.K_d] and sprite_rectangle.x < 740 or sprite_rectangle.colliderect(zed3) or sprite_rectangle.colliderect(stromkmen) or sprite_rectangle.colliderect(korunastromu):
            current_direction = "right"
            current_sprites = sprites_right
            current_frame += 0.2
            sprite_rectangle.x += speed 
        if key[pygame.K_w] and sprite_rectangle.y > 0 or sprite_rectangle.colliderect(stromkmen) or sprite_rectangle.colliderect(korunastromu):
            current_direction = "up"
            current_sprites = sprites_up
            current_frame += 0.2
            sprite_rectangle.y -= speed 
        if key[pygame.K_s] and sprite_rectangle.y < 375 or sprite_rectangle.colliderect(zed2) or sprite_rectangle.colliderect(stromkmen) or sprite_rectangle.colliderect(korunastromu):
            current_direction = "down"
            current_sprites = sprites_down
            current_frame += 0.2
            sprite_rectangle.y += speed 
        
        if current_frame >= len(current_sprites):
            current_frame = 0
        if current_frame == 3:
            current_frame = 0 

        screen.blit(pixel_art_map1, (background_x, background_y))
        screen.blit(current_sprites[int(current_frame)], sprite_rectangle)

        if sprite_rectangle.colliderect(dvere2):
            if not slunecnisoustava_completed:  
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  
                        for i, rect in enumerate(name_rects):
                            if rect.collidepoint(event.pos):
                                # Detekce kolize mezi rectanglem názvu planety a rectanglem planety
                                if PLANET_NAMES[i] == "Mercury" and planets[0].rect.collidepoint(event.pos):
                                    planets[0].color = GREEN
                                if PLANET_NAMES[i] == "Venus" and planets[1].rect.collidepoint(event.pos):
                                    planets[1].color = GREEN
                                if PLANET_NAMES[i] == "Earth" and planets[2].rect.collidepoint(event.pos):
                                    planets[2].color = GREEN
                                if PLANET_NAMES[i] == "Mars" and planets[3].rect.collidepoint(event.pos):
                                    planets[3].color = GREEN
                                if PLANET_NAMES[i] == "Jupiter" and planets[4].rect.collidepoint(event.pos):
                                    planets[4].color = GREEN
                                if PLANET_NAMES[i] == "Saturn" and planets[5].rect.collidepoint(event.pos):
                                    planets[5].color = GREEN
                                if PLANET_NAMES[i] == "Uranus" and planets[6].rect.collidepoint(event.pos):
                                    planets[6].color = GREEN
                                if PLANET_NAMES[i] == "Neptune" and planets[7].rect.collidepoint(event.pos):
                                    planets[7].color = GREEN
                                if all(planet.color == GREEN for planet in planets):
                                    slunecnisoustava_completed = True
                                    sprite_rectangle.x = 360
                                    sprite_rectangle.y = 220


                                dragging = True
                                dragging_name = i
                                offset = (rect.x - event.pos[0], rect.y - event.pos[1])
                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        dragging = False
                        dragging_name = None
                        # Resetovat příznaky kliknutí na planety
                        for planet in planets:
                            planet.clicked = False
                elif event.type == pygame.MOUSEMOTION:
                    if dragging:
                        name_rects[dragging_name].center = event.pos[0] + offset[0], event.pos[1] + offset[1]
                
                
                ## Vyčištění obrazovky
                screen.fill(BLACK)
                screen.blit(texthry1, texthry1_rect)

                # Kreslení Slunce
                pygame.draw.circle(screen, SUN_COLOR, sun_position, SUN_RADIUS)

                # Kreslení planet
                for planet in planets:
                    planet.draw()

                # Kreslení názvů planet
                for name_surface, name_rect in zip(name_surfaces, name_rects):
                    screen.blit(name_surface, name_rect) 
            else: 
                sprite_rectangle.x = 360
                sprite_rectangle.y = 220

        
        if sprite_rectangle.colliderect(dvere1):
            if not literature_quiz_completed:
                literature_quiz()
                sprite_rectangle.x = 360
                sprite_rectangle.y = 220
                literature_quiz_completed = True
            else:
                sprite_rectangle.x = 360
                sprite_rectangle.y = 220
            
            
            
        pygame.display.flip()
        
    else:
        screen.fill(WHITE)
        screen.blit(logogymplu, (100, 20))
        pygame.draw.rect(screen, BLACK, start_button_rect)
        font = pygame.font.Font(None, 36)
        start_text = font.render("Start", True, WHITE)
        start_text_rect = start_text.get_rect(center=start_button_rect.center)
        screen.blit(start_text, start_text_rect)
    
    
    pygame.display.flip()
    
# Ukončení Pygame
pygame.quit()
sys.exit()

    
        




    


