function enAction() {
  const input = document.getElementById("input-field").value;
  fetch("/encode", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      text: input,
    }),
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.msg) {
        document.getElementById("output").innerText = data.msg;
      } else {
        document.getElementById("output").innerText = "error";
      }
    });
}

function deAction() {
  const input = document.getElementById("input-field").value;
  fetch("/decode", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      text: input,
    }),
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.msg) {
        document.getElementById("output").innerText = data.msg;
      } else {
        document.getElementById("output").innerText = "error";
      }
    });
}
