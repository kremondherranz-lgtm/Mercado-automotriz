"""Lee la encuesta de mercado automotriz y renombra sus columnas a inglés.

Uso: python src/clean_survey.py
Salida: data/processed/survey.csv
"""

from pathlib import Path  # Permite construir rutas de archivos de forma portable.
import pandas as pd  # Importa pandas, la librería para leer y transformar tablas.

ROOT = Path(__file__).resolve().parent.parent  # Calcula la carpeta raíz del proyecto.
RAW_FILE = ROOT / "data/raw/ESTUDIO DEL MERCADO AUTOMOTRIZ EN LA HABANA (respuestas) - Respuestas de formulario 1 (1).csv"  # Ruta del CSV original.
OUTPUT_FILE = ROOT / "data/processed/survey.csv"  # Ruta donde se guarda el CSV transformado.

COLUMN_MAP = {  # Diccionario que traduce cada columna original a un nombre corto en inglés.
    "Marca temporal": "timestamp",  # Fecha y hora en que se llenó el formulario.
    "Consentimiento informado: \"Esta encuesta es anónima, sus datos se usarán solo con fines de estudio de la investigación de la asignatura. ¿Acepta participar?\"": "consent",  # Aceptación del consentimiento informado.
    "¿Cuál es su edad?": "age",  # Edad del encuestado.
    "Sexo": "sex",  # Sexo del encuestado.
    "¿En qué trabaja?": "occupation",  # Actividad u ocupación laboral.
    "¿Qué tiempo lleva ejerciendo la actividad o en el trabajo actual?": "work_tenure",  # Tiempo en el trabajo actual.
    "¿Cuántas personas viven con usted?": "household_size",  # Cantidad de personas en el hogar.
    "¿Cuántos vehículos posee su hogar en total?": "household_cars",  # Cantidad de vehículos del hogar.
    "Tipo de combustible que utiliza su vehículo": "fuel_type",  # Combustible del vehículo actual.
    "¿Cuántos años tiene su vehículo?": "vehicle_age",  # Antigüedad del vehículo actual.
    "¿Cuántos pasajeros se desplazan con usted o tendría que desplazar en el futuro si adquiere un vehículo?": "passengers",  # Pasajeros que se desplazan con el encuestado.
    "¿Cuenta con parqueo propio?": "has_parking",  # Indica si tiene parqueo propio.
    "¿A dónde va habitualmente?": "destinations",  # Lugares a los que suele ir.
    "¿Cómo se traslada cada día?": "transport_mode",  # Medios de transporte que usa a diario.
    "¿Cuántos kilómetros recorre al día aproximadamente?": "daily_km",  # Kilómetros recorridos por día.
    "¿Su actividad diaria le requiere movilizarse con familiares, mercancías o clientes? (seleccione el mas necesario para usted?": "mobility_need",  # Necesidad principal de movilidad.
    "¿Le interesaría comprar un vehículo en el futuro?": "buy_interest",  # Interés en comprar un vehículo.
    "¿Cuál sería su preferencia de tipo de vehículo?": "vehicle_type",  # Tipo de vehículo preferido.
    "¿Lo prefiere nuevo o de uso?": "condition",  # Preferencia entre vehículo nuevo o usado.
    "El vehículo actual o del que desearía adquirir: ¿Cuántas puertas prefiere? [Actual]": "doors_current",  # Puertas del vehículo actual.
    "El vehículo actual o del que desearía adquirir: ¿Cuántas puertas prefiere? [Preferencia]": "doors_pref",  # Puertas del vehículo deseado.
    "¿Qué uso le daría?": "use_case",  # Uso que le daría al vehículo.
    "¿Se ha fijado en algún modelo?": "model_interest",  # Indica si ya tiene un modelo en mente.
    "¿Qué le preocupa de adquirir un vehículo de combustión? (Enumere por orden de importancia, en escala de 1 a 5, donde 1 es 'menos importante' y 5 es 'muy importante') [Consumo de combustible]": "comb_fuel",  # Preocupación por el consumo de combustible.
    "¿Qué le preocupa de adquirir un vehículo de combustión? (Enumere por orden de importancia, en escala de 1 a 5, donde 1 es 'menos importante' y 5 es 'muy importante') [La importación]": "comb_import",  # Preocupación por la importación de un vehículo de combustión.
    "¿Qué le preocupa de adquirir un vehículo de combustión? (Enumere por orden de importancia, en escala de 1 a 5, donde 1 es 'menos importante' y 5 es 'muy importante') [Los impuestos a pagar]": "comb_taxes",  # Preocupación por los impuestos de un vehículo de combustión.
    "¿Qué le preocupa de adquirir un vehículo de combustión? (Enumere por orden de importancia, en escala de 1 a 5, donde 1 es 'menos importante' y 5 es 'muy importante') [Aprender a manejarlo]": "comb_driving",  # Preocupación por aprender a manejar un vehículo de combustión.
    "¿Qué le preocupa de adquirir un vehículo de combustión? (Enumere por orden de importancia, en escala de 1 a 5, donde 1 es 'menos importante' y 5 es 'muy importante') [Costo de las piezas y mantenimientos]": "comb_parts",  # Preocupación por piezas y mantenimiento de un vehículo de combustión.
    "¿Qué le preocupa de adquirir un vehículo eléctrico o híbrido? (Enumere por orden de importancia, en escala de 1 a 5, donde 1 es 'menos importante' y 5 es 'muy importante') [Cuántos kilómetros recorre (autonomía)]": "ev_range",  # Preocupación por la autonomía de un vehículo eléctrico o híbrido.
    "¿Qué le preocupa de adquirir un vehículo eléctrico o híbrido? (Enumere por orden de importancia, en escala de 1 a 5, donde 1 es 'menos importante' y 5 es 'muy importante') [Dónde cargarlo]": "ev_charging",  # Preocupación por los lugares de carga.
    "¿Qué le preocupa de adquirir un vehículo eléctrico o híbrido? (Enumere por orden de importancia, en escala de 1 a 5, donde 1 es 'menos importante' y 5 es 'muy importante') [La importación]": "ev_import",  # Preocupación por la importación de un vehículo eléctrico o híbrido.
    "¿Qué le preocupa de adquirir un vehículo eléctrico o híbrido? (Enumere por orden de importancia, en escala de 1 a 5, donde 1 es 'menos importante' y 5 es 'muy importante') [Costo de baterías y mantenimientos]": "ev_battery",  # Preocupación por baterías y mantenimiento de un vehículo eléctrico o híbrido.
    "¿Qué le preocupa de adquirir un vehículo eléctrico o híbrido? (Enumere por orden de importancia, en escala de 1 a 5, donde 1 es 'menos importante' y 5 es 'muy importante') [Aprender a manejarlo]": "ev_driving",  # Preocupación por aprender a manejar un vehículo eléctrico o híbrido.
    "¿Qué le atrae para comprar un vehículo eléctrico o híbrido?": "ev_appeal",  # Motivos que atraen la compra de un vehículo eléctrico o híbrido.
    "En caso de interés por un vehículo eléctrico: ¿Qué autonomía mínima del vehículo prefiere (En km)?": "ev_min_range_km",  # Autonomía mínima deseada en kilómetros.
    "Teniendo en cuenta la escasez y el precio de los combustibles, sumado a la situación electro energética, ¿preferiría comprar un vehículo eléctrico con panel solar incluido?": "ev_solar_panel",  # Preferencia por un vehículo eléctrico con panel solar.
    "¿Estaría dispuesto a comprar un vehículo en los próximos meses?": "buy_soon",  # Disposición a comprar en los próximos meses.
    "En el caso de vehículos de combustible: ¿En qué plazos estaría dispuesto a pagar?": "pay_terms_comb",  # Plazos de pago para un vehículo de combustión.
    "En el caso de vehículos eléctricos: ¿En qué plazos estaría dispuesto a pagar?": "pay_terms_ev",  # Plazos de pago para un vehículo eléctrico.
    "En el caso de vehículos de combustible ¿Cuánto estaría dispuesto a pagar (USD)?": "budget_comb_usd",  # Presupuesto en USD para un vehículo de combustión.
    "En el caso de vehículos eléctricos: ¿Cuánto estaría dispuesto a pagar (USD)?": "budget_ev_usd",  # Presupuesto en USD para un vehículo eléctrico.
    "¿Es usted la persona que decide las compras de vehículos en su casa?": "decision_maker",  # Indica si decide las compras de vehículos en su hogar.
    "¿Qué lo haría desistir de la compra de un vehículo?": "purchase_barrier",  # Motivos que lo harían desistir de la compra.
    "En el caso de vehículos eléctricos: ¿Dónde piensa cargarlo?": "charge_place",  # Lugar previsto para cargar un vehículo eléctrico.
    "¿Por qué medio prefiere recibir información sobre ofertas de vehículo?": "info_channel",  # Medio preferido para recibir ofertas.
    "En el caso de las redes sociales: ¿Cuál de ellas?": "social_network",  # Red social preferida para recibir información.
    "¿Qué modelo?": "preferred_model",  # Modelo de vehículo que prefiere.
}


