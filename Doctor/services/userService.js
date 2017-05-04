angular.module('doctorApp')
    .service('userService', () => {
        let getUsersByName = function (users, name) {
            let result = [];
            for (let user in users) {
                if (user.startsWith(name)) {
                    result.push(result);
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

        this.findUserByName = function (name) {
            return getUsersByName(users, name);
        }

    });