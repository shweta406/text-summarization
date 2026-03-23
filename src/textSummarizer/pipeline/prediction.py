from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.pipeline.generation_config import GENERATION_CONFIG
from transformers import AutoTokenizer
from transformers import pipeline

class PredictionPipeline:
    def __init__(self):
        self.config=ConfigurationManager().get_model_evaluation_config()


    def predict(self,text):
        tokenizer= AutoTokenizer.from_pretrained(self.config.tokenizer_path)
        
        pipe=pipeline("summarization",model= self.config.model_path,tokenizer=tokenizer)
        
        ##
        print("Dialogue:")
        print(text)
        
        output = pipe(text, **GENERATION_CONFIG)[0]["summary_text"]
        print("\nModel Summary:")
        print(output)
        return output

