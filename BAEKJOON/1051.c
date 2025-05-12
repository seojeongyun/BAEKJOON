#include <stdio.h>

int main()
{
    char rectangle[2501] = {0,}; // 주어지는 N과 M이 50이하의 자연수이기 때문에 2500
    int square_point[4] = {0,};
    int N, M = 0;
    
    scanf("%d %d",&N, &M);
    
    // 연속된 입력을 받기 위해 문자열로 값을 받음
    for(int row_idx = 0; row_idx < N; row_idx++)
    {
        scanf("%s", &rectangle[row_idx * M]);
    }
    
    // 문자로 표현된 각 숫자를 정수로 표현하기 위해 아스키코드 0만큼의 값을 빼줌
    for(int i = 0; i < N * M; i++)
    {
        rectangle[i] = rectangle[i] - '0';
//        printf("rectangle[%d] : %d\n", i, rectangle[i]);
    }
    
    int idx = 0;
    int size = 0;
    int left_upper = 0;
    int right_upper = 0;
    int left_lower = 0;
    int right_lower = 0;
    int stride_row = 0;
    int stride_col = 0;
    int max = 0;
    
    while(1)
    {
        if(N != 1)
        {
            size++;
            if(N-size < 0 || M-size <- 0)
                break;
            
            for(int stride_row = 0; stride_row < N-size; stride_row++)
            {
                for(int stride_col = 0; stride_col < M-size; stride_col++)
                {
                    left_upper = stride_row * M + stride_col;
                    left_lower = left_upper + size * M;
                    right_upper = left_upper + size;
                    right_lower = left_lower + size;
                    
                    // stride_row랑 size 계산
                    
                    // idx 계산
                    for(int row_idx = 0; row_idx < N; row_idx++)
                    {
                        for(int col_idx = 0; col_idx < M; col_idx++)
                        {
                            idx = row_idx * M + col_idx;
                            if(idx == left_upper)
                                square_point[0] = rectangle[idx];
                            else if(idx == left_lower)
                                square_point[1] = rectangle[idx];
                            else if(idx == right_upper)
                                square_point[2] = rectangle[idx];
                            else if(idx == right_lower)
                                square_point[3] = rectangle[idx];
                        }
                    }
//                    printf("size : %d\n", size);
//                    printf("(%d,  %d)\n",left_upper,right_upper);
//                    printf("(%d,  %d)\n",left_lower,right_lower);
//                    printf("(%d,  %d)\n",square_point[0],square_point[2]);
//                    printf("(%d,  %d)\n",square_point[1],square_point[3]);
                    //
                    if(square_point[0] == square_point[1] &&
                       square_point[0] == square_point[2] &&
                       square_point[0] == square_point[3] &&
                       square_point[1] == square_point[2] &&
                       square_point[1] == square_point[3] &&
                       square_point[2] == square_point[3])
                    {
//                        printf("size: %d",size);
//                        printf("1123123213");
                        if(max < size+1)
                            max = size+1;
                    }
                }
            }
            if(max == 0)
                max = 1;
        }
        //
        //
        //
        //
        else
        {
            max = 1;
            break;
        }
        
        
    }
    printf("%d", max*max);
    return 0;
}
