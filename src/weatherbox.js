/*
 * RPC API that handles client forecast requests.
 *
 * Base URL:
 *      http://[ip-address]:3000/
 * 
 * Web forecast requests:
 *      - Full forecast:
 *          
 *      - Current forecast:
 * 
 *      - Minutely forecast:
 * 
 *      - Hourly forecast:
 * 
 *      - Daily forecast:
 * 
 * Parameters: 
 *      - location (optional): location weather request
 *          e.g. ?latitude=<latitude>&latitude=<latitude>
 *      - language (optional): language of response; english by default
 *          e.g. ?language=<language code>
 *      - units (optional): units of response; imperial by default
 *          e.g. ?units=<units code>
 *      - extend (optional): extend hourly forecast
 *          e.g. ?extend=<true/false>
 */

const express = require('express');
let darkSky = require('./darksky.js');
let geolocation = require('./geolocation.js');
let darkSkyConfig = require('../config/darksky-config');
let geoConfig = require('../config/ipstack-config.json');

const app = express();
const port = 3000;

darkSky = new darkSky(darkSkyConfig);
geolocation = new geolocation(geoConfig);

/**
 * Gets the entire forecast.     
 */
app.get('/web/getForecast', async (req, res) => {
    let parameters = getParameters(req);

    if (!parameters.location) {
        let geo = await geolocation.geolocate(req.ip);
        
        parameters.location = {
            latitude: geo.latitude,
            longitude: geo.longitude
        }
    }

    res.send(await darkSky.getForecast(parameters));
});

/**
 * Gets only the current forecast.
 */
app.get('/web/getCurrently', (req, res) => {
    let parameters = getParameters(req);

    if (!parameters.location) {
        let geo = await geolocation.geolocate(req.ip);
        
        parameters.location = {
            latitude: geo.latitude,
            longitude: geo.longitude
        }
    }

    res.send(await darkSky.getCurrentForecast(parameters));
});

/**
 * Gets only the minute-by-minute forecast.
 */
app.get('/web/getMinutely', (req, res) => {
    let parameters = getParameters(req);

    if (!parameters.location) {
        let geo = await geolocation.geolocate(req.ip);
        
        parameters.location = {
            latitude: geo.latitude,
            longitude: geo.longitude
        }
    }

    res.send(await darkSky.getMinutelyForecast(parameters));
});

/**
 * Gets only the hour-by-hour forecast.
 */
app.get('/web/getHourly', (req, res) => {
    let parameters = getParameters(req);

    if (!parameters.location) {
        let geo = await geolocation.geolocate(req.ip);
        
        parameters.location = {
            latitude: geo.latitude,
            longitude: geo.longitude
        }
    }

    res.send(await darkSky.getHourlyForecast(parameters));
});

/**
 * Gets only the daily forecast.
 */
app.get('/web/getDaily', (req, res) => {
    let parameters = getParameters(req);

    if (!parameters.location) {
        let geo = await geolocation.geolocate(req.ip);
        
        parameters.location = {
            latitude: geo.latitude,
            longitude: geo.longitude
        }
    }

    res.send(await darkSky.getDailyForecast(parameters));
});

/**
 * Gets only the alerts.
 */
app.get('/web/getAlerts', (req, res) => {
    let parameters = getParameters(req);

    if (!parameters.location) {
        let geo = await geolocation.geolocate(req.ip);
        
        parameters.location = {
            latitude: geo.latitude,
            longitude: geo.longitude
        }
    }

    res.send(await darkSky.getAlerts(parameters));

    // let options = getQueries(req);

    // if (!options.location) {
    //     geolocation.geolocate(req.ip).then((geo) => {
    //         options.location = {
    //             latitude: geo.latitude,
    //             longitude: geo.longitude
    //         };

    //         darkSky.getAlerts(options).then((forecast) => {
    //             res.send(forecast);
    //         });
    //     });
    // } else {
    //     darkSky.getAlerts(options).then((forecast) => {
    //         res.send(forecast);
    //     });
    // }
});

/**
 * Extracts queries from the http request.
 * 
 * @param {object} request http request.
 * 
 * @return an object containing the queries from req.
 */
function getParameters(request) {
    // TODO: find a cleaner way to do this
    return {
        location: !request.query.location ? undefined : {
            latitude: request.query.latitude,
            longitude: request.query.longitude
        },
        language: request.query.language,
        units: request.query.units,
        extend: request.query.extend
    };
}

app.listen(port, '0.0.0.0', () => {
    console.log(`WeatherBox listening on port ${port}`);
});