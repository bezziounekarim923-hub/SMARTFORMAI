from math import sqrt

# ==========================================================
# Distances
# ==========================================================


def center(rect):

    return (
        rect.x + rect.width / 2,
        rect.y + rect.height / 2,
    )


def distance(a, b):

    ax, ay = center(a)
    bx, by = center(b)

    return sqrt((ax - bx) ** 2 + (ay - by) ** 2)


def horizontal_distance(a, b):

    if a.x < b.x:
        return b.x - (a.x + a.width)

    return a.x - (b.x + b.width)


def vertical_distance(a, b):

    if a.y < b.y:
        return b.y - (a.y + a.height)

    return a.y - (b.y + b.height)


# ==========================================================
# Alignement
# ==========================================================


def same_line(a, b, tolerance=10):

    ay = a.y + a.height / 2
    by = b.y + b.height / 2

    return abs(ay - by) <= tolerance


def same_column(a, b, tolerance=15):

    ax = a.x + a.width / 2
    bx = b.x + b.width / 2

    return abs(ax - bx) <= tolerance


# ==========================================================
# Positions
# ==========================================================


def is_left_of(a, b):

    return (a.x + a.width) <= b.x


def is_right_of(a, b):

    return (b.x + b.width) <= a.x


def is_above(a, b):

    return (a.y + a.height) <= b.y


def is_below(a, b):

    return (b.y + b.height) <= a.y


# ==========================================================
# Overlap
# ==========================================================


def horizontal_overlap(a, b):

    left = max(a.x, b.x)
    right = min(a.x + a.width, b.x + b.width)

    return max(0, right - left)


def vertical_overlap(a, b):

    top = max(a.y, b.y)
    bottom = min(a.y + a.height, b.y + b.height)

    return max(0, bottom - top)


def intersects(a, b):

    return (
        horizontal_overlap(a, b) > 0
        and vertical_overlap(a, b) > 0
    )


def intersection_area(a, b):

    return (
        horizontal_overlap(a, b)
        * vertical_overlap(a, b)
    )


# ==========================================================
# IoU
# ==========================================================


def iou(a, b):

    inter = intersection_area(a, b)

    if inter == 0:
        return 0

    area_a = a.width * a.height
    area_b = b.width * b.height

    union = area_a + area_b - inter

    return inter / union


# ==========================================================
# Containment
# ==========================================================


def contains(outer, inner):

    return (
        inner.x >= outer.x
        and inner.y >= outer.y
        and inner.x + inner.width <= outer.x + outer.width
        and inner.y + inner.height <= outer.y + outer.height
    )


# ==========================================================
# Similarité de taille
# ==========================================================


def similar_height(a, b, tolerance=8):

    return abs(a.height - b.height) <= tolerance


def similar_width(a, b, tolerance=20):

    return abs(a.width - b.width) <= tolerance