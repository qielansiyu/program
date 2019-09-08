def fun(m,n):
    a = 1
    for i in range(m):
        a*=n
        n-=1
    for i in range(2,m+1):
        a/=i
    return a
n, m = list(map(int, input().split()))
base = fun(n,n+m)
s = 0
count=m+n-1
while 1:
    if n-1>count:
        break
    s+=fun(n-1,count)
    count-=2

res = s/base
print('%.5f' % round(res,5))
'''
public class Test {
    static Double[][] dp;
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();   // red
        int m = in.nextInt();   // blue
        dp = new Double[n+1][m+1];
        double res = helper(n,m);
        System.out.println(String.format("%.5f",res));
    }
 
    private static double helper(int n, int m){
        if (n<=0 || m<0){
            return 0;
        }else if (n+m <= 2){
            if (m == 0) // n=1 m=0 || n=2 m=0
                return 1;
            else
                return 0.5; // n=1 m=1
        }else if (dp[n][m] != null)
            return dp[n][m];
        else{
            double ans = 1.0*n/(m+n);   // A 直接选择 red
            double t = 1.0*m/(m+n)*(m-1)/(m+n-1);   // A、B 选择 blue
            ans += helper(n-1,m-2)*t*n/(m+n-2) + helper(n,m-3)*t*(m-2)/(m+n-2); // C 选择 red || C 选择 blue
            dp[n][m] = ans;
            return ans;
        }
    }
 
 
}
'''