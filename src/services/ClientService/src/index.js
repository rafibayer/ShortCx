const {LoginRequest, LogoutRequest, CreateUserRequest} = require('./apiservice_pb.js');
const {APIServiceClient} = require('./apiservice_grpc_web_pb.js');

// TODO: resolve or get endpoint from .env
let shortCxClient = new APIServiceClient("http://localhost:8080");

// Populate login/signup or account/signout
PopulateSessionModules();

function PopulateSessionModules() {
    let authToken = localStorage.getItem("Authorization");
    if (authToken) {
        // try to get state
        return;
    } 

    // No token or expired session -> login/signup modules
    document.body.appendChild(LoginModule(DoLogin));
    document.body.appendChild(SignupModule(DoSignup));

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
        }
    });
}

function LoginModule(callback) {
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
        callback(username.value, password.value);
    });

    return div;
}

function SignupModule(callback) {
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
        callback(username.value, password.value, passwordConf.value);
    });

    return div;
}

