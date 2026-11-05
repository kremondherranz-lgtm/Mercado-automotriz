# Journal de documentación - 2026-11-05

## Objetivo

Dejar constancia de la auditoría de documentación y de la reorganización de rutas del proyecto.

## Revisión realizada

- Se comprobó que el `README.md` raíz describía carpetas inexistentes:
  - `docs/pdf/`, cuando los catálogos están en `docs/fuentes/`;
  - `docs/encuesta_compradores.md`, cuando el cuestionario está en `docs/methodology/`;
  - `docs/contexto_mercado.md`, que no existe como archivo.
- Se verificó que los scripts activos son `src/transform.py` y `src/clean_survey.py`, con salidas en `data/processed/`.
- Se documentó el contenido real de cada carpeta de primer nivel en su propio `README.md`.

## Cambios de documentación

- `README.md` raíz: estructura, comandos y fuentes actualizados.
- `Anexos/README.md`: anexos del informe y copia de la muestra de Revolico.
- `Storytelling/README.md`: guion de presentación.
- `data/README.md`: inventario de `raw/` y `processed/`.
- `docs/README.md`: fuentes, metodología y journals.
- `evidencia/README.md`: propósito del directorio, actualmente vacío.
- `journals/README.md` y `src/README.md`: descripción de su contenido.

## Notas metodológicas

No hubo cambios en el procesamiento ni en el análisis: la encuesta, la codificación de variables y los resultados se mantienen. La actualización fue exclusivamente de estructura y documentación.

El análisis de la encuesta sigue en `docs/methodology/ANALISIS_POR_PREGUNTA_Y_RESPUESTAS.md`.
