PROMPT_TEMPLATE = """
# Context
{context}

# Doucment
{document}

# Feedback
{feedback}
-----
Your task now is to revise the 'Doucment' in accordance with the 'Feedback'. 
Make sure to address the Feedback adequately while maintaining the format of the document.
Attention: Only return the content of modified document, begining with '##', not '#'
"""