import pyautogui
import time

# Ждем 3 секунды, чтобы дать пользователю время для переключения на нужное окно
pyautogui.PAUSE = 2.5
pyautogui.click(500, 300)
pyautogui.PAUSE = 0.25
# Определяем координаты кнопки "выбрать все спектры"
save_button_location = pyautogui.locateOnScreen('select_all.png')
# Кликаем по кнопке
pyautogui.click(save_button_location)
# Ждем 0.5 секунды
pyautogui.PAUSE = 0.5

# Наводзім мыш на кнопку  "файл"
pyautogui.dragTo(41, 32, 2)
# file_button_location = pyautogui.locateOnScreen('file.png')
# position "file" button X: 41 Y: 32 RGB: (  0,   0,   0)
# Кликаем по кнопке
pyautogui.click()
# Ждем 1 секунду
pyautogui.PAUSE = 0.5
# Тоже для кнопки "сохранить как"
pyautogui.dragTo(207, 96, 2)
# save_as_button_location = pyautogui.locateOnScreen('save_as.png')
# X:  207 Y:   96 RGB: (237, 241, 246)
pyautogui.click()
time.sleep(2)
# Тоже для кнопки "выбрать формат"
select_1_button_location = pyautogui.locateOnScreen('select_format_1.png')
pyautogui.click(select_1_button_location)
time.sleep(1)
# Тоже для кнопки "сохранить как csv"
select_2_button_location = pyautogui.locateOnScreen('select_format_2.png')
pyautogui.click(select_2_button_location)
time.sleep(1)
# Тоже для кнопки "указать имя"
file_name_button_location = pyautogui.locateOnScreen('file_name.png')
pyautogui.click(file_name_button_location)
time.sleep(1)
# Тоже для кнопки "сохранить"
ok_button_location = pyautogui.locateOnScreen('save_button.png')
pyautogui.click(ok_button_location)
time.sleep(1)

# Повторяем все действия до тех пор, пока окна не перестанут появляться
# Здесь можно добавить логику, чтобы прервать цикл после определенного числа повторений
while pyautogui.locateOnScreen('file_name.png'):
    # Определяем координаты кнопки "Имя файла" на экране
    save_button_location = pyautogui.locateOnScreen('file_name.png')
    pyautogui.click(save_button_location)
    time.sleep(0.5)
    ok_button_location = pyautogui.locateOnScreen('save_button.png')
    pyautogui.click(ok_button_location)
    time.sleep(0.5)
print("Сохранение успешно завершено")