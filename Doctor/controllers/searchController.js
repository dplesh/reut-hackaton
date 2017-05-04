angular.module('doctorApp')
    .controller('searchController', ['$scope', 'userService', '$q', '$log', '$interval', '$location', function ($scope, userService, $q, $log, $interval, $location) {

        var self = this;

        self.simulateQuery = false;
        self.isDisabled = false;

        self.querySearch = querySearch;
        self.selectedItemChange = selectedItemChange;

        self.goToUser = function (keyEvent) {
            if (keyEvent.which === 13)
                if (self.selectedItem){
                    goToUser(self.selectedItem);
                }
        }

        let goToUser = function(user){
            $location.path("/user/" + user.value.id);
        }

        // ******************************
        // Internal methods
        // ******************************

        /**
         * Search for states... use $timeout to simulate
         * remote dataservice call.
         */
        function querySearch(query) {
            if (!query || query == '') {
                return [{
                    display: 'No patient found',
                    value: ''
                }];
            }
            var results = userService.findUsersByName(query);
            if (results.length == 0) {
                return [{
                    display: 'No patient found',
                    value: ''
                }];
            }
            return results;
        }



        function selectedItemChange(item) {
            $log.info('Item changed to ' + JSON.stringify(item));
        }

    }]);