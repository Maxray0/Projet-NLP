from transformers import pipeline as hf_pipeline

class BaseHFModel:
    
    def __init__(self, task, model, tokenizer=None):
        self.model = hf_pipeline(task=task, model=model, tokenizer=tokenizer)
        
    def predict(self, inputs, *args):
        return self.model(inputs)