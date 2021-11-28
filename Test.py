import urllib.request, PIL, baniscii
print(type(urllib.request.urlopen("https://gadgets.buienradar.nl/gadget/zoommap/?lat=51.44083&lng=5.47778&overname=2&zoom=8&naam=eindhoven&size=3&voor=1").read()))
