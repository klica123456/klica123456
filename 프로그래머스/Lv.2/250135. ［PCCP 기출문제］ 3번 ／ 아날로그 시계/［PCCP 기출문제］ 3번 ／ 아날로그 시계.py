def solution(h1, m1, s1, h2, m2, s2):
    answer = 0
    h_angle = m1 / 60 * 30 + s1 / 3600 * 30 + h1 * 30
    m_angle = s1 / 60 * 6 + m1 * 6
    s_angle = s1 / 60 * 360
    if h_angle == s_angle:
        answer += 1
    if m_angle == s_angle:
        answer += 1
    if m_angle == h_angle:
        answer -= 1
    while h1 != h2 or m1 != m2 or s1 != s2:
        if h1 >= 12:
            h1 -= 12
            h2 -= 12
        h_angle = m1 / 60 * 30 + s1 / 3600 * 30 + h1 * 30
        m_angle = s1 / 60 * 6 + m1 * 6
        s_angle = s1 / 60 * 360
        h = 0
        m = 0
        if h_angle > s_angle:
            h = 1
        if m_angle > s_angle:
            m = 1
        s1 += 1
        h_angle = m1 / 60 * 30 + s1 / 3600 * 30 + h1 * 30
        m_angle = s1 / 60 * 6 + m1 * 6
        s_angle = s1 / 60 * 360
        if s_angle >= h_angle and h == 1:
            answer += 1
        if s_angle >= m_angle and m == 1:
            answer += 1
        if m_angle == s_angle and h == 1 and m == 1:
            answer -= 1
        if s1 == 60:
            m1 += 1
            s1 = 0
            if m1 == 60:
                h1 += 1
                m1 = 0

    return answer