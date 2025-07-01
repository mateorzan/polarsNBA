# 🏀 polarsNBA

Un proyecto de análisis de datos NBA centrado en herramientas modernas de Python: **uv** para gestión de entornos y **Polars** para procesamiento de datos de alto rendimiento.

## 🎯 Objetivos

- Implementar **uv** como gestor de paquetes y entornos virtuales
- Utilizar **Polars** para operaciones ETL eficientes
- Crear un pipeline de datos actualizable para estadísticas NBA
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
- **requests**: Peticiones HTTP para obtener datos
- **beautifulsoup4**: Web scraping (si es necesario)
- **pytest**: Testing

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
│   ├── processed/           # Datos procesados
│   └── external/            # Datos externos
├── notebooks/               # Jupyter notebooks para análisis
├── tests/
└── scripts/
    └── update_data.py       # Script de actualización
```

## 🔄 Pipeline de Datos

### 1. Extracción (Extract)
```python
import polars as pl
import requests

def extract_nba_data():
    # Implementar extracción de APIs NBA
    pass
```

### 2. Transformación (Transform)
```python
def transform_data(df: pl.DataFrame) -> pl.DataFrame:
    return (
        df
        .with_columns([
            pl.col("date").str.to_datetime(),
            pl.col("points").cast(pl.Int32)
        ])
        .filter(pl.col("season") == "2024-25")
        .group_by("player")
        .agg([
            pl.col("points").mean().alias("avg_points"),
            pl.col("rebounds").sum().alias("total_rebounds")
        ])
    )
```

### 3. Carga (Load)
```python
def load_data(df: pl.DataFrame, output_path: str):
    df.write_parquet(output_path)
```

## 🗂️ Uso Básico

### Ejecutar el pipeline completo:

```bash
uv run src/main.py
```

### Actualizar datos:

```bash
uv run scripts/update_data.py
```

### Ejecutar tests:

```bash
uv run pytest tests/
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
- [ ] Implementación del pipeline ETL con Polars
- [ ] Script de actualización automática de datos
- [ ] Tests unitarios

### 📋 Pendiente
- [ ] Integración con APIs NBA oficiales
- [ ] Dashboard interactivo
- [ ] Base de datos PostgreSQL/DuckDB
- [ ] CI/CD con GitHub Actions
- [ ] Documentación con Sphinx


## 📝 Comandos Útiles

```bash
# Desarrollo
uv run pytest tests/ -v             # Tests con verbosidad

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