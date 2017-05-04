angular.module('doctorApp')
    .service('userService', ['$q', '$http', function ($q, $http) {
        let getUsersByName = function (users, name) {
            let result = [];
            for (let user of users) {
                if (user.toLowerCase().startsWith(name.toLowerCase())) {
                    result.push({
                        display: user,
                        value: user
                    });
                }
            }
            return result;
        }
        /*
                let users = [{
                        name: "Avi Neelavi",
                        id: "318422574"
                    },
                    {
                        name: "Avi Ron",
                        id: "424582253"
                    },
                    {
                        name: "Avi Von",
                        id: "483729562"
                    },
                    {
                        name: "Levi Von",
                        id: "212758839"
                    }
                ];
        */
        this.findUsersByName = function (name) {
            let deferred = $q.defer();
            return $http({
                method: 'GET',
                url: 'http://172.22.5.241:5000/users'
            }).then(function successCallback(response) {
                let users = response.data.data;
                let filteredUsers = getUsersByName(users, name);
                deferred.resolve(filteredUsers);
                return deferred.promise;
            }, function errorCallback(response) {
                console.error('Failed getting users from server.');
                deferred.reject('Failed getting users from server.');
                return deferred.promise;
            });
        }
    }]);