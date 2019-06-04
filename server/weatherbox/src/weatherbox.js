/*
 * RPC API that handles client forecast requests.
 *
 * Base URL:
 *      http://[ip-address]:3000/
 * 
 * Subscription request:
 *      POST http://[ip-address]:3000/subscribe
 *      body: {
 *          location: {
 *              latitude: ...
 *              longitude: ...
 *          }    
 *          language: ...
 *          ...
 *      }    
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
 */

const express = require('express');
const bodyParser = require("body-parser");
let darkSky = require('./internal/lib/darksky.js');
let geolocation = require('./internal/lib/geolocation.js');
let darkSkyConfig = require('./internal/config/darksky-config.json');
let geoConfig = require('./internal/config/ipstack-config.json');
const uuidv1 = require('uuid/v1');
let {subscriptions, subscription} = require('./internal/lib/subscription-service.js');

const app = express();
app.use(bodyParser.json()); 
const port = 3000;

darkSky = new darkSky(darkSkyConfig);
geolocation = new geolocation(geoConfig);

/**
 * Registers the client and it's desired DarkSky parameters.
 */
app.post('/web/subscribe', async (req, res) => {
    const clientId = uuidv1();
    console.log(clientId)

    if (!subscriptions.clientId) {
        let parameters = req.body;
        console.log(req)

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
app.get('/web/getFull', async (req, res) => {
    const clientId = req.query.clientId;

    if (!subscriptions[clientId]) {
        res.sendStatus(400);
        return;
    }

    res.send(await darkSky.getFull(subscriptions[clientId].parameters));
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

    res.send(await darkSky.getCurrently(subscriptions[clientId].parameters));
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

    res.send(await darkSky.getMinutely(subscriptions[clientId].parameters));
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

    res.send(await darkSky.getHourly(subscriptions[clientId].parameters));
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

    res.send(await darkSky.getDaily(subscriptions[clientId].parameters));
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

app.listen(port, '0.0.0.0', () => {
    console.log(`WeatherBox listening on port ${port}`);
});