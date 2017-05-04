angular.module('doctorApp')
    .controller('painDiaryController', ['$scope', 'Reports', function ($scope, Reports) {
        
        $scope.reports = [];

        Reports.get({
            userName: 'dan'
        }).$promise.then(function (response) {
            $scope.reports = response.reports;
        });

        $scope.try = function () {
            console.log("a");
        }

    }]);