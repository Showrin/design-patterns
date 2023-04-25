# Singleton Pattern

## What is it?

Singleton is a design pattern that make sure there is only one instance of a class throughout the app. That means if we have a class A, and we call it twice like the following:

```
x = A()
y = A()
```

Then, x and y will be the same instance.

## Use cases

This pattern is useful in the situation where having multiple instance can create problems, stability and cost issues (Cost can be performance cost, memory cost or management cost). There are some scenarios provided like that:

1. Env Files
2. Database Connection
3. Application Configuration
4. Caching
5. Logging

### Env File

In our applications, we regularly use env files to separate our secret values from the implementation code.

Here, env file acts as a singleton instance. Every files and code blocks access this.

### Database Connection

Opening, maintaining and closing a database connection is very expensive. That's why in most of the cases it's desirable to have one database connection and reuse it across multiple requests.

### Application Configuration

In many softwares, there's a central configuration manager that maintain the settings and share it with other components across the app. To maintain consistency, it needs to have one config file and reuse it in the whole app.

### Caching

To save performance cost, sometimes we need to use caching technique. In brief, what it does is it stores the output and next time it doesn't execute the function or process for the output. It just returns the first one (if there's no chance of different output).

### Logging

While logging in the application, it should use single instance throughout the app. Cause, if we use multiple instances, there might be a risk of conflict in writing the log file. Like, multiple logging instance may try to write the same file at a time which can create inconsistency.

## Implementation

### Singleton pattern in JS

```
class SettingsManager {
  static instance = undefined;

  constructor() {
    if (SettingsManager.instance === undefined) {
      SettingsManager.instance = this;
    }

    return SettingsManager.instance;
  }
}

const a = new SettingsManager();
a.color = "red";

const b = new SettingsManager();
b.color = "blue";

// a & b will display the same instance object
console.log(a.color);
console.log(b.color);
console.log(a === b);

```

#### Output

```
blue
blue
true
```

### Singleton pattern in Python

```
class SettingsManager:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance


a = SettingsManager()
a.color = "red"

b = SettingsManager()
b.color = "blue"

# a & b will display the same instance dictionary
print(a.color)
print(b.color)
print(a is b)

```

#### Output

```
blue
blue
True
```
