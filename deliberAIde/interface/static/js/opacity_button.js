document.querySelector(".main-button").addEventListener("click", function() {
    this.style.opacity = "0.6";
    document.getElementById("operationMessage").textContent = "Currently fetching the topics... Standby";
    console.log("Button clicked!"); // Logs message to the console when the button is clicked
});