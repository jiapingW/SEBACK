from langchain.chat_models import AzureChatOpenAI
from typing import List
from langchain.prompts.chat import (
    SystemMessagePromptTemplate,
)
from langchain.schema import (
    AIMessage,
    SystemMessage,
    HumanMessage,
    BaseMessage,
)
from segpt.prompts.role import PREFIX_TEMPLATE
from settings import BASE_URL, DEPLOYMENT_NAME, API_KEY, API_VERSION, API_TYPE
from segpt.memory.basic_memory import Memory

class SEAgent:
    # 所有agent共有一个memory，用来存储所有的对话记录。需要在run后将内容存到memory中
    history = {}

    def __init__(self, name="", profile="", goal="", constraints="", desc="") -> None:
        sys_prompt = SystemMessagePromptTemplate.from_template(PREFIX_TEMPLATE)
        self.system_message = sys_prompt.format_messages(
            profile=profile,
            name=name,
            goal=goal,
            constraints=constraints
        )[0]
        self.model = AzureChatOpenAI(
            openai_api_base=BASE_URL,
            openai_api_version=API_VERSION,
            deployment_name=DEPLOYMENT_NAME,
            openai_api_key=API_KEY,
            openai_api_type=API_TYPE,
            temperature=0.4,
        )
        self.memory = Memory()
        

    def reset(self) -> None:
        self.init_messages()

    def init_messages(self) -> None:
        # stored_messages中存的是符合langchain格式的message
        # self.stored_messages = [self.system_message]
        self.memory.add(self.system_message)

    def savemessage(self,messages:List[BaseMessage]):
        for message in messages:
            self.memory.add(message)
            
    def step(
        self,
        input_message: HumanMessage,
    ) -> AIMessage:
        # 要发的信息
        oldsummary = self.memory.get_summary()
        summarymessage = SystemMessage(content=oldsummary)
        messages = [summarymessage,input_message]
        output_message = self.model(messages)
        return output_message
