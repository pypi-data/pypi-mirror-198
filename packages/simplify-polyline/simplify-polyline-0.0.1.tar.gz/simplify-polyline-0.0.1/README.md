# simplify_polyline

Simplify an open or closed polyline.

## Two functions:

Visvalingham-Whyatt removes the smallest triangles formed by three consecutive points
in a polyline or polygon. The big advantage for my purposes is that the starting
point on a polygon will not affect the result. The big disadvantage is that tall,
thin spikes are removed along with short, thin triangles. So the smoothed polygon or
polyline may not fit in anything close to the convex hull of the input.

use the Visvalingham-Whyatt algorithm with `vs_simplify`

Douglas-Peucker gives a better representation of the convex hull. The big
disadvantage with Douglas-Peucker is that the starting point on a polygon will affect
the result. I've addressed this in the slow, but ideal (for my purposes) `simplify`
function.

use the Douglas-Peucker algoritm with `simplify`

This will usually be the better choice.

## arguments


**verts** vertices along polyline. Anything that can be cast into a '*, 2'
    array.

(`simplify`) **min_dist** minimum height above a line segment for a point to be
included.

(`vw_simplify`) **min_area** minimum area of a triangle for a point to be
included.

**is_closed** optionally specify whether verts describe a polyline or polygon.
If not specified, is_closed is inferred from verts[0] == verts[-1]. The form of
the input (last vert == first vert) will be replicated in the output.

If verts is (a, b, c, d, a), return value will be (a, ..., a)

If verts is (a, b, c, d), and is_closed is True, return value will be (a, ..., d)

So, there are two ways to deal with closed polygons:

* close by repeating first point at the end. Return value will keep this format

* close by specifying `is_closed`. Return value will not repeat last point

## install

~~~
pip install simplify_polyline
~~~
