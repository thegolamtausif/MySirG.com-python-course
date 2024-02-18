def permute(s):
    out = [] 
    if len(s) == 1:
        return [s] 
    else:
        for i in range(len(s)): 
            rest = s[:i] + s[i+1:] 
            for perm in permute(rest):
                out.append(s[i] + perm) 
    return out

s = "bc" 
p = permute(s)
print(p)
