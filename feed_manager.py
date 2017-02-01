import simplejson as json

class Feed_Manager():
    def __init__(self):
        self.current_feed_data = None
        self.feed_headers = [
            {'field': 'wynit_pn', 'type': 'text', 'label': '', 'func_apply': None, 'maps_to_cms_field': None},
            {'field': 'manufacturer_pn', 'type': 'text', 'label': '', 'func_apply': None},
            {'field': 'category_descript', 'type': 'text', 'label': '', 'func_apply': None},
            {'field': 'vendor_name', 'type': 'text', 'label': '', 'func_apply': None, 'maps_to_cms_field': None},
            {'field': 'brief_part_descript', 'type': 'text', 'label': '', 'func_apply': None, 'maps_to_cms_field': None},
            {'field': 'quantity_available', 'type': 'integer', 'label': '', 'func_apply': None, 'maps_to_cms_field': None},
            {'field': 'CA_qty_avail', 'type': 'integer', 'label': '', 'func_apply': None, 'maps_to_cms_field': None},
            {'field': 'NY_qty_avail', 'type': 'integer', 'label': '', 'func_apply': None, 'maps_to_cms_field': None},
            {'field': 'TN_qty_avail', 'type': 'integer', 'label': '', 'func_apply': None, 'maps_to_cms_field': None},
            {'field': 'seller_price', 'type': 'decimal', 'label': '', 'func_apply': None, 'maps_to_cms_field': None},
            {'field': 'upc_code', 'type': 'text', 'label': '', 'func_apply': None, 'maps_to_cms_field': None},
            {'field': 'msrp', 'type': 'decimal', 'label': '', 'func_apply': None, 'maps_to_cms_field': None},
            {'field': 'weight_lb', 'type': 'text', 'label': '', 'func_apply': None, 'maps_to_cms_field': None},
            {'field': 'length', 'type': 'text', 'label': '', 'func_apply': None, 'maps_to_cms_field': None},
            {'field': 'width', 'type': 'text', 'label': '', 'func_apply': None, 'maps_to_cms_field': None},
            {'field': 'height', 'type': 'text', 'label': '', 'func_apply': None, 'maps_to_cms_field': None},
            {'field': 'MAP', 'type': 'text', 'label': '', 'func_apply': None, 'maps_to_cms_field': None},
            {'field': 'sub_category_descript', 'type': 'text', 'label': '', 'func_apply': None, 'maps_to_cms_field': None},
            {'field': 'marketing_descript', 'type': 'text', 'label': '', 'func_apply': None, 'maps_to_cms_field': None},
            {'field': 'product_thumbnail', 'type': 'text', 'label': '', 'func_apply': None, 'maps_to_cms_field': None},
            {'field': 'product_full_image' 'type': 'text', 'label': '', 'func_apply': None, 'maps_to_cms_field': None}
        ]

    def get_feed_data_from_text(self, path):
        pass

    def parse_current_feed(self):
        pass
    @staticmethod
    def __sample():
        return [
            "'0000049551'",
            "'000-0049-551'",
            "Marine Electronics",
            "Lowrance",
            'LMF-200 NMEA 2000 Gauge 2"',
            0,
            0,
            0,
            0,
            137.14,
            "'042194526812'",
            169.00,
            2.4,
            ,12
            6,
            8.75,
            0,
            "Marine Electronics Accessory"
            "Advanced multi-function, high-contrast round dot matrix gauge displaying graphic and numerical digital data. NMEA 2000? data communications certified, and connect within an affordable, high-performance LowranceNET? network to display real-time readings from an array of compatible electronic probes (E.P.s), like fluid level, temp, speed, and more! Capable of displaying the following NMEA 2000 data: paddlewheel speed, GPS speed, tachometer, battery voltage, alternator voltage, engine temperature, water pressure, engine oil pressure, fuel pressure, boost pressure, transmission oil pressure, atmospheric pressure, temperature, depth, engine loads, engine hours, fuel flow, fuel economy, fuel remaining, fuel used, fuel range, trip fuel used, seasonal fuel used, engine synchronizer, fluid level, GPS position, trim tab position, engine trim position, and engine alarms and warnings",
            "http://content.etilize.com/images/200/1024354337.jpg?noimage=logo"
        ]
