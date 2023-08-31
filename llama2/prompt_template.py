from langchain import PromptTemplate, LLMChain
from langchain import HuggingFacePipeline

llm = HuggingFacePipeline(pipeline = pipeline, model_kwargs = {'temperature':0}) # pipeline is created in model_download.py file

template = """
              You are an intelligent chatbot that gives out useful information to humans.
              You return the responses in sentences with arrows at the start of each sentence
              {query}
           """

prompt = PromptTemplate(template=template, input_variables=["query"])

llm_chain = LLMChain(prompt=prompt, llm=llm)