from langchain.retrievers import BM25Retriever, EnsembleRetriever
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import AzureChatOpenAI
from settings import BASE_URL, DEPLOYMENT_NAME, API_KEY, API_VERSION, API_TYPE

from langchain.schema import BaseMessage
import tiktoken
from langchain.schema import (
    HumanMessage,
    BaseMessage,
)

PROMPT_TEMPLATE = """ Returns a concise summary capturing the main points of the conversation. \n CONVERSATION """

class Memory:
    def __init__(self) -> None:
        self.previous_summary = ""  # 上一次的summary
        self.messages = []
        self.notsum = 0
        # self.storage = []
        self.embedding = OpenAIEmbeddings(
            openai_api_base="https://wjp-gpt3.openai.azure.com/",
            openai_api_version="2023-03-15-preview",
            openai_api_key="7903f0912b9e4626bcb5412830524a83",
            openai_api_type="azure",
            deployment="text-embedding-ada-002"
        )
        self.model = AzureChatOpenAI(
            openai_api_base=BASE_URL,
            openai_api_version=API_VERSION,
            deployment_name=DEPLOYMENT_NAME,
            openai_api_key=API_KEY,
            openai_api_type=API_TYPE,
        )

    def add(self, message: BaseMessage):
        self.messages.append(message.type+":"+message.content)
        self.notsum += 1

    def get_summary(self):
        if self.notsum == 0:
            return self.previous_summary
        # 生成summary
        
        encoding = tiktoken.get_encoding("cl100k_base")
        previous_num = len(encoding.encode(PROMPT_TEMPLATE + self.previous_summary))
        
        later = ""
        for i in range(self.notsum):
            later = later + self.messages[i-self.notsum]
            if len(encoding.encode(later))+previous_num > 4000:
                later = self.model(PROMPT_TEMPLATE + self.messages).content
        summary = self.model([HumanMessage(content=PROMPT_TEMPLATE + self.previous_summary + later)])
        self.previous_summary = summary.content
        self.notsum = 0
        return summary.content
    
    def checkrelevant(self, task):
        """
        检索与task最相关的内容返回
        """
        print(self.previous_summary)
        bm25_retriever = BM25Retriever.from_texts(self.previous_summary)
        bm25_retriever.k = 2

        
        faiss_vectorstore = FAISS.from_texts(self.previous_summary, self.embedding)
        faiss_retriever = faiss_vectorstore.as_retriever(search_kwargs={"k": 1})

        # initialize the ensemble retriever
        ensemble_retriever = EnsembleRetriever(retrievers=[bm25_retriever, faiss_retriever], weights=[0.5, 0.5])
        docs = ensemble_retriever.get_relevant_documents(task)
        # 检索的最相关的多条信息，取出Document数据结构中的字符串内容，拼接成一个字符串返回
        return '\n'.join([i.page_content for i in docs])

if __name__ == "__main__":
    memory = Memory()
    memory.add(HumanMessage(content="hello"))
    memory.add(HumanMessage(content="hi"))
    print(memory.get_summary())