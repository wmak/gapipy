from __future__ import unicode_literals

from ..base import Resource
from .details import DossierDetail, DossierDetailsMixin
from ...utils import humanize_price, LocationLabelMixin, DurationLabelMixin


class ActivityDossier(Resource, DossierDetailsMixin, DurationLabelMixin, LocationLabelMixin):
    _resource_name = 'activity_dossiers'

    _as_is_fields = [
        'id', 'href',
        'name',
        'duration_min', 'duration_max',
        'price_per_person_min', 'price_per_person_max',
        'price_per_group_min', 'price_per_group_max',
        'currency',
        'dossier_segment',
    ]

    _date_time_fields_local = ['date_created', 'date_last_modified']

    _resource_fields = [
        ('start_location', 'Place'),
        ('end_location', 'Place'),
    ]

    _model_collection_fields = [
        ('details', DossierDetail),
    ]

    def __repr__(self):
        return '<{} {}>'.format(self.__class__.__name__, self.name)

    @property
    def duration(self):
        """
        Simulate the duration dict in `ItineraryComponent` objects,
        so we can reuse the `DurationLabelMixin`
        """
        if self.duration_min or self.duration_max:
            return {
                'min_hr': self.duration_min,
                'max_hr': self.duration_max,
            }

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
