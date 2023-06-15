$(document).ready(function(){
    setTimeout(function(){
        $("#loading-screen").fadeOut(4000, function () {
            $(this).addClass('fadeOut');
        });
    }, 200); // delay of 0.2 second before beginning the fadeout
    var socket = io.connect();  // Connect to the server-side socket. Adjust the URL as necessary.

    $('#topics').change(function() {
        if (this.checked) {
            $('#viewpoints-filter').fadeIn();
        } else {
            $('#viewpoints-filter').fadeOut();
            $('#viewpoints').prop('checked', false);
            $('#arguments-filter').fadeOut();
            $('#arguments').prop('checked', false);
        }
    });

    $('#viewpoints').change(function() {
        if (this.checked) {
            $('#arguments-filter').fadeIn();
        } else {
            $('#arguments-filter').fadeOut();
            $('#arguments').prop('checked', false);
        }
    });

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
        //console.log(data);

        // If no checkboxes are checked, show a notification
        if (!data.topics) {
            showNotification("You must at least select topics for deliberAIde to work.");
            return;  // Exit the function
        }
        // Check if the text is empty or if the length is less than the required minimum


        if (!data.text || data.text.trim().length === 0) {
            console.log("About to show notification...");
            showNotification("A transcript must be entered for deliberAIde to assist you.");
            return;  // Exit the function
        }
        if (data.text.trim().length < 100) {
            console.log("About to show notification...");
            showNotification("Sorry, you must enter a longer transcript for deliberAIde to assist you.");
            return;  // Exit the function
        }

        // Emit the button_called event, sending the data
        socket.emit('button_called', data);

        // Set the min-height property of the #output div
        $('#output').css('min-height', '400px');
        $('#status-message').text('Generating topics...');
    });

    // Listen for update events
    socket.on('update', function(data) {
        console.log("Received data: ", data);
        // Do something with the data. This depends on the structure of your data.
        if (data.topics_mindmap) {
            console.log('topics mindmap detected');
            // Append topics mindmap to the output div
            var topicsDiv = $('<div class="mermaid">');
            topicsDiv.text(data.topics_mindmap);
            topicsDiv.hide().appendTo('#output').fadeIn(1000);
            mermaid.init(undefined, topicsDiv);
            // Check if the mindmap is initialized
            console.log('topics mindmap initialized');
            if (data.viewpoints_filter) {
                $('#status-message').text('Generating viewpoints...');
            }
            else if (data.arguments_filter) {
                $('#status-message').text('Generating arguments...');
            }
            else {
                $('#status-message').text('Completed.');
            }
        }

        if (data.viewpoints_mindmap) {
            $('#output').html('');  // Clear the output div
            console.log('viewpoints mindmap detected');
            console.log(data.viewpoints);
            console.log('above is the raw viewpoints json, below is views mindmap string')
            // Append topics mindmap to the output div
            var viewpointsDiv = $('<div class="mermaid">');
            viewpointsDiv.text(data.viewpoints_mindmap);
            console.log(viewpointsDiv);
            viewpointsDiv.hide().appendTo('#output').fadeIn(1000);
            mermaid.init(undefined, viewpointsDiv);
            // Check if the mindmap is initialized
            console.log('viewpoints mindmap initialized');
            if (data.arguments_filter) {
                $('#status-message').text('Generating arguments...');
            }
            else {
                $('#status-message').text('Completed.');
            }
        }

        if (data.arguments_mindmap) {
            $('#output').html('');  // Clear the output div
            console.log('arguments mindmap detected');
            console.log(data.arguments);
            console.log('above is the raw arguments json, below is args mindmap string')
            console.log(data.arguments_mindmap);
            // Append topics mindmap to the output div
            var argumentsDiv = $('<div class="mermaid">');
            argumentsDiv.text(data.arguments_mindmap);
            console.log(argumentsDiv);
            argumentsDiv.hide().appendTo('#output').fadeIn(1000);
            mermaid.init(undefined, argumentsDiv);
            // Check if the mindmap is initialized
            console.log('arguments mindmap initialized');
            $('#status-message').text('Completed.')
        }


        $('html, body').animate({
            scrollTop: $("#output").offset().top
        }, 2000); // 2000 milliseconds for scrolling

    // Listen for error events
    socket.on('error', function(data) {
        console.log("Error: " + data.error);
    });
    });
});

function showNotification(message) {
    // Insert the message text
    $("#notificationText").html(message);
    // Show the modal
    $("#notificationModal").modal('show');

    // Hide the modal after 3 seconds
    setTimeout(function(){
        $("#notificationModal").modal('hide');
    }, 5000);  // in milliseconds
}

      //var output = document.getElementById('output'); Old scroll
      //output.scrollIntoView({behavior: "smooth"});


      // if(data.topics) {
      //     var topicsDiv = $('<div>');
      //     // append topics to the output div
      //     var topicsHTML = '<br><h2> Here are the topics:</h2>';
      //     topicsHTML += '<p>' + data.topics.main_topic + '</p>';
      //     topicsDiv.html(topicsHTML);
      //     topicsDiv.hide().appendTo('#output').fadeIn(1000);

      //     console.log('topics as a list appended');
      // }

      // if(data.viewpoints) {
      //     // Append viewpoints to the output div
      //     var viewpointsDiv = $('<div>');
      //     var viewpointsHTML = '<br><h2> Here are the viewpoints:</h2>';

      //     // Iterate over the viewpoints array
      //     $.each(data.viewpoints.viewpoints, function(index, viewpointObj){
      //         // Access viewpoint and append to HTML
      //         var viewpoint = viewpointObj.viewpoint;
      //         console.log("viewpoint here is: ", viewpoint);
      //         viewpointsHTML += '<p>' + viewpoint + '</p>';

      //         // Check for any sub-viewpoints and append
      //         var subViewpoints = viewpointObj.sub_viewpoints;
      //         $.each(subViewpoints, function(index, subViewpointObj){
      //             var subViewpoint = subViewpointObj.viewpoint;
      //             console.log("Subviewpoint here is: ", subViewpoint);
      //             viewpointsHTML += '<p>---' + subViewpoint + '</p>';
      //         });
      //     });

      //     viewpointsDiv.html(viewpointsHTML);
      //     viewpointsDiv.hide().appendTo('#output').fadeIn(1000);

      //     // Check if viewpoints are appended
      //     console.log('viewpoints appended');
      // if(data.arguments) {
      //     // Append arguments to the output div
      //     var argumentsHTML = '<br><h2> Here are the arguments:</h2>';
      //     var argumentsDiv = $('<div>');
      //     // Iterate over the viewpoints array
      //     $.each(data.arguments.viewpoints, function(index, viewpointObj){
      //         // Access viewpoint
      //         //var viewpoint = viewpointObj.viewpoint;
      //         // console.log("viewpoint here is: ", viewpoint);
      //         // argumentsHTML += '<p><strong>' + viewpoint + '</strong></p>';

      //         // Access and append each argument for the viewpoint
      //         var arguments = viewpointObj.arguments;
      //         $.each(arguments, function(index, argumentObj){
      //             var argumentSummary = argumentObj.summary;
      //             console.log("Argument summary here is: ", argumentSummary);
      //             argumentsHTML += '<p>-- ' + argumentSummary + '</p>';
      //         });
      //     });
      //     argumentsDiv.html(argumentsHTML);
      //     //$('#output').append(argumentsHTML);
      //     argumentsDiv.hide().appendTo('#output').fadeIn(1000);
      //     //$('#output').hide().fadeIn(1000);  // Add this line for fade in
      //     console.log('arguments appended');
      // }
