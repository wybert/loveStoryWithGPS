## encoding:utf-8




from bs4 import BeautifulSoup
import json
import string

reader = open('14.gpx')
text = ''.join(reader.readlines())
soup = BeautifulSoup(text)

to_json = []
for point in soup.findAll('trkpt'):
    ono_point_dict={}
    ono_point_dict['lat'] = string.atof(point['lat'])
    ono_point_dict['lon'] = string.atof(point['lon'])
    to_json += [ono_point_dict]

to_json = json.dumps(to_json)

writer = open('14.json','wb')
writer.write(to_json)
writer.close()
