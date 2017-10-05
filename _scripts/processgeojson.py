import json

with open('data/visited.geojson') as data_file:    
    data = json.load(data_file)
for feature in data['features']:
    try:
        #print feature
        lon = feature['geometry']['coordinates'][0]
        lat = feature['geometry']['coordinates'][1]
        title = feature['properties']['name']
        year = feature['properties'].get('string',"")
        description = feature['properties']['description']
        f = open("_travel/"+title+".md","w")
#{u'geometry': {u'type': u'Point', u'coordinates': [-57.9688024520874, -31.38702238295994, 0]}, u'type': u'Feature', u'properties': {u'name': u'Salto', u'string': u'Abroad', u'description': u'This is where we lived during our time in Salto\n\nUruguay 533'}}
        f.write("""---
title: "%s"
layout: travel
datePosted: %s
photo: "/travel/image.jpg"
location:
  lat: %2f
  lng: %2f
---
# %s

%s
""" % (title, year, lat, lon, title, description))
        f.close()
    except Exception as e:
        print e
        print feature
