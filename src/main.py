from data_collecting import craw_save_clean_corpus
from feature_mapping import MappingRel
from read import base_read
from nearest_weibo import nearest_weibo_index
from create_favorite import create_favorite

craw_save_clean_corpus()

map_rel = MappingRel()
map_rel.mapping("/Users/wumengling/PycharmProjects/customized_weibo/data/latests.txt",
                "/Users/wumengling/PycharmProjects/customized_weibo/data/mapped_latests.txt")
map_rel.mapping("/Users/wumengling/PycharmProjects/customized_weibo/data/favorites.txt",
                "/Users/wumengling/PycharmProjects/customized_weibo/data/mapped_favorites.txt")

favorites_id, favorites = base_read("/Users/wumengling/PycharmProjects/customized_weibo/data/mapped_favorites.txt")
latest_id, latest = base_read("/Users/wumengling/PycharmProjects/customized_weibo/data/mapped_latests.txt")

ind = nearest_weibo_index(latest, favorites)
create_favorite(ind, latest_id)
