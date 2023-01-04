// No use of any template system
const express = require('express'),
  logger = require('morgan'),
  fs = require('fs');
const app = express();
var x = 1;
var y = 2;

// Determining the contents of the middleware stack
app.use(logger('dev'));                            // Place an HTTP request recorder on the stack — each request will be logged in the console in 'dev' format
// app.use(express.static(__dirname + '/public')); // Place the built-in middleware 'express.static' — static content (files .css, .js, .jpg, etc.) will be provided from the 'public' directory

// *** Route definitions ***

// The first route
app.get('/', function (req, res) {
  res.send(`
<!DOCTYPE html>
<html lang="en" data-bs-theme="dark">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD"
      crossorigin="anonymous">
    <title>Your first page</title>
  </head>
  <body>
    <main class="container">
      <h1>Hello World</h1>
      <p id="equation">` + x.toString() + " + " + y.toString() + " = " + (x+y).toString() + `</p>
    </main>
    <script
      src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"
      integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN"
      crossorigin="anonymous">
    </script>
  </body>
</html>
`); // Send a response to the browser
});

app.get('/json/:name', function(req, res) {
  var filename = req.params.name;
  console.log(filename);
  fs.readFile(filename, 'utf8', (err, data) => {
    console.log(err);
    const obj = JSON.parse(data);
    var my_table = "<table style=\"width:100%;\" border=\"1\"><tr><td>x</td><td>Operation</td><td>y</td><td>Result</td></tr>";
    for (const [key, val] of Object.entries(obj)) {
        my_table += "<tr>" + "<td>" + val["0"].toString() + "</td>" +
            "<td>" + key + "</td>" +
            "<td>" + val["1"].toString() + "</td>";
            if (key == '+')
              my_table += "<td>" + (val["0"] + val["1"]).toString() + "</td>" + "</tr>";
            if (key == '-')
              my_table += "<td>" + (val["0"] - val["1"]).toString() + "</td>" + "</tr>";
            if (key == '*')
              my_table += "<td>" + (val["0"] * val["1"]).toString() + "</td>" + "</tr>";
            if (key == '/')
              my_table += "<td>" + (val["0"] / val["1"]).toString() + "</td>" + "</tr>";
    }
    my_table += "</table>";
    res.send(`
<!DOCTYPE html>
<html lang="en" data-bs-theme="dark">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD"
      crossorigin="anonymous">
    <title>Your first page</title>
  </head>
  <body>
    <main class="container">
      <h1>Hello World</h1>
      <p id="equation">` + my_table + `</p>
    </main>
    <script
      src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"
      integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN"
      crossorigin="anonymous">
    </script>
  </body>
</html>
`);
      });
})

// The application is to listen on port number 3000
app.listen(3000, function () {
  console.log('The application is available on port 3000');
});