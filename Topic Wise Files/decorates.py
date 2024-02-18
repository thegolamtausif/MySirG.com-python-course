def decor_result(result_fun):
    def distinction(marks):
        for m in marks:
            if m>= 75:
                print("Congrats,you have got distinction")
        else:
            result_fun(marks)
    return distinction
@decor_result
def result(marks):
    for m in marks:
        if m>33:
            pass
        else:
            print("failed.")
            break
    else:
        print("passed")

result([35,45,76,82,35,53])