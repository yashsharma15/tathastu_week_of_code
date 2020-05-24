for i in range (1,4):
  runs = int(input("run scored by the player in 60 balls:"))
  strike_rate = (runs / 60) * 100
  extra_runs = int((strike_rate / 100) * 120)
  max_six = runs // 6
  print (strike_rate)
  print (extra_runs)
  print (max_six)
