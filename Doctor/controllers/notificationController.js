angular.module('doctorApp')
.controller('notificationController', ['$scope', 'notificationService' ,function($scope, notificationService){
    let self = this;
    self.notifications = notificationService.getUnreadNotifications();
    self.firstIterationMade = true;
    self.markNotificationAsRead = function(notification){
        let index = self.notifications.indexOf(notification);
        self.notifications.splice(index, 1);
        notificationService.markNotificationAsRead(notification.id);
        $scope.$apply(function(){
            $scope.loading = false;
        });
    }
    self.isNotificationsPresent = function(){
        return self.notifications.length > 0;
    }
}]);
