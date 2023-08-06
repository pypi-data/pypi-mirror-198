from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline
from nltk import sent_tokenize

class TranslationPipeline():
    
    """
    Translation pipeline that uses Hugging Face's transformers library to perform
    machine translation from a source language to a target language.
    """
    
    language_codes = {
     "english": "en",
     "german": "de",
     "french": "fr",
     "spanish": "es",
     "italian": "it",
     "dutch": "nl",
     "polish": "pl",
     "portuguese": "pt",
     "turkish": "tr",
     "russian": "ru",
     "arabic": "ar",
     "chinese": "zh",
     "japanese": "ja",
     "korean": "ko",
     "vietnamese": "vi",
     "thai": "th",
     "hindi": "hi",
     "bengali": "bn",
    
    }
    def __init__(self, model, tokenizer,source_lang, target_lang, input_length=64, device=0) -> str:
        
        """
        Initializes the TranslationPipeline object with a pre-trained model and tokenizer
        for the specified source and target languages.

        Args:
            model_path (str): Path to the pre-trained model and tokenizer.
            source_lang (str): Source language to translate from.
            target_lang (str): Target language to translate to.
            input_length (int, optional): Maximum length of input sequences. Defaults to 64.
            device (int, optional): Device to run the model on (CPU or GPU). Defaults to 0.
        """
                
        self.model = model
        self.tokenizer = tokenizer
        self.target_lang = target_lang
        self.source_lang = source_lang
        self.input_length = input_length
        self.device = device
        self.task = "translation_" + TranslationPipeline.language_codes[source_lang] + "_to_" + TranslationPipeline.language_codes[target_lang]
        self.pipeline = pipeline(
                                    task=self.task,
                                    model=self.model,
                                    tokenizer=self.tokenizer,
                                    device= self.device,  # set to -1 for CPU or use GPU device ID for GPU
                                    max_length=512,
                                    num_beams=4,
                                    early_stopping=True,
                                    num_return_sequences=1,
                                    repetition_penalty=2.0,
                                    length_penalty=0.9,
                                    no_repeat_ngram_size=3,
                                    do_sample=True,
                                    top_k=50,
                                    top_p=0.95,
                                    truncation=True

                                )


    
    def SplitText(self, text):
        """
        Splits the input text into sentences and creates batches of sentences to be fed into the model.

        Args:
            text (str): The input text to be split into sentences.

        Returns:
            A list of lists, where each inner list contains a batch of sentences. Each batch is represented as a list of strings.
        """        

        paragraphs = text.split("\n")
        sentenced_paragraphs = [sent_tokenize(paragraph, language=self.source_lang) if paragraph else ['<p>--</p>'] for paragraph in paragraphs]
        input_paragraphs = [" ".join([sentence + " end_of_sentence" for sentence in sentences]) for sentences in sentenced_paragraphs]
             

        input_sentences = []
        for input_paragraph in input_paragraphs:
            temp = []
            text_tokens = input_paragraph.split()
            start_idx = 0

            while start_idx < len(text_tokens):
                end_idx = start_idx + self.input_length
                if end_idx > len(text_tokens):
                    end_idx = len(text_tokens)
                chunk = " ".join(text_tokens[start_idx:end_idx])
                if chunk.endswith("end_of_sentence"):
                    temp.append(chunk.replace(" end_of_sentence", "").replace("end_of_sentence", ""))
                    start_idx = end_idx
                else:
                    for i in range(end_idx, len(text_tokens)):
                        chunk += " " + text_tokens[i]
                        if text_tokens[i].endswith("end_of_sentence"):
                            temp.append(chunk.replace("end_of_sentence", ""))
                            start_idx = i + 1
                            break
            input_sentences.append(temp)
        return input_sentences
        
    def Translate(self, text):
        
        """
        Args:
            text (list of str): A list of texts to be translated.
        Returns:
            translated_texts (list of str): A list of translated texts in the target language. 
            The order of the texts in the output list corresponds to the order of the input texts in the text parameter.
        """
        input_texts_list = [self.SplitText(input_text) for input_text in text]
        translated_texts = []
        for input_texts in input_texts_list:
        # Translate each input chunk and combine the translated chunks into the final translated text
            output_texts = []
            for texts in input_texts:
                # print(texts)
                translation_result = self.pipeline(texts)
                # translated_result = [result["translation_text"] for result in translation_result]
                translated_result = [result["translation_text"] for result in translation_result]
                output_texts.append(" ".join(translated_result).replace("<p>--</p>", ""))
            translated_texts.append("\n".join(output_texts).replace("<p>--</p>", ""))
        return translated_texts
        
