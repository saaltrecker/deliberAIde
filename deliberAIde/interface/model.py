# import csv

# ## Getting transcript from csv file
# with open('/Users/colmofuarthain/code/saaltrecker/deliberAIde/deliberAIde/data/validation_one.csv', newline='') as csvfile:
#     test_transcript = csv.reader(csvfile, delimiter=' ', quotechar='|')
#     for row in test_transcript:
#         test_transcript = ' '.join(row)


def deliberaide_output(transcript: str): # Mock function, replace with our finished model function
    """This function takes in the transcript and returns a string of the output from our model.
    For our testing purposes of the HTML, it will just return a string saying 'deliberaide is working!'"""
    targets = {'topics': ['topic1', 'topic2', 'topic3'], 
                    'viewpoints': ['viewpoint1', 'viewpoint2', 'viewpoint3'],
                    'arguments': ['arg1', 'arg2', 'arg3']
    }
    return targets