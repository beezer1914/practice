from sympy import false, true


is_magician = False
is_expert = False

#check if magician and expert: If true, print "you are a master magician"
#check if magician and not expert:"your tried"
#if not a magician "Leave this place"

if is_magician and is_expert:
    print('You are a master magician!')
elif is_magician and not is_expert:
    print('At least youre trying')
elif not is_magician and not is_expert:
    print('you suck')
    
    
          
