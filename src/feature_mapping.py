# coding=utf-8
from io import open


class MappingRel:
    """代表所有文档包含的所有词条和整型值的对应关系"""

    def __init__(self):
        self._data = dict()

    def mapping(self, doc_file, mapped_doc_file):
        with open(mapped_doc_file, "w") as out_file:
            with open(doc_file, "r", encoding="utf-8") as in_file:
                for line in in_file:
                    mapped_doc = list()
                    text_id, text = line.strip().split("||")
                    for word in text.split(" "):
                        self._data.setdefault(word, len(self._data))
                        mapped_doc.append(unicode(self._data[word]))
                    out_file.write(text_id + "||" + " ".join(mapped_doc) + "\n")
        return self


if __name__ == '__main__':
    map_rel = MappingRel()
    map_rel.mapping("/Users/wumengling/PycharmProjects/customized_weibo/data/latests.txt",
                    "/Users/wumengling/PycharmProjects/customized_weibo/data/mapped_latests.txt")
    map_rel.mapping("/Users/wumengling/PycharmProjects/customized_weibo/data/favorites.txt",
                    "/Users/wumengling/PycharmProjects/customized_weibo/data/mapped_favorites.txt")
