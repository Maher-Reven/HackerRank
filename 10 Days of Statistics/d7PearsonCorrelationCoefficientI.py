import math

def corrCof(x,y):
    result=cov(x,y)/(std(x)*std(y))
    return round(result,3) 

def cov(x,y):
    mean_x=sum(x)/len(x)
    mean_y=sum(y)/len(y)
    result=0
    for i in range(len(x)):
        result+=(x[i]-mean_x)*(y[i]-mean_y)
    return result/len(x) 
def std(x):
    num_items = len(x)
    mean = sum(x) / num_items
    differences = [x - mean for x in x]
    sq_differences = [d ** 2 for d in differences]
    ssd = sum(sq_differences)
    variance = ssd / num_items
    sd = math.sqrt(variance)
    return sd

n=int(input())
X=[float(x) for x in input().split()]
Y=[float(x) for x in input().split()]
print(corrCof(X,Y))


#2nd solution 
N = int(input())
X = list(map(float,input().strip().split()))
Y = list(map(float,input().strip().split()))

mu_x = sum(X) / N
mu_y = sum(Y) / N

stdv_x = (sum([(i - mu_x)**2 for i in X]) / N)**0.5
stdv_y = (sum([(i - mu_y)**2 for i in Y]) / N)**0.5


covariance = sum([(X[i] - mu_x) * (Y[i] -mu_y) for i in range(N)])

correlation_coefficient = covariance / (N * stdv_x * stdv_y)

print(round(correlation_coefficient,3))