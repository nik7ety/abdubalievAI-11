#бла бла бла бла бла бебебебебебебебебебебебе
import tkinter as shp

root = shp.Tk()
root.title("КАЛькулятор") #АГУЗООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООК
root.geometry("500x200")

entry = shp.Entry(root, width=30, font=("Arial", 17))           
entry.pack(pady=10)


btn = shp.Button(root, text="Посчитать")
btn.pack()
root.bind("<Return>", lambda ivent: btn.invoke())

output_label = shp.Label(root, text="", font=("Arial", 18, "bold"), fg="blue")
output_label.pack(pady=20)

def summ_of():
    userput = entry.get()
    result = eval(userput)

root.mainloop()
summ_of
