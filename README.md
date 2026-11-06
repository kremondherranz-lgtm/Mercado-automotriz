# Mercado de autos en Cuba

Proyecto de la asignatura Introducción a la Ciencia de Datos. Queremos saber qué carros se venden en Cuba, a qué precio, por qué canal (concesionarios frente a mercado informal) y qué busca el comprador.

## Estructura

```
requirements.txt     # librerías necesarias
AGENTS.md            # convenciones y reglas del proyecto
Anexos/              # anexos del trabajo (cuestionario, fotos, datos de apoyo)
Storytelling/        # guion y artículo de presentación de resultados
data/
  raw/               # un archivo por fuente, sin procesar
  processed/         # resultados listos para análisis
    survey.csv
    INFORME_4_11_2026_con_interpretaciones.docx
    tablas_graficas/
docs/
  fuentes/           # catálogos PDF, libro de mercado y fuentes oficiales (ONEI, ICEX)
  methodology/       # cuestionario, leyenda, pasos seguidos y análisis por pregunta
  journals/          # diarios de investigación
evidencia/           # evidencias del trabajo de campo (fotos)
journals/            # diarios de trabajo del equipo
src/
  transform.py       # une los CSV de data/raw/ y guarda data/processed/unified_cars.csv
  clean_survey.py    # limpia la encuesta y guarda data/processed/survey.csv
```

Cada carpeta de primer nivel tiene su propio `README.md` con el detalle de sus archivos.

El flujo es: **raw → processed**.

## Cómo se ejecuta

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt

python src/transform.py      # genera data/processed/unified_cars.csv
python src/clean_survey.py   # genera data/processed/survey.csv
```

## Columnas del resultado

`company, seller_type, channel, brand, model, year, price, currency, price_usd, province, source`

`price` y `currency` son el precio tal como aparece en la fuente original (EUR, USD o CUP).
`price_usd` es ese mismo precio convertido a dólares con las tasas informales en
`EXCHANGE_RATE_TO_CUP` dentro de `src/transform.py` (mercado cubano, 2026-10-25). Para
usar una tasa más reciente, basta con actualizar ese diccionario.

`channel` es `"formal"` (concesionarios/catálogos) o `"informal"` (Revolico), calculado
a partir de `company`.

`brand` para los catálogos viene tal cual del raw. Para Revolico, `data/raw/revolico_cars.csv`
ya trae su propia columna `marca` (se agregó a mano detectando palabras clave en el título,
como "Toyota" o "Hyundai"); `src/transform.py` solo la renombra y normaliza, no la calcula.
Lo que no se pudo identificar queda como `"No identificada"`.

## Fuentes

- **Concesionarios y comercializadoras:** MCV Comercial, Womy, Dongfeng Cuba, BDC One (catálogos en PDF y web).
- **Mercado informal:** anuncios de carros de Revolico.
- **Registro de vehículos eléctricos:** datos de adquisiciones por particulares y por entidades estatales.
- **Fuentes oficiales:** estadísticas de la ONEI y estudio de componentes del mercado automovilístico cubano (ICEX).
- **Bibliografía y catálogos adicionales:** `LIBRO_ESTUDIO_DE_MERCADO_VF (1).pdf` (libro de estudio de mercado) y `vehiculos-comerciales-abril-2026.CRrY5k95.pdf`.
- Los catálogos en PDF, el libro y las fuentes oficiales están en `docs/fuentes/`.

## Journals

Los diarios de trabajo se encuentran en:
- `journals/` - diarios generales del proyecto
- `docs/journals/` - diarios metodológicos e investigación
- `data/journals/` - notas sobre fuentes y procesamiento de datos

## Pendiente

- Ampliar la muestra de la encuesta y mantener actualizados los resultados del formulario.
- Tabla para emparejar modelos entre canales.
- Ir mejorando la redacción de la metodología.
- Regenerar `data/processed/unified_cars.csv` (no está versionada actualmente).
- Excluir los temporales de Office (`Anexos/~$...` y `data/processed/~$...`).
- Evaluar Git LFS para los PDF grandes de `docs/fuentes/`.


## Metodología y análisis de la encuesta

Se realizó una búsqueda inicial sobre el tema de investigación para conocer que es el mercado de un producto o servicio y los elementos que hay que tener en cuenta. La búsqueda nos permitió consultar el libro: Introducción al estudio del mercado de una autora peruana, a partir de estudiar los ejemplos que aparecen en el libro, se elaboró una primera versión  del cuestionario con cerca de 28 preguntas, que fue mejorado a partir de la consulta de la profesora Ariadna Velázquez y posteriormente adicionado a form.google.com para completar digitalmente las respuestas. En la carpeta methodology se encuentra un archivo con la explicación de los pasos seguidos, las fuentes consultadas y también el cuestionario final aplicado y las respuestas de los entrevistados hasta el día de hoy

- [docs/methodology/ANALISIS_POR_PREGUNTA_Y_RESPUESTAS.md](docs/methodology/ANALISIS_POR_PREGUNTA_Y_RESPUESTAS.md)

Este documento incluye: codificación de variables, frecuencias/porcentajes por pregunta, ejemplos textuales de respuestas múltiples, principales hallazgos y resumen ejecutivo.
