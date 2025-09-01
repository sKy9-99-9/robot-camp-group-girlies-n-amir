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

from print_laura import act1_laura, act2_laura, act3_laura
from print_pixie import act1_pixie, act2_pixie, act3_pixie
from print_amir import act1_amir, act2_amir, act3_amir
from print_mathilde import act1_mattie, act2_mattie, act3_mattie
from print_alissa import act1_alissa, act2_alissa, act3_alissa

def build_story() -> str:
    paragraphs = [
        # Act I (Laura → Pixie → Amir → Mattie → Alissa)
        act1_laura(), act1_pixie(), act1_amir(), act1_mattie(), act1_alissa(),
        # Act II (Laura → Pixie → Mattie → Amir → Alissa)
        act2_laura(), act2_pixie(), act2_mattie(), act2_amir(), act2_alissa(),
        # Act III (Laura → Pixie → Amir → Mattie → Alissa)
        act3_laura(), act3_pixie(), act3_amir(), act3_mattie(), act3_alissa(),
    ]
    return "\n".join(paragraphs)

print(build_story())
