# import random and matplotlib
import random
import matplotlib.ticker
import matplotlib.pyplot as plt


# Strategy Usage
def strategy(maxNumberToAdd, CurrentAmount):
    totalnumber = 0
    
    while totalnumber <= maxNumberToAdd:
        add = random.randint(1,6)
        if add == 1:
            totalnumber = 0
            return totalnumber
        totalnumber = totalnumber + add
        if CurrentAmount + totalnumber >= 100:
            return totalnumber
    return totalnumber

# PigGame
def PigGame(Repeater):
    CurrentRepeat = 0
    
    strategy1Win = 0
    strategy2Win = 0
    strategy3Win = 0
    
    while CurrentRepeat < Repeater:
        strategy_1 = 0
        strategy_2 = 0
        strategy_3 = 0
        
        while strategy_1 <= 100 and strategy_2 <= 100 and strategy_3 <= 100:
            
            strategy_1 += strategy(12,strategy_1)
            if strategy_1 >= 100:
                strategy1Win += 1
                CurrentRepeat += 1
                
            strategy_2 += strategy(33,strategy_2)
            if strategy_2 >= 100:
                strategy2Win += 1
                CurrentRepeat += 1
                
            strategy_3 += strategy(25,strategy_3)
            if strategy_3 >= 100:
                strategy3Win += 1
                CurrentRepeat += 1

    Procent_strategy1 = strategy1Win / Repeater * 100
    Procent_strategy2 = strategy2Win / Repeater * 100
    Procent_strategy3 = strategy3Win / Repeater * 100

    print('Strategy 1 Won: ' + str(strategy1Win) + ' Games.\n' + 'Strategy 2 Won: ' + str(strategy2Win) + ' Games.\n' + 'Strategy 3 Won: ' + str(strategy3Win) + ' Games.')
    output = [int(Procent_strategy1),int(Procent_strategy2),int(Procent_strategy3)]
    return output


# Pig Game Output (Easy Changeable)
output_piggame = PigGame(100000)
                
#  Matplotlib output

plt.bar(1,output_piggame[0],color=['red'],label='Strategy 1 (' + str(output_piggame[0]) + '%)')
plt.bar(2,output_piggame[1],color=['grey'],label='Strategy 2 (' + str(output_piggame[1]) + '%)')
plt.bar(3,output_piggame[2],color=['blue'],label='Strategy 3 (' + str(output_piggame[2]) + '%)')

plt.gca().xaxis.set_major_locator(matplotlib.ticker.MultipleLocator(1))
plt.axis([0,4,0,100])
plt.legend()

plt.show()

#Student Info:

# Patryk Kulik
# 0989317
# INF1J



