import datacamp as d

def test_string_replace():
    text = "D t C mpBl ckFrid yS le"
    replacement_val = "a"
    val = " "

    assert d.string_replace(text=text, val=val, replacement_val=replacement_val) == "DataCampBlackFridaySale"

def test_perfect_square():
   val = 10
   assert d.perfect_square(val) == False

   val = 36
   assert d.perfect_square(val) == True

   val = -4
   assert d.perfect_square(val) == False




if __name__ == '__main__':
    

#   text = "D t C mpBl ckFrid yS le"
#   replacement_val = "a"
#   val = " "

#   print(d.string_replace(text=text, val=val, replacement_val=replacement_val))

#   val = -4
#   print(d.perfect_square(val))
    val = 7
    print(d.trailing_zeros(val))
