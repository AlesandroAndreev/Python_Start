

def sorti(sort):
   itera = 0
   while itera != len(sort):
       itera=itera+1
       for i in range(len(sort)-1):
           if sort[i] > sort[i+1]:
               save = int(sort[i])
               sort.remove(save)
               sort.insert(i+1,save)
   return sort
