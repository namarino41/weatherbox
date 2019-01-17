const express = require('express');
let darkSky = require('./darksky.js');
let darkSkyConfig = require('../config/darksky-config');
const app = express();

const port = 3000;

darkSky = new darkSky(darkSkyConfig);

app.get('/web/forecast', (req, res) => {
    const location = req.query.location;
    const language = req.query.language;
    const units = req.query.units;
    const extend = req.query.extend;

    if (!location) {
        res.sendStatus(400);
        return;
    }

    darkSky.getForecast(location, language, units, extend).then((forecast) => {
        res.send(forecast);
    });
});

app.get('/web/currently', (req, res) => {
    const language = req.query.language;
    const units = req.query.units;
    const extend = req.query.extend; 

    if (!location) {
        res.sendStatus(400);
        return;
    }

    darkSky.getCurrentForecast(lagnuage, units, extend).then((forecast) => {
        res.send(forecast);
    });
});

app.get('/web/minutely', (req, res) => {
    const language = req.query.language;
    const units = req.query.units;
    const extend = req.query.extend;

    if (!location) {
        res.sendStatus(400);
        return;
    }
    
    darkSky.getMinutelyForecast(lagnuage, units, extend).then((forecast) => {
        res.send(forecast);
    });
});

app.get('/web/hourly', (req, res) => {
    const language = req.query.language;
    const units = req.query.units;
    const extend = req.query.extend;

    if (!location) {
        res.sendStatus(400);
        return;
    }

    darkSky.getHourlyForecast(language, units, extend).then((forecast) => {
        res.send(forecast);
    });
});

app.get('/web/daily', (req, res) => {
    const language = req.query.language;
    const units = req.query.units;
    const extend = req.query.extend;

    if (!location) {
        res.sendStatus(400);
        return;
    }

    darkSky.getDailyForecast(language, units, extend).then((forecast) => {
        res.send(forecast);
    });
});

app.get('/web/alerts', (req, res) => {
    const language = req.query.language;
    const units = req.query.units;
    const extend = req.query.extend;

    if (!location) {
        res.sendStatus(400);
        return;
    }

    darkSky.getAlerts(language, units, extend).then((forecast) => {
        res.send(forecast);
    });
});

app.listen(port, () => console.log(`WeatherBox listening on port ${port}!`));