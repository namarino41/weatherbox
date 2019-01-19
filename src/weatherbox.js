const express = require('express');
let darkSky = require('./darksky.js');
let geolocation = require('./geolocation.js');
let darkSkyConfig = require('../config/darksky-config');
let geoConfig = require('../config/ipstack-config.json');

const app = express();
const port = 3000;

darkSky = new darkSky(darkSkyConfig);
geolocation = new geolocation(geoConfig);

app.get('/web/forecast/getForecast', (req, res) => {
    let options = getQueries(req);

    if (!options.location) {
        geolocation.geolocate(req.ip).then((geo) => {
            options.location = {
                latitude: geo.latitude,
                longitude: geo.longitude
            };

            darkSky.getForecast(options).then((forecast) => {
                res.send(forecast);
            });
        });
    } else {
        darkSky.getForecast(options).then((forecast) => {
            res.send(forecast);
        });
    }
});


app.get('/web/forecast/getCurrently', (req, res) => {
    let options = getQueries(req);

    if (!options.location) {
        geolocation.geolocate(req.ip).then((geo) => {
            options.location = {
                latitude: geo.latitude,
                longitude: geo.longitude
            };

            darkSky.getCurrentForecast(options).then((forecast) => {
                res.send(forecast);
            });
        });
    } else {
        darkSky.getCurrentForecast(options).then((forecast) => {
            res.send(forecast);
        });
    }
});

app.get('/web/forecast/getMinutely', (req, res) => {
    let options = getQueries(req);

    if (!options.location) {
        geolocation.geolocate(req.ip).then((geo) => {
            options.location = {
                latitude: geo.latitude,
                longitude: geo.longitude
            };

            darkSky.getMinutelyForecast(options).then((forecast) => {
                res.send(forecast);
            });
        });
    } else {
        darkSky.getMinutelyForecast(options).then((forecast) => {
            res.send(forecast);
        });
    }
});

app.get('/web/forecast/getHourly', (req, res) => {
    let options = getQueries(req);

    if (!options.location) {
        geolocation.geolocate(req.ip).then((geo) => {
            options.location = {
                latitude: geo.latitude,
                longitude: geo.longitude
            };

            darkSky.getHourlyForecast(options).then((forecast) => {
                res.send(forecast);
            });
        });
    } else {
        darkSky.getHourlyForecast(options).then((forecast) => {
            res.send(forecast);
        });
    }
});

app.get('/web/forecast/getDaily', (req, res) => {
    let options = getQueries(req);

    if (!options.location) {
        geolocation.geolocate(req.ip).then((geo) => {
            options.location = {
                latitude: geo.latitude,
                longitude: geo.longitude
            };

            darkSky.getDailyForecast(options).then((forecast) => {
                res.send(forecast);
            });
        });
    } else {
        darkSky.getDailyForecast(options).then((forecast) => {
            res.send(forecast);
        });
    }
});

app.get('/web/forecast/getAlerts', (req, res) => {
    let options = getQueries(req);

    if (!options.location) {
        geolocation.geolocate(req.ip).then((geo) => {
            options.location = {
                latitude: geo.latitude,
                longitude: geo.longitude
            };

            darkSky.getAlerts(options).then((forecast) => {
                res.send(forecast);
            });
        });
    } else {
        darkSky.getAlerts(options).then((forecast) => {
            res.send(forecast);
        });
    }
});

function getQueries(req) {
    return {
        location: {
            latitude: req.query.latitude,
            longitude: req.query.longitude
        },
        language: req.query.language,
        units: req.query.units,
        extend: req.query.extend
    };
}

// /**
//  * TODO
//  * 
//  * @param {Promise} forecast resolves to requested forecast
//  * @param {Object} options request query fragments
//  * @param {Object} req http response
//  * @param {Object} res http request
//  */
// function sendResponse(forecast, options, req, res) {
//     if (!options.location) {
//         geolocation.geolocate(req.ip).then((geo) => {
//             options.location = {
//                 latitude: geo.latitude,
//                 longitude: geo.longitude
//             };

//             forecast.then((forecast) => {
//                 res.send(forecast);
//             });
//         }).catch((er) => {
//             console.log(er);
//         });
//     } else {
//         forecast(options).then((forecast) => {
//             res.send(forecast);
//         });
//     }
// }

app.listen(port, '0.0.0.0', () => console.log(`WeatherBox listening on port ${port}`));