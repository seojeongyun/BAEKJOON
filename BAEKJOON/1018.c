#include <stdio.h>

int main()
{
    char chess_map[64] = {0,};
    char continuous_idx_of_chess_map[2] = {2,3};
    
    int row, col = 0;
    scanf("%d %d", &row, &col);
    
    char input_map[row*col+1];
    for(int i=0; i<row; i++)
    {
        scanf("%s",&input_map[col * i]);
    }
    input_map[row*col] = '\0';
    
    char input_map_rep_num[row*col];
    for(int i=0; i<row*col; i++)
    {
        if(input_map[i] == 'W')
            input_map_rep_num[i] = 1;
        
        else
            input_map_rep_num[i] = 0;
    }
    
    char temp = 0;
    char temp_ = 0;
    
    int receptive_field_idx = 0;
    int start_idx = 0;
    int receptive_field_row_cnt = 1;
    int trigger = 0;
    int min = 64;
    int cnt = 0;
    while(1)
    {
        // CNN처럼 stride, receptive_field 계산
        for(int row_idx = 0; row_idx < 8; row_idx++)
        {
            for(int col_idx = 0; col_idx < 8; col_idx++)
            {
                receptive_field_idx = (col_idx + start_idx) + (col * row_idx);
                chess_map[col_idx + 8 * row_idx] = input_map_rep_num[receptive_field_idx];
                
//                if(col_idx == 0 && row_idx == 0)
//                    printf("receptive_field_idx: %d\n", receptive_field_idx);
//                if(col_idx == 7 && row_idx == 7)
//                    printf("receptive_field_idx: %d\n", receptive_field_idx);
            }
        }
        
        // start idx 계산
        // col - 8까지 계산하고, 이후 start_idx += 8
        if(start_idx < (receptive_field_row_cnt * col - 8))
        {
//            printf("start_idx: %d \n", start_idx);
//            printf("receptive_field_row_cnt * col - 8): %d\n", receptive_field_row_cnt * col - 8);
            start_idx++;
        }
            
        
        else
        {
            start_idx = receptive_field_row_cnt * col;
            receptive_field_row_cnt++;
        }
//        printf("\nstart_idx: %d \n", start_idx-1);
        
        // 연속된 두 개의 값 비교
        for(int i = 0; i < 2; i++)
        {
            cnt = 0;
            continuous_idx_of_chess_map[0] = 2;
            continuous_idx_of_chess_map[1] = 3;
            for(int row_idx = 0; row_idx < 8; row_idx++)
            {
                for(int col_idx = 0; col_idx < 8; col_idx++)
                {
                    // 0 -> 1 로 값을 계속 밀어넣어줌, 쉬프트 시킴
                    //
                    if((col_idx + 8 * row_idx) == 0) // 좌상단이 0인 경우와 1인 경우로 나누기 위한 조건
                    {
                        continuous_idx_of_chess_map[0] = i; // 좌상단이 0인 경우와 1인 경우를 for문으로 구현
                        if(chess_map[0] != i) // 제공된 input_map에서 좌상단이 0으로 제공되었는데, 0이 아닌 1로 두고 고려할 때
                            cnt++; // 0 -> 1로 교체해야하니 cnt++
                    }
                    
                    else  // 좌상단을 제외한 나머지 부분
                    {
                        temp = continuous_idx_of_chess_map[0];
                        if(!trigger)    // 값이 같지 않은 경우
                            continuous_idx_of_chess_map[1] = temp; // 계속 쉬프트
                        else    // 값이 같은 경우
                            continuous_idx_of_chess_map[1] = temp_; // 이전의 값을 반전시켜서 1로 쉬프트
                        continuous_idx_of_chess_map[0] = chess_map[col_idx + 8 * row_idx];
                    }
                    //
                    
                    if(continuous_idx_of_chess_map[0] == continuous_idx_of_chess_map[1] && col_idx + 8 * row_idx != 8 * row_idx)
                    {
                        trigger = 1;
                        temp_ = !continuous_idx_of_chess_map[0];
                        cnt++;
                    }
                    
                    else if(continuous_idx_of_chess_map[0] != continuous_idx_of_chess_map[1] && col_idx + 8 * row_idx == 8 * row_idx && row_idx > 0)
                        // 첫 행의 마지막(idx = 7)과 두 번째 행의 시작(idx = 8)은 같아야 정상.
                        // 그래서 idx=8에서 값이 다른 경우도 값을 반전시킴
                        // 다만 row_idx = 0일 땐, col_idx + 8 * row_idx == 8 * row_idx 조건에서 시작하자마자 0 == 0으로 일치하게 되고
                        // 2,3 으로 초기화되어있기 때문에 시작부터 값을 교체하게 되어서 이상한 결과가 나옴.
                        // 그래서 row_idx > 0을 추가
                    {
                        trigger = 1;
                        temp_ = !continuous_idx_of_chess_map[0];
                        cnt++;
                    }
                    
                    else trigger = 0;
//                    printf("%d  ", chess_map[col_idx + 8 * row_idx]);
                } // col_idx
//                printf("\n");
            } // row_idx
//            printf("\n");
            if(min > cnt)
                min = cnt;
//            printf("i: %d, min: %d\n", i, min);
//            printf("i: %d, cnt: %d\n",i,cnt);
        } // i
//        printf("\n\n\n");
        
        
        if(receptive_field_idx == col * row - 1)
            break;
    }
    
    printf("%d", min);
    return 0;
}
