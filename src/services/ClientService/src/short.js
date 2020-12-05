function hello() {
    const h1 = document.createElement("h1");
    h1.innerText = "ShortCx! Redirecting..."
    return h1
}

function getToken() {
    let segments = window.location.href.split("/");
    const token = segments.pop() || segments.pop();
    console.log("Token: " + token);
    return token;
}
document.body.appendChild(hello());

let token = getToken();
