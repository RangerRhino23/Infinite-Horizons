from ursina import *
import os

app = Ursina()
Sky(texture='assets/black_sky.png')
Audio('assets/audio/ambientmusic.mp3', loop=True, autoplay=True)

#Variables
spaceship_on = False
coords_cooldown = 0
spaceship_speed = 1/10

def update():
    global spaceship_on, coords_cooldown, spaceship_speed

    #Positions Spaceship to be infront of camera
    spaceship.position = camera.position + camera.forward * 1 + (0,-0.09,0)
    spaceship.rotation = camera.rotation

    #Controls Ship
    if spaceship_on == True:
        camera.position += camera.forward * spaceship_speed
    if held_keys['w']:
        camera.rotation_x -= 10 * time.dt
    if held_keys['s']:
        camera.rotation_x += 10 * time.dt
    if held_keys['a']:
        camera.rotation_y -= 30 * time.dt
    if held_keys['d']:
        camera.rotation_y += 30 * time.dt
    if held_keys['q']:
        camera.rotation_z -= 20 * time.dt
    if held_keys['e']:
        camera.rotation_z += 20 * time.dt
    
    #Sends you to coresponding planets
    hit_info = spaceship.intersects()
    if hit_info.hit:
        #Sends you to Mercury
        if hit_info.entity == mercury:
            os.startfile('assets\planets\mercury.py')
            quit()
        #Sends you to Venus
        if hit_info.entity == venus:
            os.startfile('assets\planets\\venus.py')
            quit()
        #Sends you to Earth
        if hit_info.entity == earth:
            os.startfile('assets\planets\earth.py')
            quit()
        #Sends you to Mars
        if hit_info.entity == mars:
            os.startfile('assets\planets\mars.py')
            quit()
        #Sends you to Jupiter
        if hit_info.entity == jupiter:
            os.startfile('assets\planets\jupiter.py')
            quit()
        #Sends you to Saturn
        if hit_info.entity == saturn:
            os.startfile('assets\planets\saturn.py')
            quit()
    
    coords_cooldown = coords_cooldown + 1
    if coords_cooldown == 55:
        coords_cooldown = 0
        print_on_screen(f'''X:{round(camera.x)}
Y:{round(camera.y)}
Z:{round(camera.z)}''', position=(-0.85,0.4))

def input(key):
    if key == 'escape':
        quit()
    global spaceship_on, spaceship_speed
    if key == 'enter':
        if spaceship_on == True:
            spaceship_on = False
        elif spaceship_on == False:
            spaceship_on = True
    if key == '1':
        spaceship_speed = 1/10
        print('changed speed')
    if key == '2':
        spaceship_speed = 1/5
        print('changed speed')
    if key == '3':
        spaceship_speed = 1/2
        print('changed speed')
    if key == '4':
        spaceship_speed = 1/1
        print('changed speed')
    


#Spaceship the player is flying
spaceship = Entity(model='assets/models/spaceship.glb', scale=0.02)
spaceship.collider = BoxCollider(spaceship, center=spaceship.position, size=Vec3(1,1,1))

#Planet Mercury
mercury = Entity(model='assets/models/mercury.glb', scale=10, position=(40,20,150))
mercury.collider = SphereCollider(mercury, center=Vec3(0,0,0), radius=0.25)


#Planet Venus
venus = Entity(model='assets\models\\venus.glb', scale=10, position=(20,5,250))
venus.collider = SphereCollider(venus, center=Vec3(0,0,0), radius=0.25)


#Planet Earth
earth = Entity(model='assets/models/earth.glb', scale=10, position=(20,25,400))
earth.collider = SphereCollider(earth, center=Vec3(0,0,0), radius=0.25)


#Planet Mars
mars = Entity(model='assets/models/mars.glb', scale=10, position=(-5,-5,550))
mars.collider = SphereCollider(mars, center=Vec3(0,0,0), radius=0.25)

#Planet Jupiter
jupiter = Entity(model='assets/models/jupiter.glb', scale=20, position=(-30,10,650))
jupiter.collider = SphereCollider(jupiter, center=Vec3(0,0,0), radius=0.55)

#Planet Saturn
saturn = Entity(model='assets/models/saturn.glb', scale=15, position=(10,-3,850))
saturn.collider = SphereCollider(saturn, center=Vec3(0,0,0), radius=0.55)


#Sun
sun = Entity(model='assets/models/sun.glb', position=(0,0,0), scale=30)


camera.position = (1, 0, 6)
app.run()