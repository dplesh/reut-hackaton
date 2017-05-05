angular.module('doctorApp')
    .service('notificationService', function ($http) {
        this.getUnreadNotifications = function () {
            /*
        let notifications = [
            {
                id : 0,
                isRead: false,
                message: "Mikel forgot taking his pills.",
                severity: 'medium'
                
            },
            {
                id : 1,
                isRead: false,
                message: "Omri forgot taking his pills.",
                severity: 'medium'
            },
            {
                id : 2,
                isRead: false,
                message: "Or forgot taking his pills.",
                severity: 'medium'
            },
            {
                id : 3,
                isRead: false,
                message: "Dan forgot taking his pills.",
                severity: 'high'
            },
            {
                id : 4,
                isRead: false,
                message: "Levi forgot taking his pills.",
                severity: 'medium'
            }
        ];
*/

        }

        this.markNotificationAsRead = function (notificationId) {
            var url ='http://172.22.5.241:5000/readnotif/' + notificationId;
            console.log(url);
            $http.get(url).then(() => {});
        }
    });