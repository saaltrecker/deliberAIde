$(document).ready(function(){
    $('.main-button').click(function(e){
        e.preventDefault(); // Prevent the form from being submitted normally

        // Prepare the data to be sent
        var data = {
            text: $('[name=text]').val(),
            topics: $('#topics').is(':checked'),
            viewpoints: $('#viewpoints').is(':checked'),
            arguments: $('#arguments').is(':checked'),
        };
        console.log(data);

        // Send the AJAX request
        $.ajax({
            url: '/process_mission',
            type: 'POST',
            contentType: 'application/json',  // tell the server you're sending JSON
            data: JSON.stringify(data),
            success: function(response){
                // Initiate a new event source
            console.log("SUCCESS RESPONSE: ", response);
            const source = new EventSource("/process_mission");
            // When a message is received, handle it
            source.onmessage = function(event) {
                let jsonString = event.data.replace('data: ', '').trim();
                var response = JSON.parse(jsonString);
                console.log(response);

                if(response.error) {
                    alert(response.error);
                    source.close();  // Close the connection if an error occurs
                    return;
                }

                if(response.topics) {
                    // append topics to the output div
                    var topicsHTML = '<h2> Here are the topics:</h2><br>';
                    $.each(response.topics, function(i, topic){
                        topicsHTML += '<p>' + topic + '</p>';
                    });
                    $('#output').append(topicsHTML);
                    console.log('topics appended');
                }

                if(response.viewpoints) {
                    // append viewpoints to the output div
                    var viewpointsHTML = '<h2> Here are the viewpoints:</h2><br>';
                    $.each(response.viewpoints, function(i, viewpoint){
                        viewpointsHTML += '<p>' + viewpoint + '</p>';
                    });
                    $('#output').append(viewpointsHTML);
                    console.log('viewpoints appended');
                }

                if(response.arguments) {
                    // append arguments to the output div
                    var argumentsHTML = '<h2> Here are the arguments:</h2><br>';
                    $.each(response.arguments, function(i, argument){
                        argumentsHTML += '<p>' + argument + '</p>';
                    });
                    $('#output').append(argumentsHTML);
                    console.log('arguments appended');
                }
            };

            // When an error occurs, handle it
            source.onerror = function(event) {
                console.error("EventSource failed:", event);
                source.close();  // Close the connection if an error occurs
            };
        },
        error: function(xhr, status, error){
            console.log("Error: " + error);

        }
    });
    console.log('ajax request sent');
});
});