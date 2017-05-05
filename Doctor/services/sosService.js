var app = angular.module('doctorApp');

app.factory('Sos', ['$resource', function ($resource) {
    return $resource('http://172.22.5.241:5000/:userName/sos', {
        userName: '@id'
    }, {
        get: {
            method: 'GET',
            isArray: false
        }
    });
}]);