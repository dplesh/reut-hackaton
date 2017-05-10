var app = angular.module('doctorApp', ['ngRoute', 'ngMaterial', 'ngResource']);

app.config(function ($routeProvider, $locationProvider) {
    $routeProvider
        .when('/user', {
            templateUrl: './views/user.html',
            controller: 'userController'
        })
        .when('/home', {
            templateUrl: './views/home.html'
        })
        .when('/painDiary/:user', {
            templateUrl: './views/painDiary.html',
            controller: 'painDiaryController'
        })
        .when('/', {
            templateUrl: './views/notifications.html',
            controller: 'notificationController'
        })
        .when('/notifications', {
            templateUrl: './views/notifications.html',
            controller: 'notificationController'
        })
        .otherwise({
            templateUrl: './views/notifications.html',
            controller: 'notificationController'

        });

    $locationProvider.html5Mode({
        enabled: false,
        requireBase: false
    });
});