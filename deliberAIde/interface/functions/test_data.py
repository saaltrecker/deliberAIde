
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


views_format_2 = {'main_topic': 'Youth violence in the community and potential solutions', 
                  'viewpoints': 
                      {'Mentoring programs': {}, 
                       'Increased police presence': {}, 
                       'Addressing social issues': {}, 
                       'Support for families': {}, 
                       'Improving schools': {}, 
                       'Teaching healthy relationships and choices': {}
                     }
             }

args_format_2 = {'main_topic': 'Youth violence in the community and potential solutions', 
                 'viewpoints': 
                     {'Mentoring programs': 
                         {'arguments': 
                             ['Mentoring programs can address social issues and provide guidance to youths']
                             }, 
                        'Increased police presence': 
                            {'arguments': 
                                ['A stronger police presence can deter youth violence']}, 
                        'Addressing social issues': 
                            {'arguments': 
                                ['Tackling social issues can help reduce the root causes of youth violence']
                                }, 
                        'Support for families': 
                            {'arguments': 
                                ['Supporting families can improve family structure and reduce youth violence']
                                }, 
                        'Improving schools': 
                            {'arguments': 
                                ['Better-funded schools can offer quality education and extracurricular activities, reducing youth violence']
                                }, 
                        'Teaching healthy relationships and choices': 
                            {'arguments': 
                                ['Educating youths on healthy relationships and choices can counteract peer pressure and reduce violence']
                                }
                    }
             }

def get_topics(transcript: str):
    return topics_json

def get_viewpoints_by_topic(viewpoints, transcript: str):
    return viewpoints_by_topics
def get_arguments_by_viewpoint(text, viewpoints: str):
    return arguments_by_viewpoints