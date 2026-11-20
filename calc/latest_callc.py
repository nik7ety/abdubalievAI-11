#бла бла бла бла бла бебебебебебебебебебебебе
import tkinter as shp
import ast
import operator
import math


root = shp.Tk()
root.title("КАЛькулятор") #АГУЗООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООК
root.geometry("500x200")

entry = shp.Entry(root, width=30, font=("Arial", 17))           
entry.pack(pady=10)

safe_poOPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.FloorDiv: operator.floordiv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
}
safe_funcfun = {
    "sqrt": math.sqrt,
    "abs":  abs,
    "sin":  math.sin,
    "cos":  math.cos,
    "tan":  math.tan,
}

safe_coc = {
    "pi": math.pi,
    "e":  math.e,
}

def summ_of():
    userput = entry.get()
    result = eval(userput)
    root2 = shp.Toplevel()
    root2.title("Результат")
    root2.geometry("250x100")
    label = shp.Label (root2, text=str(result), font=("Arial", 18,"bold"))
    label.pack(pady=20)


btn = shp.Button(root, text="Посчитать",command=summ_of)
btn.pack()




root.mainloop()
