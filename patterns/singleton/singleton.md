# Singleton Pattern


## What is it?

Singleton is a design pattern that make sure there is only one instance of a class throughout the app. That means if we have a class A, and we call it twice like ther following:

```
x = A()
y = A()
```
Then, x and y will be the same instance.


## Use cases

This pattern is usefull in the situation where having multiple instance can create problems, unstability and cost issues (Cost can be performance cost, memory cost or management cost). There are some scenerios provided like that:

1. Database Connection
2. Application Configuration
3. Caching
4. Logging


### Databse Connection

Opening, maintaining and closing a database connection is very expensive. That's why in most of the cases it's desirable to have one database connection and reuse it across multiple requests.

### Application Configuration

In many softwares, there's a central configuration manager that maintain the settings and share it with other components across the app. To maintain consistency, it needs to have one config file and reuse it in the whole app.

### Caching

To save performance cost, sometimes we need to use caching technique. In brief, what it does is it stores the output and next time it doesn't execute the function or process for the output. It just returns the first one (if there's no chance of different output).

### Logging

While logging in the application, it should use single instance throughout the app. Cause, if we use multiple instances, there might be a risk of conflict in writing the log file. Like, multiple logging instance may try to write the same file at a time which can create inconsistency.
