import geoplotlib
from geoplotlib.utils import read_csv, BoundingBox


data = read_csv('/Users/ancu/Dropbox/phd/code-projects/geoplotlib/examples/data/bus.csv')
geoplotlib.voronoi(data, f_tooltip=lambda r: r['name'])
geoplotlib.set_bbox(BoundingBox.KBH)
geoplotlib.show()
