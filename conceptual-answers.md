### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
Python uses a class-based inheritance model while Javascript uses a prototype-based inheritance model.

Javascript conforms to the ECMAScript specification, while Python was developed to emphasize code readability.

JavaScript is also known as the browser’s language.

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
  <!-- trying to output value of absent key -->
print ("The value associated with 'c' is : ")
print (d['c'])

- What is a unit test?
Unit testing is testing the smallest testable unit of an application.

- What is an integration test?
A type of testing where software modules are integrated logically and tested as a group.

- What is the role of web application framework, like Flask?
It allows developers to get started easily with projects, as well as to scale them up quickly into applications.

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
/foods/pretzel would usually be predefined or categorical as /foods/X could be any possible food. Foods?Type is probably more for search based routing.

- How do you collect data from a URL placeholder parameter using Flask?
request.args

- How do you collect data from the query string using Flask?
request.url

- How do you collect data from the body of the request using Flask?
request.args.get 

- What is a cookie and what kinds of things are they commonly used for?
Cookies are very small pieces of data that are tied to a user that will be accessed along with the route that is used to access a website. This could be search history, user preferences, etc.
- What is the session object in Flask?
A session is similar to a cookie, as it stores information on a user\computer that is carried over during the course of a browsers life. This can help keep track of constantly updating variables that will be referencable as long as the browser\window remain open. Not affected by refreshes.
It is used to track the session data which is a dictionary object that contains a key-value pair of the session variables and their associated values.

- What does Flask's `jsonify()` do?
returns a Response object.
