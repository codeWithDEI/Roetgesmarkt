import json

INPUT_FILE = "roetgesmarkt_input.geojson"
OUTPUT_FILE = "roetgesmarkt_upload.geojson"


def looks_like_lat_lon(coords):
    """
    Heuristic check:
    In Germany:
    - Latitude is typically ~47–55
    - Longitude is typically ~5–15

    If first value looks like latitude and second like longitude,
    the pair is (lat, lon) and needs swapping.
    """
    if not isinstance(coords, list) or len(coords) != 2:
        return False

    first, second = coords

    return 45 <= first <= 60 and 5 <= second <= 15


def fix_feature(feature):
    geometry = feature.get("geometry")
    if not geometry:
        return feature

    coords = geometry.get("coordinates")

    # Only handle Point geometries
    if geometry.get("type") == "Point" and looks_like_lat_lon(coords):
        # Swap lat/lon → lon/lat
        geometry["coordinates"] = [coords[1], coords[0]]

    return feature


def main():
    with open(INPUT_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)

    if data.get("type") != "FeatureCollection":
        raise ValueError("Input must be a GeoJSON FeatureCollection")

    features = data.get("features", [])

    fixed_features = []
    for feature in features:
        fixed_features.append(fix_feature(feature))

    data["features"] = fixed_features

    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)

    print(f"Done. Uploadable GeoJSON saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()