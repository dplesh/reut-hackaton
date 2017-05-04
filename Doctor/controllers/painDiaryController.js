angular.module('doctorApp')
    .controller('painDiaryController', ['$scope', 'Reports', function ($scope, Reports) {

        $scope.reports = [];

        var divName = 'myDiv';

        var layout = {
            title: 'Pain Diary',
            height: 450,
            width: 1000,
            yaxis: {
                range: [0, 10]
            },
            legend: {
                y: 0.5,
                yref: 'paper',
                font: {
                    family: 'Arial, sans-serif',
                    size: 20,
                    color: 'grey',
                }
            }
        };

        var reportsTimes = [];

        var reportsPainValues = [];

        var texts = [];

        UpdatePainGraph = function (newReports) {
            newReportsPainValues = newReports.map(function (report) {
                return report.level;
            });

            newReportsTimes = newReports.map(function (report) {
                return report.date;
            });

            reportsTimes = reportsTimes.concat(newReportsTimes);
            reportsPainValues = reportsPainValues.concat(newReportsPainValues);
            $scope.reports.concat(newReports);
            CreatePainReportsGraph();

        };

        CreatePainReportsGraph = function () {
            var trace1 = {
                x: reportsTimes,
                y: reportsPainValues,
                text: texts,
                mode: 'lines+markers',
                name: 'Pain'
            };

            var data = [trace1];

            Plotly.newPlot(divName, data, layout);
        };

        GetReportText = function (report) {
            return "Mood: " + report.mood + "<br>" +
                "Influences: " + report.influences + "<br>" +
                "Pain type: " + report.type.toString() + "<br>" +
                "Pain place: " + report.body_parts.toString() + "<br>" +
                "Pain duration: " + report.duration + " minutes";
        };

        Reports.get({
            userName: 'Mikel'
        }).$promise.then(function (response) {
            $scope.reports = response.data;

            reportsPainValues = $scope.reports.map(function (report) {
                return report.level;
            });

            reportsTimes = $scope.reports.map(function (report) {
                return report.date;
            });

            texts = $scope.reports.map(function (report) {
                return GetReportText(report);
            });
            CreatePainReportsGraph(response.data, reportsTimes, reportsPainValues);
            /*setTimeout(function () {
                UpdatePainGraph([{
                    "body_parts": ["leg", "hand"],
                    "date": "2017-05-12 16:05:46.694339",
                    "level": 6,
                    "duration": "9",
                    "context": "Sports",
                    "type": ["burn", "sharp"],
                    "was_sos_med": false,
                    "influences": "Couldn't walk...",
                    "mood": "depressed"
                }]);
            }, 10000);*/

        });
    }]);