from print_pixie import get_name
from print_laura import print_laura
from print_amir import mfut
from print_alissa import print_alissa
from print_mathilde import print_mathilde
from intro import get_intro

def get_group_names():

  intro = get_intro()
  
  names = [
        get_name(),
        print_laura(), 
        mfut(),
        print_alissa(),
        print_mathilde()
  ]
    
  return intro + " " + ", ".join(names)

print(get_group_names())
