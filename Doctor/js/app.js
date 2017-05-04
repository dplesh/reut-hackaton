var app = angular.module('doctorApp', ['ngRoute', 'ngMaterial']);

app.config(function($routeProvider, $locationProvider) {
    $routeProvider
        .when('/user', {
            templateUrl: './views/user.html',
            controller: 'userController'
        })
        .when('/', {
            templateUrl: './views/home.html',
            controller: 'mainController'
        });
});