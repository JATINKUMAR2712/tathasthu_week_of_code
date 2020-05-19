
  run_player1 =int(input("ENTER RUN SCORE BY PLAYER1 IN 60 BALLS :"))
  run_player2 =int(input("ENTER RUN SCORE BY PLAYER2 IN 60 BALLS :"))
  run_player3 =int(input("ENTER RUN SCORE BY PLAYER3 IN 60 BALLS :"))

  STRIKE_RATE1 =run_player1 * 100 /60
  STRIKE_RATE2 =run_player1 * 100 /60
  STRIKE_RATE3 =run_player1 * 100 /60

  print("STRIKE RATE OF PLAYER1 IS : ",STRIKE_RATE1)
  print("STRIKE RATE OF PLAYER2 IS : ",STRIKE_RATE2)
  print("STRIKE RATE OF PLAYER3 IS : ",STRIKE_RATE3)

 print("RUN SCORED BY PLAYER1 IF HE PLAY 60 BALL MORE : ",run_player1*2)
 print("RUN SCORED BY PLAYER2 IF HE PLAY 60 BALL MORE : ",run_player2*2)
 print("RUN SCORED BY PLAYER3 IF HE PLAY 60 BALL MORE : ",run_player2*2)

 print("Maximum Six hit by PLayer 1  : ",run_player1//6)
 print("Maximum Six hit by PLayer 2  : ",run_player2//6)
 print("Maximum Six hit by PLayer 3  : ",run_player3//6)
