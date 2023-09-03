# Bring in deps
import os 

import streamlit as st 
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain 
from langchain.memory import ConversationBufferMemory
from langchain.utilities import WikipediaAPIWrapper 

from segpt.roles.architect import Architect
import sys
from segpt.roles.product_manager import ProductManager
from segpt.roles.architect import Architect
from segpt.roles.project_manager import ProjectManager
from segpt.roles.project_manager import ProjectManager
from segpt.roles.engineer import Engineer

import sys
import pymmd
# App framework
st.title('🦜🔗 SEGPT')
prompt = st.text_input('Plug in your idea here') 

if prompt: 
    pm = ProductManager()
    arch = Architect()
    pm2 = ProjectManager()
    eng = Engineer()

    output_requirment = pm.write_prd(prompt)
    print(output_requirment.content)
    st.markdown(output_requirment.content)
    
    output_design = arch.write_design(output_requirment)
    print(output_design.content)
    st.markdown(output_design.content)

    output_tasks = pm2.write_tasks(output_design)
    st.markdown(output_tasks.content)
    output_code = eng.write_code(output_tasks)
    
