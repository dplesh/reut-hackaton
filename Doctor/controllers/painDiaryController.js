angular.module('doctorApp')
    .controller('painDiaryController', ['$scope', 'Reports', function ($scope, Reports) {

        $scope.reports = [];



        $scope.try = function () {
            console.log("a");
        }

        Reports.get({
            userName: 'dan'
        }).$promise.then(function (response) {
            $scope.reports = response.reports;
            CreatePainReportsGraph('myDiv', response.reports)
        });


        CreatePainReportsGraph = function (divName, reports) {

            reportsTimes = reports.map(function (report) {
                return report.date;
            });

            reportsPainValues = reports.map(function (report) {
                return report.level;
            });

            var trace1 = {
                x: reportsTimes,
                y: reportsPainValues,
                mode: 'lines'
            };

            var data = [trace1];

            var layout = {
                title: 'Pain Diary',
                height: 400,
                width: 480,
                yaxis: {
                    range: [0, 10]
                },
            };

            Plotly.newPlot(divName, data, layout);
        }


    }]);