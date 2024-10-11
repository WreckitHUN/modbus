let start = document.querySelector("#start")
let stopp = document.querySelector("#stop")

start.addEventListener("mousedown", () => {sendCommand("start1")} )
start.addEventListener("mouseup", () => {sendCommand("stop1")})
stopp.addEventListener("mousedown", () => {sendCommand("start2")})
stopp.addEventListener("mouseup", () => {sendCommand("stop2")})

function sendCommand(command) {
    fetch('/send-command', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ command: command })
    })
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error('Error:', error));
}