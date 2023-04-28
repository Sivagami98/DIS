const loginForm = document.getElementById("login-form");
const signupForm = document.getElementById("signup-form");
const signupLink = document.getElementById("signup-link");

signupLink.addEventListener("click", (e) => {
	e.preventDefault();
	loginForm.classList.add("hidden");
	signupForm.classList.remove("hidden");
});

signupForm.addEventListener("submit", (e) => {
	e.preventDefault();
	// handle sign up form submission
});

loginForm.addEventListener("submit", (e) => {
	e.preventDefault();
	// handle login form submission
});
