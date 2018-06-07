import datetime
from calendar import monthrange

daysOfWeek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
mounth = ['January', 'February', 'March', 'April', 'May', 'June', 'July','August', 'September', 'October', 'November', 'December']

def solution(Y, A, B, W):
    m1 = mounth.index(A) + 1
    m2 = mounth.index(B) + 1

    d1 = datetime.date(Y, m1, 1)
    d2 = datetime.date(Y, m2, (monthrange(Y, m2)[1]-7))

    nm = next_weekday(d1, 0)
    ns = next_weekday(d2, 6)

    #print(nm, ns, int((ns - nm).days/7))
    return int((ns - nm).days/7)


def next_weekday(d, weekday):
    days_ahead = weekday - d.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    return d + datetime.timedelta(days_ahead)

if __name__ == '__main__':
    #print(solution(2014, "April", "May", "Wednesday"))
    assert 6 == solution(2014, "April", "May", "Wednesday")