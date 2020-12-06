const {LoginRequest, LogoutRequest, CreateUserRequest, GetSessionRequest} = require('./apiservice_pb.js');
const {APIServiceClient} = require('./apiservice_grpc_web_pb.js');

// TODO: resolve or get endpoint from .env
let shortCxClient = new APIServiceClient("http://localhost:8080");

// Populate login/signup or account/signout
window.addEventListener('load', function() {
    PopulateSessionModules();
});

function PopulateSessionModules() {
    let dest = document.getElementById("accounts");
    let authToken = localStorage.getItem("Authorization");
    let foundSession = false;
    if (authToken) {
        let request = new GetSessionRequest();
        request.setAuthToken(authToken);
        shortCxClient.getSession(request, {}, (err, resp) => {
            if (err) {
                console.warn("Session invalid or expired: " + err);
            } else {
                foundSession = true;
                let respObj = resp.toObject();
                clearContents(dest);
                dest.appendChild(AccountModule(respObj.username, DoLogout));
            }
        });
    } 

    // No token or expired session -> login/signup modules
    if (!foundSession) {
        clearContents(dest);
        dest.appendChild(LoginModule(DoLogin));
        dest.appendChild(SignupModule(DoSignup));
    } 
}

function clearContents(element) {
    while (element.firstChild) {
        element.removeChild(element.lastChild);
    }
}

function DoLogin(username, password) {
    let request = new LoginRequest();
    request.setUsername(username);
    request.setPassword(password);

    shortCxClient.login(request, {}, (err, resp) => {
        if (err) {
            console.error(err);
        } else {
            let respObj = resp.toObject();
            localStorage.setItem("Authorization", respObj.authToken);
            console.log("Login Succeeded!");
            PopulateSessionModules();
        }
    });
}

function DoLogout() {
    let request = new LogoutRequest();
    request.setAuthToken(localStorage.getItem("Authorization"));

    shortCxClient.logout(request, {}, (err, resp) => {
        if (err) {
            console.error(err);
        } else {
            localStorage.removeItem("Authorization");
            console.log("Successfully logged out!");
            PopulateSessionModules();
        }
    });
}

function DoSignup(username, password, passwordConf) {
    let request = new CreateUserRequest();
    request.setUsername(username);
    request.setPassword(password);
    request.setPasswordConf(passwordConf);

    shortCxClient.createUser(request, {}, (err, resp) => {
        if (err) {
            console.error(err);
        } else {
            let respObj = resp.toObject();
            localStorage.setItem("Authorization", respObj.authToken);
            console.log("Creation Succeeded");
            PopulateSessionModules();
        }
    });
}

function AccountModule(username, logoutCallback) {
    const div = document.createElement("div");
    const header = document.createElement("h3");
    header.innerText = `Welcome, ${username}!`;
    div.appendChild(header);
 
    let logout = document.createElement('input');
    logout.setAttribute('type', 'button');
    logout.setAttribute('value', 'Logout');
    div.appendChild(logout);

    logout.addEventListener("click", () => {
        logoutCallback();
    });

    return div;
}

function LoginModule(loginCallback) {
    const div = document.createElement("div");
    div.classList.add("FormModule");
    const header = document.createElement("h3");
    header.innerText = "Login";
    div.appendChild(header);

    let username = document.createElement('input'); 
    username.setAttribute('type', 'text');
    username.setAttribute('placeholder', 'Username');
    div.appendChild(username);

    let password = document.createElement('input'); 
    password.setAttribute('type', 'password');
    password.setAttribute('placeholder', 'Password');
    div.appendChild(password);

    let submit = document.createElement('input');
    submit.setAttribute('type', 'button');
    submit.setAttribute('value', 'Login');
    div.appendChild(submit);

    submit.addEventListener("click", () => {
        loginCallback(username.value, password.value);
    });

    return div;
}

function SignupModule(signupCallback) {
    const div = document.createElement("div");
    div.classList.add("FormModule");
    const header = document.createElement("h3");
    header.innerText = "Sign Up";
    div.appendChild(header);


    let username = document.createElement('input'); 
    username.setAttribute('type', 'text');
    username.setAttribute('placeholder', 'Username');
    div.appendChild(username);

    let password = document.createElement('input'); 
    password.setAttribute('type', 'password');
    password.setAttribute('placeholder', 'Password');
    div.appendChild(password);

    let passwordConf = document.createElement('input'); 
    passwordConf.setAttribute('type', 'password');
    passwordConf.setAttribute('placeholder', 'Retype Password');
    div.appendChild(passwordConf);

    let submit = document.createElement('input');
    submit.setAttribute('type', 'button');
    submit.setAttribute('value', 'Sign Up');
    div.appendChild(submit);

    submit.addEventListener("click", () => {
        signupCallback(username.value, password.value, passwordConf.value);
    });

    return div;
}

