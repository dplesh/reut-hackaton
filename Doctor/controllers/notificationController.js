angular.module('doctorApp')
    .controller('notificationController', ['$scope', 'notificationService', '$http', function ($scope, notificationService, $http) {
        let self = this;

        var getNotifications = function () {
            $http({
                    method: 'GET',
                    url: 'http://172.22.5.241:5000/notifications'
                }).then(function successCallback(response) {
                    console.log(response);
                    let newNotifications = [];
                    if (response.data) {
                        newNotifications = response.data.filter(function (x) {
                            return x.isRead == 'false';
                        })
                    }
                    self.notifications = newNotifications;
                })
                .catch(function (err) {
                    console.log(err);
                    self.notifications = [];
                })
        }
        getNotifications();
        setInterval(
            getNotifications, 3000);



        self.firstIterationMade = true;
        self.markNotificationAsRead = function (notification) {
            let index = self.notifications.indexOf(notification);
            self.notifications.splice(index, 1);
            notificationService.markNotificationAsRead(notification.id);
        }
        self.isNotificationsPresent = function () {
            if (self.notification) {
                return self.notifications.length > 0;
            }
            return true;
        }
    }]);