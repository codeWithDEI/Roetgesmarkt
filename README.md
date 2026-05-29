# Roetgesmarkt

This repository contains a GeoJSON file with geospatial data for the Roetgesmarkt.

## Contents

* `dorfflohmarkt_template.geojson`

  * Format: GeoJSON (`FeatureCollection`)
  * Each entry contains at least:

    * Geometry (`Point`)
    * Name/address
    * Visualization options from uMap

## Purpose

The file can be used for:

* Map visualization in uMap
* Import into GIS software such as QGIS
* Location analysis or documentation
* Further processing in custom applications

## Usage

### uMap

1. Create a new map in uMap
2. Select “Import data”
3. Upload the `.geojson` file

### QGIS

1. Open QGIS
2. Select “Add Layer” → “Add Vector Layer”
3. Choose the GeoJSON file

## Format

This repository uses the standardized GeoJSON format:

```json
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [lng, lat]
      },
      "properties": {
        "name": "Example address"
      }
    }
  ]
}
