var app = angular.module('doctorApp');

app.factory('MedsTasks', ['$resource', function ($resource) {
    return $resource('http://172.22.5.241:5000/:userName/meds/', {
        userName: '@id'
    }, {
        get: {
            method: 'GET',
            isArray: false
        }
    });
}]);