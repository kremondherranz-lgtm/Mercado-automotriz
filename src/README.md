# src

Scripts de procesamiento del proyecto.

## Contenido

- `transform.py` — lee los catálogos formales y la muestra de Revolico de `data/raw/`, normaliza las columnas, convierte los precios a USD y genera `data/processed/unified_cars.csv`.
- `clean_survey.py` — lee la encuesta de Google Forms, renombra las columnas a inglés y genera `data/processed/survey.csv`.

## Ejecución

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt

python src/transform.py
python src/clean_survey.py
```

## Reglas

- `transform.py` es la fuente de verdad para el mapeo de columnas, el canal (`formal`/`informal`), la marca y la conversión a USD.
- La conversión usa `EXCHANGE_RATE_TO_CUP` con tasas informales; para actualizarla, se edita ese diccionario.
- `clean_survey.py` procesa la exportación `(1)` del formulario.
