const path = require("path");

module.exports = {
  entry: "./static/js/index.js", // Your main JavaScript file
  output: {
    filename: "bundle.js",
    path: path.resolve(__dirname, "static/dist"), // Output directory
  },
  mode: "development", // Change to "production" for production builds
};
