from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import assets.APIs.first_person_movement_api as fpm
import assets.APIs.gun_api as ga
import assets.APIs.shooting_api as sa


app = Ursina()
Sky(texture='..\\black_sky.png')
Audio('assets/audio/mars_ambientmusic.mp3', loop=True, autoplay=True)

#Variables
player_speed = 15
sa.shoot_setup()
world_barrier = []
m16 = ga.Gun('M16 Rifle', 30, 5)
m16.show_gun('assets/models/m16rifle.obj')


def update():
    fpm.player_movement(player, player_speed)
    sa.shoot_update(world_barrier)
    if distance(player, spaceship) < 8:
        os.startfile('space.py')
        quit()

def input(key):
    if key == 'q':
        quit()
    if mouse.left:
        if m16.fire(player,camera) == 'fired':
            Audio('assets/audio/m16gunshot.mp3', loop=False, autoplay=True)
    if key == 'r':
        if m16.reload() == 'reloaded':
            Audio('assets/audio/gunreload.mp3', loop=False, autoplay=True)

terrain = Entity(model=Terrain('heightmap_1', skip=8), scale=(500,10,500), texture='grass', collider='mesh', y=-3, color=color.rgb(234,214,184))
world_barrier.append(terrain)


player = FirstPersonController(position=(144,6,-6))



spaceship = Entity(model='..\models\spaceship.glb', scale=1, position=(168, 6, -4))
world_barrier.append(spaceship)

app.run()