import tkinter as tk
import pyscreenshot

def sc():
    image = pyscreenshot.grab() 

# To display the captured screenshot 
    image.show() 

# To save the screenshot 
    image.save("c.png") 


r = tk.Tk()
r.title('Screen')
button = tk.Button(r, text='ScreenShot', width=25,command=sc)
button.pack(pady=20)
r.mainloop()

