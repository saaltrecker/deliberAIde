
topics_json = {'main_topic': 'Animal testing in medical research'}

viewpoints_by_topics = {'main_topic': 'Animal testing in medical research', 
                        'viewpoints': [
                            {'viewpoint': 'Necessity for medical advancements', 
                             'sub_viewpoints': []}, 
                            {'viewpoint': 'Ethical concerns and animal welfare', 
                             'sub_viewpoints': []}, 
                            {'viewpoint': 'Alternatives to animal testing', 
                             'sub_viewpoints': []}, 
                            {'viewpoint': 'Regulation and minimization', 
                             'sub_viewpoints': []}, 
                            {'viewpoint': 'Transparency and accountability', 
                             'sub_viewpoints': []}
                        ]
        }

arguments_by_viewpoints =  {"main_topic": "Animal testing in medical research",
        "viewpoints": [
            {
                "viewpoint": "Necessity for medical advancements",
                "sub_viewpoints": [],
                "arguments": [
                    {
                        "summary": "Animal testing contributes to numerous medical advancements and development of life-saving treatments"
                    }
                ]
            },
            {
                "viewpoint": "Ethical concerns and animal welfare",
                "sub_viewpoints": [],
                "arguments": [
                    {
                        "summary": "Animals deserve compassionate treatment and should not suffer for human benefits"
                    }
                ]
            },
            {
                "viewpoint": "Alternatives to animal testing",
                "sub_viewpoints": [],
                "arguments": [
                    {
                        "summary": "In vitro testing and computer simulations can provide reliable results without harming animals"
                    }
                ]
            },
            {
                "viewpoint": "Regulation and minimization",
                "sub_viewpoints": [],
                "arguments": [
                    {
                        "summary": "Striking a balance between scientific progress and animal welfare is crucial"
                    }
                ]
            },
            {
                "viewpoint": "Transparency and accountability",
                "sub_viewpoints": [],
                "arguments": [
                    {
                        "summary": "Researchers should provide clear justifications for using animals and ensure humane conduct"
                    }
                ]
            }
        ]
    }

def get_topics(transcript: str):
    return topics_json

def get_viewpoints_by_topic(viewpoints, transcript: str):
    return viewpoints_by_topics
def get_arguments_by_viewpoint(text, viewpoints: str):
    return arguments_by_viewpoints