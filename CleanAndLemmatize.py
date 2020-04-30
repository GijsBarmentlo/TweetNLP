# Import and load spacy
import spacy
nlp = spacy.load('en')


# Cleaning text and lemmatize
def lemmatize_text(input_string, remove_stopwords = True):
  lemmatized_text = ""

  spacy_doc = nlp(input_string)
  if remove_stopwords == False:
    for token in spacy_doc:
      lemmatized_text = lemmatized_text + ' ' + token.lemma_

  if remove_stopwords:
    for token in spacy_doc:
      if token.is_stop == False:
        lemmatized_text = lemmatized_text + " " + token.lemma_

  return lemmatized_text

def remove_mentions_hashtags(input_text):
  """
  Removes # and @
  """
  clean_text = re.sub(r'@\w+', '', input_text)
  clean_text = clean_text.replace("#", "")
  return clean_text


def remove_punctuation(input_text):
  """
  Takes input string and returns string without punctuation
  """
  clean_text = re.sub(r'[^\w\s]','',input_text)
  return clean_text


def clean_and_lemmatize(input_text, remove_stopwords = True, remove_mentions_hashtags = True, remove_punctuation = True):
  """
  Removes punctuation, stopwords, hashtags and handles. Then lemmatizes with spacy("en").
  """
  clean_text = remove_mentions_hashtags(input_text) if remove_mentions_hashtags else input_text
  clean_text = remove_punctuation(clean_text) if remove_punctuation else clean_text
  clean_text = lemmatize_text(clean_text, remove_stopwords) #has condition built into function
  
  return clean_text
  return clean_text
