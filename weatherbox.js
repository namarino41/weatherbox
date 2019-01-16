const express = require('express');
const app = express();
const port = 3000;

let darkSky = require('./darksky.js');

// todo: figure out a better place to put this later.
const darkSkyConfig = {
    endpoint: 'https://api.darksky.net/forecast/',
    apiKey: '928831417a19ef3bfae5a3f103c9a8f4',
}

darkSky = new darkSky(darkSkyConfig);

app.get('/internet/forecast', (req, res) => {
    darkSky.getForecast().then((forecast) => {
        res.send(forecast);
    });
});

app.get('/internet/currently', (req, res) => {
    darkSky.getCurrentForecast().then((forecast) => {
        res.send(forecast);
    });
});

app.get('/internet/currently', (req, res) => {
    darkSky.getCurrentForecast().then((forecast) => {
        res.send(forecast);
    });
});

app.listen(port, () => console.log(`WeatherBox listening on port ${port}!`));