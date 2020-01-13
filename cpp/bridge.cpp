#include <string>
#include <vector>
#include <queue>
using namespace std;

int solution(int bridge_length, int weight, vector<int> truck_weights) 
{
    queue<int> q;
    int sum = 0;
    int time = 0;
    
    for(int i = 0; i < truck_weights.size(); i++)
    {
        while(1)
        {
            // 트럭이 도착점에 도착하면 빼준다
            if(q.size() == bridge_length)
            {
                sum -= q.front();
                q.pop();
            }
            
            if(q.empty())
            {
                q.push(truck_weights[i]);
                sum += truck_weights[i];
                time++;
                break;
            }
            else
            {
                // 트럭의 무게가 다리의 무게보다 더 크면, 0을 삽입해서 트럭을 도착점으로 민다
                if(sum + truck_weights[i] > weight)
                {
                    q.push(0);
                    time++;
                }
                else
                {
                    q.push(truck_weights[i]);
                    sum += truck_weights[i];
                    time++;
                    break;
                }
            }
        }
    }
    
    // 마지막 트럭이 도착하는 시간을 더해준다
    return time+bridge_length;
}