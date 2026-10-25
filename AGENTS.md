# AGENTS.md

## Objetivo del proyecto
- Proyecto de **Introducción a la Ciencia de Datos**: estudio del mercado automotriz en Cuba.
- Combina **datos de concesionarios/comercializadoras** (canal formal) con **anuncios de Revolico** (canal informal), además de un **cuestionario a compradores potenciales**.
- El fin es recolectar, unificar y analizar estos datos para extraer conclusiones sobre precios, marcas, canales y preferencias de compra.

## Convenciones obligatorias
- **Código en inglés.** Nombres de variables, funciones, archivos y lógica deben ir en inglés.
- **Comentarios en español.** Cualquier comentario explicativo debe estar en español.
- **Mantener `README.md` siempre actualizado.** Si añades fuentes, columnas, scripts, flujo o cambios relevantes, actualízalo.

## Flujo de datos
```
data/raw/*.csv  →  src/transform.py  →  data/processed/unified_cars.csv
```
- **Raw:** un CSV por fuente, sin procesar.
- **Processed:** salida unificada y lista para análisis.

## Archivos clave
- `src/transform.py` - Único script de transformación. Fuente de verdad para el mapeo, canal, marca y conversión a USD.
- `requirements.txt` - Dependencias necesarias.
- `data/raw/` - Fuentes crudas. Destacan: `revolico_cars.csv`, `dongfeng_nwi_commercial.csv`, `mcv_commercial_2026-03-03.csv`, `womy_catalog_july_2026.csv`, `bdcone_commercial.csv`
- `docs/encuesta_compradores.md` - Cuestionario para compradores potenciales (pendiente de aplicar).
- `docs/methodology/ANALISIS_POR_PREGUNTA_Y_RESPUESTAS.md` - Análisis detallado por pregunta con frecuencias, codificación y hallazgos.
- `docs/contexto_mercado.md` - Contexto oficial (ONEI, ICEX) para contrastar con el dataset.
- `docs/pdf/` - Catálogos de concesionarios en PDF.

## Comandos exactos
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python src/transform.py   # genera data/processed/unified_cars.csv
```

## Reglas críticas (no adivinar)
- **Conversión a USD:** `price_usd` se calcula con `EXCHANGE_RATE_TO_CUP` dentro de `src/transform.py`. Usa tasas informales cubanas (2026-10-25 por defecto). Si se necesita una tasa más reciente, **actualizar ese diccionario directamente**.
- **Canal:** `channel` es `"formal"` (concesionarios/catálogos) o `"informal"` (Revolico). Se determina a partir de `company`.
- **Marca de Revolico:** **No se infiere por NLP** en `transform.py`. `data/raw/revolico_cars.csv` debe traer su propia columna `marca` añadida manualmente (detección por palabras clave en título). `transform.py` solo la renombra/normaliza. Si no se identifica → `"No identificada"`.
- **Precios originales:** `price` y `currency` se conservan tal como vienen en la fuente (EUR, USD o CUP). Solo `price_usd` es el valor convertido.
- **Columnas de salida:** `company, seller_type, channel, brand, model, year, price, currency, price_usd, province, source`
- **Fuentes:** Formales = MCV Comercial, Womy, Dongfeng Cuba, BDC One. Informal = Revolico.
