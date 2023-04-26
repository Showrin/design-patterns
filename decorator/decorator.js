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

// Output
// Passing Request Data to api view function.
// Got Request Data for executing further operations.
// Got users: Neymar, Messi, Ronaldo for organization id 1.
// Ending the api call.
// ------------------------------
// No data found for Organization Id: 2. Not calling the api.
// ------------------------------
