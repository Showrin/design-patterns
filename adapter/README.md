# Adapter Pattern

## What is it?

Adapter pattern is a structural design pattern that helps us to collaborate between objects with incompatible interfaces.

Suppose, you have a mobile that needs a USB C (male) type ports to connect external memories with your phone. You have a pendrive. Unfortunately the pendrive has USB A (male) type port that is incompatible with the phone. Now what can we do here?

Yes, we can search for an adapter that has USB A (female) and USB C (male) port so that we can connect our pendrive with that adapter and the adapter with our phone. This is the ultimate adapter design pattern.

## Real life use case

### Serializer

Wee often use serializer to convert complex object into json response and vise versa. It's an example of Adapter pattern.

## Implementation

### Implementation in Python

```
class Serializer:
    data = None

    def __init__(self, obj=None, data=None) -> None:
        if obj:
            self.data = self.convert_to_json(obj)
        elif data:
            self.data = self.convert_to_object(data)

    def convert_to_json(self, obj):
        print("Converted Python Object to JSON.")
        return f"{obj} in json format"

    def convert_to_object(self, data):
        print("Converted JSON to Python Object.")
        return f"{data} in object format"


class ApiView:
    def list(self, request):
        data = request["data"]

        serialized_request_data = Serializer(data=data).data
        print(serialized_request_data)

        print("-------------------------")
        excepted_result = "Expected result"

        serialized_response_data = Serializer(excepted_result).data
        print(serialized_response_data)

        return serialized_response_data


list_api_view = ApiView().list(request={
    "data": "Request body"
})

```

#### Output

```
Output:
Converted JSON to Python Object.
Request body in object format
-------------------------
Converted Python Object to JSON.
Expected result in json format
```

### Implementation in JS

```
class Serializer {
  data = null;

  constructor({ obj, data }) {
    if (obj) {
      this.data = this.convert_to_json(obj);
    } else if (data) {
      this.data = this.convert_to_object(data);
    }
  }

  convert_to_json(obj) {
    console.log("Converted JS Object to JSON.");
    return `${obj} in json format`;
  }

  convert_to_object(data) {
    console.log("Converted JSON to JS Object.");
    return `${data} in object format`;
  }
}

class ApiView {
  list(request) {
    const data = request["data"];

    const serialized_request_data = new Serializer({ data }).data;
    console.log(serialized_request_data);

    console.log("-------------------------");
    const excepted_result = "Expected result";

    const serialized_response_data = new Serializer({ obj: excepted_result })
      .data;
    console.log(serialized_response_data);

    return serialized_response_data;
  }
}

list_api_view = new ApiView().list({ data: "Request body" });

```

#### Output

```
Output:
Converted JSON to JS Object.
Request body in object format
-------------------------
Converted JS Object to JSON.
Expected result in json format
```
