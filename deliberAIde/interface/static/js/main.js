$(document).ready(function(){
    var socket = io.connect('http://localhost:5000/');  // Connect to the server-side socket. Adjust the URL as necessary.

    $('.main-button').click(function(e){
        e.preventDefault();

        // Prepare the data to be sent
        var data = {
            text: $('[name=text]').val(),
            topics: $('#topics').is(':checked'),
            viewpoints: $('#viewpoints').is(':checked'),
            arguments: $('#arguments').is(':checked'),
        };

        console.log(data);

        // Emit the button_called event, sending the data
        socket.emit('button_called', data);
    });

    // Listen for update events
    socket.on('update', function(data) {
        console.log("Received data: ", data);
        // Do something with the data. This depends on the structure of your data.
        if(data.topics) {
            // append topics to the output div
            var topicsHTML = '<br><h2> Here are the topics:</h2>';
            topicsHTML += '<p>' + data.topics.main_topic + '</p>';
            $('#output').append(topicsHTML);
            console.log('topics appended');
        }
        if(data.viewpoints) {
            // Append viewpoints to the output div
            var viewpointsHTML = '<h2> Here are the viewpoints:</h2><br>';
        
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
        
            $('#output').append(viewpointsHTML);
            console.log('viewpoints appended');
        }
        
        if(data.arguments) {
            // Append arguments to the output div
            var argumentsHTML = '<h2> Here are the arguments:</h2><br>';
        
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
        
            $('#output').append(argumentsHTML);
            console.log('arguments appended');
        }
        
    // Listen for error events
    socket.on('error', function(data) {
        console.log("Error: " + data.error);
    });
    });
});
