# Datos

Datos del estudio del mercado automotriz en Cuba, separados por etapa del flujo.

```
data/raw/*.csv  →  src/transform.py      →  data/processed/unified_cars.csv
data/raw/*.csv  →  src/clean_survey.py   →  data/processed/survey.csv
```

## raw/

Un archivo por fuente, sin procesar.

**Oferta formal (concesionarios y comercializadoras):**

- `dongfeng_nwi_commercial.csv` — catálogo de Dongfeng Cuba.
- `mcv_commercial_2026-03-03.csv` — catálogo de MCV Comercial (marzo 2026).
- `womy_catalog_july_2026.csv` — catálogo de Womy (julio 2026).
- `bdcone_commercial.csv` — catálogo de BDC One.
- `bdcone_commercial_tipo_de_propulsion.csv` — variante de BDC One con tipo de propulsión.
- `oferta_4_concecionarias.xlsx` — oferta consolidada de las cuatro concesionarias.

**Oferta informal:**

- `revolico_cars.csv` — 100 anuncios de Revolico, con columna `marca` añadida manualmente.
- `oferta_de_revolico.csv` — copia de la misma muestra de Revolico.

**Demanda (encuesta):**

- `ESTUDIO DEL MERCADO AUTOMOTRIZ EN LA HABANA (respuestas) - Respuestas de formulario 1 (*).csv` — exportaciones sucesivas del formulario de Google (11 a 33 respuestas). La versión que procesa `clean_survey.py` es la `(1)`.
- `prefrencias_propulsion_encuesta.xlsx` — preferencias de propulsión de los encuestados.

**Fuentes complementarias:**

- `arrendadores_vivienda_plaza.xlsx` — arrendadores de vivienda en La Habana.
- `Registro de vehiculos_electricos.xlsx` — registro de vehículos eléctricos.
- `Registro de autos_electricos_adquiridos por particulares.xlsx` — adquisiciones de eléctricos por particulares.
- `Registro de autos_electricos_adquiridos por entidades estatales.xlsx` — adquisiciones de eléctricos por entidades estatales.
- `Mcv_tipo de carros.xlsx`, `Gongfeng_tipo de carros.xlsx`, `womy_tipo de carros.xlsx`, `BDCone_tipo de carros.xlsx` — desglose por tipo de vehículo de cada comercializadora.

## processed/

Resultados listos para análisis.

- `unified_cars.csv` — tabla unificada que genera `src/transform.py`. Columnas: `company, seller_type, channel, brand, model, year, price, currency, price_usd, province, source`.
- `survey.csv` — encuesta con columnas renombradas a inglés, generada por `src/clean_survey.py`.
- `INFORME_4_11_2026_con_interpretaciones.docx` — informe con interpretaciones de los resultados.
- `tablas_graficas/` — tablas y gráficas del análisis exploratorio de la encuesta.

## journals/

Notas de trabajo sobre las fuentes y el procesamiento. Contiene `README.md` y `2026-11-05.md` (inventario y duplicados detectados).

## Reglas

- No editar manualmente los archivos de `raw/` salvo la columna `marca` de `revolico_cars.csv`, que se completa a mano.
- Los precios se conservan en su moneda original; `price_usd` se calcula en `src/transform.py`.
- Los archivos `~$...` son temporales de Office y no forman parte de los datos.
