const rp = require('request-promise');

/**
 * Client interface for making forecast requests to DarkSky.net.
 */
class DarkSky {
    constructor(config) {
        this.config = config;
    }
    
    /**
     * Requests the entire forecast, i.e 'current', 'minutely', 'hourly', 'daily'
     * 
     * @return {Promise} promise containing the entire forecast.
     */
    getFull(parameters) {
        const request = new RequestBuilder(this.config)
            .location(parameters.location)
            .language(parameters.language)
            .units(parameters.units)
            .extend(parameters.extend)
            .build();

        console.log(request);

        return this._makeRequest(request);
    }

    /**
     * Requests only the 'currently' forecast.
     * 
     * @return {Promise} promise containing the 'currently' forecast.
     */
    getCurrently(parameters) {
        const request = new RequestBuilder(this.config)
            .location(parameters.location)
            .language(parameters.language)
            .units(parameters.units)
            .extend(parameters.extend)
            .exclude(['minutely', 'hourly', 'daily', 'alerts'])
            .build();
        
        return this._makeRequest(request);
    }

    /**
     * Requests only the 'minutely' forecast.
     * 
     * @return {Promise} promise containing the 'minutely' forecast.
     */
    getMinutely(parameters) {
        const request = new RequestBuilder(this.config)
            .location(parameters.location)    
            .language(parameters.language)
            .units(parameters.units)
            .extend(parameters.extend)
            .exclude(['currently', 'hourly', 'daily', 'alerts'])
            .build();

        return this._makeRequest(request);
    }

    /**
     * Requests only the 'hourly' forecast.
     * 
     * @return {Promise} promise containing the 'hourly' forecast.
     */
    getHourly(parameters) {
        const request = new RequestBuilder(this.config)
            .location(parameters.location)
            .language(parameters.language)
            .units(parameters.units)
            .extend(parameters.extend)
            .exclude(['currently', 'minutely', 'daily', 'alerts'])
            .build();

        return this._makeRequest(request);
    }

    /**
     * Requests only the 'daily' forecast.
     * 
     * @return {Promise} promise containg the 'daily' forecast.
     */
    getDaily(parameters) {
        const request = new RequestBuilder(this.config)
            .location(parameters.location)
            .language(parameters.language)
            .units(parameters.units)
            .extend(parameters.extend)
            .exclude(['currently', 'minutely', 'hourly', 'alerts'])
            .build();

        return this._makeRequest(request);
    }

    /**
     * Requests only the 'alerts'.
     * 
     * @return {Promise} promise containing the 'alerts'.
     */
    getAlerts(parameters) {
        const request = new RequestBuilder(this.config)
            .location(parameters.location)
            .language(parameters.language)
            .units(parameters.units)
            .extend(parameters.extend)
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

    location(location) {
        this.loc = `${location.latitude},${location.longitude}`;
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
        let parameters = [];
        
        if (this.tim)
            parameters.push(this.tim);
        if (this.excl)
            parameters.push(this.excl);
        if (this.ext)
            parameters.push(this.ext);
        if (this.lang)
            parameters.push(this.lang);
        if (this.uni)
            parameters.push(this.uni);

        request = `${request}${parameters.join('&')}`;

        return request;
    }
}

module.exports = DarkSky;