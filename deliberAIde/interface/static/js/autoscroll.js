// This function runs when the page loads
document.addEventListener("DOMContentLoaded", function() {
    console.log("DOMContentLoaded event fired"); // Just some troubleshooting
    var shouldScroll = document.getElementById('should_scroll').value;
    console.log("Should scroll: " + shouldScroll); //Just some troubleshooting
    if (shouldScroll == 'True') { 
        //console.log("Scrolling to bottom"); // Just some troubleshooting
        //window.scrollTo(0, document.body.scrollHeight); // Just some troubleshooting
        var output = document.getElementById('output');
        output.scrollIntoView({behavior: "smooth"});
}
});