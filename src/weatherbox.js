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
    let forecast = darkSky.getForecast(options);

    sendResponse(forecast, options, req, res);
});


app.get('/web/forecast/getCurrently', (req, res) => {
    let options = getQueries(req);
    let forecast = darkSky.getCurrentForecast(options);

    sendResponse(forecast, options, req, res);
});

app.get('/web/forecast/getMinutely', (req, res) => {
    let options = getQueries(req);
    let forecast = darkSky.getMinutelyForecast(options);

    sendResponse(forecast, options, req, res);
});

app.get('/web/forecast/getHourly', (req, res) => {
    let options = getQueries(req);
    let forecast = darkSky.getHourlyForecast(options);

    sendResponse(forecast, options, req, res);
});

app.get('/web/forecast/getDaily', (req, res) => {
    let options = getQueries(req);
    let forecast = darkSky.getDailyForecast(options);

    sendResponse(forecast, options, req, res);
});

app.get('/web/forecast/getAlerts', (req, res) => {
    let options = getQueries(req);
    let forecast = darkSky.getAlerts(options);

    sendResponse(forecast, options, req, res);
});

function getQueries(req) {
    return {
        location: req.query.location,
        langauge: req.query.language,
        units: req.query.units,
        extend: req.query.extend
    };
}

/**
 * TODO
 * 
 * @param {Promise} forecast resolves to requested forecast
 * @param {*} options request query fragments
 * @param {*} req http response
 * @param {*} res http request
 */
function sendResponse(forecast, options, req, res) {
    if (!options.location) {
        geolocation.geolocate(req.ip).then((geo) => {
            options.location = {
                latitude: geo.latitude,
                longitude: geo.longitude
            };

            forecast.then((forecast) => {
                res.send(forecast);
            });
        }).catch((er) => {
            console.log(er);
        });
    } else {
        forecast(options).then((forecast) => {
            res.send(forecast);
        });
    }
}

app.listen(port, '0.0.0.0', () => console.log(`WeatherBox listening on port ${port}`));