////
////  Untitled.h
////  
////
////  Created by 서정윤 on 7/23/25.
////
//

//#include <stdio.h>
//#include <stdlib.h>
//
//typedef struct
//{
//    int* data;
//    int rear;
//    int front;
//} Queue;
//
//void DFS(int idx, int N, int *visited, int graph[][N+1]);
//void BFS(Queue q, int N, int* visited, int graph[][N+1]);
//
//void DFS(int idx, int N, int *visited, int graph[][N+1])
//{
//    visited[idx] = 1;
//    printf("%d ", idx);
//    
//    for (int next = 0; next < N + 1; next++)
//    {
//        if (visited[next] == 0 && graph[idx][next] == 1)
//            DFS(next, N, visited, graph);
//    }
//}
//
//void BFS(Queue q, int N, int* visited, int graph[][N+1])
//{
//    while(q.front < q.rear)
//    {
//        int curr = q.data[++q.front];
//        printf("%d ", curr);
//        for(int next = 0; next < N + 1; next++)
//        {
//            if(visited[next] == 0 && graph[curr][next] == 1)
//            {
//                q.data[++q.rear] = next;
//                visited[next] = 1;
//            }
//        }
//    }
//}
//
//int main()
//{
//    int N, M, V = 0;
//    scanf("%d %d %d", &N, &M, &V);
//    
//    int (*graph)[N+1] = malloc(sizeof(int) * (N+1) * (N+1));
//    int (*visited) = malloc(sizeof(int) * (N+1));
//    
//    int idx_a, idx_b = 0;
//    for (int i = 0; i < M; i++)
//    {
//        scanf("%d %d", &idx_a, &idx_b);
//        graph[idx_a][idx_b] = 1;
//        graph[idx_b][idx_a] = 1;
//    }
//    
//    // DFS
//    DFS(V, N, visited, graph);
//    printf("\n");
//    
//    // BFS
//    for (int i = 0; i < N + 1; i++)
//    {
//        visited[i] = 0;
//    }
//    
//    Queue q;
//    q.data = (int*)malloc(sizeof(int) * N+1);
//    q.rear = -1;
//    q.front = -1;
//    q.data[++q.rear] = V;
//    visited[V] = 1;
//    
//    BFS(q, N, visited, graph);
//
//    
//    return 0;
//}
