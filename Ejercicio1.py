from tkinter import *
import tkinter.ttk as ttk
from tkinter import ttk

# Crear una ventana raíz
root = Tk()

# Crear un notebook (panel tabulado)
notebook = ttk.Notebook(root)
notebook.configure(width=600, height=450)

# Crear pestañas dentro del notebook
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
tab3 = ttk.Frame(notebook)
tab4 = ttk.Frame(notebook)
tab5 = ttk.Frame(notebook)

# Modificar el estilo por defecto de las etiquetas
style = ttk.Style()
style.configure('TLabel', font=('Arial', 14))

# Agregar widgets a cada pestaña
ttk.Label(tab1, text="Este es el contenido de la pestaña 1").grid(column=0, row=0, padx=10, pady=10)
ttk.Label(tab2, text="Este es el contenido de la pestaña 2").grid(column=0, row=0, padx=10, pady=10)
ttk.Label(tab3, text="Este es el contenido de la pestaña 3").grid(column=0, row=0, padx=10, pady=10)
ttk.Label(tab4, text="Este es el contenido de la pestaña 4").grid(column=0, row=0, padx=10, pady=10)
ttk.Label(tab5, text="Este es el contenido de la pestaña 5").grid(column=0, row=0, padx=10, pady=10)

# Agregar las pestañas al notebook
notebook.add(tab1, text="       Add      ")
notebook.add(tab2, text="       Delete      ")
notebook.add(tab3, text="       Search      ")
notebook.add(tab4, text="       Services      ")
notebook.add(tab5, text="       Help       ")

# Crear un estilo personalizado para las pestañas
style.theme_create("MyStyle", parent="alt", settings={
    "TNotebook.Tab": {
        "configure": {"background": "skyblue1", "foreground": "black", "font": ("Arial", 14)},
        "map": {"background": [("selected", "Dodgerblue2")], "foreground": [("selected", "white")]}
    }
})
style.theme_use("MyStyle")

# Mostrar el notebook
notebook.pack(expand=True, fill=BOTH)

#Frame 1 (0,0)

BaseFrame = ttk.Frame(tab1, padding="5 30 5 5")
BaseFrame.grid(column=0, row= 0)

#Frame 2

Frame2 = ttk.Frame(BaseFrame, padding="25 5 25 2", relief="groove")
Frame2.grid(column=0, row=0)

#Frame 3

Frame3 = ttk.Frame(Frame2, padding="10 7 35 7")
Frame3.grid(column=0, row=0, pady=10)

FName = StringVar()
LName = StringVar()
Country = StringVar()

ttk.Label(Frame3, text="First Name: ", font=("Arial", 12)).grid(column=0, row=0, sticky=(W,N), pady=1)
ttk.Label(Frame3, text="Last Name: ", font=("Arial", 12)).grid(column=2, row=0,sticky=(W,N),padx=5, pady=1)
ttk.Label(Frame3, text="", font=("Arial", 12)).grid(column=5, row=0,sticky=(W,N),padx=10, pady=1)

FirstNameEntry = ttk.Entry(Frame3, textvariable=FName, width=15, font=("Arial", 12)).grid(column=1, row=0, sticky=(W),padx=5)
LastNameEntry = ttk.Entry(Frame3, textvariable=LName, width=15, font=("Arial", 12)).grid(column=3, row=0, sticky=(W),padx=5)

#Frame 4

Frame4 = ttk.Frame(Frame2, padding="10 7 35 0")
Frame4.grid(column=0, row=1, sticky=(S))

Dia = IntVar()
Mes = StringVar()
Año = IntVar()

ttk.Label(Frame4, text="Birth Date ", font=("Arial", 12)).grid(column=0, row=0, sticky=(W,S),pady=10)
ttk.Label(Frame4, text="", font=("Arial", 12)).grid(column=5, row=0, sticky=(W,S), padx=9,pady=10)
ttk.Label(Frame4, text="Country: ", font=("Arial", 12)).grid(column=6, row=0, sticky=(W,S),pady=10)
CountryEntry = ttk.Entry(Frame4,textvariable=Country, width=10, font=("Arial", 12)).grid(column=7, row=0, sticky=(W))
ttk.Label(Frame4, text="", font=("Arial", 12)).grid(column=8, row=0, sticky=(W,S), padx=51,pady=10)


            #listas
