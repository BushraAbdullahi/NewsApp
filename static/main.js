
// listening for the webapge loading then executing the anonymous callback function
window.addEventListener('load', () => {
    
    var corner1 = L.latLng(-90, -180),
    corner2 = L.latLng(90, 180),
    bounds = L.latLngBounds(corner1, corner2);
    
    var map = L.map('map', {
        maxBounds: bounds,
        maxBoundsViscosity: 1.0
    }).setView([51.505, -0.09], 2);
    
    L.tileLayer('https://api.mapbox.com/styles/v1/bushra1175/ckvq0bfl17wv414mzlozg3po9/tiles/256/{z}/{x}/{y}@2x?access_token=pk.eyJ1IjoiYnVzaHJhMTE3NSIsImEiOiJja3ZweHk1YTA4OXJ0MnBxd215eng4aHc2In0.Gr8rimI7waYVpeDLbsGc3A', {
        attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
        maxZoom: 12,
        minZoom: 4,
        id: 'mapbox/streets-v11',
        tileSize: 512,
        zoomOffset: -1,
        accessToken: 'pk.eyJ1IjoiYnVzaHJhMTE3NSIsImEiOiJja3ZweHk1YTA4OXJ0MnBxd215eng4aHc2In0.Gr8rimI7waYVpeDLbsGc3A'
    }).addTo(map);


 
   fetch("/static/cities.json").then(response => response.json()).then(json => {
    cities = json;

    for(i = 0; i < 50; i++){

        const marker = L.marker(cities[i].location) 
        marker.bindTooltip(cities[i].name, {permanent: true, className: "city_label", offset: [0, 0] })
        marker.addTo(map);
    
    }

    });

    
})

