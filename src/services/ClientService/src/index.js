function hello() {
    const h1 = document.createElement("h1");
    h1.innerText = "Hello ShortCx!"
    return h1
}
document.body.appendChild(hello());