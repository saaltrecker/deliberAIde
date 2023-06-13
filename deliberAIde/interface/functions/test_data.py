
topics_json = {'main_topic': 'Animal testing in medical research'}

viewpoints_by_topics = {'main_topic': 'Animal testing in medical research', 
                   'viewpoints': 
                       {'Necessity for medical advancements': {}, 
                        'Ethical concerns': {}, 
                        'Alternatives to animal testing': {}, 
                        'Regulation and minimization': 
                            {'sub-viewpoints': {'Transparency and accountability': {}
                                                }
                                }
                       }
}

arguments_by_viewpoints = {'arguments': {'main_topic': 'Animal testing in medical research', 
                  'viewpoints': 
                      {'Necessity for medical advancements': 
                          {'arguments': ['Contributions to numerous medical advancements', 'Development of life-saving treatments']}, 
                          'Ethical concerns': 
                              {'arguments': ['Animals deserve compassionate treatment', 'Animals should not suffer for human benefits']}, 
                              'Alternatives to animal testing': {'arguments': ['In vitro testing and computer simulations as reliable alternatives', 'Prioritizing development and adoption of alternatives']}, 
                              'Regulation and minimization': 
                                  {'sub-viewpoints': {'Transparency and accountability': 
                                      {'arguments': ['Need for clear justifications for animal use', 'Ensuring humane conduct in animal testing']}
                                      }
                                }
                    }
                }
}

def get_topics(transcript: str):
    return topics_json

def get_viewpoints_by_topic(viewpoints, transcript: str):
    return viewpoints_by_topics
def get_arguments_by_viewpoint(viewpoints: str):
    return arguments_by_viewpoints