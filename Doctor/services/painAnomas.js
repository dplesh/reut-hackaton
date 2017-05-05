var app = angular.module('doctorApp');

app.factory('PainAnomas', ['$resource', function ($resource) {
    return $resource('http://172.22.5.241:5000/:userName/pain_anomalies', {
        userName: '@id'
    }, {
        get: {
            method: 'GET',
            isArray: false
        }
    });
}]);