import asyncio
from bscpylgtv import WebOsClient
import os

KEY_FILE_PATH = os.environ.get('PYLGTV_KEY')
TV_IP = os.environ.get('LGTV_IP')

def generate_sequence(text):
    layout = [
        ['a', 'b', 'c', 'd', 'e', 'f'],
        ['g', 'h', 'i', 'j', 'k', 'l'],
        ['m', 'n', 'o', 'p', 'q', 'r'],
        ['s', 't', 'u', 'v', 'w', 'x'],
        ['y', 'z', '1', '2', '3', '4'],
        ['5', '6', '7', '8', '9', '0']
    ]
    
    # Build position map
    pos_map = {char: (i, j) for i, row in enumerate(layout) for j, char in enumerate(row)}

    # Initialize
    sequence = []
    current_pos = (0, 0)
    count = 0

    for char in text.lower():
        count = count + 1
        if char not in pos_map:
            continue  # ignore unsupported characters
        target_pos = pos_map[char]
        dy = target_pos[0] - current_pos[0]
        dx = target_pos[1] - current_pos[1]

        # Vertical movement
        if dy < 0:
            sequence.extend(['UP'] * abs(dy))
        elif dy > 0:
            sequence.extend(['DOWN'] * dy)

        # Horizontal movement
        if dx < 0:
            sequence.extend(['LEFT'] * abs(dx))
        elif dx > 0:
            sequence.extend(['RIGHT'] * dx)

        # Press enter for every sequence except the dummy x at last
        if count != len(text):
            sequence.append('ENTER')

        # Update current position
        current_pos = target_pos

    return sequence

async def enter_text(client: WebOsClient, title):
    seq = generate_sequence(title)
    for step in seq:
        await client.button(step)
        if step == 'ENTER':
            await asyncio.sleep(2) # needed as the button takes time

async def open_show(client: WebOsClient, title):
    await enter_text(client, title)
    await client.button('RIGHT')
    await client.button('ENTER')
    await asyncio.sleep(4)
    print('Entered the show')
    await client.button('ENTER')

# fn to test seq generation
async def print_sequence(text):
    text_seq = generate_sequence(text)
    for seq in text_seq:
        print(seq)

async def play_netflix(title):
    client = await WebOsClient.create(TV_IP, key_file_path=KEY_FILE_PATH, ping_interval=None, states=[])
    await client.connect()

    # need this as the navigation is designed from home screen
    try:
        await client.close_app('netflix')
        print('Closing the App')
        await asyncio.sleep(10)
    except Exception:
        print('App was already closed')
    
    await client.launch_app('netflix')
    print('Opening the App')

    # needed as the app takes long time to load
    await asyncio.sleep(20)

    # select default profile
    await client.button('ENTER')
    print('Selected default profile')

    await asyncio.sleep(10)

    await client.button('LEFT')
    await client.button('UP')
    await client.button('ENTER')
    print('Entered Search Menu')

    await asyncio.sleep(5)

    await open_show(client, title + 'x') # the x is needed to navigate to right column to open first result
    print('Show started')

    await asyncio.sleep(5)

    await client.disconnect()

#asyncio.run(play_netflix('bridgerton'))
#asyncio.run(print_sequence('bridgerton'))