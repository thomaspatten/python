def grade_calc(physics, maths, english):
    total_score= (physics+maths+english)      
    percentage=total_score/3
    grade=()
    
    if percentage<50:
        grade=("d")
    elif percentage>=50 and percentage<60:
        grade= ("c")
    elif percentage>=60 and percentage<70:
        grade= ("b")
    elif percentage>=70 and percentage<80:
        grade= ("a")

    return grade


    
        