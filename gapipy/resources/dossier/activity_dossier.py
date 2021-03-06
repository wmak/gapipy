# Python 2 and 3
from __future__ import unicode_literals

from ...utils import humanize_price, LocationLabelMixin, DurationLabelMixin, enforce_string_type
from ..base import Resource
from ..tour.image import Image
from ..tour.tour_category import TourCategoryList
from ..tour.video import Video
from .details import DossierDetail, DossierDetailsMixin
from .dossier_features import DossierFeature


class ActivityDossier(Resource, DossierDetailsMixin, DurationLabelMixin, LocationLabelMixin):
    _resource_name = 'activity_dossiers'

    _as_is_fields = [
        'currency',
        'distance_max',
        'distance_min',
        'dossier_segment',
        'duration_min', 'duration_max',
        'flags',
        'href',
        'id',
        'name',
        'physical_grading',
        'price_per_group_max',
        'price_per_group_min',
        'price_per_person_max',
        'price_per_person_min',
        'publish_state',
        'type',
    ]

    _date_time_fields_local = ['date_created', 'date_last_modified']

    _resource_fields = [
        ('start_location', 'Place'),
        ('end_location', 'Place'),
    ]

    _model_collection_fields = [
        ('details', DossierDetail),
        ('features', DossierFeature),
        ('categories', TourCategoryList),
        ('images', Image),
        ('videos', Video),
    ]

    @enforce_string_type
    def __repr__(self):
        return '<{} {}>'.format(self.__class__.__name__, self.name)

    @property
    def duration(self):
        """
        Simulate the Duration model in `ItineraryComponent` objects,
        so we can reuse the methods therein until this models inconsistency
        can be rectified (currently, this model has two duration fields
        instead of a duration map/obj).
        """
        if not self.duration_min or not self.duration_max:
            return None

        from gapipy.resources import Duration
        duration = Duration(
            data=dict(
                min_hr=self.duration_min,
                max_hr=self.duration_max),
            client=self._client,
        )
        return duration

    @property
    def price_per_person_label(self):
        return humanize_price(
            self.price_per_person_min,
            self.price_per_person_max,
            self.currency,
        )

    @property
    def price_per_group_label(self):
        return humanize_price(
            self.price_per_group_min,
            self.price_per_group_max,
            self.currency,
        )

    @property
    def operational_notes(self):
        return self._get_detail_body('ACTIVITY__OPERATIONAL_NOTES')
