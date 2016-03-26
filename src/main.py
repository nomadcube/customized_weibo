from read import base_read
from nearest_items.cluster_distance import cluster_similarity


favorites = base_read("/Users/wumengling/PycharmProjects/customized_weibo/data/mapped_favorites.txt")
latest = base_read("/Users/wumengling/PycharmProjects/customized_weibo/data/mapped_latests.txt")


for one_latest in latest:
    print cluster_similarity(one_latest, favorites)


