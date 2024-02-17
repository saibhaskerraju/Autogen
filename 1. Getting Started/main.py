import autogen
from autogen import AssistantAgent, UserProxyAgent

llm_config = {
    "config_list": [
  {
    "model": "TheBloke/phi-2-GGUF",
    "base_url": "http://host.docker.internal:1234/v1",
    "api_key":"not-needed"
  }
],
}



assistant = AssistantAgent(name="assistant", llm_config=llm_config)

user_proxy = UserProxyAgent(
    "user_proxy",
    code_execution_config={
        "work_dir": "coding",
        "use_docker": False,  # Please set use_docker=True if docker is available to run the generated code. Using docker is safer than running the generated code directly.
    },
)

user_proxy.initiate_chat(assistant, message="when was the last prediction on 'end of world'?")