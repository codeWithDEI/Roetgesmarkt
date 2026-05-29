# Roetgesmarkt

Dieses Repository enthält eine GeoJSON-Datei mit Geodaten zum Rötgesmarkt.

## Inhalt

* `dorfflohmarkt_template.geojson`

  * Format: GeoJSON (`FeatureCollection`)
  * Jeder Eintrag besitzt mindestens:

    * Geometrie (`Point`)
    * Name/Adresse
    * Darstellungsoptionen aus uMap

## Verwendungszweck

Die Datei kann beispielsweise verwendet werden für:

* Kartenvisualisierung in uMap
* Import in GIS-Software wie QGIS
* Analyse oder Dokumentation von Standorten
* Weiterverarbeitung in eigenen Anwendungen

## Verwendung

### uMap

1. Neue Karte in uMap erstellen
2. „Import data“ auswählen
3. Die `.geojson` Datei hochladen

### QGIS

1. QGIS öffnen
2. „Layer hinzufügen“ → „Vektorlayer hinzufügen“
3. GeoJSON-Datei auswählen

## Format

Das Repository nutzt das standardisierte GeoJSON-Format:

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
        "name": "Beispieladresse"
      }
    }
  ]
}
```

## Hinweise

* Die Datei wurde für Karten-/Standortdarstellung erstellt.
* Änderungen können direkt mit einem Texteditor, GIS-Werkzeugen oder uMap vorgenommen werden.
* Das Repository enthält aktuell ausschließlich die GeoJSON-Daten.
