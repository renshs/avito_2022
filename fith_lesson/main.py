import imp
from typing import List

class CountVectorizer:
    def __init__(self) -> None:
        self.vocabulary = {}

    def fit_transform(self, data: list) -> List[list]:
        """
        This function creating a dictionary vocabulary{} with features names.
        Then it creates document term matrix and returns it.
        """
        index = 0
        dtm = []
        for string in data:
            string = string.lower()
            if not string[-1].isalpha():
                string = string[:-1]
            for word in string.split():
                if word not in self.vocabulary:
                    self.vocabulary[word] = index
                    index += 1
        for string in data:
            string = string.lower()
            if not string[-1].isalpha():
                string = string[:-1]
            row = [0] * len(self.vocabulary.keys())
            for word in string.split():
                row[self.vocabulary[word]] += 1
            dtm.append(row)

        return dtm

    def get_feature_names(self) -> List[str]:
        """
        This function returns a list of features names.
        """
        return list(self.vocabulary.keys())


if __name__ == '__main__':
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(count_matrix)
