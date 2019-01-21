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
const bodyParser = require("body-parser");
let darkSky = require('./internal/darksky.js');
let geolocation = require('./internal/geolocation.js');
let darkSkyConfig = require('../config/darksky-config');
let geoConfig = require('../config/ipstack-config.json');
const uuidv1 = require('uuid/v1');
let {subscriptions, subscription} = require('./internal/subscription-service.js');

const app = express();
app.use(bodyParser.json()); 
const port = 3000;

darkSky = new darkSky(darkSkyConfig);
geolocation = new geolocation(geoConfig);

/**
 * 
 */
app.post('/web/subscribe', async (req, res) => {
    const clientId = uuidv1();

    if (!subscriptions.clientId) {
        let parameters = req.body;

        if (!parameters.location) {
            let geo = await geolocation.geolocate(req.ip);
        
            parameters.location = {
                latitude: geo.latitude,
                longitude: geo.longitude
            }
        }
        subscriptions[clientId] = new subscription(clientId, parameters);
    }

    res.send(clientId);
});

/**
 * Gets the entire forecast.     
 */
app.get('/web/getForecast', async (req, res) => {
    const clientId = req.query.clientId;

    if (!subscriptions[clientId]) {
        res.sendStatus(400);
        return;
    }

    res.send(await darkSky.getForecast(subscriptions[clientId].parameters));
});

/**
 * Gets only the current forecast.
 */
app.get('/web/getCurrently', async (req, res) => {
    const clientId = req.query.clientId;

    if (!subscriptions[clientId]) {
        res.sendStatus(400);
        return;
    }

    res.send(await darkSky.getForecast(subscriptions[clientId].parameters));
});

/**
 * Gets only the minute-by-minute forecast.
 */
app.get('/web/getMinutely', async (req, res) => {
    const clientId = req.query.clientId;

    if (!subscriptions[clientId]) {
        res.sendStatus(400);
        return;
    }

    res.send(await darkSky.getMinutelyForecast(subscriptions[clientId].parameters));
});

/**
 * Gets only the hour-by-hour forecast.
 */
app.get('/web/getHourly', async (req, res) => {
    const clientId = req.query.clientId;

    if (!subscriptions[clientId]) {
        res.sendStatus(400);
        return;
    }

    res.send(await darkSky.getHourlyForecast(subscriptions[clientId].parameters));
});

/**
 * Gets only the daily forecast.
 */
app.get('/web/getDaily', async (req, res) => {
    const clientId = req.query.clientId;

    if (!subscriptions[clientId]) {
        res.sendStatus(400);
        return;
    }

    res.send(await darkSky.getDailyForecast(subscriptions[clientId].parameters));
});

/**
 * Gets only the alerts.
 */
app.get('/web/getAlerts', async (req, res) => {
    const clientId = req.query.clientId;

    if (!subscriptions[clientId]) {
        res.sendStatus(400);
        return;
    }

    res.send(await darkSky.getAlerts(subscriptions[clientId].parameters));
});

/**
 * Extracts parameters from the http request.
 * 
 * @param {object} request http request.
 * 
 * @return an object containing the parameters from req.
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