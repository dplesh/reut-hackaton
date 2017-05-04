var app = angular.module('doctorApp');

app.factory('Reports', ['$resource', function ($resource) {
    return $resource('http://172.22.5.241:5000/:userName/pain/', {
        userName: '@id'
    }, {
        get: {
            method: 'GET',
            isArray: false
        }
    });
}]);