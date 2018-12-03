from . import models
from haystack import indexes


class GoodsInfoIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, user_template=True)

    def get_model(self):
        return models.GoodsInfo

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
