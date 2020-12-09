const { LoginRequest, LogoutRequest, CreateUserRequest,
        GetSessionRequest, CreateShortcutRequest, DeleteShortcutRequest,
        GetAllShortcutsRequest} = require('./apiservice_pb.js');
const {APIServiceClient} = require('./apiservice_grpc_web_pb.js');

// TODO: resolve or get endpoint from .env
let shortCxClient = new APIServiceClient("http://localhost:8080");

// Populate login/signup or account/signout
window.addEventListener('load', function() {
    PopulatePage();
});

function PopulatePage() {
    let accounts = document.getElementById("accounts");
    let creation = document.getElementById("creation");
    let management = document.getElementById("management");
    let authToken = localStorage.getItem("Authorization");
    let foundSession = false;
    
    if (authToken) {
        let request = new GetSessionRequest();
        request.setAuthToken(authToken);
        shortCxClient.getSession(request, {}, (err, resp) => {
            if (err) {
                console.warn("Session invalid or expired: " + err);
            } else {
                clearContents(accounts);
                clearContents(creation);
                clearContents(management);
                foundSession = true;
                let respObj = resp.toObject();
                accounts.appendChild(AccountModule(respObj.username, DoLogout));
                creation.appendChild(ShortcutCreateModule(DoCreate));
                management.appendChild(ManagementModule());
            }
        });
    } 

    // No token or expired session -> login/signup modules
    if (!foundSession) {
        clearContents(accounts);
        clearContents(creation);
        clearContents(management);
        accounts.appendChild(LoginModule(DoLogin));
        accounts.appendChild(SignupModule(DoSignup));
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
            alert(err.message);
            console.error(err);
        } else {
            let respObj = resp.toObject();
            localStorage.setItem("Authorization", respObj.authToken);
            console.log("Login Succeeded!");
            PopulatePage();
        }
    });
}

function DoLogout() {
    let request = new LogoutRequest();
    request.setAuthToken(localStorage.getItem("Authorization"));

    shortCxClient.logout(request, {}, (err, resp) => {
        if (err) {
            alert(err.message);
            console.error(err);
        } else {
            localStorage.removeItem("Authorization");
            console.log("Successfully logged out!");
            PopulatePage();
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
            alert(err.message);
            console.error(err);
        } else {
            let respObj = resp.toObject();
            localStorage.setItem("Authorization", respObj.authToken);
            console.log("Creation Succeeded");
            PopulatePage();
        }
    });
}

function DoCreate(targetUrl) {
    let request = new CreateShortcutRequest();
    request.setAuthToken(localStorage.getItem("Authorization"));
    request.setTargetUrl(targetUrl);
    
    shortCxClient.createShortcut(request, {}, (err, resp) => {
        if (err) {
            alert(err.message);
            console.error(err);
        } else {
            let respObj = resp.toObject().shortcut;
            let management = document.getElementById("management");
            management.appendChild(ShortcutDetailModule(
                respObj.urlToken,
                respObj.targetUrl,
                respObj.createdAt,
                respObj.visits));
        }
    })
}

function DoDelete(urlToken, element) {
    let request = new DeleteShortcutRequest();
    request.setAuthToken(localStorage.getItem("Authorization"));
    request.setUrlToken(urlToken);

    shortCxClient.deleteShortcut(request, {}, (err, resp) => {
        if (err) {
            alert(err.message);
            console.error(err);
        } else {
            element.parentNode.removeChild(element);
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

function ShortcutCreateModule(createCallback) {
    const div = document.createElement("div");
    div.classList.add("FormModule");
    const header = document.createElement("h3");
    header.innerText = "Create Shortcut";
    div.appendChild(header);
    
    let targetUrl = document.createElement('input'); 
    targetUrl.setAttribute('type', 'text');
    targetUrl.setAttribute('placeholder', 'Destination');
    div.appendChild(targetUrl);

    let create = document.createElement('input');
    create.setAttribute('type', 'button');
    create.setAttribute('value', 'Create Shortcut');
    div.appendChild(create);

    create.addEventListener("click", () => {
        createCallback(targetUrl.value);
    });
    return div;
}

function ManagementModule() {
    let div = document.createElement("div");
    let request = new GetAllShortcutsRequest();
    request.setAuthToken(localStorage.getItem("Authorization"));

    shortCxClient.getAllShortcuts(request, {}, (err, resp) => {
        if (err) {
            alert(err.message);
            console.error(err);
        } else {
            let allItems = resp.toObject().shortcutsList;
            allItems.forEach(shortcut => {
                div.appendChild(
                    ShortcutDetailModule(
                        shortcut.urlToken,
                        shortcut.targetUrl,
                        shortcut.createdAt,
                        shortcut.visits));
            });
        }
    });

    return div;
}

function ShortcutDetailModule(token, target, createdAt, visits) {
    let div = document.createElement("div");
    div.classList.add("ShortcutDetail");

    let header = document.createElement("h3");
    header.innerText =  `${window.location.host}/${token}`;
    div.appendChild(header);

    let anchor = document.createElement("a");
    anchor.setAttribute("href", target);
    anchor.innerText = target;
    div.appendChild(anchor);

    let date = document.createElement("p");
    date.innerText = `Created on ${createdAt}`;
    div.appendChild(date);

    let visitsDisp = document.createElement("p");
    visitsDisp.innerText = `Visits: ${visits}`;
    div.appendChild(visitsDisp);

    let deleteBtn = document.createElement("input");
    deleteBtn.setAttribute('type', 'button');
    deleteBtn.setAttribute('value', 'Delete');
    div.appendChild(deleteBtn);

    deleteBtn.addEventListener("click", () => {
        if (confirm("Delete this shortcut?")) {
            DoDelete(token, div);
        }
    });
    return div;
}

