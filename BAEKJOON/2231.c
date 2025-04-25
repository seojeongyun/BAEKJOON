// -*-*-*-*-* 2231 -*-*-*-*-*
//#include <stdio.h>
//
//int main()
//{
//    int N;
////    printf("자연수(1 ~ 1,000,000)을 입력하세요: ");
//    scanf("%d", &N);
//
//    int N_ = N;
//    int a,b,c,d,e,f,g = 0;
//    int sum = 0;
//    int min = N;
//
//    while(N != 0)
//    {
//        a = N / 1000000;
//        b = N % 1000000 / 100000;
//        c = N % 100000 / 10000;
//        d = N % 10000 / 1000;
//        e = N % 1000 / 100;
//        f = N % 100 / 10;
//        g = N % 10 / 1;
//
//        sum = N + a + b + c + d + e + f + g;
//
//        if(min > N && sum == N_) min = N;
//
//        N--;
//    }
//
//    if(min == N_) min = 0;
//
//    printf("%d", min);
//    return 0;
//}
