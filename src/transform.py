"""Transforma TODOS los CSV de data/raw/ y los une en una sola tabla.

Cada archivo de data/raw/ trae columnas con nombres distintos (algunos en español, otros en
inglés), así que este script les pone a todos los mismos nombres, convierte
precio y año a número, agrega el precio en dólares y guarda el resultado en
data/processed/, listo para hacer consultas con pandas.

Uso: python src/transform.py
"""
from pathlib import Path

import pandas as pd

# Carpeta del proyecto (un nivel arriba de la carpeta src/).
ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = ROOT / "data/raw"
OUTPUT_FILE = ROOT / "data/processed/unified_cars.csv"

# Columnas que va a tener la tabla final, en este orden.
COLUMNS = [
    "company", "seller_type", "channel", "brand", "model",
    "year", "price", "currency", "price_usd", "province", "source",
]

# Tasas informales del mercado cubano al 2026-10-25, en CUP por 1 unidad de
# cada moneda. Para pasar un precio a dólares: precio * tasa[moneda] / tasa["USD"].
EXCHANGE_RATE_TO_CUP = {
    "CUP": 1.00,
    "USD": 835.00,
    "EUR": 930.00,
    "MLC": 685.23,
    "CAD": 535.90,
    "MXN": 51.95,
    "ZELLE": 824.12,
    "CLA": 755.96,
}


def read_catalog(file_name: str) -> pd.DataFrame:
    """Lee un catálogo de concesionario (dongfeng, mcv o womy).

    Los tres traen exactamente las mismas columnas, solo que en español.
    """
    df = pd.read_csv(RAW_DIR / file_name, dtype=str)

    df["company"] = df["empresa"]
    df["seller_type"] = df["tipo_vendedor"]
    df["brand"] = df["marca"]
    df["model"] = df["modelo"]
    df["year"] = df["anio"]
    df["price"] = df["precio"]
    df["currency"] = df["moneda"]
    df["province"] = df["provincia"]
    df["channel"] = "formal"
    df["source"] = file_name

    return df


def read_revolico() -> pd.DataFrame:
    """Lee los anuncios de Revolico.

    Son siempre particulares vendiendo directamente, así que company y
    seller_type son el mismo texto para todas las filas.
    """
    file_name = "revolico_cars.csv"
    df = pd.read_csv(RAW_DIR / file_name, dtype=str)

    df["company"] = "Mercado informal (Revolico)"
    df["seller_type"] = "Particulares y revendedores"
    df["channel"] = "informal"
    df["brand"] = df["marca"]
    df["model"] = df["titulo"]
    df["price"] = df["precio"]
    df["currency"] = df["moneda"]
    df["province"] = df["provincia"]
    df["source"] = file_name

    # El año casi siempre está escrito dentro del título ("Hyundai Tucson 2019").
    # Se busca un número de 4 dígitos entre 1930 y 2029 para no confundirlo con
    # otros números del título (teléfonos, precios, etc.).
    df["year"] = df["titulo"].str.extract(r"\b(19[3-9]\d|20[0-2]\d)\b")

    return df


def clean_up(df: pd.DataFrame) -> pd.DataFrame:
    """Convierte precio y año a número, y limpia espacios sueltos en el texto."""
    df["price"] = pd.to_numeric(df["price"], errors="coerce")

    # "Int64" (con mayúscula) es un entero que admite vacíos. Así el año sale
    # como 1957 en el CSV final, y no como 1957.0.
    df["year"] = pd.to_numeric(df["year"], errors="coerce").astype("Int64")

    df["currency"] = df["currency"].str.strip().str.upper()
    for column in ["company", "seller_type", "brand", "model", "province"]:
        df[column] = df[column].str.strip()

    return df


def add_price_in_usd(df: pd.DataFrame) -> pd.DataFrame:
    """Agrega price_usd: el precio convertido a dólares según su moneda."""
    currency_rate = df["currency"].map(EXCHANGE_RATE_TO_CUP)
    usd_rate = EXCHANGE_RATE_TO_CUP["USD"]
    df["price_usd"] = (df["price"] * currency_rate / usd_rate).round(2)
    return df


def main() -> None:
    tables = [
        read_catalog("dongfeng_nwi_commercial.csv"),
        read_catalog("mcv_commercial_2026-03-03.csv"),
        read_catalog("womy_catalog_july_2026.csv"),
        read_catalog("bdcone_commercial.csv"),
        read_revolico(),
    ]

    df = pd.concat(tables, ignore_index=True)
    df = clean_up(df)
    df = add_price_in_usd(df)
    df = df[COLUMNS]  # se descartan las columnas en español que ya no hacen falta

    # Comprobación mínima: si esto falla, algo se rompió en la unión o la limpieza.
    assert len(df) > 0, "la tabla final quedó vacía"
    assert df["price_usd"].notna().any(), "ningún registro quedó con precio en dólares"

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT_FILE, index=False, encoding="utf-8")

    print(f"{len(df)} filas -> {OUTPUT_FILE}")
    print(df["company"].value_counts())


if __name__ == "__main__":
    main()
