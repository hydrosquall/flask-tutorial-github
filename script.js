$.getJSON("https://api.github.com/search/repositories?q=Space%20Invaders%20HTML5+language:JavaScript&callback=?", function(data) {
    console.log(data);
});

/*Open up test_js.html in your browser and see the response from your JSON request in the JavaScript Console.

A couple of gotchas here:

We add the parameter callback=?; this is a JSONP callback to get around the same-origin policy. It's necessary for security reasons; for more information, see those links.
We process the data in a callback (that's the function(data) { ... } bit). This is because loading data over the internet takes time; rather than stop everything up while we're waiting for that to finish, JavaScript moves on and executes the next statement. We tell JavaScript what we want it to do once it's finished loading the data; that's the body of the function we pass to getJSON.
That's it! You've successfully queried GitHub's API using JavaScript and jQuery.*/