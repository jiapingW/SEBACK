class Message:
    def __init__(self, content=None, role=None) -> None:
        self.content = content
        self.role = role
        
    def to_str(self):
        return f"{self.role}: {self.content}"
    
    def to_dict(self):
        return {
            "role": self.role,
            "content": self.content
        }


class AIMessage(Message):
    def __init__(self, content: str) -> None:
        super().__init__(content, 'assistant')
        
        
class UserMessage(Message):
    def __init__(self, content: str) -> None:
        super().__init__(content, 'user')


class SystemMessage(Message):
    def __init__(self, content: str) -> None:
        super().__init__(content, 'system')