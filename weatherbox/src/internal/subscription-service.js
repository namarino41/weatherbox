
let subscriptions = {};

class Subscription {
    constructor(clientId, parameters) {
        this.clientId = clientId;
        this.parameters = parameters;
    }
}

module.exports.subscription = Subscription;
module.exports.subscriptions = subscriptions;