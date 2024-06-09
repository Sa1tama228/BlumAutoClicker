import pyautogui
import pygetwindow as gw
import time
import keyboard
import random
from pynput.mouse import Button, Controller

mouse = Controller()
time.sleep(0.5)

text = '''
╔╗──╔╗╔╗──╔╗╔╗──╔╗╔══╗╔╗─╔╗╔═══╗╔════╗╔╗╔══╗╔══╗───╔══╗╔═══╗╔═══╗╔═══╗───╔╗╔╗╔═══╗╔═══╗
║║──║║║║──║║║║──║║║╔╗║║╚═╝║║╔══╝╚═╗╔═╝║║║╔═╝╚╗╔╝───║╔═╝║╔═╗║║╔══╝║╔══╝───║║║║║╔══╝║╔═╗║
║╚╗╔╝║║╚╗╔╝║║╚╗╔╝║║║║║║╔╗─║║╚══╗──║║──║╚╝║───║║────║╚═╗║╚═╝║║╚══╗║╚══╗───║║║║║╚══╗║╚═╝║
║╔╗╔╗║║╔╗╔╗║║╔╗╔╗║║║║║║║╚╗║║╔══╝──║║──║╔╗║───║║────║╔═╝║╔╗╔╝║╔══╝║╔══╝───║╚╝║║╔══╝║╔╗╔╝
║║╚╝║║║║╚╝║║║║╚╝║║║╚╝║║║─║║║╚══╗──║║──║║║╚═╗╔╝╚╗───║║──║║║║─║╚══╗║╚══╗───╚╗╔╝║╚══╗║║║║─
╚╝──╚╝╚╝──╚╝╚╝──╚╝╚══╝╚╝─╚╝╚═══╝──╚╝──╚╝╚══╝╚══╝───╚╝──╚╝╚╝─╚═══╝╚═══╝────╚╝─╚═══╝╚╝╚╝─

'''
print(text)
def click(x, y):
    mouse.position = (x, y + random.randint(1, 3))
    mouse.press(Button.left)
    mouse.release(Button.left)


print('Контент-мейкер? сотрудничай с нами!')
time.sleep(1)
print('https://t.me/mmmonetki')
time.sleep(2)
window_name = input('\n[✅] | Введите название окна (1 - TelegramDesktop): ')

if window_name == '1':
    window_name = "TelegramDesktop"

paused = False

# Ввод количества пропусков кликов
skip_count = int(input("[✅] | Введите количество пропусков кликов: "))
current_skip = 0

while True:
    if keyboard.is_pressed('q'):
        paused = not paused
        if paused:
            print('[✅] | Пауза.')
        else:
            print('[✅] | Продолжение работы.')
        time.sleep(0.2)

    if paused:
        continue

    check = gw.getWindowsWithTitle(window_name)
    if not check:
        print(f"[❌] | Окно - {window_name} не найдено! Ожидание повторного запуска...")
        while not check:
            time.sleep(1)
            check = gw.getWindowsWithTitle(window_name)
        print(f"[✅] | Окно найдено - {window_name}\n[✅] | Нажмите \'q\' для паузы.")

    telegram_window = check[0]

    window_rect = (
        telegram_window.left, telegram_window.top, telegram_window.width, telegram_window.height
    )

    if telegram_window:
        try:
            telegram_window.activate()
        except:
            telegram_window.minimize()
            telegram_window.restore()

    scrn = pyautogui.screenshot(region=(window_rect[0], window_rect[1], window_rect[2], window_rect[3]))

    width, height = scrn.size
    pixel_found = False

    for x in range(0, width, 20):
        for y in range(0, height, 20):
            r, g, b = scrn.getpixel((x, y))
            if (b in range(0, 125)) and (r in range(102, 220)) and (g in range(200, 255)):
                if current_skip < skip_count:
                    current_skip += 1
                    continue  # Пропуск нажатия

                # Сброс счетчика пропусков после достижения заданного количества
                current_skip = 0

                screen_x = window_rect[0] + x
                screen_y = window_rect[1] + y
                click(screen_x + 4, screen_y)
                time.sleep(0.001)
                pixel_found = True

print('[✅] | Остановлено.')
