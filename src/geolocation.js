const rp = require('request-promise');
const publicIp = require('public-ip');
var ip = require('ip');

class Geolocation {
    constructor(config) {
        this.config = config;
    }

    geolocate(requestIp) {
        if (this._isPrivateIP(requestIp)) {
            return publicIp.v4().then((publicIp) => {
                return this._geolocate(publicIp);
            });
        } else {
            return this._geolocate(requestIp);
        }
    }

    _isPrivateIP(ip) {
        var parts = ip.split('.');

        return ip == 'localhost' || ip == '127.0.0.1' ||
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

// //192.168.1.146

// new Geolocation({
//     "endpoint": "http://api.ipstack.com/",
//     "apiKey": "9c8144a3dc134abc91b021d086ba3656"
// }).geolocate("192.168.1.146").then((res) => {
//     console.log(res)
// });