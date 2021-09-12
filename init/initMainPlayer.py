import pygame


def init(main_player):
    my_key = pygame.key.get_pressed()
    if my_key[pygame.K_d]:
        main_player.state = 'walk_forward'
        main_player.face_state = 'forward'
    elif my_key[pygame.K_a]:
        main_player.state = 'walk_back'
        main_player.face_state = 'back'
    elif my_key[pygame.K_w]:
        if main_player.state != 'jump_above':
            main_player.state = 'jump_above'
    else:
        if main_player.face_state == 'forward' and main_player.state != 'jump_above':
            main_player.state = 'idle_forward'
        elif main_player.face_state == 'back' and main_player.state != 'jump_above':
            main_player.state = 'idle_back'
