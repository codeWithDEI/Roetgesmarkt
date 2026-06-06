# Roetgesmarkt GeoJSON Tools

This repository contains a small utility for preparing location data for the Roetgesmarkt map.

The workflow starts with a manually maintained GeoJSON file where coordinates may have been copied from OpenStreetMap in `latitude, longitude` order. The included Python script converts the data into a standards-compliant GeoJSON export (`longitude, latitude`), removes generated IDs, and creates a CSV file that can be imported into Google My Maps.

## Repository Structure

- `roetgesmarkt_input.geojson`
  - Source data maintained by hand.
  - May contain coordinates in `lat, lon` order.

- `transform_lat_long.py`
  - Validates and transforms the GeoJSON.
  - Swaps coordinates when required.
  - Removes generated feature IDs.
  - Exports a Google My Maps compatible CSV.

- `roetgesmarkt_upload.geojson`
  - Generated GeoJSON ready for import into mapping tools.

- `roetgesmarkt_upload_google_maps.csv`
  - Generated CSV for Google My Maps imports.

## Features

The transformation script performs the following steps:

1. Loads a GeoJSON `FeatureCollection`.
2. Detects point coordinates that appear to be stored as `latitude, longitude`.
3. Converts them to the GeoJSON standard `longitude, latitude` order.
4. Removes existing `id` fields from features.
5. Writes a cleaned GeoJSON export.
6. Creates a CSV export with:
   - Name
   - Latitude
   - Longitude

## Coordinate Detection

The script uses a heuristic optimized for locations in Germany:

- Latitude: approximately `47–55`
- Longitude: approximately `5–15`

If a coordinate pair matches the pattern:

```text
[latitude, longitude]
```

it is automatically converted to:

```text
[longitude, latitude]
```

## Requirements

- Python 3.9+

No external dependencies are required.

## Usage

Run the transformation:

```bash
python transform_lat_long.py
```

Generated files:

```text
roetgesmarkt_upload.geojson
roetgesmarkt_upload_google_maps.csv
```

## Import into uMap

1. Create a new map in uMap.
2. Select **Import Data**.
3. Upload `roetgesmarkt_upload.geojson`.

## Import into Google My Maps

1. Create or open a map in Google My Maps.
2. Choose **Import**.
3. Upload `roetgesmarkt_upload_google_maps.csv`.
4. Select:
   - Latitude → `Latitude`
   - Longitude → `Longitude`
5. Use `Name` as the label column.

## GeoJSON Output Format

```json
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [7.123456, 52.123456]
      },
      "properties": {
        "name": "Example Location"
      }
    }
  ]
}
```
