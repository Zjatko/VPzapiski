const fs = require('fs');

module.exports = {
	HOST: process.env.HOST || "0.0.0.0",
	PORT: process.env.PORT || 3000,
	JWT_ALGORITHMS: ['RS256', 'HS256', 'ES256'],
	PRIVATE_KEY: fs.readFileSync('./secret/private.pem', 'utf8'),
	PUBLIC_KEY: fs.readFileSync('./secret/public.pem', 'utf8'),
}
