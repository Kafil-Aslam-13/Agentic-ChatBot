import streamlit as st 

from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI 
from src.langgraphagenticai.LLMS.groqllm import GroqLLM
from src.langgraphagenticai.graph.graph_builder import GraphBuilder
from src.langgraphagenticai.ui.streamlitui.display_result import DisplayResultStreamlit




def load_langgraph_agenticai_app():
    """
    Loads and runs the LangGraph Agentic AI application with streamlit ui.
    this fn initializes the ui , handles user ip , configures the llm model,
    sets up the graph based on selected use case, and displays the output while
    implementing exception handling for robustness.

    """

    ## Load UI
    ui=LoadStreamlitUI()
    user_input=ui.load_streamlit_ui()

    if not user_input:
        st.error("ERROR: Failed to load user input from the UI")
        return
    user_message=st.chat_input("Enter Your Message: ")

    if user_message:
        try:
            # Configure LLM
            obj_llm_config=GroqLLM(user_controls_input=user_input)
            model=obj_llm_config.get_llm_model()

            if not model:
                st.error("Error: LLM Model could not be Initialized.")
                return
            # INITIALIZE  and set up the graph based on use case
            usecase=user_input.get('selected_usecase')
            if not usecase:
                st.error('Error: No use case selected')
                return
            ## building my graph
            graph_builder=GraphBuilder(model=model)
            try:
                graph=graph_builder.setup_graph(usecase)
                DisplayResultStreamlit(usecase=usecase,graph=graph,user_message=user_message).display_result_on_ui()

            except Exception as e:
                st.error(f"Error: Graph Setup Failed {e}")
                return


        except Exception as e:
            st.error(f"Error: Graph setup failed")
            return