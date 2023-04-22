import os
import pyfiglet
import requests
import json
from termcolor import colored


os.system("cls" if os.name == "nt" else "clear") # Limpia la ventana de la terminal
ascii_text = pyfiglet.figlet_format("Erik Ware")
print(colored(ascii_text, "green"))

# Pide al usuario que introduzca la URL de la webhook
WEBHOOK_URL = input("Webhook:")

# Extrae el token y la ID de la webhook de la URL
url_parts = WEBHOOK_URL.split("/")
webhook_id = url_parts[-2]
webhook_token = url_parts[-1]

# Imprime la ID y el token de la webhook en azul y rojo respectivamente
print(f"\n{colored('La ID de la webhook es:', 'blue')} {colored(webhook_id, 'red')}")
print(f"{colored('El token de la webhook es:', 'blue')} {colored(webhook_token, 'red')}\n")

# Pide al usuario que introduzca el mensaje a enviar
MESSAGE_CONTENT = input("Introduce el mensaje que quieres enviar: ")

# Crea un diccionario con el contenido del mensaje
message = {"content": MESSAGE_CONTENT}

# Convierte el diccionario en una cadena JSON
message_json = json.dumps(message)

# Define las cabeceras de la petición con la token
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bot {webhook_token}"
}

# Realiza una petición POST a la URL de la webhook con el contenido del mensaje
response = requests.post(WEBHOOK_URL, data=message_json, headers=headers)

# Imprime la respuesta de la petición
print(response.text)

# Pregunta al usuario si desea eliminar la webhook
eliminar_webhook = input("¿Desea eliminar la webhook? (s/n)")

if eliminar_webhook.lower() == "s":
    # Define la URL para eliminar la webhook
    delete_url = f"https://discord.com/api/webhooks/{webhook_id}/{webhook_token}"
    
    # Realiza una petición DELETE para eliminar la webhook
    response = requests.delete(delete_url)
    
    # Imprime la respuesta de la petición
    print(response.text)

# Imprime el texto ASCII "Crovax Product" y el logo de copyright
print("\n")
ascii_text = pyfiglet.figlet_format("Erik Product")
print(colored(ascii_text, "green"))
print(colored("Copyright © All rights reserved.", "green"))
