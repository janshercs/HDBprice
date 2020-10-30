from django import forms
from django.core.exceptions import ValidationError
from django.core import validators

class flat_attributes(forms.Form):
    flat_models = [('NEW GENERATION', 'NEW GENERATION'),
                    ('IMPROVED', 'IMPROVED'),
                    ('MODEL A', 'MODEL A'),
                    ('STANDARD', 'STANDARD'),
                    ('SIMPLIFIED', 'SIMPLIFIED'),
                    ('MODEL A-MAISONETTE', 'MODEL A-MAISONETTE'),
                    ('APARTMENT', 'APARTMENT'),
                    ('MAISONETTE', 'MAISONETTE'),
                    ('TERRACE', 'TERRACE'),
                    ('2-ROOM', '2-ROOM'),
                    ('IMPROVED-MAISONETTE', 'IMPROVED-MAISONETTE'),
                    ('MULTI GENERATION', 'MULTI GENERATION'),
                    ('PREMIUM APARTMENT', 'PREMIUM APARTMENT'),
                    ('Improved', 'Improved'),
                    ('New Generation', 'New Generation'),
                    ('Model A', 'Model A'),
                    ('Standard', 'Standard'),
                    ('Apartment', 'Apartment'),
                    ('Simplified', 'Simplified'),
                    ('Model A-Maisonette', 'Model A-Maisonette'),
                    ('Maisonette', 'Maisonette'),
                    ('Multi Generation', 'Multi Generation'),
                    ('Adjoined flat', 'Adjoined flat'),
                    ('Premium Apartment', 'Premium Apartment'),
                    ('Terrace', 'Terrace'),
                    ('Improved-Maisonette', 'Improved-Maisonette'),
                    ('Premium Maisonette', 'Premium Maisonette'),
                    ('2-room', '2-room'),
                    ('Model A2', 'Model A2'),
                    ('Type S1', 'Type S1'),
                    ('Type S2', 'Type S2'),
                    ('Premium Apartment Loft', 'Premium Apartment Loft'),
                    ('DBSS', 'DBSS')]
    flat_types = [('1 ROOM', '1 ROOM'),
                    ('2 ROOM', '2 ROOM'),
                    ('3 ROOM', '3 ROOM'),
                    ('4 ROOM', '4 ROOM'),
                    ('5 ROOM', '5 ROOM'),
                    ('EXECUTIVE', 'EXECUTIVE'),
                    ('MULTI GENERATION', 'MULTI GENERATION')]
    storey_ranges =[(1,"1-5"),
                    (2,"6-10"),
                    (3,"11-15")]
    towns = [('ANG MO KIO', 'ANG MO KIO'),
            ('BEDOK', 'BEDOK'),
            ('BISHAN', 'BISHAN'),
            ('BUKIT BATOK', 'BUKIT BATOK'),
            ('BUKIT MERAH', 'BUKIT MERAH'),
            ('BUKIT TIMAH', 'BUKIT TIMAH'),
            ('CENTRAL AREA', 'CENTRAL AREA'),
            ('CHOA CHU KANG', 'CHOA CHU KANG'),
            ('CLEMENTI', 'CLEMENTI'),
            ('GEYLANG', 'GEYLANG'),
            ('HOUGANG', 'HOUGANG'),
            ('JURONG EAST', 'JURONG EAST'),
            ('JURONG WEST', 'JURONG WEST'),
            ('KALLANG/WHAMPOA', 'KALLANG/WHAMPOA'),
            ('MARINE PARADE', 'MARINE PARADE'),
            ('QUEENSTOWN', 'QUEENSTOWN'),
            ('SENGKANG', 'SENGKANG'),
            ('SERANGOON', 'SERANGOON'),
            ('TAMPINES', 'TAMPINES'),
            ('TOA PAYOH', 'TOA PAYOH'),
            ('WOODLANDS', 'WOODLANDS'),
            ('YISHUN', 'YISHUN'),
            ('LIM CHU KANG', 'LIM CHU KANG'),
            ('BUKIT PANJANG', 'BUKIT PANJANG'),
            ('PASIR RIS', 'PASIR RIS'),
            ('SEMBAWANG', 'SEMBAWANG'),
            ('PUNGGOL', 'PUNGGOL')]
    flat_model = forms.CharField(label = 'Flat Model', widget = forms.Select(choices = flat_models))
    flat_type = forms.CharField(label = 'Flat Type', widget = forms.Select(choices = flat_types))
    floor_area_sqm = forms.FloatField(label = 'Floor area in sqm')
    lease_commence_date = forms.IntegerField(label = 'Year lease commenced')
    remaining_lease = forms.IntegerField(label = 'Years of lease remaining')
    storey_range = forms.IntegerField(label = 'Storey range', widget = forms.Select(choices = storey_ranges))
    town = forms.CharField(label = 'Town', widget = forms.Select(choices = towns))
    postalcode = forms.IntegerField(label = 'Postal Code')