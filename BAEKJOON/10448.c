//#include <stdio.h>
//int calc_triangle_num(int num)
//{
//    return num * (num+1) / 2;
//}
//
//int main()
//{
//    int case_num;
//    scanf("%d", &case_num);
//    
//    int num[case_num];
//    for(int i = 0; i < case_num; i++)
//    {
//        scanf("%d", &num[i]);
//    }
//    
//    for(int z = 0; z < case_num; z++)
//    {
//        int num_ = 0;
//        int triangle_num = 0;
//        
//        while(triangle_num <= num[z])
//        {
//            num_++;
//            triangle_num = calc_triangle_num(num_);
//        };
//        
//        int triangle_num_array_size = num_;
//        int triangle_num_array[triangle_num_array_size];
//        for(int i = 1; i <= triangle_num_array_size; i++)
//        {
//            triangle_num = calc_triangle_num(i);
////            printf("triangle_num : %d\n", triangle_num);
//            triangle_num_array[i-1] = triangle_num;
////            printf("triangle_num_array[%d] : %d\n", i-1, triangle_num_array[i-1]);
//        }
//        
//        int selected_triangle_num[3] = {0,};
//        int loop_break_trigger = 0;
//        
//        // *-*-*-*-*-*- DEBUG *-*-*-*-*-*-
//        //    printf("triangle_num_array_size : %d\n", triangle_num_array_size);
//        //
//        //    for (int i = 0; i < triangle_num_array_size; i++)
//        //    {
//        //        printf("triangle_num_array[%d] : %d\n", i, triangle_num_array[i]);
//        //    }
//        // *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
//        
//        for(int i = 0; i < triangle_num_array_size; i++)
//        {
//            for(int j = 0; j < triangle_num_array_size; j++)
//            {
//                for(int k = 0; k < triangle_num_array_size; k++)
//                {
//                    selected_triangle_num[0] = triangle_num_array[i];
//                    selected_triangle_num[1] = triangle_num_array[j];
//                    selected_triangle_num[2] = triangle_num_array[k];
//                    
//                    //                    printf("\n");
//                    //                    printf("*-*-*-*-*-*-*-*-*-*\n");
//                    //                    //                printf("selected_triangle_num[%d] : %d\n", 0, selected_triangle_num[0]);
//                    //                    //                printf("selected_triangle_num[%d] : %d\n", 1, selected_triangle_num[1]);
//                    //                    //                printf("selected_triangle_num[%d] : %d\n", 2, selected_triangle_num[2]);
//                    //                    printf("selected_triangle_num[0+1+2] : %d\n",selected_triangle_num[0] + selected_triangle_num[1] + selected_triangle_num[2]);
//                    //                    printf("*-*-*-*-*-*-*-*-*-*\n");
//                    //                    printf("\n");
//                    
//                    if(selected_triangle_num[0] + selected_triangle_num[1] + selected_triangle_num[2] == num[z])
//                    {
////                        printf("selected_triangle_num[0+1+2] : %d\n",selected_triangle_num[0] + selected_triangle_num[1] + selected_triangle_num[2]);
//                        loop_break_trigger = 1;
//                        break;
//                    }
//                }
//                if(loop_break_trigger) break;
//            }
//            if(loop_break_trigger) break;
//        }
//        
//        if(loop_break_trigger) printf("1\n");
//        else printf("0\n");
//    }
//
//    
//    return 0;
//}
