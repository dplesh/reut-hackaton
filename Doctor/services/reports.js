var app = angular.module('doctorApp', ['ngResource', 'ngRoute']);

// Some APIs expect a PUT request in the format URL/object/ID
// Here we are creating an 'update' method
app.factory('Reports', ['$resource', function ($resource) {
    return $resource('../painReports/:userName', {
        userId: '@id'
    });
}]);