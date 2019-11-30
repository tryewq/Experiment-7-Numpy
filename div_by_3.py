import numpy as np
M = np.array(range(1,101))
M.resize(10,10)
s = M*M

#Elements that are divisible by 3:
D = s[s%3==0]

np.save('div_by_3', D)

        
    
    
