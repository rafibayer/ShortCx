const {GetShortcutRequest} = require('./apiservice_pb.js');
const {APIServiceClient} = require('./apiservice_grpc_web_pb.js');

function hello() {
    const h1 = document.createElement("h1");
    h1.innerText = "ShortCx! Redirecting..."
    return h1
}

function backupLink(url) {
    const p = document.createElement("p");
    p.innerText = "You should be redirected shortly...";
    const a = document.createElement("a");
    a.href = url;
    a.title = "Click Here to go now!"
    p.appendChild(a);
    return p;
}

function getToken() {
    let segments = window.location.href.split("/");
    let token = segments.pop() || segments.pop();
    console.log("Token: " + token);
    return token;
}
document.body.appendChild(hello());
let token = getToken();

// TODO either resolve URL from window location, or inject with webpack .env
let shortCxClient = new APIServiceClient("http://localhost:8080");
let request = new GetShortcutRequest();
request.setUrlToken(token);
shortCxClient.getShortcut(request, {}, (err, resp) => {
    if (err) {
        console.error(err);
    } else {
        let destination = resp.toObject().targetUrl;
        document.body.appendChild(backupLink(destination));
        window.location.replace(destination);
    }
});
