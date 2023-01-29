TP = 60                        #TakeProfitLevel
RL = 30                        #Recovery Line 
TPR1 = TP - RL     
TPR2 = TP + RL

PPO = 1                        #Pip Profit Offset
L1 = 0.01

L2 = abs(L1*TP)/(TPR1-PPO)

L3 = abs((L1*TP)-(L2*TPR2))/(TP-PPO)

L4 = abs((-L1*TP)+(L2*TPR1)-(L3*TP))/(TPR1 - PPO)

L5 = abs((L1*TP)-(L2*TPR2)+(L3*TP)-(L4*TPR2))/(TP-PPO)

L6 = abs((-L1*TP)+(L2*TPR1)-(L3*TP)+(L4*TPR1)-(L5*TP))/(TPR1 - PPO)

L7 = abs((L1*TP)-(L2*TPR2)+(L3*TP)-(L4*TPR2)+(L5*TP)-(L6*TPR2))/(TP-PPO)

L8 = abs((-L1*TP)+(L2*TPR1)-(L3*TP)+(L4*TPR1)-(L5*TP)+(L6*TPR1)-(L7*TP))/(TPR1 - PPO)

L9 = abs((L1*TP)-(L2*TPR2)+(L3*TP)-(L4*TPR2)+(L5*TP)-(L6*TPR2)+(L7*TP)-(L8*TPR2))/(TP-PPO)

L10 = abs((-L1*TP)+(L2*TPR1)-(L3*TP)+(L4*TPR1)-(L5*TP)+(L6*TPR1)-(L7*TP)+(L8*TPR1)-(L9*TP))/(TPR1 - PPO)

print(round(L2,2))
print(round(L3,2))
print(round(L4,2))
print(round(L5,2))
print(round(L6,2))
print(round(L7,2))
print(round(L8,2))
print(round(L9,2))
print(round(L10,2))


P1 = L1*TP
R1 = -L1*TP

P2 = (-L1*TP) + (L2*TPR1)
R2 = (L1*TP) - (L2*TPR2)

P3 = (L1*TP) - (L2*TPR2) + (L3*TP)
R3 = (-L1*TP) + (L2*TPR1) - (L3*TP)

P4 = (-L1*TP) + (L2*TPR1) - (L3*TP) + (L4*TPR1)
R4 = (L1*TP) - (L2*TPR2) + (L3*TP) - (L4*TPR2)

P5 = (L1*TP) - (L2*TPR2) + (L3*TP) - (L4*TPR2) + (L5*TP)
R5 = (-L1*TP) + (L2*TPR1) - (L3*TP) + (L4*TPR1) - (L5*TP)

P6 = (-L1*TP) + (L2*TPR1) - (L3*TP) + (L4*TPR1) - (L5*TP) + (L6*TPR1)
R6 = (L1*TP) - (L2*TPR2) + (L3*TP) - (L4*TPR2) + (L5*TP) - (L6*TPR2)

P7 = (L1*TP) - (L2*TPR2) + (L3*TP) - (L4*TPR2) + (L5*TP) - (L6*TPR2)+ (L7*TP)
R7 = (-L1*TP) + (L2*TPR1) - (L3*TP) + (L4*TPR1) - (L5*TP) + (L6*TPR1) - (L7*TP)

P8 = (-L1*TP) + (L2*TPR1) - (L3*TP) + (L4*TPR1) - (L5*TP) + (L6*TPR1) - (L7*TP) + (L8*TPR1)
R8 = (L1*TP) - (L2*TPR2) + (L3*TP) - (L4*TPR2) + (L5*TP) - (L6*TPR2) + (L7*TP) - (L8*TPR2)

P9 = (L1*TP) - (L2*TPR2) + (L3*TP) - (L4*TPR2) + (L5*TP) - (L6*TPR2)+ (L7*TP) - (L8*TPR2)+ (L9*TP)
R9 = (-L1*TP) + (L2*TPR1) - (L3*TP) + (L4*TPR1) - (L5*TP) + (L6*TPR1) - (L7*TP) + (L8*TPR1) - (L9*TP)

P10 = (-L1*TP) + (L2*TPR1) - (L3*TP) + (L4*TPR1) - (L5*TP) + (L6*TPR1) - (L7*TP) + (L8*TPR1) - (L9*TP) + (L10*TPR1)
R10 = (L1*TP) - (L2*TPR2) + (L3*TP) - (L4*TPR2) + (L5*TP) - (L6*TPR2) + (L7*TP) - (L8*TPR2) + (L9*TP) - (L10*TPR2)

print('----------------------------------')
print('Max Lots : ',round(P10,2))
print('Max Loss : ',round(R10,2))
