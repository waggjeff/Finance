# Little script to calculate your pension savings versus age (JW - July, 2020)
s0 = 100000.# initial pension savings 
a0 = 42. # initial age 

grow = 1.06 # expected average annual growth 
infl = 1.02 # expected average annual inflation
chargs = 0.0062 # annual fund charges 
savemnth = 1000. # amout to save each month

astp = 50. # age at which to stop saving 
nyrs = 30 # number of years to iterate over
yrsnat = 7. # number of years of national insurance contrib.
natins = 9000. # national insurance per year
futnatins = 0.

s = s0
a = a0

for i in range(0,nyrs):
    if (yrsnat >= 10. and a <= 67.):
       futnatins = (yrsnat/35.)*natins
           
    if (a < astp):
        s = (1. - chargs)*s*grow + (savemnth*12.)*infl**i 
    if (a == astp and a >= 55.):
        s = (1. - chargs)*s*grow
        w = 0.25*s
        s = 0.75*s
        print("At age ",a," withdraw 25%, or {:9.2f} tax free".format(w))
    if (a > astp):
        s = (1. - chargs)*s*grow

    a = a + 1.
    yrsnat = yrsnat + 1.
    print(a," inflation corrected: {:7.2f} GBP, and {:5.2f} GBP/yr from National insurance from 67.".format(s /infl**i,futnatins))

    
