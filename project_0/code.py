def code(string_):
    count = 0
    de_code, final_code = '', ''
    current_simbol = string_[0]
    for simbol in string_:
        if current_simbol == simbol:
           count += 1
        else:
            de_code = current_simbol + str(count )
            final_code = final_code + de_code
            current_simbol = simbol
            count = 1
    return final_code

print(code('aaabbccccdaa'))