from itertools import count
from typing import List
from math import log


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
            if isinstance(string, list):
                string = map(str, string)
                string = ' '.join(string)
            string = string.lower()
            if not string[-1].isalpha():
                string = string[:-1]
            for word in string.split():
                if word not in self.vocabulary:
                    self.vocabulary[word] = index
                    index += 1
        for string in data:
            if isinstance(string, list):
                string = map(str, string)
                string = ' '.join(string)
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


class TfidfTransformer:
    def __init__(self):
        pass

    def tf_transform(self, data):
        tf_matrix = []
        for row in range(len(data)):
            summ = sum(data[row])
            tf_row = []
            for term in range(len(data[row])):
                tf_row.append(round(data[row][term] / summ, 3))
            tf_matrix.append(tf_row)
        return tf_matrix

    def idf_transform(self, data):
        if not data:
            return []
        idf_vector = []
        all_documents_n = len(data)

        for term in range(len(data[0])):
            d_with_term = 0
            for i in range(all_documents_n):
                d_with_term += bool(data[i][term])
            idf = log((all_documents_n + 1) / (d_with_term + 1)) + 1
            idf_vector.append(round(idf, 3))

        return idf_vector

    def fit_transform(self, count_matrix):
        result = []
        tf = self.tf_transform(count_matrix)
        idf = self.idf_transform(count_matrix)

        for row in tf:
            result.append([round(a*b, 3) for a, b in zip(idf, row)])
        return result


class TfidfVectorizer(CountVectorizer, TfidfTransformer):
    def __init__(self) -> None:
        super().__init__()
        self.tf_idf = TfidfTransformer()

    def fit_transform(self, data: list) -> List[list]:
        count_matrix = super().fit_transform(data)
        return self.tf_idf.fit_transform(count_matrix)


if __name__ == '__main__':
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    transformer = TfidfTransformer()
    tfidf_matrix = transformer.fit_transform(count_matrix)
    print(tfidf_matrix)
