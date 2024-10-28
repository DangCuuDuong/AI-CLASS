import math
MIN = -math.inf
MAX = math.inf

def alpha_beta_maxmin(depth,node,maximizing,value,alpha,beta):
    if depth ==4:
        return value[node]
    if maximizing:
        best = MIN
        for i in range(0,2):
            val = alpha_beta_maxmin(depth +1, node *2+i,False,value,alpha,beta)
            best = max(best,val)
            alpha = max(alpha,best)
            if beta <= alpha:
                break
        return best
    else:
        best =MAX
        for i in range(0,2):
            val = alpha_beta_maxmin(depth +1, node *2+i,True,value,alpha,beta)
            best = min(best,val)
            beta= min(beta,best)
            if beta <= alpha:
                break
        return best
    
tree = [80, 30, 25, 35, 55, 20, 5, 65, 40, 10, 70, 15, 50, 45, 60, 75]
print("The optimal value:", alpha_beta_maxmin(0,0,True,tree,MIN,MAX))
#https://drive.google.com/drive/folders/1TNaIHJjqzf0z4eRTp8LfDjNSl0AERugK?usp=sharing

        