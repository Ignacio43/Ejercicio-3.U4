import tkinter as tk
from tkinter import messagebox
#import requests

class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()
        
        #Ventana
        self.geometry("300x100")
        self.title("Conversor moneda")
        
        #json
        url = "https://www.dolarsi.com/api/api.php?type=dolar"
        #json_data = requests.get(url).json()
        
        #dato = (json_data[0]["casa"]["venta"])
        
        #array = dato.split(",")
        #num = array[0]+"."+array[1]
        
        self.Dolar = tk.DoubleVar()
        #self.Dolar.set(num)
        self.Dolar.set(490)
        
        self.valorPeso=tk.StringVar()
        self.valorDolar=tk.StringVar()
        
        self.valorDolar.trace('w',self.calcula)
        
        
        #Atributos Labels
        opts={"padx":5 , "pady":5}
        
        #Label
        
        tk.Label(self,text="dolares").grid(row=0,column=3,**opts)
        tk.Label(self,text="es equivalente a ").grid(row=2,column=0,**opts)
        tk.Label(self,text="pesos").grid(row=2,column=3,**opts)
        tk.Label(self,textvariable=self.valorPeso).grid(row=2,column=2,**opts)
        
        #Entrys
        tk.Entry(self,textvariable=self.valorDolar,width=8).grid(row=0,column=2,**opts)
        
        #Button
        tk.Button(self,text="Salir",command=self.salir,width=10).grid(row=3,column=3,**opts)
        
        self.mainloop()

    def calcula(self, *args):
        self.valorPeso.set(str(float(self.valorDolar.get())*float(self.Dolar.get())))

    def salir(self):
        self.destroy()


if __name__=='__main__':
    aplicacion= Aplicacion()