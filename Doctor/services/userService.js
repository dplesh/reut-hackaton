angular.module('doctorApp')
    .service('userService',['$q', function($q){
        let getUsersByName = function (users, name) {
            let result = [];
            for (let user of users) {
                if (user.name.toLowerCase().startsWith(name.toLowerCase())) {
                    result.push({display: user.name, value: user});
                }
            }
            return result;
        }

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

        this.findUsersByName = function (name) {
            return getUsersByName(users, name);
        }
    }]);