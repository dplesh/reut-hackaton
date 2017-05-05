angular.module('doctorApp')
    .controller('mainController', ['$scope', '$interval', '$http', function ($scope, $interval, $http) {
        let lastPolledNotifications = [];

        let getNotifications = function () {
            return $http({
                method: 'GET',
                url: 'http://localhost:5000/notifications'
            }).then(function successCallback(response) {
                let newNotifications = response.data.filter(function(x){
                    return x.isRead == 'false';
                });
                let notificationDiff = getNotificationDiff(newNotifications, lastPolledNotifications);
                for (let notification of notificationDiff) {
                    notifyMe("New notification received", notification.message, "#!/notifications");
                    console.log("New notiication rececived!");
                }
                lastPolledNotifications = newNotifications;
            });
            return resultNotifications;
        }

        let getNotificationDiff = function (newArray, oldArray) {
            let result = [];
            for (let notification1 of newArray) {
                let notificationFound = false;
                for (let notification2 of oldArray) {
                    if (notification1.id == notification2.id) {
                        notificationFound = true;
                        break;
                    }
                }
                if (!notificationFound){
                    result.push(notification1);
                }
            }
            return result;
        }

        setInterval(getNotifications, 3000);
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