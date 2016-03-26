from read import base_read
from nearest_items.select_weibo import top_weibo_index, find_original_weibo


favorites = base_read("/Users/wumengling/PycharmProjects/customized_weibo/data/mapped_favorites.txt")
latest = base_read("/Users/wumengling/PycharmProjects/customized_weibo/data/mapped_latests.txt")

ind = top_weibo_index(latest, favorites)
print find_original_weibo("/Users/wumengling/PycharmProjects/customized_weibo/data/latests.txt", ind)
