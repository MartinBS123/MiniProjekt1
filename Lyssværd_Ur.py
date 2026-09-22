import pygame
import math 
import time
pygame.init()
screen_size = (640, 640)

screen = pygame.display.set_mode(screen_size)


start_position = (screen_size[0]/2, screen_size[1]/2)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    screen.fill((0, 0, 0))

    #Billede lavet med ChatGPT
    Deathstar = pygame.image.load("Bedre_Deathstar.jpeg")
    #Størrelse af billede - tilpasset efter urets omkreds, fordi billed ikke er perfekt rund
    Deathstar = pygame.transform.scale(Deathstar, (445,435))
    #Placering af billede
    screen.blit(Deathstar, (100, 100))


    #Cirkel / omkredsen af ur
    pygame.draw.circle(screen, (0,0,0), start_position, 200, 5)
    #Cirkel i midten af ur
    pygame.draw.circle(screen, (0,0,0), start_position, 7)



    # Time markeringer
    center_point = (screen_size[0]/2, screen_size[1]/2)
    start_marking = 188
    end_marking = 200
    hour_mark_angle_offset = 360/12


    # 12 time markeringer
    #Starter et loop som kører 0-11 gange 12, 1, 2, 3... op til 11
    for hour_mark_index in range(12):
        # Hvilken vinkel hvor den skal være på cirklen
        angle = hour_mark_angle_offset*hour_mark_index
        #Beregner hvor den skal starte
        start_point = (center_point[0] + math.cos(math.radians(angle))*start_marking, center_point[1] + math.sin(math.radians(angle))*start_marking)
        #Beregner hvor den skal slutte
        end_point = (center_point[0] + math.cos(math.radians(angle))*end_marking, center_point[1] + math.sin(math.radians(angle))*end_marking)
        #Tegn en sort streg fra hvor den skal starte til hvor den skal slutte
        pygame.draw.line(screen, (0, 0, 0), start_point, end_point, 5)


    #Timenumre på ur
    #Størrelse af tal
    font = pygame.font.Font(None, 25)
    for i in range(1, 13):
        angle = math.radians(i * 30 - 90)
        #placering
        x = 320 + 180 * math.cos(angle)
        y = 320 + 180 * math.sin(angle)
        #Farve af tal
        text = font.render(str(i), True, (0, 0, 0))
        text_rect = text.get_rect(center=(x, y))
        screen.blit(text, text_rect)

    #Kode for at kører uret i realtid
    rn = time.localtime()

    #Kode til at få viserne til at bevæge sig glidende i stedet for at hoppe fra sekund til sekund
    Glidene_Bevægelse = time.time()
    Sekund_angle = (Glidene_Bevægelse % 60) * 6 - 90
    Minut_angle = (Glidene_Bevægelse / 60 % 60) * 6 - 90
    Time_angle = (Glidene_Bevægelse / 3600 % 12)+2 * 30 - 90


    #SekundViser - Rødt lyssværd
    radius = 190
    end_offset = [radius*math.cos(math.radians(Sekund_angle)), radius*math.sin(math.radians(Sekund_angle))]
    end_position = (start_position[0]+end_offset[0], start_position[1]+end_offset[1])
    pygame.draw.line(screen, (255,0,0), start_position, end_position, 5)

    #MinutViser - Blåt lyssværd
    radius = 180
    end_offset = [radius*math.cos(math.radians(Minut_angle)), radius*math.sin(math.radians(Minut_angle))]
    end_position = (start_position[0]+end_offset[0], start_position[1]+end_offset[1])
    pygame.draw.line(screen, (0,100,255), start_position, end_position, 5)

    #TimeViser - Grønt lyssværd
    radius = 100
    end_offset = [radius*math.cos(math.radians(Time_angle)), radius*math.sin(math.radians(Time_angle))]
    end_position = (start_position[0]+end_offset[0], start_position[1]+end_offset[1])
    pygame.draw.line(screen, (15,255,0), start_position, end_position, 6)

    #SekundViser - Hvid streg i Rødt lyssværd
    radius = 188
    end_offset = [radius*math.cos(math.radians(Sekund_angle)), radius*math.sin(math.radians(Sekund_angle))]
    end_position = (start_position[0]+end_offset[0], start_position[1]+end_offset[1])
    pygame.draw.line(screen, (255,255,255), start_position, end_position, 1)
    
    #MinutViser - Hvid streg i Blåt lyssværd
    radius = 178
    end_offset = [radius*math.cos(math.radians(Minut_angle)), radius*math.sin(math.radians(Minut_angle))]
    end_position = (start_position[0]+end_offset[0], start_position[1]+end_offset[1])
    pygame.draw.line(screen, (255,255,255), start_position, end_position, 1)
    
    #TimeViser - Hvid streg i Grønt lyssværd
    radius = 98
    end_offset = [radius*math.cos(math.radians(Time_angle)), radius*math.sin(math.radians(Time_angle))]
    end_position = (start_position[0]+end_offset[0], start_position[1]+end_offset[1])
    pygame.draw.line(screen, (255,255,255), start_position, end_position, 2)

        #SekundViser - Grå markering på Rødt lyssværd håndtag
    radius = -35
    end_offset = [radius*math.cos(math.radians(Sekund_angle)), radius*math.sin(math.radians(Sekund_angle))]
    end_position = (start_position[0]+end_offset[0], start_position[1]+end_offset[1])
    pygame.draw.line(screen, (80, 82, 85), start_position, end_position, 5)

    #MinutViser - Grå markering på Blåt lyssværd håndtag
    radius = -35
    end_offset = [radius*math.cos(math.radians(Minut_angle)), radius*math.sin(math.radians(Minut_angle))]
    end_position = (start_position[0]+end_offset[0], start_position[1]+end_offset[1])
    pygame.draw.line(screen, (80, 82, 85), start_position, end_position, 5)

    #TimeViser - Grå markering på Grønt lyssværd håndtag
    radius = -35
    end_offset = [radius*math.cos(math.radians(Time_angle)), radius*math.sin(math.radians(Time_angle))]
    end_position = (start_position[0]+end_offset[0], start_position[1]+end_offset[1])
    pygame.draw.line(screen, (80, 82, 85), start_position, end_position, 5)

    #SekundViser - Rødt lyssværd håndtag
    radius = -33
    end_offset = [radius*math.cos(math.radians(Sekund_angle)), radius*math.sin(math.radians(Sekund_angle))]
    end_position = (start_position[0]+end_offset[0], start_position[1]+end_offset[1])
    pygame.draw.line(screen, (140, 142, 145), start_position, end_position, 2)

    #MinutViser - Blåt lyssværd håndtag
    radius = -33
    end_offset = [radius*math.cos(math.radians(Minut_angle)), radius*math.sin(math.radians(Minut_angle))]
    end_position = (start_position[0]+end_offset[0], start_position[1]+end_offset[1])
    pygame.draw.line(screen, (140, 142, 145), start_position, end_position, 2)

    #TimeViser - Grønt lyssværd håndtag
    radius = -33
    end_offset = [radius*math.cos(math.radians(Time_angle)), radius*math.sin(math.radians(Time_angle))]
    end_position = (start_position[0]+end_offset[0], start_position[1]+end_offset[1])
    pygame.draw.line(screen, (140, 142, 145), start_position, end_position, 2)


    pygame.display.flip()



