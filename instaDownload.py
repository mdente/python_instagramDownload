# Official Page -> https://instaloader.github.io/

# Step 1 : pip install instaloader
# Step 2 : pip install instaDP
# Step 3 : input your login and password
# Step 4 : Play ! ( All files will be in a subfolder with the profile name in the project folder.)

# Attention!!! 
# Instagram services will block connections in case of excessive requests. 
# An interval of approximately 20 minutes will occur every 200 downloads.

# Let´s Hack!!
# marcelo.dente@live.com
# 
#Thanks Alexander Graf !! ( https://github.com/sponsors/aandergr )
# Buy Alex a Coffee --> https://www.paypal.com/paypalme/aandergr   Or BitCoin : 1Nst4LoadeYzrKjJ1DX9CpbLXBYE9RKLwY

# The current Unix epoch time is  1633300352


import instaloader

getInsta = instaloader.Instaloader()


login   = 'enter your instagram user'
passwd  = 'enter your instagram password'
account = 'enter target instagram account'

getInsta.login(login,passwd)
getInsta.download_profile(account)

