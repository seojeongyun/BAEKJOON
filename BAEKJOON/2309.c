// -*-*-*-*-* 2309 -*-*-*-*-*
//#include <stdio.h>
//
//int main()
//{
//    int orig[9] = {0,};
//    int correct[7] = {0,};
//    int break_trigger = 0;
//    for(int i = 0; i < 9; i++)
//    {
//        scanf("%d", &orig[i]);
//    }
//
//    for(int i = 0; i < 9; i++)
//    {
//        for(int j = 0; j < 9; j++)
//        {
//            if(i != j)
//            {
//                int sum = 0;
//                int correct_idx = 0;
//                for(int k = 0; k < 9; k++)
//                {
//                    if(k!=i && k!=j)
//                    {
//                        correct[correct_idx] = orig[k];
//                        sum += orig[k];
////                        printf("sum: %d         orig[%d] : %d\n",sum,k,orig[k]);
//                        correct_idx++;
//                    }
//                }
//                if(sum == 100)
//                {
////                    for(int i=0; i<7; i++)
////                        printf("correct[%d] : %d, when sum is 100\n", i, correct[i]);
////                    printf("sum: %d\n",sum);
//                    break_trigger = 1;
//                    break;
//                }
//            }
//        }
//        if(break_trigger == 1) break;
//    }
//
//    int swap = 0;
//
//    for(int i = 0; i < 7; i++)
//    {
//        for(int j = 0; j < 7; j++)
//        {
//            if(correct[i] > correct[j] && i != j)
//            {
//                swap = correct[i];
//                correct[i] = correct[j];
//                correct[j] = swap;
//            }
//
//        }
//    }
//
//    for(int i = 6; i >= 0; i--)
//        printf("%d\n", correct[i]);
//
//    return 0;
//}
