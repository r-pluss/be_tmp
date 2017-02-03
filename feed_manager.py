import csv
import simplejson as json

def _remove_single_quotes(string):
    return string.replace("'", "")

class Feed_Manager():
    def __init__(self):
        self.current_feed_data = None
        self.cms_headers = [
            "Product ID","Product Type",
            "Code",
            "Name",
            "Brand",
            "Description",
            "Cost Price",
            "Retail Price",
            "Sale Price",
            "Calculated Price",
            "Fixed Shipping Price",
            "Free Shipping",
            "Warranty",
            "Weight",
            "Width",
            "Height",
            "Depth",
            "Allow Purchases",
            "Product Visible",
            "Product Availability",
            "Product Inventoried",
            "Stock Level",
            "Low Stock Level",
            "Date Added",
            "Date Modified",
            "Category Details",
            "Images",
            "Page Title",
            "META Keywords",
            "META Description",
            "Product Condition",
            "Product URL",
            "Redirect Old URL?",
            "Product Tax Code",
            "Product Custom Fields"
        ]
        self.feed_headers = [
            {'field': 'wynit_pn', 'type': 'text', 'label': '', 'func_apply': _remove_single_quotes, 'maps_to_cms_field': None},
            {'field': 'manufacturer_pn', 'type': 'text', 'label': '', 'func_apply': _remove_single_quotes, 'maps_to_cms_field': None},
            {'field': 'category_descript', 'type': 'text', 'label': '', 'func_apply': None, 'maps_to_cms_field': None},
            {'field': 'vendor_name', 'type': 'text', 'label': '', 'func_apply': None, 'maps_to_cms_field': "Brand"},
            {'field': 'brief_part_descript', 'type': 'text', 'label': '', 'func_apply': None, 'maps_to_cms_field': None},
            {'field': 'quantity_available', 'type': 'integer', 'label': '', 'func_apply': None, 'maps_to_cms_field': None},
            {'field': 'CA_qty_avail', 'type': 'integer', 'label': '', 'func_apply': None, 'maps_to_cms_field': None},
            {'field': 'NY_qty_avail', 'type': 'integer', 'label': '', 'func_apply': None, 'maps_to_cms_field': None},
            {'field': 'TN_qty_avail', 'type': 'integer', 'label': '', 'func_apply': None, 'maps_to_cms_field': None},
            {'field': 'seller_price', 'type': 'decimal', 'label': '', 'func_apply': None, 'maps_to_cms_field': "Cost Price"},
            {'field': 'upc_code', 'type': 'text', 'label': '', 'func_apply': _remove_single_quotes, 'maps_to_cms_field': None},
            {'field': 'msrp', 'type': 'decimal', 'label': '', 'func_apply': None, 'maps_to_cms_field': "Retail Price"},
            {'field': 'weight_lb', 'type': 'decimal', 'label': '', 'func_apply': None, 'maps_to_cms_field': 'Weight'},
            {'field': 'length', 'type': 'decimal', 'label': '', 'func_apply': None, 'maps_to_cms_field': 'Depth'},
            {'field': 'width', 'type': 'decimal', 'label': '', 'func_apply': None, 'maps_to_cms_field': 'Width'},
            {'field': 'height', 'type': 'decimal', 'label': '', 'func_apply': None, 'maps_to_cms_field': 'Height'},
            {'field': 'MAP', 'type': 'text', 'label': '', 'func_apply': None, 'maps_to_cms_field': None},
            {'field': 'sub_category_descript', 'type': 'text', 'label': '', 'func_apply': None, 'maps_to_cms_field': None},
            {'field': 'marketing_descript', 'type': 'text', 'label': '', 'func_apply': None, 'maps_to_cms_field': None},
            {'field': 'product_thumbnail', 'type': 'text', 'label': '', 'func_apply': None, 'maps_to_cms_field': None},
            {'field': 'product_full_image' 'type': 'text', 'label': '', 'func_apply': None, 'maps_to_cms_field': None}
        ]




    def get_feed_data_from_text(self, path):
        with open(path, 'r') as f:
            csv_data = csv.reader(f, delimiter = '\t')





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
