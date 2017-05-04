angular.module('doctorApp')
    .controller('painDiaryController', ['$scope', 'Reports', function ($scope, Reports) {
        $scope.reports = Reports.get({
            userName: 'dan'
        });

        
    }]);