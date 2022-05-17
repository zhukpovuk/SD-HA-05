import nltk

# download the file averaged_perceptron_tagger from http://www.nltk.org/nltk_data/ and save it in tagger folder

class Splitter(object):
    def __init__(self):
        self.nltk_splitter = nltk.data.load('english.pickle')
        self.nltk_tokenizer = nltk.tokenize.TreebankWordTokenizer()

    def split(self, text):

        sentences = self.nltk_splitter.tokenize(text)
        tokenized_sentences = [self.nltk_tokenizer.tokenize(sent) for sent in sentences]
        return tokenized_sentences


class POSTagger(object):
    def __init__(self):
        pass        
    def pos_tag(self, sentences):
        pos = [nltk.pos_tag(sentence) for sentence in sentences]
        pos = [[(word, [postag]) for (word, postag) in sentence] for sentence in pos]
        return pos

text = """Text messaging, or texting, is the act of composing and sending electronic messages,
typically consisting of alphabetic and numeric characters, between two or more users of
mobile devices, desktops/laptops, or another type of compatible computer."""

splitter = Splitter()
postagger = POSTagger()

splitted_sentences = splitter.split(text)
print('splitted_sentences:', splitted_sentences)
pos_tagged_sentences = postagger.pos_tag(splitted_sentences)
print('pos_tagged_words:',pos_tagged_sentences)



'''splitted_sentences: [['Text', 'messaging', ',', 'or', 'texting', ',', 'is', 'the', 'act',
'of', 'composing', 'and', 'sending', 'electronic', 'messages', ',', 'typically',
'consisting', 'of', 'alphabetic', 'and', 'numeric', 'characters', ',', 'between',
'two', 'or', 'more', 'users', 'of', 'mobile', 'devices', ',', 'desktops/laptops', ',', 'or',
'another', 'type', 'of', 'compatible', 'computer', '.']]
pos_tagged_words: [[('Text', ['NNP']), ('messaging', ['NN']),
(',', [',']), ('or', ['CC']), ('texting', ['NN']), (',', [',']), ('is', ['VBZ']),
('the', ['DT']), ('act', ['NN']), ('of', ['IN']), ('composing', ['VBG']), ('and', ['CC']),
('sending', ['VBG']), ('electronic', ['JJ']), ('messages', ['NNS']), (',', [',']), ('typically',
['RB']), ('consisting', ['VBG']), ('of', ['IN']), ('alphabetic', ['JJ']), ('and', ['CC']),
('numeric', ['JJ']), ('characters', ['NNS']), (',', [',']), ('between', ['IN']), ('two', ['CD']),
('or', ['CC']), ('more', ['JJR']), ('users', ['NNS']), ('of', ['IN']), ('mobile', ['JJ']), ('devices',
['NNS']), (',', [',']), ('desktops/laptops', ['NNS']), (',', [',']), ('or', ['CC']), ('another', ['DT']),
('type', ['NN']), ('of', ['IN']), ('compatible', ['JJ']), ('computer', ['NN']), ('.', ['.'])]]'''
