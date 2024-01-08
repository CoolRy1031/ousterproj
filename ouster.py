pcap_path = '/Users/thatguy/Desktop/ousterdata/os.json'
metadata_path = '/Users/thatguy/Desktop/ousterdata/osd.pcap'

from ouster import client
with open(metadata_path, 'r') as f:
  info = client.SensorInfo(f.read())
from ouster import pcap
source = pcap.Pcap(pcap_path, info)