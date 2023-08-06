# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['simplify_polyline']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.24.2,<2.0.0']

setup_kwargs = {
    'name': 'simplify-polyline',
    'version': '0.0.2',
    'description': 'Simplify an open of closed polyline',
    'long_description': "# simplify_polyline\n\nSimplify an open or closed polyline.\n\n## Two functions:\n\nVisvalingham-Whyatt removes the smallest triangles formed by three consecutive points\nin a polyline or polygon. The big advantage for my purposes is that the starting\npoint on a polygon will not affect the result. The big disadvantage is that tall,\nthin spikes are removed along with short, thin triangles. So the smoothed polygon or\npolyline may not fit in anything close to the convex hull of the input.\n\nuse the Visvalingham-Whyatt algorithm with `vs_simplify`\n\nDouglas-Peucker gives a better representation of the convex hull. The big\ndisadvantage with Douglas-Peucker is that the starting point on a polygon will affect\nthe result. I've addressed this in the slow, but ideal (for my purposes) `simplify`\nfunction.\n\nuse the Douglas-Peucker algoritm with `simplify`\n\nThis will usually be the better choice.\n\n## arguments\n\n\n**verts** vertices along polyline. Anything that can be cast into a '*, 2'\n    array.\n\n(`simplify`) **min_dist** minimum height above a line segment for a point to be\nincluded.\n\n(`vw_simplify`) **min_area** minimum area of a triangle for a point to be\nincluded.\n\n**is_closed** optionally specify whether verts describe a polyline or polygon.\nIf not specified, is_closed is inferred from verts[0] == verts[-1]. The form of\nthe input (last vert == first vert) will be replicated in the output.\n\nIf verts is (a, b, c, d, a), return value will be (a, ..., a)\n\nIf verts is (a, b, c, d), and is_closed is True, return value will be (a, ..., d)\n\nSo, there are two ways to deal with closed polygons:\n\n* close by repeating first point at the end. Return value will keep this format\n\n* close by specifying `is_closed`. Return value will not repeat last point\n\n## install\n\n~~~\npip install simplify_polyline\n~~~\n",
    'author': 'Shay Hill',
    'author_email': 'shay_public@hotmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
