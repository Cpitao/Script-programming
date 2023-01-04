// snippet e4-ex(TAB)
app.use(function (req, res, next) {
    res.status(404).send('404 - Not Found!');
});