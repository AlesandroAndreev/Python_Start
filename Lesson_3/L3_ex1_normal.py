def fibonachi(n,m):
    f_o =[1,1]
    for i in range(0,m+1):
        n_min_1 = i
        n_min_2 = i+1
        f_plus = f_o[n_min_1] + f_o[n_min_2]
        f_o.append(f_plus)
    return f_o[n:(m+1)]




