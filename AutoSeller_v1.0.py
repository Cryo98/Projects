import mouse
import time
import keyboard

delay = 0.1
# set_pos_button = '<'

def doubleclick():
    mouse.click()
    mouse.click()

print('||AutoSeller - SPFS||\n')
print('Over upon the sell button and right click')
_ = mouse.record()
sell_pos = mouse.get_position()
again = 'y'
while again == 'y':
    print('Over upon the item you want to sell and right click')
    _ = mouse.record()
    item_pos = mouse.get_position()
    times = input('How many times you want to sell it? ')
    print('Right click to start...')
    _ = mouse.record()
    for i in range(int(times)):
        keyboard.send('alt+tab')
        time.sleep(delay)
        mouse.move(item_pos[0], item_pos[1], delay)
        time.sleep(delay)
        doubleclick()
        time.sleep(delay)
        keyboard.send('alt+tab')
        time.sleep(delay)
        mouse.move(sell_pos[0], sell_pos[1], delay)
        time.sleep(delay)
        doubleclick()
        time.sleep(delay)
    again = input('Want to sell something else? (y/n) ').lower()
print('All items sold!')