# Rasterio

Učni notebook v slovenščini za delo z rastri v Pythonu s knjižnico [rasterio](https://rasterio.readthedocs.io/). Primeri so narejeni na podatkih najdišča Pivola.

## Vsebina

- odpiranje in prikaz rastra (DEM, SLRM)
- pretvorba med koordinatami pikslov in prostorskimi koordinatami
- RGB kompozit iz Sentinel-2 kanalov
- shranjevanje rastra
- preprojekcija v EPSG:3794
- izrez rastra z vektorskim slojem

## Zagon

```bash
pip install rasterio numpy geopandas pyproj matplotlib jupyterlab
jupyter lab rasterio.ipynb
```

## Podatki

| Datoteka | Opis | Vir |
|---|---|---|
| `Pivola.tif` | DEM, 0,5 m, EPSG:3794 | LiDAR, [ARSO](https://gis.arso.gov.si/evode/) |
| `Pivola_SLRM_R20.tif` | Simple Local Relief Model (polmer 20), izračunan iz DEM-a | lastna obdelava |
| `Browser_images/*.tiff` | Sentinel-2 L2A, kanali B02, B03, B04, B08, 6. 10. 2026 | [Copernicus Browser](https://browser.dataspace.copernicus.eu/) |
| `Pivola.gpkg` | vektorski sloj poligonov za izrez | lastna izdelava |

Datoteke `kompozit.tif`, `prerpojektiran.tif` in `izrez.tif` nastanejo ob zagonu notebooka.

## Viri

- Vsebuje spremenjene podatke Copernicus Sentinel (2026).
- LiDAR podatki: Agencija Republike Slovenije za okolje (ARSO).
