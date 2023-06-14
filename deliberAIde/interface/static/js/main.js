$(document).ready(function(){
    var socket = io.connect();  // Connect to the server-side socket. Adjust the URL as necessary.

    $('.main-button').click(function(e){
        e.preventDefault();

        $('#output').html('');  // Clear the output div

        // Prepare the data to be sent
        var data = {
            text: $('input[name=text]').val(),
            topics: $('#topics').is(':checked'),
            viewpoints: $('#viewpoints').is(':checked'),
            arguments: $('#arguments').is(':checked'),
        };

        console.log(data);

        // Emit the button_called event, sending the data
        socket.emit('button_called', data);

        // Set the min-height property of the #output div
        $('#output').css('min-height', '500px');
    });

    // Listen for update events
    socket.on('update', function(data) {
        console.log("Received data: ", data);
        // Do something with the data. This depends on the structure of your data.
        if(data.topics) {
            var topicsDiv = $('<div>');
            // append topics to the output div
            var topicsHTML = '<br><h2> Here are the topics:</h2>';
            topicsHTML += '<p>' + data.topics.main_topic + '</p>';
            topicsDiv.html(topicsHTML);
            //$('#output').append(topicsHTML);
            topicsDiv.hide().appendTo('#output').fadeIn(1000);
            console.log('topics appended');
        }
        if(data.viewpoints) {
            // Append viewpoints to the output div
            var viewpointsDiv = $('<div>');
            var viewpointsHTML = '<br><h2> Here are the viewpoints:</h2>';

            // Iterate over the viewpoints array
            $.each(data.viewpoints.viewpoints, function(index, viewpointObj){
                // Access viewpoint and append to HTML
                var viewpoint = viewpointObj.viewpoint;
                console.log("viewpoint here is: ", viewpoint);
                viewpointsHTML += '<p>' + viewpoint + '</p>';

                // Check for any sub-viewpoints and append
                var subViewpoints = viewpointObj.sub_viewpoints;
                $.each(subViewpoints, function(index, subViewpointObj){
                    var subViewpoint = subViewpointObj.viewpoint;
                    console.log("Subviewpoint here is: ", subViewpoint);
                    viewpointsHTML += '<p>---' + subViewpoint + '</p>';
                });
            });

            viewpointsDiv.html(viewpointsHTML);
            //$('#output').append(viewpointsHTML);
            viewpointsDiv.hide().appendTo('#output').fadeIn(1000);
            //$('#output').hide().fadeIn(1000);  // Add this line
            console.log('viewpoints appended');
        }
        if(data.arguments) {
            // Append arguments to the output div
            var argumentsHTML = '<br><h2> Here are the arguments:</h2>';
            var argumentsDiv = $('<div>');
            // Iterate over the viewpoints array
            $.each(data.arguments.viewpoints, function(index, viewpointObj){
                // Access viewpoint
                //var viewpoint = viewpointObj.viewpoint;
                // console.log("viewpoint here is: ", viewpoint);
                // argumentsHTML += '<p><strong>' + viewpoint + '</strong></p>';

                // Access and append each argument for the viewpoint
                var arguments = viewpointObj.arguments;
                $.each(arguments, function(index, argumentObj){
                    var argumentSummary = argumentObj.summary;
                    console.log("Argument summary here is: ", argumentSummary);
                    argumentsHTML += '<p>-- ' + argumentSummary + '</p>';
                });
            });
            argumentsDiv.html(argumentsHTML);
            //$('#output').append(argumentsHTML);
            argumentsDiv.hide().appendTo('#output').fadeIn(1000);
            //$('#output').hide().fadeIn(1000);  // Add this line for fade in
            console.log('arguments appended');
        }
        //var output = document.getElementById('output'); Old scroll
        //output.scrollIntoView({behavior: "smooth"});
        $('html, body').animate({
            scrollTop: $("#output").offset().top
        }, 2000); // 2000 milliseconds for scrolling

    // Listen for error events
    socket.on('error', function(data) {
        console.log("Error: " + data.error);
    });
    });
});
