# Home Away Controller

Home Away Controller es un Software pensando para ejecutar acciones en tus dispositivos domésticos cuando entras o 
cuando sales de casa.

Aunque algunos sistemas como Homekit o Google Assistant ya pueden hacerlo en base a la localización de tu teléfono 
móvil, esto puede implicar un consumo extra de batería. Este programa viene a solucionar ese problema, detectando si 
estás en casa o no comprobando únicamente si tu dispositivo está conectado a tu red Wifi.

## Away Controllers
Para detectar si estás en casa o no, existe un módulo denominado `away_controllers` donde se encuentran algunas 
utilidades que permiten detectar si estás en casa o no. La idea en este caso es ir extendiendo este módulo a través de
contribuciones de la comunidad.

Actualmente, los controllers que existen son:

1. Movistar MitraStar HGU (`MovistarHGUMitraStarController`): este controller se conecta por SSH a tu router HGU de la
marca MitraStar y comercializado por Movistar, y detecta si estás en casa o no, viendo el estado LAN y comprobando si la
MAC de tu dispositivo está activa o no.

## Devices Managers
Para interactuar con la domótica de tu casa cuando entras o sales, existe un módulo denominado `devices_managers` que
permite interactuar con los dispositivos, para activarlos o desactivarlos, en función de tus necesidades. La idea en 
este caso es ir extendiendo este módulo a través de contribuciones de la comunidad.

Actualmente, los managers que existen son:

1. Homebrige (`HomeBridgeDeviceManager`): permite interactuar con tus dispositivos a través de
[HomeBridge](https://homebridge.io). 

## Configuración

Tanto los away controllers como los devices managers necesitan ser configurados, ya que necesitarás:

1. Definir los dispositivos que indican si estás en casa o no.
2. Establecer passwords para conectarte a tu router.
3. Definir los dispositivos con los que interactuar.
4. Establecer la forma de interactuar con esos dispositivos. 

Tienes un ejemplo de configuración en el archivo `config.json.template`:

* `away_controller`: Contiene la configuración del módulo que comprueba si estás en casa o no:
  * `class`: La clase del módulo que define si estás en casa o no.
  * `config`: La configuración específica del módulo.
  * `devices_to_control`: La lista de dispositivos que indican si estás en casa o no.
* `devices_managers`: Una lista de managers que gestionan los dispositivos con los que interactuar. Por cada uno:
  * `class`: La clase del módulo que permite interactuar con los dispositivos deseados.
  * `config`: La configuración específica del módulo.

### `MovistarHGUMitraStarController`

* `host`: La dirección IP del router.
* `user`: El usuario con el que conectarte al router (generalmente `1234`).
* `password`: La password de acceso al router (pegatina debajo del router).

### `HomeBridgeDeviceManager`

* `host`: La dirección IP de Homebridge.
* `user`: El usuario con el que conectarte Homebridge (generalmente `admin`).
* `password`: La password de acceso al Homebridge.
* `devices`: La lista de dispositivos con los que debe interactuar HomeBridge:
  * `id`: El ID único de dispositivo (lo puedes obtener llamando a la API `http://<HOMEBRIDGE_HOST>:8581/api/accessories`)
  * `type`: Tipo de dispositivo (`On`, `argetHeatingCoolingState`)
  * `home_value`: El valor a establecer al dispositivo cuando llegas a casa.
  * `away_value`: El valor a establecer al dispositivo cuando sales de casa.

## Ejecución

Para poder ejecutar, el programa necesita que definas la variable de entorno `CONFIG_FILE` con el path del fichero de 
configuración. Por ejemplo:

```
export CONFIG_FILE="/home/pi/home_away_controller/config.json"
cd home_away_controller
python3 /home/pi/home_away_controller/main.py
```

Lo ideal es que el programa ejecute cada minuto, cosa que puedes conseguir con una instrucción `cron` tal que:

```
*/1 * * * * /home/pi/home_away_launcher.sh >> /home/pi/home_away_controller.log 2>&1
```


