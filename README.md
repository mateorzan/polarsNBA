# 🏀 polarsNBA

Un proyecto de análisis de datos NBA centrado en herramientas modernas de Python: **uv** para gestión de entornos y **Polars** para procesamiento de datos de alto rendimiento.

## 🎯 Objetivos

- Implementar **uv** como gestor de paquetes y entornos virtuales
- Utilizar **Polars** para operaciones ETL eficientes
- Establecer las bases para una futura base de datos

## 🚀 Configuración del Entorno

### Instalación de uv

Instala uv siguiendo las [instrucciones oficiales](https://docs.astral.sh/uv/#installation):

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
source $HOME/.cargo/env
```

Verifica la instalación:

```bash
uv --version
```

### Configuración del Proyecto

#### Opción 1: Crear un nuevo proyecto

```bash
# Crear directorio del proyecto
mkdir polarsNBA
cd polarsNBA

# Inicializar proyecto con uv
uv init

# Ejecutar el script principal (crea el entorno automáticamente)
uv run main.py
```

#### Opción 2: Clonar este repositorio

```bash
# Clonar el repositorio
git clone <url-del-repositorio>
cd polarsNBA

# Sincronizar dependencias
uv sync

# Activar el entorno virtual
uv run main.py
```

### Gestión de Dependencias

Añadir nuevas dependencias:

```bash
uv add polars pandas requests beautifulsoup4
```

Ver dependencias instaladas:

```bash
uv pip list
```

Actualizar dependencias:

```bash
uv sync --upgrade
```

## 📦 Dependencias Principales

- **polars**: Procesamiento de datos de alto rendimiento
- **ipykernel**: Gestor para poder ejecutar los notebooks

## 🏗️ Estructura del Proyecto

```
polarsNBA/
├── README.md
├── pyproject.toml
├── uv.lock
├── main.py
├── .python-version
├── archive/
│   ├── raw/                 # Datos en bruto
│   └── processed/           # Datos procesados
├── notebooks/               # Jupyter notebooks para análisis
└── scripts/
    └── 
```

## 📊 Características de Polars

### Ventajas sobre Pandas:
- **Velocidad**: Hasta 10x más rápido en operaciones complejas
- **Memoria**: Uso eficiente de memoria con lazy evaluation
- **Sintaxis**: API expresiva y consistente
- **Tipos**: Sistema de tipos robusto

### Ejemplo de uso:

```python
import polars as pl

# Lectura lazy (no carga en memoria inmediatamente)
df = (
    pl.scan_csv("data/nba_stats.csv")
    .filter(pl.col("season") == "2024-25")
    .group_by("team")
    .agg([
        pl.col("points").mean().alias("avg_points"),
        pl.col("wins").sum().alias("total_wins")
    ])
    .sort("avg_points", descending=True)
    .collect()  # Ejecuta todas las operaciones
)
```

## 🎯 Roadmap

### ✅ Completado
- [x] Configuración de uv
- [x] Estructura básica del proyecto

### 🔄 En Progreso
- [ ] Implementación del ETL con Polars
- [ ] Modelado de datos
- [ ] Cuadro de mandos en PowerBI

### 📋 Pendiente
- [ ] Integración con APIs NBA oficiales
- [ ] Dashboard interactivo
- [ ] Base de datos PostgreSQL


## 📝 Comandos Útiles

```bash
# Gestión del entorno
uv venv --python 3.11               # Crear entorno con Python específico
uv pip install -e .                 # Instalar en modo desarrollo
uv export --format requirements-txt # Exportar requirements.txt
```

## 📞 Contacto

- **Autor**: Mateo Iglesias
- **Email**: mateorzan@gmail.com
- **GitHub**: [@mateorzan](https://github.com/tu-usuario)

---

⭐ Si este proyecto te resulta útil, ¡dale una estrella en GitHub!