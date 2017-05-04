var app = angular.module('doctorApp', ['ngRoute', 'ngMaterial']);

app.config(function ($routeProvider, $locationProvider) {
    $routeProvider
        .when('/user', {
            templateUrl: './views/user.html',
            controller: 'userController'
        })
        .when('/home', {
            templateUrl: './views/home.html',
            controller: 'mainController'
        })
        .when('/', {
            templateUrl: './views/home.html',
            controller: 'mainController'
        })
        .when('/search', {
            templateUrl: './views/search.html',
            controller: 'searchController'
        })
        .otherwise({
            templateUrl: './views/home.html',
            controller: 'mainController'
        });

    $locationProvider.html5Mode({
        enabled: false,
        requireBase: false
    });
});