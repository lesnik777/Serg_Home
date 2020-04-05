def areYouPlayingBanjo(name):
     #Implement me!
     if name[0] in ('r','R'):     
         return name +' playing banjo'
     else: 
        return name + ' does not play banjo'
   
print(areYouPlayingBanjo('John'))

#################################

def areYouPlayingBanjo(name):
     #Implement me!    
     if str(name[0]).lower()=='r':    
         return name +' playing banjo'
     else: 
        return name + ' does not play banjo'
   
print(areYouPlayingBanjo('John'))

#################################
def areYouPlayingBanjo(name):
     #Implement me!    
    return name +' playing banjo' if name[0] in ('r','R') else name + ' does not play banjo'

print(areYouPlayingBanjo('John'))
