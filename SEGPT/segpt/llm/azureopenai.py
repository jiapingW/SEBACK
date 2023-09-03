from settings import API_KEY, API_TYPE, API_VERSION, BASE_URL, DEPLOYMENT_NAME, EMBEDDING_API_KEY, EMBEDDING_URL, DEPLOYMENT
from langchain.chat_models import AzureChatOpenAI
from langchain.embeddings import OpenAIEmbeddings


class AzureOpenAI:
    def __init__(self) -> None:
        self.model = AzureChatOpenAI(
            openai_api_base=BASE_URL,
            openai_api_version=API_VERSION,
            deployment_name=DEPLOYMENT_NAME,
            openai_api_key=API_KEY,
            openai_api_type=API_TYPE,
        )
        
    def get_model(self):
        return self.model
    
    
class OpenAIEmbedding:
    def __init__(self) -> None:
        self.model = self.embeddings = OpenAIEmbeddings(
            openai_api_base=EMBEDDING_URL,
            openai_api_version=API_VERSION,
            openai_api_key=EMBEDDING_API_KEY,
            openai_api_type=API_TYPE,
            deployment=DEPLOYMENT,
        )
    
    def get_model(self):
        return self.model