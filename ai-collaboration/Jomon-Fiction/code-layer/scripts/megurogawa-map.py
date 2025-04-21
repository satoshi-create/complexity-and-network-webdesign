import folium

features = [
  {
    "name": "Meguro Fudo Site",
    "type": "archaeological site",
    "coords": [
      35.6346,
      139.7144
    ]
  },
  {
    "name": "Shinagawa Shrine",
    "type": "shrine",
    "coords": [
      35.6073,
      139.7381
    ]
  },
  {
    "name": "Omori Shell Mound",
    "type": "shell mound",
    "coords": [
      35.5869,
      139.7343
    ]
  },
  {
    "name": "Isarago Shell Mound",
    "type": "shell mound",
    "coords": [
      35.6423,
      139.7384
    ]
  },
  {
    "name": "Hikawa Site",
    "type": "archaeological site",
    "coords": [
      35.6514,
      139.6876
    ]
  },
  {
    "name": "Enyuji Site",
    "type": "archaeological site",
    "coords": [
      35.6216,
      139.6937
    ]
  }
]

m = folium.Map(location=[35.63, 139.72], zoom_start=13)

for f in features:
    folium.Marker(
        location=f["coords"],
        popup=f"{f['name']} ({f['type']})",
        icon=folium.Icon(color="blue", icon="info-sign")
    ).add_to(m)

m.save("megurogawa-jomon-map.html")
print("Map saved as megurogawa-jomon-map.html")
