# Teclado Mecánico Virtual

Teclado Mecánico Virtual es una aplicación desarrollada en Python que simula los sonidos de un teclado mecánico cuando se presionan las teclas en tu computadora. La aplicación permite a los usuarios elegir entre diferentes tipos de sonidos de teclas, ajustar el volumen y asegura que todos los sonidos se reproduzcan sin interrupciones, incluso cuando las teclas se presionan rápidamente.

## Características

-   **Interfaz moderna y minimalista**: Utiliza `tkinter` para una GUI sencilla y elegante.
-   **Varios sonidos de teclas**: Selecciona entre diferentes tipos de sonidos de teclado mecánico.
-   **Control de volumen**: Ajusta el volumen de los sonidos a tu preferencia.
-   **Reproducción en paralelo**: Los sonidos se reproducen simultáneamente sin interrupciones, incluso con pulsaciones rápidas.
-   **Persistencia de configuración**: Guarda las preferencias de sonido y volumen en un archivo JSON para que se recuerden entre sesiones.

## Requisitos

-   Python 3.x
-   Pygame
-   Pynput

## Instalación

1. Clona este repositorio:

    ```bash
    git clone https://github.com/yoezequiel/Klack.git
    cd klack
    ```

2. Instala las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

3. Ejecuta la aplicación:

    ```bash
    python3 main.py
    ```

## Uso

1. Al iniciar la aplicación, se abrirá una ventana con un menú desplegable para seleccionar el tipo de sonido del teclado y un deslizador para ajustar el volumen.
2. Selecciona el sonido deseado y ajusta el volumen según tu preferencia.
3. Comienza a presionar las teclas en tu teclado y disfruta de los sonidos del teclado mecánico virtual.

## Configuración

La configuración se guarda en un archivo `config.json`. Este archivo almacena el nombre del sonido seleccionado, su ruta y el volumen. La aplicación carga esta configuración al iniciarse para recordar las preferencias del usuario.

Ejemplo de `config.json`:

```json
{
    "sound_name": "CherryMX",
    "sound_path": "sounds/cherry_mx.mp3",
    "volume": 0.5
}
```

## Contribuciones

Las contribuciones son bienvenidas. Si encuentras algún error o tienes alguna mejora, por favor abre un issue o envía un pull request.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.
