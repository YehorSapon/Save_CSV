import pyautogui
import time

# Ждем 5 секунд, чтобы дать пользователю время для переключения на нужное окно
time.sleep(3)
pyautogui.click(500, 300)
time.sleep(2)
# Нажимаем Ctrl+W для закрытия текущего окна
save_button_location = pyautogui.locateOnScreen('select_all.png')

# Кликаем по кнопке "Save"
pyautogui.click(save_button_location)
# Ждем 2 секунды перед нажатием F12
time.sleep(1)

# Нажимаем F12 для открытия диалогового окна сохранения файла
# Определяем координаты кнопки "Save" на экране
save_button_location = pyautogui.locateOnScreen('file.png')

# Кликаем по кнопке "Save"
pyautogui.click(save_button_location)

# Ждем, пока появится окно сохранения файла
time.sleep(1)
save_button_location = pyautogui.locateOnScreen('save_as.png')

# Кликаем по кнопке "Save"
pyautogui.click(save_button_location)
time.sleep(1)

save_button_location = pyautogui.locateOnScreen('select_format_1.png')
pyautogui.click(save_button_location)
time.sleep(1)
save_button_location = pyautogui.locateOnScreen('select_format_2.png')
pyautogui.click(save_button_location)
time.sleep(1)
# Определяем координаты кнопки "Save" на экране
save_button_location = pyautogui.locateOnScreen('file_name.png')

# Кликаем по кнопке "Save"
pyautogui.click(save_button_location)

# Ждем, пока появится окно подтверждения сохранения файла
time.sleep(1)

# Определяем координаты кнопки "OK" на экране
ok_button_location = pyautogui.locateOnScreen('save_button.png')

# Кликаем по кнопке "OK"
pyautogui.click(ok_button_location)

# Ждем, пока появится следующее окно
time.sleep(2)

# Повторяем все действия до тех пор, пока окна не перестанут появляться
# Здесь можно добавить логику, чтобы прервать цикл после определенного числа повторений
while pyautogui.locateOnScreen('file_name.png'):
    # Определяем координаты кнопки "Имя файла" на экране
    save_button_location = pyautogui.locateOnScreen('file_name.png')

    # Кликаем по кнопке "Save"
    pyautogui.click(save_button_location)

    # Ждем, пока появится окно подтверждения сохранения файла
    time.sleep(2)

    # Определяем координаты кнопки "save" на экране
    ok_button_location = pyautogui.locateOnScreen('save_button.png')

    # Кликаем по кнопке "OK"
    pyautogui.click(ok_button_location)

    # Ждем, пока появится следующее окно
    time.sleep(2)
