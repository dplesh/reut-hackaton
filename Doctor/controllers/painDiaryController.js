angular.module('doctorApp')
    .controller('painDiaryController', ['$scope', 'Reports', 'MedsTasks', 'PainAnomas', 'SosAnomas', 'Sos',
        function ($scope, Reports, MedsTasks, PainAnomas, SosAnomas, Sos) {

            $scope.reports = [];
            var sosAnomas = [];
            var painAnomas = [];
            var sosTimes = [];
            var divName = 'myDiv';

            var layout = {
                title: 'Pain Diary',
                height: 500,
                width: 1000,
                yaxis: {
                    range: [0, 10.5]
                },
                font: {
                    family: 'Courier New, monospace',
                    size: 18,
                    color: '#7f7f7f'
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


            var takenMedsTime = [];
            var unTakenMedsTimes = [];

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

            GetSortedTimes = function (timesToSort) {
                var sorted = JSON.parse(JSON.stringify(timesToSort));
                sorted.sort();
                return sorted;
            }

            GetClosestTime = function (times, time) {
                let sortedTimes = GetSortedTimes(times);

                for (var i = 0; i < times.length - 1; i++) {
                    if (sortedTimes[i] <= time && time <= sortedTimes[i + 1]) {
                        return [sortedTimes[i], sortedTimes[i + 1]]
                    }
                }


                console.log("shemesh is a liar ");


            }

            GetPainPointY = function (time) {
                index = reportsTimes.indexOf(time);
                return reportsPainValues[index];
            }

            GetPainByTime = function (time) {
                if (reportsTimes.includes(time)) {
                    return GetPainPointY(time);
                } else {
                    let closestTimes = GetClosestTime(reportsTimes, time);
                    let x = new Date(time).getTime();
                    let x1 = new Date(closestTimes[0]).getTime();
                    let x2 = new Date(closestTimes[1]).getTime();
                    let y1 = GetPainPointY(closestTimes[0]);
                    let y2 = GetPainPointY(closestTimes[1]);
                    return (y1 - y2) / (x1 - x2) * (x - x1) + y1;
                }
            };


            GetPainValues = function (times) {
                return times.map(function (time) {
                    return GetPainByTime(time);
                });
            };

            GetTimesBetweenPoints = function (firstTime, lastTime) {
                let times = [];
                let startIndex = reportsTimes.indexOf(firstTime);
                let endIndex = reportsTimes.indexOf(lastTime);
                for (var i = startIndex; i <= endIndex; i++) {
                    times.push(reportsTimes[i]);
                }
                return times;
            };

            CreatePainReportsGraph = function () {
                var painTrace = {
                    x: reportsTimes,
                    y: reportsPainValues,
                    text: texts,
                    mode: 'lines+markers',
                    name: 'Pain',
                    marker: {
                        size: 11
                    }
                };

                let takenMedsValues = GetPainValues(takenMedsTime);
                var takenMedsTrace = {
                    x: takenMedsTime,
                    y: takenMedsValues,
                    mode: 'markers',
                    name: 'Taken Meds',
                    marker: {
                        color: 'rgb(0, 102, 0)',
                        size: 11
                    }
                };

                let unTakenMedsValues = GetPainValues(unTakenMedsTimes);
                var unTakenMedsTrace = {
                    x: unTakenMedsTimes,
                    y: unTakenMedsValues,
                    mode: 'markers',
                    name: 'Un Taken Meds',
                    marker: {
                        color: 'rgb(153, 0, 0)',
                        size: 11
                    }
                };

                let sosValues = GetPainValues(sosTimes);
                var sosTrace = {
                    x: sosTimes,
                    y: sosValues,
                    mode: 'markers',
                    name: 'Sos taken',
                    marker: {
                        color: 'rgb(228, 47, 203)',
                        size: 11
                    }
                };

                var data = [painTrace, takenMedsTrace, unTakenMedsTrace, sosTrace];
                for (var i = 0, len = painAnomas.length; i < len; i++) {
                    let painAnomasTimes = GetTimesBetweenPoints(painAnomas[i].startWorseningTime, painAnomas[i].endWorseningTime)
                    let values = GetPainValues(painAnomasTimes);
                    let painAnomasTrace = {
                        x: painAnomasTimes,
                        y: values,
                        mode: 'markers+lines',
                        name: 'Pain anomality ' + (i + 1),
                        marker: {
                            color: 'rgb(0, 0, 0)',
                            size: 11
                        }
                    };
                    data.push(painAnomasTrace);
                }

                for (var i = 0, len = sosAnomas.length; i < len; i++) {
                    let sosAnomasTimes = GetTimesBetweenPoints(sosAnomas[i].startWorseningTime, sosAnomas[i].endWorseningTime)
                    let values = GetPainValues(sosAnomasTimes);
                    let sosAnomasTrace = {
                        x: sosAnomasTimes,
                        y: values,
                        mode: 'markers+lines',
                        name: 'SOS anomality ' + (i + 1),
                        marker: {
                            color: 'rgb(122, 122,122)',
                            size: 11
                        }
                    };
                    data.push(sosAnomasTrace);
                }



                var a = Plotly.newPlot(divName, data, layout);
            };

            GetReportText = function (report) {
                return "Mood: " + report.mood + "<br>" +
                    "Influences: " + report.influences + "<br>" +
                    "Pain type: " + report.type.toString() + "<br>" +
                    "Pain place: " + report.body_parts.toString() + "<br>" +
                    "Pain duration: " + report.duration + " minutes";
            };

            Sos.get({
                userName: 'Mikel'
            }).$promise.then(function (response) {
                sosTimes = response.data.map(function (sos) {
                    return sos.time_taken;
                });

            });

            SosAnomas.get({
                userName: 'Mikel'
            }).$promise.then(function (response) {
                sosAnomas = response.data;
            });

            PainAnomas.get({
                userName: 'Mikel'
            }).$promise.then(function (response) {
                painAnomas = response.data;
            });

            MedsTasks.get({
                userName: 'Mikel'
            }).$promise.then(function (response) {
                medsTasks = response.data;
                takenMedsTime = [];
                unTakenMedsTimes = [];
                for (var i = 0, len = medsTasks.length; i < len; i++) {
                    if (medsTasks[i].timeTaken != "0") {
                        takenMedsTime.push(medsTasks[i].timeTaken);
                    } else {
                        unTakenMedsTimes.push(medsTasks[i].timeNeeded);
                    }
                }
            });

            Reports.get({
                userName: 'Mikel'
            }).$promise.then(function (response) {
                response.data.sort(function (a, b) {
                    // Compare the 2 dates
                    if (a.date < b.date) return -1;
                    if (a.date > b.date) return 1;
                    return 0;
                });

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


            });
        }
    ]);