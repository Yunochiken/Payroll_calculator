mon_start = float(input("Monday start time "))
mon_finish = float(input("Monday finish time "))
mon_total = (float(mon_finish) - float(mon_start)) / 100
tue_start = float(input("Tuesday start time "))
tue_finish = float(input("Tuesday finish time "))
tue_total = (float(tue_finish) - float(tue_start)) / 100
wed_start = float(input("Wednesday start time "))
wed_finish = float(input("Wednesday's finish time "))
wed_total = (float(wed_finish) - float(wed_start)) / 100
thu_start = float(input("Thursday start time "))
thu_finish = float(input("Thursday finish time "))
thu_total = (float(thu_finish) - float(thu_start)) / 100
fri_start = float(input("Friday start time "))
fri_finish = float(input("Fridays finish time "))
fri_total = (float(fri_finish) - float(fri_start)) / 100
sat_start = float(input("Saturday start time "))
sat_finish = float(input("Saturday finish time "))
sat_total = (float(sat_finish) - float(sat_start)) / 100
sun_start = float(input("Sunday start time "))
sun_finish = float(input("Sunday finish time "))
sun_total = (float(sun_finish) - float(sun_start)) / 100
total_hours = sum = float(mon_total) + float(tue_total) + float(wed_total) + float(thu_total) + float(fri_total) + float(sat_total) + float(sun_total)
print("You've worked ", + total_hours)
total_pay = float(total_hours) * 22.89
print("$", + total_pay)
