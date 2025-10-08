from src.langgraphagenticai.state.state import State


class BasicChatbotNode:
    """
    Basic Chatbot logic implementation

    """
    def __init__(self,model):
        self.llm=model
    
    def process(self,state:State)->dict:
        """
        Processes the Input state and Generates a chatbot response.

        """
        return{"messages":self.llm.invoke(state["messages"])}

