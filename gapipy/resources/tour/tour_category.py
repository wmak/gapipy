# Python 2 and 3
from __future__ import unicode_literals

from ..base import Resource, BaseModel

class TourCategoryList(BaseModel):
    _as_is_fields = [
        'id',
        'href',
        'name',
    ]

    _resource_fields = [
        ('category_type', 'TourCategory'),
    ]


class TourCategory(Resource):

    _resource_name = 'tour_categories'

    _as_is_fields = ['id', 'href', 'name', 'description']
    _resource_fields = [('category_type', 'TourCategory')]
