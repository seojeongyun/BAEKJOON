//
//  Untitled.h
//  
//
//  Created by 서정윤 on 7/23/25.
//

#include <stdio.h>

void dfs(int idx);
void bfs(void);

#define MAX 1000
typedef struct
{
    int front, rear;
    int data[MAX];
} Queue;

int N, V, M = 0;
int visited[MAX] = {0,};
int graph[MAX][MAX] = {0,};

Queue q;

int main(void)
{
    scanf("%d %d %d", &N, &M, &V);
    
    // Graph
    int x,y = 0;
    //

    for(int j = 0; j < M; j++)
    {
        scanf("%d %d", &x, &y);
        graph[x][y] = 1;
        graph[y][x] = 1;
    }
        

    // DFS
    dfs(V);
    printf("--");
    // BFS
    for(int i = 0; i < MAX; i++)
    {
        visited[i] = 0;
    }
    
    q.front = -1;
    q.rear = -1;
    q.data[++q.rear] =  V;
    visited[V] = 1;
    
    bfs();
    
    return 0;
}


void dfs(int idx)
{
    visited[idx] = 1;
    printf("%d ", idx);
    
    for(int next = 0; next < M+1; next++)
    {
        if(visited[next] != 1 && graph[idx][next])
        {
            dfs(next);
        }
    }
}


void bfs(void)
{
    int curr;
    
    while(q.front < q.rear)
    {
        curr = q.data[++q.front];
        printf("%d ", curr);
        
        for(int next = 0; next < M+1; next++)
        {
            if(visited[next] != 1 && graph[curr][next])
            {
                visited[next] = 1;
                q.data[++q.rear] = next;
            }
        }
    }
}

