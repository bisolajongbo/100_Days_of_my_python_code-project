def calculate_score(name1,name2):
    both_name= name1+name2.lower()

    t=both_name.count("t")
    r=both_name.count("r")
    u=both_name.count("u")
    e=both_name.count("e")
    first_word=t+r+u+e

    l=both_name.count("l")
    o=both_name.count("o")
    v=both_name.count("v")
    e=both_name.count("e")
    second_word= l+o+v+e
    result=int(str(first_word)+str(second_word))
    print(result)
calculate_score("Bisol","Frank")