from const import DATA_PATH
from langchain.embeddings import OpenAIEmbeddings
from settings import API_VERSION, API_TYPE, EMBEDDING_URL, EMBEDDING_API_KEY, DEPLOYMENT
from segpt.actions.get_folder_name import GETProductName
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.document_loaders import TextLoader


class MemoryStorage():
    def __init__(self, role_id: str):   # role_id为角色的名称
        self.role_id = role_id  # 当前memory归属的role
        self.embeddings = OpenAIEmbeddings(
            openai_api_base=EMBEDDING_URL,
            openai_api_version=API_VERSION,
            openai_api_key=EMBEDDING_API_KEY,
            openai_api_type=API_TYPE,
            deployment=DEPLOYMENT,
        )
        self.faiss = None
    
    # 根据不同的role使用不同的文件来进行memory的embedding
    def add(self, filePath: str):
        document = TextLoader(filePath).load()
        text_splitter = text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=800,
            chunk_overlap=0,
            # length_function=len,
            is_separator_regex=False,
        )
        if self.faiss is None:
            self.faiss = FAISS.from_documents(text_splitter.split_documents(document), self.embeddings)
        else:
            self.faiss.add_documents(document)
     
    # 将memory进行存储到文件   
    def persist(self):
        self.faiss.save_local(str(GETProductName.workspace)+self.role_id+"/memory/faiss_index")
        
    # 搜索最相关的k条memory,k=0表示全部取出
    def similarity_search(self, query: str, k: int = 0):
        docs = self.similarity_search(query=query, k=k)
        # 目前是这样的形式[Document(page_content='Tomorrow is sunny.We can go hiking.', metadata={'source': '2.txt'}), Document(page_content='## Original Requirements....,metadata={...}]
        return docs
        # 下面是处理后的形式
        ## Original Requirements:
        # Tomorrow is sunny.We can go hiking.
        # Create a snake cli game

        # ## Product Goals:

        # - Develop a command-line interface (CLI) snake game that is interactive and enjoyable to play.
        # - Implement smooth and responsive snake movement with intuitive controls.
        # - Provide a visually appealing and user-friendly game interface.

        ## User Stories:
        # ans = ""
        # for doc in docs:
        #     ans.append(doc.page_content)
        # return ans
    
    # 使用faiss_index文件夹构造faiss
    def load_faiss(self, index_file_path: str):
        db = FAISS.load_local(str(GETProductName.workspace)+self.role_id+"/memory/faiss_index", self.embeddings)
        return db
        
        
    