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
- `evidencia/README.md`: propósito del directorio (en ese momento vacío).
- `journals/README.md` y `src/README.md`: descripción de su contenido.

## Notas metodológicas

No hubo cambios en el procesamiento ni en el análisis: la encuesta, la codificación de variables y los resultados se mantienen. La actualización fue exclusivamente de estructura y documentación.

El análisis de la encuesta sigue en `docs/methodology/ANALISIS_POR_PREGUNTA_Y_RESPUESTAS.md`.

## Actualización posterior (misma fecha)

### Nuevos cambios de documentación y fuentes

- Los catálogos PDF se consolidaron en `docs/fuentes/` (se eliminó `docs/pdf/`).
- Se añadieron `docs/fuentes/estadisticas ONEI.docx` y `docs/fuentes/estudio-mercado-automovil-componentes-cuba-2026-resumen.pdf`.
- La metodología quedó en `docs/methodology/Explicacion_pasos_seguidos_4_11_2026_metodologia_oficial_corregido.docx`; se eliminaron las versiones anteriores `Explicacion pasos seguidos.docx` e `INFORME_hoy.docx`.
- `evidencia/` ya contiene cuatro imágenes de WhatsApp del trabajo de campo; en ese momento su `README.md` aún decía que estaba vacío (corregido en la actualización siguiente).
- `Storytelling/Guion storytelling.docx` quedó ubicado dentro de `Storytelling/`.

### Pendiente

- Mantener actualizados los README cuando se añadan fuentes o resultados.
- Eliminar los temporales de Office que aún permanecen en `Anexos/` y `data/processed/`.

### Últimos ajustes (commits `48bcb6d` a `e74309e`)

- Se actualizó `evidencia/README.md` para reflejar las cuatro imágenes del trabajo de campo.
- Se eliminó el temporal `docs/methodology/~$plicacion_pasos_seguidos_4_11_2026_metodologia_oficial_corregido.docx`.
- Se añadieron a `docs/fuentes/` el libro `LIBRO_ESTUDIO_DE_MERCADO_VF (1).pdf` y el catálogo `vehiculos-comerciales-abril-2026.CRrY5k95.pdf`.
- Se añadieron a `docs/methodology/` el `Anexo_2_Cuestionario final_demanda_para form_google_.docx` y la `leyenda_para_respuestas del cuestionario.docx`.
- Se añadió el artículo de divulgación `Storytelling/Hay demanda de eléctricos en La Habana, pero el precio está lejos de quienes más.docx`.
- Se revisaron y actualizaron todos los `README.md` para reflejar el inventario actual.
