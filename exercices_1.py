def check_is_balanced(text):
    text = text.upper()
    
    count_r = text.count("R")
    count_j = text.count("J")
    
    print(f"count_r: {count_r} count_j: {count_j}")
   
    return count_r == count_j

# test 
print(check_is_balanced("RRJJ"))
print(check_is_balanced("RRRRJJ"))
print(check_is_balanced("RRJJJJJJ"))
print(check_is_balanced("awwwaqAQAQA"))