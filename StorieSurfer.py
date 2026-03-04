import pyautogui
import pynput
import time

cont = 0
tecl = pynput.keyboard.Controller()
resp = int(input("Deseja iniciar 1-SIM 2-NÃO: "))
if resp == 1:
    so = int(input("1-windows 10 2-windows 11: "))
    app = int(input("1-navegador 2-aplicativo do instagram: "))
    if (app == 1):
        nv = input("digite qual é o seu navegador: ")
        print("iniciando em:")
        for s in range(5, 0, -1):
            time.sleep(1)
            print("{}".format(s))
        if (so == 1):
            for i in range(0, 2):
                tecl.press(pynput.keyboard.Key.ctrl_l)
                tecl.press(pynput.keyboard.Key.esc)
                time.sleep(1)
                tecl.release(pynput.keyboard.Key.ctrl_l)
                tecl.release(pynput.keyboard.Key.esc)
                time.sleep(1)
                pyautogui.write(nv)
                time.sleep(1)
                pyautogui.press('enter')
                time.sleep(5)
                pyautogui.write("instagram.com")
                time.sleep(1)
                pyautogui.press('delete')
                time.sleep(1)
                pyautogui.press('enter')
                time.sleep(5)
                for i in range(0, 2):
                    pyautogui.press('tab')
                    pyautogui.press('tab')
                    pyautogui.press('tab')
                    pyautogui.press('tab')
                    pyautogui.press('tab')
                    pyautogui.press('tab')
                    pyautogui.press('tab')
                    pyautogui.press('tab')
                    pyautogui.press('tab')
                    pyautogui.press('tab')
                    pyautogui.press('tab')
                    time.sleep(5)
                    pyautogui.press('enter')
                    time.sleep(2)
                    break
                while cont < 10000:
                    for i in range(0, 10001):
                        cont = cont + 1
                        time.sleep(0.5)
                        pyautogui.press('right')
                        break
        else:
            for i in range(0, 2):
                tecl.press(pynput.keyboard.Key.ctrl_l)
                tecl.press(pynput.keyboard.Key.esc)
                time.sleep(1)
                tecl.release(pynput.keyboard.Key.ctrl_l)
                tecl.release(pynput.keyboard.Key.esc)
                time.sleep(1)
                pyautogui.write(nv)
                time.sleep(1)
                pyautogui.press('enter')
                time.sleep(5)
                pyautogui.write('instagram.com')
                time.sleep(1)
                pyautogui.press('delete')
                time.sleep(1)
                pyautogui.press('enter')
                time.sleep(5)
                for i in range(0, 2):
                    pyautogui.press('tab')
                    pyautogui.press('tab')
                    pyautogui.press('tab')
                    pyautogui.press('tab')
                    pyautogui.press('tab')
                    pyautogui.press('tab')
                    pyautogui.press('tab')
                    pyautogui.press('tab')
                    pyautogui.press('tab')
                    pyautogui.press('tab')
                    pyautogui.press('tab')
                    time.sleep(5)
                    pyautogui.press('enter')
                    time.sleep(2)
                    break
                while cont < 10000:
                    for i in range(0, 10001):
                        cont = cont + 1
                        time.sleep(0.5)
                        pyautogui.press('right')
                        break
    else:
        if (so == 1):
            for i in range(0, 2):
                tecl.press(pynput.keyboard.Key.ctrl_l)
                tecl.press(pynput.keyboard.Key.esc)
                time.sleep(1)
                tecl.release(pynput.keyboard.Key.ctrl_l)
                tecl.release(pynput.keyboard.Key.esc)
                time.sleep(1)
                pyautogui.write("instagram")
                time.sleep(1)
                pyautogui.press('enter')
                time.sleep(10)
                for i in range(0, 2):
                    pyautogui.press('tab')
                    pyautogui.press('tab')
                    pyautogui.press('tab')
                    pyautogui.press('tab')
                    pyautogui.press('tab')
                    pyautogui.press('tab')
                    pyautogui.press('tab')
                    pyautogui.press('tab')
                    pyautogui.press('tab')
                    pyautogui.press('tab')
                    pyautogui.press('tab')
                    time.sleep(5)
                    pyautogui.press('enter')
                    time.sleep(2)
                    break
                while cont < 10000:
                    for i in range(0, 10001):
                        cont = cont + 1
                        time.sleep(0.5)
                        pyautogui.press('right')
                    break
        else:
            for i in range(0, 2):
                tecl.press(pynput.keyboard.Key.ctrl_l)
                tecl.press(pynput.keyboard.Key.esc)
                time.sleep(1)
                tecl.release(pynput.keyboard.Key.ctrl_l)
                tecl.release(pynput.keyboard.Key.esc)
                time.sleep(1)
                pyautogui.write("instagram")
                time.sleep(1)
                pyautogui.press('enter')
                time.sleep(10)
                for i in range(0, 2):
                    pyautogui.press('tab')
                    pyautogui.press('tab')
                    pyautogui.press('tab')
                    pyautogui.press('tab')
                    pyautogui.press('tab')
                    pyautogui.press('tab')
                    pyautogui.press('tab')
                    pyautogui.press('tab')
                    pyautogui.press('tab')
                    pyautogui.press('tab')
                    pyautogui.press('tab')
                    time.sleep(5)
                    pyautogui.press('enter')
                    time.sleep(2)
                    break
                while cont < 10000:
                    for i in range(0, 10001):
                        cont = cont + 1
                        time.sleep(0.5)
                        pyautogui.press('right')
                        break

else:
    print("fechando em")
    for i in range(5, 0, -1):
        time.sleep(1)
        print("{}".format(i))
