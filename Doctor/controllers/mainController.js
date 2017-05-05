angular.module('doctorApp')
    .controller('mainController', ['$scope', '$interval', '$http', function ($scope, $interval, $http) {
        let lastPolledNotifications = [];

        let getNotifications = function () {
            return $http({
                method: 'GET',
                url: 'http://172.22.5.241:5000/notifications'
            }).then(function successCallback(response) {
                let resultNotifications = response.data.map((value) => {
                    
                    if (!(lastPolledNotifications.indexOf(value) == -1)){
                        notifyMe("New notification received", value.message, "#!/notifications");
                        console.log("New notiication rececived!");
                    }
                });
                lastPolledNotifications = resultNotifications;

                return resultNotifications;
            }, function errorCallback(response) {
                return [];
            });
        }

        $interval(getNotifications, 2000);
        $scope.currentNavItem = 'page1';

        
        


        //Internal, black box Danelkis functions

        // request permission on page load
        document.addEventListener('DOMContentLoaded', function () {
            if (!Notification) {
                alert('Desktop notifications not available in your browser. Try Chromium.');
                return;
            }

            if (Notification.permission !== "granted")
                Notification.requestPermission();
        });

        function notifyMe(title, text, url_to_open) {
            if (Notification.permission !== "granted")
                Notification.requestPermission();
            else {
                var notification = new Notification(title, {
                    icon: 'images/reut.png',
                    body: text,
                });

                notification.onclick = function () {
                    window.open(url_to_open);
                };
            }
        }

        document.onkeypress = function (e) {
            e = e || window.event;
            console.log("pressed :" + e.keyCode);

            if (e.keyCode == 96 || e.keyCode == 59) {
                notifyMe("Dan is not feeling well", "An anomaly was found in Dan's pain reports. You better check in on him.", "google.com");
            }
        };


    }]);