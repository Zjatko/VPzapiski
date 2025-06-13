const crypto = require('crypto');

const randompass = crypto.randomBytes(20).toString('hex');


module.exports = {
	users: [
		{
			id: 1,
			username: "admin",
			password: randompass,
		},
		{
			id:	2,
			username: "guest",
			password: "guest",
		}
	],
}
