from django import forms
from django.core.exceptions import ValidationError
from django.core import validators

class flat_attributes(forms.Form):
    flat_models = [('New Generation', 'New Generation'),
                ('Improved', 'Improved'),
                ('Model A', 'Model A'),
                ('Standard', 'Standard'),
                ('Simplified', 'Simplified'),
                ('Model A-Maisonette', 'Model A-Maisonette'),
                ('Apartment', 'Apartment'),
                ('Maisonette', 'Maisonette'),
                ('Terrace', 'Terrace'),
                ('2-room', '2-room'),
                ('Improved-Maisonette', 'Improved-Maisonette'),
                ('Multi Generation', 'Multi Generation'),
                ('Premium Apartment', 'Premium Apartment'),
                ('Adjoined flat', 'Adjoined flat'),
                ('Premium Maisonette', 'Premium Maisonette'),
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
    storey_ranges =[(0, '01 TO 05'),
                (1, '06 TO 10'),
                (2, '11 TO 15'),
                (3, '16 TO 20'),
                (4, '21 TO 25'),
                (5, '26 TO 30'),
                (6, '31 TO 35'),
                (7, '36 TO 40'),
                (8, '41 TO 42'),
                (9, '43 TO 45'),
                (10, '46 TO 48'),
                (11, '49 TO 51')]
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
    
    def clean_floor_area_sqm(self):
        data = self.cleaned_data['floor_area_sqm']
        if data < 20 or data > 400:
            raise ValidationError('Area is out of range.')
        return data

    def clean_lease_commence_date(self):
        data = self.cleaned_data['lease_commence_date']
        if 1965 > data or data > 2020:
            raise ValidationError('Please enter valid year')
        return data
    
    def clean_postalcode(self):
        data = self.cleaned_data['postalcode']
        if len(str(data)) != 6:
            raise ValidationError('Postal codes should be 6 digits.')
        return data

    def clean_remaining_lease(self):
        data = self.cleaned_data['remaining_lease']
        if data > 99 or data < 0:
            raise ValidationError('Remaining lease should be less than 99 and more than 0.')