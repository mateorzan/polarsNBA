# Proyecto polarsNBA

En este proyecto se centra en la implementacion de nuevas herramientas como uv para crear un entorno local simple y reproducible y polars. El objetivo es explicar su funcionamiento y rendimiento, aqui se explica como se configuraria y funcionarian estas herramientas en un entorno local

## Preparacion de entorno (UV)

Instalacion de la herramienta uv, para mas informacion mirar en (https://docs.astral.sh/uv/#installation)

´´´
curl -Ls https://astral.sh/uv/install.sh | bash
source $HOME/.local/bin/env

´´´python

Verificamos si esta Instalado

´´´python
uv --version
´´´

Creamos el entorno vitual uv, nos posicionamos en la carpeta que deseamos crear el entorno y hacemos un uv init, luego ejecutamos el script main que nos creara el entorno. Este paso es solo si quieres crear un entorno nuevo si estas clonando este repositoria te lo puedes saltar.

´´´python
uv init
uv run main.py
´´´
Para añadir dependencias se usa el comando uv add con este comando instalamos y añadimos el paquete a nuestro proyecto.

´´´python
uv add paquete1 paquete2
´´´

Si estas clonando este repositorio simplemente con el comando uv sync ya que se instalaran todos los paquetes que yo añadi a este proyecto. Instalar dependencias: 

´´´python
uv sync
source .venv/bin/activate
´´´

COSAS QUE HACER 

Implementar uv para instalar las diferentes dependencias del proyecto.

Usar polars para el proceso de etl.

Crear un script que actualice el csv incial con datos nuevos para asi tener datos actuales.

En un futuro crear una base de datos que almacene los datos y gestionarlos desde ahi.