from textSummarizer.config.configuration import ConfigurationManager
from transformers import AutoTokenizer, GenerationConfig, pipeline

class PredictionPipeline:
    def __init__(self):
        self.config=ConfigurationManager().get_model_evaluation_config()


    def predict(self,text):
        tokenizer= AutoTokenizer.from_pretrained(self.config.tokenizer_path)

        # Load generation config saved with the model to avoid warnings
        gen_config = GenerationConfig.from_pretrained(self.config.model_path)

        pipe=pipeline(
            "summarization",
            model=self.config.model_path,
            tokenizer=tokenizer,
            generation_config=gen_config,
        )

        print("Dialogue:")
        print(text)

        output = pipe(text)[0]["summary_text"]
        print("\nModel Summary:")
        print(output)
        return output

