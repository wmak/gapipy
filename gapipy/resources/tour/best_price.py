from ..base import BaseModel, Resource

class PromotionModel(BaseModel):
    _as_is_fields = ['id', 'href', 'amount', ]


class DepartureModel(BaseModel):
    _as_is_fields = ['id', 'href', ]


class AvailabilityModel(BaseModel):
    _as_is_fields = ['status', 'total', 'male', 'female', ]



class PriceModel(BaseModel):
    _as_is_fields = ['currency', 'price', 'original_price']

    _model_fields = [
        ('departure', DepartureModel),
        ('promotion', PromotionModel),
        ('availability', AvailabilityModel),
    ]


class BestPriceRoom(BaseModel):
    _as_is_fields = ['code', 'name']

    _model_collection_fields = [
        ('prices', PriceModel),
    ]


class BestPrice(Resource):
    _resource_name = 'best_prices'
    _is_parent_resource = False

    _as_is_fields = ['id', 'href', ]
    _model_collection_fields = [
        ('rooms', BestPriceRoom),
    ]
