const rp = require('request-promise');
const publicIp = require('public-ip');
var ip = require('ip');

/**
 * Client for making geolocation requests to ipstack.com.
 */
class Geolocation {
    constructor(config) {
        this.config = config;
    }

    /**
     * Makes a geolocation request to ipstack.com and returns the approximate
     * geolocation of the client.
     * 
     * @param {string} requestIp client's ip address.
     * 
     * @return {Promise} resolves to geolocation object.
     */
    async geolocate(requestIp) {
        // If the requestIp is private (on the same network), 
        // find the public IP of this machine make a geolocation request.
        // If the requestIp is not private, it's public, so request a 
        // geolocation for that IP.
        if (this._isPrivateIp(requestIp)) {
            return this._geolocate(await publicIp.v4());
        } else {
            return this._geolocate(requestIp);
        }
    }

    _isPrivateIp(ip) {
        var parts = ip.split('.');

        return ip == 'localhost' ||
            ip == '127.0.0.1' ||
            parts[0] === '10' || 
           (parts[0] === '172' && (parseInt(parts[1], 10) >= 16 && parseInt(parts[1], 10) <= 31)) || 
           (parts[0] === '192' && parts[1] === '168');
    }

    _geolocate(ip) {
        const options = {
            uri: `${this.config.endpoint}${ip}?access_key=${this.config.apiKey}`,
            json: true
        }
        
        return rp(options);
    }
}

module.exports = Geolocation;