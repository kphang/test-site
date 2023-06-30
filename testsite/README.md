# Test Site

Test Site is a set of two ```FastAPI``` endpoints designed for testing applications making web requests, particularly for testing in conditions of rate-limiting. 


## How to Use

Clone the repository and run ```app.py```.

Use ```http://127.0.0.1:9000``` to test requests to an endpoint in an unrestricted manner.

Use ```http://127.0.0.1:9000/limited``` for simulating requests sent to a rate-limited API utilizing ```slowapi```.

Sending a request to either will yield a standardized response containing some data from the original request along with some diagnostic information.

Viewing the terminal where the app is run will show log info relating to limiters.

As common with FastAPI sites, OpenAPI documentation is auto-generated and can be reached at ```http://127.0.0.1:9000/docs``` 


### Utilizing the Limited Endpoint

The limited endpoint provides the following functionality:
- limiting the # of allowed requests over a period using a moving window strategy (e.g. 10/second with a max of 10000/month)    
- limiting the maximum # of concurrent requests
- enabling throttling of requests when exceeding rates in the form of doubling wait times
- adding random delays to simulate processing time (enabling a small amount is highly recommended in order to meaningfully test asynchronous requests)

These settings can be adjusted by varying the values in ```limitedsettings.txt``` which follows the syntax of an env file. Validation of inputs is provided using ```pydantic```.


## Planned Features

- Fix the quota to be a true quota based on a fixed window from the start of each defined period
- Different types of responses (such as HTML pages, CSV, other files) in the form of default content or that can be provided by the user by pointing at a file on their system.
- Different response behaviours based on query, path, and body
- While ```GET``` and ```POST``` are both currently allowed, there is no difference in behaviours. A future version will have different types of behaviours enabled by each.
