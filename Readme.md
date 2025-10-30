# Archivo requirements.txt
<br> Vamos a ver este archivo, éste gestiona todas las dependencias y en qué versiones se necesitan,
vamos a dejar acá los comandos para que alguien logre contribuir en este proyecto, los comandos son los
siguientes:<br>

¨¨¨sh
    git clone https://...
    cd app
    python3 -m venv env #se debe crear el entorno virtual,este no se comparte desde GitHub
    source env/bin/activate #activamos el entorno en linux
    venv/Script/activate #activa el entorno en windows
    pip3 install -r requirements.txt #instala las dependencias el r- significa reutilizar
    python3 main.py #ejecutamos el programa