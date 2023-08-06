#Author: AIMPED
#Date: 2023-March-20
#Description: Contains the translation functions for aimped library.

def language_code(language):
    languages = {
    "Mandarin Chinese": "zh",
    "Spanish": "es",
    "English": "en",
    "Hindi": "hi",
    "Arabic": "ar",
    "Bengali": "bn",
    "Portuguese": "pt",
    "Russian": "ru",
    "Japanese": "ja",
    "Punjabi": "pa",
    "German": "de",
    "Javanese": "jv",
    "Wu Chinese": "wuu",
    "Malay": "ms",
    "Telugu": "te",
    "Vietnamese": "vi",
    "Korean": "ko",
    "French": "fr",
    "Marathi": "mr",
    "Tamil": "ta",
    "Urdu": "ur",
    "Turkish": "tr",
    "Italian": "it",
    "Yue Chinese": "yue",
    "Thai": "th",
    "Gujarati": "gu",
    "Jin Chinese": "cjy",
    "Persian": "fa",
    "Polish": "pl",
    "Pashto": "ps"
}
    return languages[language]

def split_text(text, source_language, input_length=64):
    """
    Splits the input text into sentences and creates batches of sentences to be fed into the model.

    Args:
        text (str): The input text to be split into sentences.

    Returns:
        A list of lists, where each inner list contains a batch of sentences. Each batch is represented as a list of strings.
    """        
    from nltk import sent_tokenize

    paragraphs = text.split("\n")
    sentenced_paragraphs = [sent_tokenize(paragraph, language=source_language) if paragraph else ['<p>--</p>'] for paragraph in paragraphs]
    input_paragraphs = [" ".join([sentence + " end_of_sentence" for sentence in sentences]) for sentences in sentenced_paragraphs]
            

    input_sentences = []
    for input_paragraph in input_paragraphs:
        temp = []
        text_tokens = input_paragraph.split()
        start_idx = 0

        while start_idx < len(text_tokens):
            end_idx = start_idx + input_length
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

def translate(text, source_language, pipeline):
    
    """
    Args:
        text (list of str): A list of texts to be translated.
    Returns:
        translated_texts (list of str): A list of translated texts in the target language. 
        The order of the texts in the output list corresponds to the order of the input texts in the text parameter.
    """
    input_texts_list = [split_text(input_text, source_language=source_language) for input_text in text]
    translated_texts = []
    for input_texts in input_texts_list:
    # Translate each input chunk and combine the translated chunks into the final translated text
        output_texts = []
        for texts in input_texts:
            # print(texts)
            translation_result = pipeline(texts)
            # translated_result = [result["translation_text"] for result in translation_result]
            translated_result = [result["translation_text"] for result in translation_result]
            output_texts.append(" ".join(translated_result))
        translated_texts.append("\n".join(output_texts).replace("<p>--</p>", ""))
    return translated_texts
