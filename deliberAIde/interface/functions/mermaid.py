#topics json to one or multiple Mermaid mindmaps (if multiple topics) that have to be rendered separately
def topics_json_to_mermaid_mindmap(output: dict):
    mermaid_graphs = []
    main_topics = output.get('main_topics') or [output.get('main_topic')]
    if main_topics:
        for topic in main_topics:
            mermaid_graph = f'mindmap\n  root(({topic}))\n'
            mermaid_graph += '\n'
            mermaid_graphs.append(mermaid_graph)
    return mermaid_graphs

#viewpoints json to one or multiple Mermaid mindmaps (if multiple viewpoints) that have to be rendered separately
def views_json_to_mermaid_mindmap(output: dict):
    mermaid_graphs = []

    def process_viewpoints(viewpoints, indent='    '):
        mermaid_graph = ''
        for viewpoint in viewpoints:
            if isinstance(viewpoint, str):
                mermaid_graph += f'{indent}{viewpoint}\n'
            elif isinstance(viewpoint, dict):
                viewpoint_text = viewpoint.get('viewpoint') or viewpoint.get('sub_viewpoint')
                if viewpoint_text:
                    mermaid_graph += f'{indent}{viewpoint_text}\n'
                    arguments = viewpoint.get('arguments')
                    if arguments:
                        if isinstance(arguments, list):
                            for argument in arguments:
                                mermaid_graph += f'{indent}    [{argument}]\n'
                        else:
                            mermaid_graph += f'{indent}    [{arguments}]\n'
                    sub_viewpoints = viewpoint.get('sub_viewpoints') or []
                    mermaid_graph += process_viewpoints(sub_viewpoints, indent + '    ')
        return mermaid_graph

    if 'main_topics' in output:
        main_topics = output.get('main_topics')
        for topic in main_topics:
            topic_text = topic.get('topic')
            if topic_text:
                mermaid_graph = f'mindmap\n  root(({topic_text}))\n'
                viewpoints = topic.get('viewpoints') or []
                mermaid_graph += process_viewpoints(viewpoints)
                mermaid_graph += '\n'
                mermaid_graphs.append(mermaid_graph)
    else:
        main_topic = output.get('main_topic')
        if main_topic:
            mermaid_graph = f'mindmap\n  root(({main_topic}))\n'
            viewpoints = output.get('viewpoints') or []
            mermaid_graph += process_viewpoints(viewpoints)
            mermaid_graph += '\n'
            mermaid_graphs.append(mermaid_graph)
    return mermaid_graphs

#Arguments mindmap - working well and displaying arguments for sub-viewpoints
def args_json_to_mermaid_mindmap(output: dict):
    mermaid_graphs = []

    def process_viewpoints(viewpoints, indent='    '):
        mermaid_graph = ''
        for viewpoint in viewpoints:
            if isinstance(viewpoint, str):
                mermaid_graph += f'{indent}{viewpoint}\n'
            elif isinstance(viewpoint, dict):
                viewpoint_text = viewpoint.get('viewpoint') or viewpoint.get('sub_viewpoint')
                if viewpoint_text:
                    mermaid_graph += f'{indent}{viewpoint_text}\n'
                    arguments = viewpoint.get('arguments')
                    if arguments:
                        if isinstance(arguments, list):
                            for argument in arguments:
                                mermaid_graph += f'{indent}    [{argument}]\n'
                        else:
                            mermaid_graph += f'{indent}    [{arguments}]\n'
                    sub_viewpoints = viewpoint.get('sub_viewpoints') or []
                    mermaid_graph += process_viewpoints(sub_viewpoints, indent + '    ')
        return mermaid_graph

    if 'main_topics' in output:
        main_topics = output.get('main_topics')
        for topic in main_topics:
            topic_text = topic.get('topic')
            if topic_text:
                mermaid_graph = f'mindmap\n  root(({topic_text}))\n'
                viewpoints = topic.get('viewpoints') or []
                mermaid_graph += process_viewpoints(viewpoints)
                mermaid_graph += '\n'
                mermaid_graphs.append(mermaid_graph)
    else:
        main_topic = output.get('main_topic')
        if main_topic:
            mermaid_graph = f'mindmap\n  root(({main_topic}))\n'
            viewpoints = output.get('viewpoints') or []
            mermaid_graph += process_viewpoints(viewpoints)
            mermaid_graph += '\n'
            mermaid_graphs.append(mermaid_graph)
    return mermaid_graphs