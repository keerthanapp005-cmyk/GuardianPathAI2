def get_direction(box, frame_width):
    """
    Determines whether an object is on the
    left, center, or right of the camera view.
    """

    x1, y1, x2, y2 = box

    center_x = (x1 + x2) / 2

    if center_x < frame_width / 3:
        return "left"

    elif center_x < 2 * frame_width / 3:
        return "ahead"

    else:
        return "right"