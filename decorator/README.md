# Decorator Pattern

Decorator pattern is a structural pattern that lets user attach new behaviors to objects by placing these objects inside special wrapper objects that contain the behaviors.

## Real world examples

1. React HOC
2. HMR (Hot Module)
3. Redux connect function
4. Python Decorators
5. DRF @api_view()
6. DRF @permission_classes

## Implementation

### Decorator pattern in Python

```
organizations = {
    "1": ["Neymar", "Messi", "Ronaldo"]
}


class Request:
    data = "Request Data"


def api_decorator(func):
    def wrapper_func(*args, **kwargs):
        org_id = kwargs["org_id"]
        org_users = organizations.get(org_id)
        request = Request()

        if org_users:
            print(f"Passing {request.data} to api view function.")

            func(request, org_users, *args, **kwargs)

            print("Ending the api call.")
        else:
            print(
                f"No data found for Organization Id: {org_id}. Not calling the api.")

    return wrapper_func


@api_decorator
def get_users(request: Request, org_users: list, org_id):
    data = request.data

    print(f"Got {data} for executing further operations.")
    print(f"Got users: {', '.join(org_users)} for organization id {org_id}.")


print("------------------------------")
get_users(org_id="1")

print("------------------------------")

get_users(org_id="2")
print("------------------------------")

```

#### Output

```
------------------------------
Passing Request Data to api view function.
Got Request Data for executing further operations.
Got users: Neymar, Messi, Ronaldo for organization id 1.
Ending the api call.
------------------------------
No data found for Organization Id: 2. Not calling the api.
------------------------------

```

### Decorator Pattern in JS

```
const organizations = {
	1: ["Neymar", "Messi", "Ronaldo"],
};

class Request {
	data = "Request Data";
}

function apiView(func) {
	function wrapperFunc(...args) {
		const request = new Request();
		const orgId = args[0];
		const orgUsers = organizations?.[orgId];

		if (orgUsers) {
			console.log(`Passing ${request.data} to api view function.`);

			func(request, orgUsers, ...args);

			console.log("Ending the api call.");
		} else {
			console.log(
				`No data found for Organization Id: ${orgId}. Not calling the api.`
			);
		}
	}

	return wrapperFunc;
}

function getUsers(request, orgUsers, orgId) {
	const data = request.data;

	console.log(`Got ${data} for executing further operations.`);
	console.log(
		`Got users: ${orgUsers.join(", ")} for organization id ${orgId}.`
	);
}

console.log("------------------------------");
getUsers = apiView(getUsers);
getUsers(1);

console.log("------------------------------");

getUsers = apiView(getUsers);
getUsers(2);
console.log("------------------------------");

```

#### Output

```
Passing Request Data to api view function.
Got Request Data for executing further operations.
Got users: Neymar, Messi, Ronaldo for organization id 1.
Ending the api call.
------------------------------
No data found for Organization Id: 2. Not calling the api.
------------------------------

```
