from ursina import *
import assets.APIs.shooting_api as sa

#Version: 2.0

#REQUIREMENTS
#player = FirstPesronController()
#Shooting_api 2.1 or later

###SETUP###
#Import API: 
'import assets.APIs.gun_api as ga'

#Create Gun: 
'gun_name = ga.Gun(gun_name, 20, 5)'

#Show Gun Model: 
'gun_name.show_gun(gun_model)'

#Shoot Gun:
'''
if mouse.left:
    if gun_name.fire(player,camera) == 'fired':
        #Play Sound/ Pass
        Audio('assets/audio/audiofile.mp3', loop=False, autoplay=True)

'''

#Reload Gun:
'''
if key == 'r':
    if gun_name.reload() == 'reloaded':
        Audio('assets/audio/audiofile.mp3', loop=False, autoplay=True)    
'''


class Gun:
    def __init__(self, gun_type, magazine_capacity, max_reload):
        self.gun_type = gun_type
        self.magazine_capacity = magazine_capacity
        self.max_reload = max_reload
        self.reloads = max_reload
        self.magazine = magazine_capacity

    def fire(self, player, camera):
        if self.magazine >= 1:
            sa.shoot_input(player, camera)
            self.magazine -= 1
            return 'fired'
        elif self.magazine == 0:
            print_on_screen('Out of Ammo!', position=(0.025, 0.025))
        

    def reload(self):
        if self.reloads >= 1:
            self.magazine = self.magazine_capacity
            self.reloads -= 1
            return 'reloaded'
        elif self.magazine == 0:
            print_on_screen('Out of Reloads!', position=(0.025, 0.005))

    def show_gun(self, gun_model):
        m16_model = Entity(model=gun_model, scale=0.0045, parent=camera, rotation_y=90, x=0.1, z=0.55)
        return m16_model
    
    def scope(self, m16_model, x_scope, y_scope):
        m16_model.x= x_scope
        m16_model.y = y_scope
        return m16_model