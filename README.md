# Mercado de autos en Cuba

Proyecto de la asignatura Introducción a la Ciencia de Datos. Queremos saber qué carros se venden en Cuba, a qué precio, por qué canal (concesionarios frente a mercado informal) y qué busca el comprador.

## Estructura

```
requirements.txt     # librerías necesarias
data/
  raw/               # un CSV por fuente, sin procesar
    dongfeng_nwi_commercial.csv
    mcv_commercial_2026-03-03.csv
    womy_catalog_july_2026.csv
    bdcone_commercial.csv
    revolico_cars.csv   # ~100 anuncios, muestra representativa por marca
  processed/         # resultado final, listo para consultas
docs/
  pdf/                       # catálogos de concesionarios en PDF
  encuesta_compradores.md    # encuesta para entrevistar compradores potenciales
  contexto_mercado.md        # datos oficiales (ONEI, ICEX) para comparar contra el dataset
src/
  transform.py       # une los CSV de data/raw/ y guarda data/processed/unified_cars.csv
```

El flujo es: **raw → processed**.

## Cómo se ejecuta

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python src/transform.py   # genera data/processed/unified_cars.csv
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

## Pendiente

- Entrevistas a compradores: la encuesta ya está en `docs/encuesta_compradores.md`, falta aplicarla.
- Tabla para emparejar modelos entre canales.


## Metodología y análisis de la encuesta

Se ha documentado el análisis detallado por pregunta con sus resultados y la forma en que se presentan las respuestas de los entrevistados en:

- [docs/methodology/ANALISIS_POR_PREGUNTA_Y_RESPUESTAS.md](docs/methodology/ANALISIS_POR_PREGUNTA_Y_RESPUESTAS.md)

Este documento incluye: codificación de variables, frecuencias/porcentajes por pregunta, ejemplos textuales de respuestas múltiples, principales hallazgos y resumen ejecutivo.
