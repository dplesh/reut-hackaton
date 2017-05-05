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
            $http({
                method: 'POST',
                url: 'http://localhost:5000/readnotif',
                data: {
                    id: 1
                }
            }).then(()=>{
                // nothing
            })
            .catch((err)=>{
                console.log(err);
            })
        }
    });