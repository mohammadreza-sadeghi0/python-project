n=int(input('adad ra vared khoned: '))
adad_aval=True
for i in range(2,n):
    if n%i == 0:
        adad_aval=False
if adad_aval == True:
    print('its prime')
else:
    print('its not prime')        