def load_survey() -> pd.DataFrame:  # Define la función que carga y transforma la encuesta.
    df = pd.read_csv(RAW_FILE, dtype=str, encoding="utf-8-sig")  # Lee el CSV como texto y elimina el BOM del primer encabezado.
    df.columns = [column.strip() for column in df.columns]  # Quita espacios sobrantes en los nombres de las columnas.
    missing = [column for column in COLUMN_MAP if column not in df.columns]  # Busca columnas esperadas que no estén en el archivo.
    if missing:  # Comprueba si faltó alguna columna.
        raise ValueError(f"Faltan columnas en el CSV: {missing}")  # Detiene la ejecución si el archivo no coincide con lo esperado.
    df = df.rename(columns=COLUMN_MAP)  # Aplica el diccionario para dejar los nombres en inglés y cortos.
    df = df.apply(lambda column: column.str.strip())  # Quita espacios al inicio y al final de cada celda de texto.
    return df  # Devuelve la tabla ya transformada.


def main() -> None:  # Define la función principal del script.
    df = load_survey()  # Carga y transforma la encuesta.
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)  # Crea la carpeta data/processed/ si no existe.
    df.to_csv(OUTPUT_FILE, index=False, encoding="utf-8")  # Guarda el resultado sin el índice de pandas.
    print(f"{len(df)} filas y {len(df.columns)} columnas -> {OUTPUT_FILE}")  # Muestra el resumen de la tabla generada.
    print(", ".join(df.columns))  # Muestra las nuevas columnas en inglés.


if __name__ == "__main__":  # Comprueba que el archivo se ejecute directamente y no se importe.
    main()  # Ejecuta la función principal.
