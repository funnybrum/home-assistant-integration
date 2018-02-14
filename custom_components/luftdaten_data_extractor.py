# import json
# import urllib3
# from collections import defaultdict
#
# http = urllib3.PoolManager()
#
# def get_data(lat, lon, radius):
#     query = 'http://api.luftdaten.info/v1/filter/area=%s,%s,%s' % (lat, lon, radius)
#     response = http.request('GET', query)
#     data = json.loads(response.data.decode('utf-8'))
#     return data
#
#
# def process_data(data):
#     sensor_data = defaultdict(set)
#
#     for item in data:
#         location = '%s, %s' % (item['location']['latitude'], item['location']['longitude'])
#         id = item['sensor']['id']
#
#         key = '%s-%s' % (id, location)
#
#         readings = list(set([x['value_type'] for x in item['sensordatavalues']]))
#         for reading in readings:
#             sensor_data[key].add(reading)
#
#     for key in sensor_data:
#         print('%s -> %s' % (key, sensor_data[key]))
#
#
# process_data(get_data(42.645330,23.344518,2))