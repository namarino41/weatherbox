const rp = require('request-promise');

class DarkSky {
    constructor(config) {
        this.config = config;
    }
    
    /**
     * Requests the entire forecast, i.e 'current', 'minutely', 'hourly', 'daily'
     * 
     * @return {Promise} promise containing the entire forecast.
     */
    getForecast(options) {
        const request = new RequestBuilder(this.config)
            .location({latitude: 42.3601, longitude: -71.0589})
            .language(options.language)
            .units(options.units)
            .extend(options.extend)
            .build();
        
        return this._makeRequest(request);
    }

    /**
     * Requests only the 'currently' forecast.
     * 
     * @return {Promise} promise containing the 'currently' forecast.
     */
    getCurrentForecast(language = false, units = false, extend = false) {
        const request = new RequestBuilder(this.config)
            .location({latitude: 42.3601, longitude: -71.0589})
            .language(language)
            .units(units)
            .extend(extend)
            .exclude(['minutely', 'hourly', 'daily', 'alerts'])
            .build();
        
        return this._makeRequest(request);
    }

    /**
     * Requests only the 'minutely' forecast.
     * 
     * @return {Promise} promise containing the 'minutely' forecast.
     */
    getMinutelyForecast(language = false, units = false, extend = false) {
        const request = new RequestBuilder(this.config)
            .location({latitude: 42.3601, longitude: -71.0589})
            .language(language)
            .units(units)
            .extend(extend)
            .exclude(['currently', 'hourly', 'daily', 'alerts'])
            .build();

        return this._makeRequest(request);
    }

    /**
     * Requests only the 'hourly' forecast.
     * 
     * @return {Promise} promise containing the 'hourly' forecast.
     */
    getHourlyForecast(language = false, units = false, extend = false) {
        const request = new RequestBuilder(this.config)
            .location({latitude: 42.3601, longitude: -71.0589})
            .language(language)
            .units(units)
            .extend(extend)
            .exclude(['currently', 'minutely', 'daily', 'alerts'])
            .build();

        return this._makeRequest(request);
    }

    /**
     * Requests only the 'daily' forecast.
     * 
     * @return {Promise} promise containg the 'daily' forecast.
     */
    getDailyForecast(language = false, units = false, extend = false) {
        const request = new RequestBuilder(this.config)
            .location({latitude: 42.3601, longitude: -71.0589})
            .language(language)
            .units(units)
            .extend(extend)
            .exclude(['currently', 'minutely', 'hourly', 'alerts'])
            .build();

        return this._makeRequest(request);
    }

    /**
     * Requests only the 'alerts'.
     * 
     * @return {Promise} promise containing the 'alerts'.
     */
    getAlerts(language = false, units = false, extend = false) {
        const request = new RequestBuilder(this.config)
            .location({latitude: 42.3601, longitude: -71.0589})
            .language(language)
            .units(units)
            .extend(extend)
            .exclude(['currently', 'minutely', 'hourly', 'daily'])
            .build();
        
        return this._makeRequest(request);
    }

    /**
     * Makes a request to DarkSky web service and returns a promise
     * containing the desired forecast.                                    
     * @param {string} request the request URL.
     * 
     * @return {Promise} containing desired forecast.
     */
    _makeRequest(request) {
        const options = {
            uri: request,
            json: true
        }
        
        return rp(options);
    }
}

/**
 * Utility class for building DarkSky web requests.
 */
class RequestBuilder {
    constructor(config) {
        this.baseEndpoint = `${config.endpoint}${config.apiKey}`;
    }

    location(coordinates) {
        this.loc = `${coordinates.latitude},${coordinates.longitude}`;
        return this;
    }

    exclude(exclusions) {
        if (exclusions)
            this.excl = `?exclude=${exclusions.join(',')}`;
        return this;
    }

    extend(extend) {
        if (extend)
            this.ext = `?extend=${extend}`;
        return this;
    }

    language(language) {
        if (language) 
            this.lang = `?language=${language}`;
        return this;
    }

    units(units) {
        if (units)
            this.uni = `?units=${units}`;
        return this;
    }

    time(time) {
        if (time)
            this.tim = time;
        return this;
    }

    build() {
        let request = `${this.baseEndpoint}/${this.loc}`;
        let options = [];
        
        if (this.tim)
            options.push(this.tim);
        if (this.excl)
            options.push(this.excl);
        if (this.ext)
            options.push(this.ext);
        if (this.lang)
            options.push(this.lang);
        if (this.uni)
            options.push(this.uni);

        request = `${request}${options.join('&')}`;

        return request;
    }
}

module.exports = DarkSky;