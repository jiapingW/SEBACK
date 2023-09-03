from langchain.prompts import PromptTemplate
map_template = """The following is a set of documents
       {docs}
       Based on this list of docs, please identify the main themes 
       Helpful Answer:
"""

reduce_template = """The following is set of summaries:
{doc_summaries}
Take these and distill it into a final, consolidated summary of the main themes. 
Helpful Answer:
"""

map_prompt = PromptTemplate.from_template(map_template)
reduce_prompt = PromptTemplate.from_template(reduce_template)