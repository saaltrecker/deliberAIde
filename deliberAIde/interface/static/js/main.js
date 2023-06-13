// $(document).ready(function(){
//     $('.main-button').click(function(e){
//         e.preventDefault(); // Prevent the form from being submitted normally

//         // Prepare the data to be sent
//         var data = {
//             text: $('[name=text]').val(),
//             topics: $('#topics').is(':checked'),
//             viewpoints: $('#viewpoints').is(':checked'),
//             arguments: $('#arguments').is(':checked'),
//         };
//         console.log(data);

//         // Send the AJAX request
//         $.ajax({
//             url: '/process_mission',
//             type: 'post',
//             dataType: 'json',  // you're expecting a JSON response
//             contentType: 'application/json',  // tell the server you're sending JSON
//             data: JSON.stringify(data),
//             success: function(response){
//                 // Check for an error message in the response
//                 if (response.error) {
//                     alert(response.error);
//                     return;
//                 }

//                 if(response.topics) {
//                     // append topics to the output div
//                     var topicsHTML = '<h2> Here are the topics:</h2><br>';
//                     $.each(response.topics, function(i, topic){
//                         topicsHTML += '<p>' + topic + '</p>';
//                     });
//                     $('#output').append(topicsHTML);
//                     console.log('topics appended');
//                 }
                
//                 if(response.viewpoints) {
//                     // append viewpoints to the output div
//                     var viewpointsHTML = '<h2> Here are the viewpoints</h2><br>';
//                     $.each(response.viewpoints, function(i, viewpoint){
//                         viewpointsHTML += '<p>' + viewpoint + '</p>';
//                     });
//                     $('#output').append(viewpointsHTML);
//                     console.log('views appended');
//                 }
                
//                 if(response.arguments) {
//                     // append arguments to the output div
//                     var argumentsHTML = '<h2> Here are the arguments</h2><br>';
//                     $.each(response.arguments, function(i, argument){
//                         argumentsHTML += '<p>' + argument + '</p>';
//                     });
//                     $('#output').append(argumentsHTML);
//                     console.log('arguments appended');
//                 }
//             },
//             error: function(xhr, status, error){
//                 console.log("Error: " + error);
//             }
//         });
//         console.log('ajax request sent');
//     });
// });

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
        type: 'post',
        dataType: 'json',  // you're expecting a JSON response
        contentType: 'application/json',  // tell the server you're sending JSON
        data: JSON.stringify(data),
        success: function(response){
            console.log('success')
            // Initiate a new event source
            var source = new EventSource("/process_mission");

            // When a message is received, handle it
            source.onmessage = function(event) {
                var response = JSON.parse(event.data);

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
                    var viewpointsHTML = '<h2> Here are the viewpoints</h2><br>';
                    $.each(response.viewpoints, function(i, viewpoint){
                        viewpointsHTML += '<p>' + viewpoint + '</p>';
                    });
                    $('#output').append(viewpointsHTML);
                    console.log('views appended');
                }
                
                if(response.arguments) {
                    // append arguments to the output div
                    var argumentsHTML = '<h2> Here are the arguments</h2><br>';
                    $.each(response.arguments, function(i, argument){
                        argumentsHTML += '<p>' + argument + '</p>';
                    });
                    $('#output').append(argumentsHTML);
                    console.log('arguments appended');
                }
            };

            source.onerror = function(event) {
                source.close();  // Close the connection if an error occurs
            }
        },
        error: function(xhr, status, error){
            console.log("Error: " + error);
        }
    });
    console.log('ajax request sent');
});