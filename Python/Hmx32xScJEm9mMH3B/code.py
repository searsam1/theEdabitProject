from datetime import datetime

def longest_streak(lst):
    if len(lst) == 1:
        return 1
    if not lst:
        return 0

    l = [ datetime.strptime(d["date"], "%Y-%m-%d") for d in lst]

    streaks = [] 
    count = 1
    for i in range(1, len(l)):
        e1, e2 = l[i-1], l[i]
        res = (e2 - e1)
        if str(res) == "1 day, 0:00:00":
            count += 1
        else:
            streaks.append(count)
            count = 1
    streaks.append(count)
    return max(streaks) if streaks else count

class Test:
    i = 0 
    def assert_equals(a,b,m=None):
        Test.i += 1
        try:
            assert a == b   
        except AssertionError:
            print(f"{a}\n > should equal \n\t{b}")
            if m:
                print(m)
            print("Test: ", Test.i)




Test.assert_equals(longest_streak([
  {
    "date": "2019-09-16"
  },
  {
    "date": "2019-09-17"
  },
  {
    "date": "2019-09-21"
  },
  {
    "date": "2019-09-22"
  },
  {
    "date": "2019-09-23"
  }
]), 3)
