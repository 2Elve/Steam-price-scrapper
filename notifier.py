from plyer import notification
import datetime, keyboard
import bot


notified = False; 
time_check = '00'

while True: 
    dt_now = datetime.datetime.now() 
    min_now = str(dt_now)

    if keyboard.is_pressed('/'):
        print('Exiting program')
        break 

    if min_now[14:16] == time_check and notified == False: 
        scrapper = bot.Bot()
        notified = True
        if len(scrapper) > 1:
            elements = scrapper.split(';')

            title = elements[0]
            msg = f'"{elements[0]}" descuento de {elements[1]}\nPrecio normal-> {elements[2]}\nPrecio actual-> {elements[3]}'

            notification.notify(title = title,
                                message = msg,
                                app_icon = 'play_triangle.ico',
                                timeout = 8,
                                toast = False)

    if min_now[14:16] != time_check and notified == True:   
        notified = False 
