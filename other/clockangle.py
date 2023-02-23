

def clockAngle(h, m):

    if (h < 0 or m < 0 or h > 12 or m > 60):
        return None


    if (h == 12):
        h = 0
    if (m == 60)):
        m = 0
        h + 1
        if (h > 12):
            h = h - 12

    hour_angle = 0.5 * (h * 60 + m) 
    minute_angle = 6 * m 

    angle = abs(hour_angle - minute_angle)

    return min(angle, 360-angle)