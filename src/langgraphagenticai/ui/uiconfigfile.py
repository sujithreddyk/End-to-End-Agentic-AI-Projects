from configparser import ConfigParser

class Config:
    def __init__(self,config_file="C:\Langgraph_End_to_END_Projects\src\langgraphagenticai\ui\uiconfigfile.ini"):
        self.config = ConfigParser() #this config parser object "config" will the entire config file.
        self.config.read(config_file)

    def get_llm_option(self):
        return self.config["DEFAULT"].get("LLM_OPTIONS").split(", ")
    
    def get_usecase_options(self):
        return self.config["DEFAULT"].get("USECASE_OPTIONS").split(", ")

    def get_groq_model_options(self):
        return self.config["DEFAULT"].get("GROQ_MODEL_OPTIONS").split(", ")
    
    def get_page_title(self):
        return self.config["DEFAULT"].get("PAGE_TITLE")