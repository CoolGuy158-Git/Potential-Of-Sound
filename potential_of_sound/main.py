import serial
import time
import winsound
import threading
import tkinter as tk
from PIL import Image, ImageTk
import sys

arduino = serial.Serial("COM4", 9600, timeout=1)
time.sleep(2)
iteration = 0

# Make some cool GUI so that I can show off in yt
root = tk.Tk()
root.geometry("400x200")
root.title("Potential of sound")
root.resizable(False, False)
root.wm_attributes("-topmost", True)
root.configure(bg="teal", relief="ridge", borderwidth=10)

# Add noise to the bg
noise = Image.effect_noise((400, 200), 15).convert("RGB")
teal = Image.new("RGB", (400, 200), "#008080")
teal_texture = Image.blend(teal, noise, 0.2)
teal_texture = ImageTk.PhotoImage(teal_texture)
background = tk.Label(root, image=teal_texture)
background.place(x=0, y=0, relwidth=1, relheight=1)
background.lower()


dial = tk.Scale(root, from_=0, to=180, orient="horizontal", length=350, bg="black",troughcolor="#2c2c3b", fg="green", relief="sunken",sliderlength=35,font=("Arial", 20))
dial.pack()

red_led = tk.Label(root, bg="darkred", relief="ridge", borderwidth=10, width=10, height=2)
red_led.place(x=250, y=100)
blue_led = tk.Label(root, bg="darkblue", relief="ridge", borderwidth=10, width=10, height=2)
blue_led.place(x=150, y=100)

output = tk.Text(root, height=3, width=10, bg="black", fg="green", relief="ridge", borderwidth=10, font=("Arial", 10))
output.place(x=10, y=100)
running = True
def exit():
    global running
    winsound.Beep(600, 500)
    winsound.Beep(300, 550)
    root.quit()
    running = False
    sys.exit()

root.bind("<e>", lambda event: exit())
print_exception = False
while running:
        iteration = iteration + 1
        # The voltages coming from the potentiometer is used as the frequency
        # Well it is the og freq (for each button) + voltage * 10
        data = arduino.readline()
        voltage = float(data.split(b": ")[1])
        angle = (voltage / 5) * 180
        dial.set(angle)

        # This two data's or one and off whatever you wanna' call them
        # Are used to play sounds
        # If 1 = play a beep
        # If 0 = don't play a beep
        data = arduino.readline()
        on_off1 = int(data.split(b": ")[1])

        data = arduino.readline()
        on_off2 = int(data.split(b": ")[1])
        print("Iteration " + str(iteration))
        print(f"Voltage: {voltage}")
        print(f"Button 1 state: {on_off1}")
        print(f"Button 2 state: {on_off2}")

        # These are the starting freq
        # Also the freq when the volt is 0
        og_freq_volt1 = 300
        og_freq_volt2 = 200

        freq1 = og_freq_volt1 + voltage*20
        freq2 = og_freq_volt2 + voltage*20
        if on_off1 == 1:
            red_led.config(bg="red")
        else:
            red_led.config(bg="darkred")
        if on_off2 == 1:
            blue_led.config(bg="blue")
        else:
            blue_led.config(bg="darkblue")
        if on_off1 == 1:
            threading.Thread(target=winsound.Beep, args=(int(freq1), 200)).start() # Threading is used so that tge sounds can be synchronized

        if on_off2 == 1:
            threading.Thread(target=winsound.Beep, args=(int(freq2), 200)).start()

        print(f"freq1: {freq1}\nfreq2: {freq2}")
        print("---------------------------")
        output.insert("end", "Freq: \n")
        output.insert("end", str(freq1) + "\n")
        output.insert("end", str(freq2) + "\n")
        output.see("end")
        root.update()

# Crazy how much potential a potentiometer can have, huh?
# Get it cuz like... yea...