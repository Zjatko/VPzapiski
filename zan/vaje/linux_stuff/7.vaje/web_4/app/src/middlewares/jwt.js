const jwt = require("jwt-decode");

const config = require("../../config");

const verifyToken = (req, res, next) => {
	if (req && req.cookies) {
		const token = req.cookies["session"];

		if (token) {
			try {
				req.user = jwt.jwtDecode(token);
			} catch (err) {
				if (err) {
					console.log("JWT verify error: " + err);
					return next();
				}
			}
			return next();
		} else {
			return next();
		}
	} else {
		return next();
	}
}

module.exports = verifyToken;
