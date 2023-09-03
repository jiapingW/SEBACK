from langchain.schema import BaseMessage
from langchain.text_splitter import CharacterTextSplitter, RecursiveCharacterTextSplitter
from langchain.chains import ReduceDocumentsChain, MapReduceDocumentsChain
from langchain.chat_models import AzureChatOpenAI
from settings import BASE_URL, API_KEY, API_VERSION, API_TYPE, DEPLOYMENT_NAME
from segpt.prompts.map_reduce import map_prompt, reduce_prompt
from langchain.chains import LLMChain
from langchain.chains.combine_documents.stuff import StuffDocumentsChain
from langchain.document_loaders import DirectoryLoader
from pathlib import Path



PROMPT_TEMPLATE = """ 
Returns a concise summary capturing the main points of the conversation.
CONVERSATION 
"""

class Memory:
    file_path: str = None  # 路径应该为{workspace}/memory
        
    def __init__(self, role_id: str):
        self.file_name: int = 1
        self.role_id: str = role_id
        
    # 设置file_path同时创建memory目录和角色目录    
    def set_file_path(filePath: str):
        path = Path(filePath)
        Memory.file_path = filePath
        path.mkdir(parents=True, exist_ok=True)
    
    def set_role_id(self, roleId: str):
        self.role_id = roleId
        
    # 参数是两条message
    def add(self, message: BaseMessage):
        if self.file_name == 1:
            #创建Memory.file_path+"/"+self.role_id文件夹
            path = Path(Memory.file_path+"/"+self.role_id)
            path.mkdir(parents=True, exist_ok=True)
        with open(Memory.file_path+"/"+self.role_id+"/"+str(self.file_name)+".txt", 'w') as f:
            f.write(message.type+":"+message.content)
        self.file_name += 1
    
    # 将file_path下的role_id下的所有md文件全部load
    def load_directory(self):
        print()
        loader = DirectoryLoader(Memory.file_path+"/"+self.role_id+"/", glob="**/*.txt", show_progress=True)
        docs = loader.load()
        return docs
    
    def get_summary(self):
        if self.file_name == 1:
            return ""
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=800,
            chunk_overlap=0,
            # length_function=len,
            # is_separator_regex=False,
        )
        llm = AzureChatOpenAI(
            openai_api_base=BASE_URL,
            openai_api_version=API_VERSION,
            deployment_name=DEPLOYMENT_NAME,
            openai_api_key=API_KEY,
            openai_api_type=API_TYPE, 
        )
        map_chain = LLMChain(llm=llm, prompt=map_prompt)
        reduce_chain = LLMChain(llm=llm, prompt=reduce_prompt)
        # Takes a list of documents, combines them into a single string, and passes this to an LLMChain
        combine_documents_chain = StuffDocumentsChain(
            llm_chain=reduce_chain, document_variable_name="doc_summaries"
        )
        # Combines and iteravely reduces the mapped documents
        reduce_documents_chain = ReduceDocumentsChain(
            # This is final chain that is called.
            combine_documents_chain=combine_documents_chain,
            # If documents exceed context for `StuffDocumentsChain`
            collapse_documents_chain=combine_documents_chain,
            # The maximum number of tokens to group documents into.
            token_max=4000,
        )
        # Combining documents by mapping a chain over them, then combining results
        map_reduce_chain = MapReduceDocumentsChain(
            # Map chain
            llm_chain=map_chain,
            # Reduce chain
            reduce_documents_chain=reduce_documents_chain,
            # The variable name in the llm_chain to put the documents in
            document_variable_name="docs",
            # Return the results of the map steps in the output
            return_intermediate_steps=False,
        )

        # text_splitter = CharacterTextSplitter.from_tiktoken_encoder(
        #     chunk_size=1000, chunk_overlap=0
        # )
        
        split_docs = text_splitter.split_documents(self.load_directory())
        summary = map_reduce_chain.run(split_docs)
        return summary
    
