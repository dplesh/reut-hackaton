var app = angular.module('doctorApp');

app.factory('Reports', ['$resource', function ($resource) {
    return $resource('../painReports/:userName/reports.json', {
        userName: '@id'
    }, {
        get: {
            method: 'GET',
            isArray: false
        }
    });
}]);