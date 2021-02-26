import play
from random import randint 

play.set_backdrop((213, 0, 255))

player = play.new_circle(
    color = "blue",
    x = 0,
    y = 0,
    radius = 15,
    transparency = 100)

platform = play.new_image(
    image = "platforma.png",
    x = 0,
    y = -280,
    )

frames = 45 
lose = play.new_text(words='YOU LOSE', font_size=100, color='red')
win = play.new_text(words='YOU WIN', font_size=100, color='yellow')

blocks = []
y_cor = 250
for i in range(3):
    x_cor = -345
    for i in range(7):
        block = play.new_image(
        image = "arkanoid.png",
        x = x_cor,
        y = y_cor,
        )   
        blocks.append(block)
        x_cor += 115
    y_cor-=35


@play.when_program_starts
def start():
    platform.start_physics(can_move=True, stable=True, x_speed=0, y_speed=0, obeys_gravity=False, bounciness=1, mass=10)
    player.start_physics(can_move=True, x_speed=40, y_speed=40, obeys_gravity=False, bounciness=1, mass=10)

    lose.hide()
    win.hide()

@play.repeat_forever
async def game():
    for block in blocks:
        if player.is_touching(block):
            player.physics.y_speed *= -1
            block.remove()
            blocks.remove(block)

@play.repeat_forever
async def game():
        await play.timer(seconds=1/frames)

@play.repeat_forever
async def checking():
        if player.y <= platform.y:
            platform.hide()
            player.hide()
            exit = play.new_image(
                image = "exit.png",
                x = -197,
                y = -160,
            )
            menu = play.new_image(
                image = "menu.png",
                x = 197,
                y = -160,
            )
            for block in blocks:
                block.hide()
        if len(blocks) == 0:
            win.show()
            platforma.stop_physics()
            platform.hide()
            player.stop_physics()
            player.hide()

@play.repeat_forever
def keypads():
        if play.key_is_pressed("a", "ф", "A", "Ф"):
            platform.physics.x_speed = -20
        elif play.key_is_pressed("d", "в", "D", "В"):
            platform.physics.x_speed = 25
        else:
            platform.physics.x_speed = 0


play.start_program()
