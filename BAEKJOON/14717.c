#include <stdio.h>

int main()
{
    int num_a, num_b;
    
    scanf("%d %d",&num_a, &num_b);
    
    float total_case = (18 * 17 / 2); // 18C2 = 153
    float win_prob = 0;

    float case_num[10] = {0,};
    int cnt = 0;
    
    if(num_a == num_b) // 내 패가 땡일 경우
    {
        float lose_case_in_ddang = 10. - num_a; // 내가 질 경우는 나보다 높은 땡을 가진 경우 뿐
//        printf("lose_case_in_ddang : %f\n", lose_case_in_ddang);
        win_prob = 1 - (lose_case_in_ddang / (total_case)); // 이기거나 비길 확률이 된 것 같음.
//        printf("(lose_case_in_ddang / total_case) : %f\n", (lose_case_in_ddang / total_case_d));
    }
    
    else // 내 패가 끗 패일 경우
    {
        float total_win_case_in_kkeut = 0;
        float my_pae = num_a + num_b > 10 ? (num_a + num_b) % 10
                     : num_a + num_b == 10 ? 0 : num_a + num_b;
        float win_case_in_kkeut = my_pae; // 내 패가 3끗이라고 하면, 상대방이 0끗,1끗,2끗일 때(3개의 숫자) 내가 이김.
        
        float case_num[10] = {0,};
        
        for(int i = 1; i <= 10; i++)
        {
            for(int j = 1; j <= 10; j++)
            {
                if(i != j && (i != num_a && j != num_b)) // i != j는 끗패에 대해서만을 의미하고, (i != num_a && i != num_b는 내 패를 제외한 나머지 패만으로 0~9끗에 대한 경우의 수를 구하기 위함
                {
                    if(i+j > 10)
                    {
                        case_num[(i+j) % 10] += 2.;
//                        printf("두 패는 %d와 %d로, %d끗입니다.\n", i,j, (i+j) % 10);
                    }
                    
                    else if(i+j == 10)
                    {
                        case_num[0] += 2.;
                        // 2씩 더해주는 이유
                        // 예를 들어 들어온 패가 1과 2이라서 3끗이라고 가정할 때
                        // 상대방이 3과 7을 뽑아서 0끗을 만들 경우의 수는
                        // 첫 번째 화투 세트에서 3을 뽑고, 두 번째 화투 세트에서 7을 뽑는 경우 하나, {3,7'}
                        // 두 번째 화투 세트에서 3을 뽑고, 첫 번째 화투 세트에서 7을 뽑는 경우 하나, {3',7}
                        // 첫 번째 화투 세트에서 3을 뽑고, 첫 번째 화투 세트에서 7을 뽑는 경우 하나, {3, 7}
                        // 두 번째 화투 세트에서 3을 뽑고, 두 번째 화투 세트에서 7을 뽑는 경우 하나, {3',7'}
                        // 으로 네 가지 경우가 존재한다.
                        // 그러나 2중 포문에 의해서 첫 번째 화투 세트에 의한 값인지 두 번째 화투 세트에서 의한 값인지가 결정되고
                        // 이 때 가능한 경우는 {3, 7'} 과 {3', 7} 뿐이므로
                        // 2씩 누적을 두 번 씩 해주어 네 가지 경우를 모두 만족시켜준다.
                        // 이 경우는 나에게 들어온 패가 1과 2라서, 3과 7이 모두 두 장 씩 살아있는 경우에 대한 것이고,
                        //
                        // 만약, 상대방이 1과 9를 뽑아서 9끗을 만들게 된다면 이에 대한 경우의 수는 어떻게 될까 ?
                        // 나에게 들어온 1이 첫 번째 세트에서 들어온 1이라면
                        // 살아있는 1은 두 번째 세트에서의 한 장이고, 9는 첫 번째 세트와 두 번째 세트 모두에서 살아있기 때문에
                        // {1', 9} 와 {1', 9'} 두 가지 경우만이 존재한다.
                        // 이 때, 조건에서 (i != num_a && j != num_b)를 적용했기 때문에
                        // 2중 포문에서 {1', 9'}는 만족될 수 없으므로 2씩 누적해준다.
                        
//                        printf("두 패는 %d와 %d로, %d끗입니다.\n", i,j,0);
                    }
                    
                    else
                    {
                        case_num[i+j] += 2.;
//                        printf("두 패는 %d와 %d로, %d끗입니다.\n", i,j, i+j);
                    }
                }
            }
        }
        
//        for(int i = 0; i < 10; i++)
//            printf("case_num[%d] : %f\n", i, case_num[i]);
        
        for(int i = 0; i < win_case_in_kkeut; i++)
        {
            total_win_case_in_kkeut += case_num[i];
        }
        
        win_prob = total_win_case_in_kkeut / total_case;
    }
    
    printf("%.3f",win_prob);
    return 0;
}

