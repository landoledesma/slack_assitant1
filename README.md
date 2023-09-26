# slack_assitent1
# Asistente AI para Slack con Python & LangChain

Aquí tienes una guía paso a paso para crear un bot en Slack, instalarlo en un espacio de trabajo, configurar un código Python con Flask y usar ngrok.

Interactuar con agentes AI a través de Slack ofrece una forma de comunicación más natural e integra con el flujo de trabajo de tu equipo, permitiendo la incorporación de múltiples bots para diversas tareas. Esto puede mejorar la eficiencia y agilizar la comunicación, al mismo tiempo que permite que los agentes AI se conviertan en una parte integral de tu equipo.

## Parte 1 — Configuración de Slack

#### 1. Crea una nueva aplicación en Slack

- Elige un espacio de trabajo de Slack existente o crea uno nuevo.
- Ve a [https://api.slack.com/apps](https://api.slack.com/apps) e inicia sesión con tu cuenta de Slack.
- Haz clic en "Crear Nueva Aplicación" y proporciona un nombre para la app y selecciona tu espacio de trabajo como el espacio de desarrollo. Haz clic en "Crear App".

#### 2. Configura tu bot

- En la sección "Agregar características y funcionalidad", haz clic en "Bots".
- Haz clic en "Agregar un Usuario Bot" y completa el nombre de visualización y el nombre de usuario predeterminado. Guarda tus cambios.

#### 3. Añade permisos a tu bot

- En el menú lateral izquierdo, haz clic en "OAuth & Permisos".
- Desplázate hacia abajo hasta "Alcances" y añade los alcances de token del bot requeridos. Para este ejemplo, necesitarás al menos `app_mentions:read`, `chat:write`, y `channels:history`.

#### 4. Instala el bot en tu espacio de trabajo

- En el menú lateral izquierdo, haz clic en "Instalar App".
- Haz clic en "Instalar App en Espacio de Trabajo" y autoriza la app.

#### 5. Recupera el token del bot

- Tras la instalación, serás redirigido a la página "OAuth & Permisos".
- Copia el "Token de Acceso OAuth del Usuario Bot" (comienza con `xoxb-`). Lo necesitarás para tu script en Python.

## Parte 2 — Configuración de Python

#### 1. Configura tu entorno Python

- Instala Python 3.6 o posterior (si aún no lo has hecho).
- Instala los paquetes requeridos: `slack-sdk`, `slack-bolt` y `Flask`. Puedes hacer esto usando pip:

```other
pip install slack-sdk slack-bolt Flask
```

Además de los pasos proporcionados, también puedes crear un entorno virtual para aislar las dependencias de tu aplicación Python de otros proyectos en tu máquina. Aquí están los pasos para crear un entorno virtual usando `venv` o `conda` e instalar los paquetes requeridos:

Usando `venv`:

```bash
python3 -m venv myenv
source myenv/bin/activate
pip install slack-sdk slack-bolt Flask
```
Usando `conda`:

```other
conda create --name myenv python=3.8
conda activate myenv
pip install slack-sdk slack-bolt Flask
```

#### 2. Crea el script Python con Flask

- Crea un nuevo archivo Python (por ejemplo, `app.py`) e inserta el código de [`app.py`](https://github.com/daveebbelaar/langchain-experiments/blob/main/slack/app.py) de este repositorio.
- Si deseas usar una versión gratuita, puedes explorar los otros modelos soportados por [LangChain's Model](https://python.langchain.com/en/latest/modules/models/llms/integrations.html).

#### 3. Configura la variable de entorno en el archivo .env

- Crea un archivo .env en el directorio de tu proyecto y añade las siguientes claves:

```yaml
SLACK_BOT_TOKEN = "xoxb-tu-token"
SLACK_SIGNING_SECRET = "tu-secreto"
SLACK_BOT_USER_ID = "tu-id-de-bot"
OPENAI_API_KEY= "tu-llave-openai"
```

#### 4. Inicia tu servidor local Flask

- Ejecuta el script Python en la terminal (macOS/Linux) o en la Línea de Comandos (Windows): `python app.py`. El servidor debería iniciar y verás una salida que indica que está funcionando en [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

## Parte 3 — Configuración del Servidor (Local)

#### 1. Expone tu servidor local usando ngrok

- Si aún no has instalado ngrok, puedes descargarlo desde [https://ngrok.com/download](https://ngrok.com/download) o, en macOS, instalarlo a través de Homebrew ejecutando: `brew install ngrok`
- En una nueva terminal (macOS/Linux) o Línea de Comandos (Windows), inicia ngrok ejecutando el siguiente comando: `ngrok http 5000`
- Toma nota de la URL HTTPS proporcionada por ngrok (por ejemplo, [https://tusubdominio.ngrok.io](https://tusubdominio.ngrok.io/)). La necesitarás para el siguiente paso.

Recuerda que si instalaste ngrok vía Homebrew, puedes ejecutar `ngrok http 5000` desde cualquier directorio en la terminal. Si lo descargaste del sitio web, navega al directorio donde se instaló ngrok antes de ejecutar el comando.

#### 2. Configura tu aplicación Slack con la URL de ngrok

- Regresa a la configuración de tu aplicación Slack en [https://api.slack.com/apps](https://api.slack.com/apps).
- Haz clic en "Suscripciones a Eventos" en el menú lateral izquierdo.
- Activa los eventos e introduce tu URL de ngrok seguido de `/slack/events` (por ejemplo, [https://tusubdominio.ngrok.io/slack/events](https://tusubdominio.ngrok.io/slack/events)).
- Desplázate hacia abajo hasta "Suscribirse a eventos de bot" y haz clic en "Agregar Evento de Usuario Bot". Añade el evento `app_mention` y guarda tus cambios.

>**Nota**
> Por favor, ten en cuenta que cada vez que reinicies ngrok en la terminal, tendrás que actualizar la URL en Slack; esto es solo para pruebas.

#### 3. Reinstala tu aplicación de Slack para actualizar los permisos

- En el menú lateral izquierdo, haz clic en "Instalar Aplicación".
- Haz clic en "Reinstalar Aplicación en el Espacio de Trabajo" y autoriza la aplicación.

#### 4. Añade tu bot a un canal de Slack

- Escribe `/invite @nombre-del-bot` en el canal.

## Parte 4 — Añadir Funciones Personalizadas

#### 1. Crea una función para redactar correos electrónicos

- Crea un nuevo archivo llamado `functions.py` e inserta el código de [`functions.py`](https://github.com/daveebbelaar/langchain-experiments/blob/main/slack/functions.py)
- Importa la función en tu archivo `app.py` con `from functions import draft_email`.
- Y actualiza la función `handle_mentions`.

#### 2. Propón tus propias ideas

- ¿Qué vas a crear con esto?

## Solución de Problemas

> **Advertencia**
> El puerto 5000 está en uso por otro programa. Identifica y detén ese programa o inicia el servidor en un puerto diferente.

Para cerrar un puerto en Mac, necesitas identificar el programa o proceso que está utilizando el puerto y luego detener ese programa o proceso. Estos son los pasos que puedes seguir:

1. Abre la aplicación Terminal en tu Mac.
2. Ejecuta el siguiente comando para listar todos los puertos abiertos y los procesos que los están utilizando:

```bash
sudo lsof -i :<numero_de_puerto>
```

Reemplaza `<numero_de_puerto>` con el número de puerto que deseas cerrar.

3. Busca el ID del proceso (PID) del programa que está usando el puerto en la salida del comando `lsof`.
4. Ejecuta el siguiente comando para detener el programa o proceso:

```bash
kill <PID>
```

Reemplaza `<PID>` con el ID del proceso que obtuviste en el paso anterior.

5. Verifica que el puerto ya no esté en uso ejecutando el comando `lsof` nuevamente.

```bash
sudo lsof -i :<numero_de_puerto>
```

Si el puerto ya no está en uso, el comando no debería devolver ninguna salida.

Ten en cuenta que es posible que necesites ejecutar los comandos `lsof` y `kill` con privilegios de `sudo` si el programa o proceso pertenece a otro usuario o requiere privilegios elevados.
