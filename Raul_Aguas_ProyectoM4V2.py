import requests #Se ocupo instalar
from PIL import Image #Se ocupo instalar
from urllib.request import urlopen # se ocupo instalar
import tkinter as tk #se ocupo instalar
import PIL.ImageTk #se ocupo instalar

#Dimensiones de la ventana y titulo de la pokedex
window = tk.Tk()
window.geometry("600x600")
window.title("POKEDEX")
window.config(padx=10, pady=10)

tittle_label = tk.Label(window, text='POKEDEX')
tittle_label.config (font=('Arial', 32))
tittle_label.pack(padx=10, pady=10)

pokemon_image = tk.Label(window)
pokemon_image.pack(padx=10, pady=10)

pokemon_fault = tk.Label(window)
pokemon_fault.config (font=('Arial', 15))
pokemon_fault.pack(padx=10, pady=10)

pokemon_name = tk.Label(window)
pokemon_name.config (font=('Arial', 15))
pokemon_name.pack(padx=10, pady=10)

pokemon_information = tk.Label(window)
pokemon_information.config(font=('Arial', 15))
pokemon_information.pack(padx=10, pady=10)

label_id_name = tk.Label(window, text='Escribe el nombre del Pokemon o su #ID')
label_id_name.config(font=('Arial', 15))
label_id_name.pack(padx=10, pady=10)

pokemon_types = tk.Label(window)
pokemon_types.config(font=('Arial', 15))
pokemon_types.pack(padx=10, pady=10)

#Para poder escribir el nombre del pokemon en un cuadro de texto 
text_id_name=tk.Text(window, height=1)
text_id_name.config(font=('Arial', 15))
text_id_name.pack(padx=0, pady=0)

def load_pokemon():
    pokemon = text_id_name.get(1.0, 'end-1c')
    # print(pokemon)
    pokemon1=pokemon.lower()
    url='https://pokeapi.co/api/v2/pokemon/'+ pokemon1
    #print (url)
    try :
        respuesta =  requests.get(url, timeout=10)
        print(respuesta)
    except requests.Timeout:
        print('Error: El tiempo de espera ha finalizado')

    ## Adquiero los datos de la url condicionando a que si los encuentro me busque los datos en el codigo json y si no me imprima pokemon no encontrado
    if respuesta.status_code == 200:
        datos = respuesta.json()
        
        try: 
            Namepokemon = datos['name']
            Namepoke = Namepokemon.upper()
            print(Namepokemon)
        except:
            print('El Pokemon no tiene nombre')
            exit()
        print('Movimientos de ' + Namepokemon)  
    #Toma los datos de movimientos del pokemon y los imprime en la terminal, no los puse en el pokedex
    #ya que tendria el mismo problema que con los tipos de pokemon
        movimientos = datos['moves']
        for i in range(int(len(movimientos))):
            movimiento = movimientos[i]['move']['name']
            print(movimiento)

        # ###Toma la imagen del pokemon de la url
        try: 
            url_imagen = datos['sprites']['front_default']
            imagen = Image.open(urlopen(url_imagen))
        except:
            print('El Pokemon no tiene imagen')
            exit()
        
        img = PIL.ImageTk.PhotoImage(imagen) # para imprimir la imagen en la pantalla
        pokemon_image.config(image=img)
        pokemon_image.imag=img


        information = datos['types'] #imprime el tipo de pokemon que es 
        for i in range(int(len(information))):
            informacion = information[i]['type']['name']
            print(informacion)

        pokemon_name.config(text=Namepoke)
        # for i in range(int(len(information))):
        #      informacion2 = information[]['type']['name']
        #      print(informacion2)
        pokemon_information.config(text=f'Pokemon tipo: {informacion}') # Aqui concatena la  info del pokemon con un texto el cual indica
        #el tipo de pokemon que es, aqui tuve un problema y no puede hacer que me mostrara todos los tipos a la cual pertenece el pokemon
        #intente crear una lista para almacenar los datos y luego concatenar cada uno pero no supe como hacerlo
    else:
        pokemon_fault.config(text='Pokemon no encontrado')

#Boton para buscar pokemon le da el comando al boton de buscar una vez colocado el nombre esto esta declarado en la funcion load_pokemon
btn_load = tk.Button(window, text='Buscar Pokemon', command=load_pokemon,  bg='grey')
btn_load.config(font=('Arial', 20))
btn_load.pack(padx=10, pady=10)


window.mainloop()