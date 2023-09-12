from googletrans import Translator
from transformers import pipeline

from typing import Dict


class SentimentAnalyser:
    def __init__(self) -> None:
        self.pipe = pipeline(
            "text-classification",
            model="mrm8488/distilroberta-finetuned-financial-news-sentiment-analysis",
        )
        self.translator = Translator()

    def __call__(self, string: str) -> Dict:
        return self.pipe(self.translator.translate(text=string, dest="en").text)[0]