Framelistas = ttk.Frame(Frame4)
Framelistas.grid(column=1, row=0, sticky=(S), padx=5)

DiaBox = ttk.Combobox(Framelistas, textvariable=Dia, width=2, font=("Arial", 12))
DiaBox.grid(column=0, row=0, sticky=(W,S),pady=10)
DiaBox['values'] = ("1","2","3","4","5","6","7","8",
                    "9","10","11","12","13","14","15",
                    "16","17","18","19","20","21","22",
                    "23","24","25","26","27","28","29",
                    "30","31")

MesBox = ttk.Combobox(Framelistas, textvariable=Mes, width=2, font=("Arial", 12))
MesBox.grid(column=1, row=0, sticky=(W,S), padx=2, pady=10)
MesBox['values'] = ("January","February","March","April","May","June","July","August","September",
                    "Octuber","November","December")


AñoBox = ttk.Combobox(Framelistas, textvariable=Año,width=4, font=("Arial", 12))
AñoBox.grid(column=2, row= 0,sticky=(W,S), padx=2, pady=10)
AñoBox['values'] = tuple(range(1923, 2024))

#Frame 5

Frame5 = ttk.Frame(BaseFrame, width=450,height=600,padding="35 17 50 12", relief="groove")
Frame5.grid(column=0, row=2, sticky=(W))

    #CreditCard

creditCard = ttk.Frame(Frame5, padding="0 0 216 0")
creditCard.grid(column=0, row=0, sticky=(W))
Credit = IntVar()

ttk.Label(creditCard, text="Credir Card (if any): ", font=("Arial", 12)).grid(column=0,row=0,sticky=(W))
CreditEntry = ttk.Entry(creditCard, textvariable=Credit, width=16, font=("Arial", 12)).grid(column=1, row=0, sticky=(W),padx=5)

    #Radio Butons

radiobu = ttk.Frame(Frame5, padding="0 20 0 0")
radiobu.grid(column=0, row=1)
ttk.Label(radiobu, text="Credit Card Type(if any): ", font=("Arial", 12)).grid(column=0, row=0,sticky=(W), pady=4)

typeCreditCard=""

#style = ttk.Style()
#style.configure("TRadioButton", font=("Arial", 8))

                                                                                 #, style="TButton"
# Crear el botón de radio con el nuevo estilo de texto
visa = ttk.Radiobutton(radiobu, text="Visa", variable=typeCreditCard, value="Visa")
visa.grid(column=1, row=0, sticky=(W), padx=10)
masterCard = ttk.Radiobutton(radiobu, text="MasterCard", variable=typeCreditCard, value="MasterCard")
masterCard.grid(column=2, row=0,sticky=(W), padx=5)

radiobu.grid(column=0, row=3, sticky=(W))

# Frame 6
Frame6 = ttk.Frame(BaseFrame,padding="35 2 140 2", relief="groove")
Frame6.grid(column=0, row=3, sticky=(W))

ttk.Label(Frame6, text="RoomType: ", font=("Arial", 12)).grid(column=0, row=0, sticky=(W), pady=2)

Normal=""
Familiar=""
Special=""

Normal1 = ttk.Radiobutton(Frame6, text="Normal", variable=Normal, value="Normal")
Normal1.grid(column=1, row=0, sticky=(W), padx=10)
Familiar1 = ttk.Radiobutton(Frame6, text="Familiar", variable=Familiar, value="Familiar")
Familiar1.grid(column=1, row=1,sticky=(W), padx=10, pady=5)    
Special1 = ttk.Radiobutton(Frame6, text="Special", variable=Special, value="Special")
Special1.grid(column=1, row=2,sticky=(W), padx=10, pady=5) 

ttk.Label(Frame6, text="Total Staying Time(days): ", font=("Arial", 12),padding="35 0 0 0").grid(column=2, row=0, pady=2)
Total_Staying_Time = ttk.Entry(Frame6, textvariable=Credit, width=4, font=("Arial", 12)).grid(column=3, row=0)


# Frame 7
Frame7 = ttk.Frame(BaseFrame,padding="262 30 262 30", relief="groove")
Frame7.grid(column=0, row=4, sticky=(W))

BottonBack = Button(Frame7,text="Submit", height=2, width=10)
BottonBack.grid(column=0,row=0,pady=15)





# Iniciar el bucle de eventos
root.mainloop()
