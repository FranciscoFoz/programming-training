import os
import time

start_time = time.time()

for filename in os.listdir('../3 - Listas e Tuplas'):
    print(filename)
    
end_time = time.time()

print('\nFinal time = ',end_time-start_time,'\n')


start_time2 = time.time()

for filename in os.scandir('../3 - Listas e Tuplas'):
    print(filename)
    
end_time2 = time.time()

print('\nFinal time = ',end_time2-start_time2,'\n')


print(end_time2>end_time)