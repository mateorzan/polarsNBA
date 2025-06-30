# polarsNBA

## Preparacion de entorno

Instalacion de la herramienta uv

´´´ python 
curl -Ls https://astral.sh/uv/install.sh | bash
´´´

export PATH="$HOME/.local/bin:$PATH"

source ~/.bashrc   # o source ~/.zshrc si usas zsh


Verifica si se instalo

´´´python
uv --version
´´´



COSAS QUE HACER 

Implementar uv para instalar las diferentes dependencias del proyecto.

Usar polars para el proceso de etl.

Crear un script que actualice el csv incial con datos nuevos para asi tener datos actuales.

En un futuro crear una base de datos que almacene los datos y gestionarlos desde ahi.