function myFunction() {
  var x = document.getElementById("score-container-2");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}

let timeout;

function myFunction() {
  timeout = setTimeout(alertFunc, 3000);
}

function alertFunc() {
  alert("Thank you for participating! Please answer some review questions about what you have learned. All recorded data is anonymous");
}