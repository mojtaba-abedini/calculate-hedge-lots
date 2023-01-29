
TP = 60                        #TakeProfitLevel
RL = 30                         #Recovery Line 
TPR1 = TP - RL     
TPR2 = TP + RL

PPO = 0
L1 = 0.01

print (TPR1)
print (TPR2)



L2 = abs(L1*TP)/TPR1-PPO

L3 = abs((L1*TP)-(L2*TPR2))/TP-PPO

L4 = abs((-L1*TP)+(L2*TPR1)-(L3*TP))/TPR1 - PPO

L5 = abs((L1*TP)-(L2*TPR2)+(L3*TP)-(L4*TPR2))/TP-PPO

L6 = abs((-L1*TP)+(L2*TPR1)-(L3*TP)+(L4*TPR1)-(L5*TP))/TPR1 - PPO

L7 = abs((L1*TP)-(L2*TPR2)+(L3*TP)-(L4*TPR2)+(L5*TP)-(L6*TPR2))/TP-PPO

L8 = abs((-L1*TP)+(L2*TPR1)-(L3*TP)+(L4*TPR1)-(L5*TP)+(L6*TPR1)-(L7*TP))/TPR1 - PPO

L9 = abs((L1*TP)-(L2*TPR2)+(L3*TP)-(L4*TPR2)+(L5*TP)-(L6*TPR2)+(L7*TP)-(L8*TPR2))/TP-PPO

L10 = abs((-L1*TP)+(L2*TPR1)-(L3*TP)+(L4*TPR1)-(L5*TP)+(L6*TPR1)-(L7*TP)+(L8*TPR1)-(L9*TP))/TPR1 - PPO

print(round(L2, 2))
print(round(L3, 2))
print(round(L4, 2))
print(round(L5, 2))
print(round(L6, 2))
print(round(L7, 2))
print(round(L8, 2))
print(round(L9, 2))
print(round(L10, 2))


