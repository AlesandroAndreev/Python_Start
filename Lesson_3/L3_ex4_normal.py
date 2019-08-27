
def par(a,b,c,d):
    sort_by_x = [a,b,c,d]
    sort_by_y = [a,b,c,d]
    itera = 0
    while itera != len(sort_by_x):
        itera=itera+1
        for i in range(len(sort_by_x)-1):
            if sort_by_x[i][0] > sort_by_x[i+1][0]:
                save = sort_by_x[i]
                sort_by_x.remove(save)
                sort_by_x.insert(i+1,save)
        for i in range(len(sort_by_y)-1):
            if sort_by_y[i][1] > sort_by_y[i+1][1]:
                save = sort_by_y[i]
                sort_by_y.remove(save)
                sort_by_y.insert(i+1,save)

    ab = ((abs(sort_by_x[0][0]-sort_by_x[1][0]))**(2) + (abs(sort_by_x[0][1]-sort_by_x[1][1]))*(2))**(0.5)

    cd = ((abs(sort_by_x[2][0]-sort_by_x[3][0]))**(2) + (abs(sort_by_x[2][1]-sort_by_x[3][1]))*(2))**(0.5)

    ad = ((abs(sort_by_y[0][0]-sort_by_y[1][0]))**(2) + (abs(sort_by_y[0][1]-sort_by_y[1][1]))*(2))**(0.5)

    bc = ((abs(sort_by_y[2][0]-sort_by_y[3][0]))**(2) + (abs(sort_by_y[2][1]-sort_by_y[3][1]))*(2))**(0.5)

    if (ab == cd) and (ad == bc):
        answer = "Yes!"
    else:
        answer = "No!"


    return  answer
        
    
    
