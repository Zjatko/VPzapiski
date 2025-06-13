const express = require("express");
const path = require("path");
const morgan = require("morgan");
const cookieParser = require("cookie-parser");

const { PORT, HOST } = require("./config");

const jwt_middleware = require("./src/middlewares/jwt");

const index = require("./src/routers/index");
const auth = require("./src/routers/auth");
const jwks = require("./src/routers/jwks");
const app = express();

app.set("view engine", "ejs");
app.set("views", "./src/views");

app.use(cookieParser());
app.use(express.urlencoded({ extended: false }));
app.use("/static", express.static(path.join(__dirname, "static")));
app.use(morgan("common"));
app.use(jwt_middleware);

app.use(index);
app.use(auth);
app.use(jwks);

app.listen(PORT, HOST, () => {
  console.log(`Application is on http://${HOST}:${PORT}`);
});

