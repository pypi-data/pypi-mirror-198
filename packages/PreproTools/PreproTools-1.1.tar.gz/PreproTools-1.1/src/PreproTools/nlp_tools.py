import contractions
import re
import nltk
import os

from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords  # german, indonesia, portuguese, spanish, english, italian, chinese, basque, catalan, arabic, french, greek
from nltk.tag import pos_tag
from nltk import RegexpParser

class NLPpreprocessing:

    """
    Items from NLTK that you have to download:
        - averaged_perceptron_tagger
        - punkt
        - stopwords
        - wordnet
    You can use the function -> print(preprocess_obj.download(item))

    You have to create an object first -> preprocess = NLPpreprocessing()

    The default language of stop words is set to english. To change it -> preprocess = NLPpreprocessing(stop_words="english")

    This package has two methods:
        - "text": You pass your whole text and you get in return the sentences in a list
        - "rmv_punctuation": Remove the punctuation from your sentences
    """

    upper = "([A-Z])"
    lower = "([a-z])"

    alphabets= "([A-Za-z])"
    prefixes = "(Mr|St|Mrs|Ms|Dr)[.]"
    suffixes = "(Inc|Ltd|Jr|Sr|Co)"
    starters = "(Mr|Mrs|Ms|Dr|Prof|Capt|Cpt|Lt|He\s|She\s|It\s|They\s|Their\s|Our\s|We\s|But\s|However\s|That\s|This\s|Wherever)"
    acronyms = "([A-Z][.][A-Z][.](?:[A-Z][.])?)"
    websites = "[.](com|net|org|io|gov|edu|me)"
    digits = "([0-9])"

    chunker = RegexpParser("""
        NP: {<DT>?<JJ>*<NN>}  # To extract the NP
        P: {<IN>}             # Extracting Preprositions
        V: {<V.*>}            # Extract Verbs
        PP: {<P> <NP>}        # Extracting Preposition Phrase
        VP: {<V> <NP|PP>*}    # Extracting verb Phrase
        """)

    def __init__(self, stop_words="english"):
        self.stop_words = stop_words

    def download(self, item_id):
        # Posible 
        item_id_search = item_id + ".zip"
        result = [os.path.join(root, item_id_search) for root, dir, files in os.walk('/') if item_id_search in files]
        
        if result == []:
            correct_file = nltk.download(item_id)
            if correct_file:
                return "Item Downloaded"
            else:
                return "Item name incorrect"
        else:
            return "Item Already Downloaded"

    def text(self, text): 
        # https://stackoverflow.com/questions/4576077/how-can-i-split-a-text-into-sentences 
        
        text = " ".join([contractions.fix(word) if "U." not in word else word for word in text.split()])
        
        text = " " + text + "  "
        text = text.replace("\n"," ")
        text = re.sub(self.prefixes,"\\1<prd>",text)
        text = re.sub(self.websites,"<prd>\\1",text)
        text = re.sub(self.digits + "[.]" + self.digits,"\\1<prd>\\2",text)

        text = re.sub("Ph.D", "PhD", text)
        letters = re.findall("PhD." + " " + self.upper, text)
        for i in range(len(letters)):
            text = re.sub("PhD." + " " + letters[i], "PhD." + letters[i], text)
        letters = re.findall("PhD." + " " + self.lower, text)
        for i in range(len(letters)):
            text = re.sub("PhD." + " " + letters[i], "PhD " + letters[i], text)
        
        text = re.sub("\s" + self.alphabets + "[.] "," \\1<prd> ",text)
        text = re.sub(self.acronyms+" "+self.starters,"\\1<stop> \\2",text)
        text = re.sub(self.alphabets + "[.]" + self.alphabets + "[.]" + self.alphabets + "[.]","\\1<prd>\\2<prd>\\3<prd>",text)
        text = re.sub(self.alphabets + "[.]" + self.alphabets + "[.]","\\1<prd>\\2<prd>",text)
        text = re.sub(" "+self.suffixes+"[.] "+self.starters," \\1<stop> \\2",text)
        text = re.sub(" "+self.suffixes+"[.]"," \\1<prd>",text)
        text = re.sub(" " + self.alphabets + "[.]"," \\1<prd>",text)

        if "..." in text: text = text.replace("...","<prd><prd><prd>")
        if "”" in text: text = text.replace(".”","”.")
        if "\"" in text: text = text.replace(".\"","\".")
        if "!" in text: text = text.replace("!\"","\"!")
        if "?" in text: text = text.replace("?\"","\"?")

        text = text.replace(".",".<stop>")
        text = text.replace("?","?<stop>")
        text = text.replace("!","!<stop>")
        text = text.replace("<prd>",".")
        sentences = text.split("<stop>")
        sentences = sentences[:-1]
        sentences = [s.strip() for s in sentences]

        return sentences
    
    def rmv_punctuation(self, sentences):
        sentences = [" ".join(re.sub(r'[^\w\s]',' ',sentence).split()) for sentence in sentences]
        return sentences
    
    def lower_casing(self, sentences):
        sentences = [sentence.lower() for sentence in sentences]
        return sentences

    def lemmatizer(self, sentences):
        """
        Stemming has its application in Sentiment Analysis while Lemmatization has its 
        application in Chatbots, human-answering.
        """
        
        lemmatizer = WordNetLemmatizer()
        for i in range(len(sentences)):
            words = nltk.word_tokenize(sentences[i])
            words = [lemmatizer.lemmatize(word) for word in words if word not in stopwords.words(self.stop_words)]
            sentences[i] = ' '.join(words)
        
        return sentences
    
    def tokenize(self, sentences):
        words_sentence = [nltk.word_tokenize(sentences[i]) for i in range(len(sentences))]
        return words_sentence

    def parse_trees(self, tokenized_sentences):
        tags = []
        parse_tree = []
        for i in tokenized_sentences:
            tags.append(pos_tag(i))
            parse_tree.append(self.chunker.parse(pos_tag(i)))
        return tags, parse_tree
    
