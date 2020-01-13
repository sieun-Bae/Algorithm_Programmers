#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <iostream>
using namespace std;

bool cmp(pair<int, int> a, pair<int, int> b)
{
    if(a.first > b.first)
    {
        return true;
    }
    else if(a.first == b.first)
    {
        if(a.second < b.second)
        {
            return true;
        }
        else
        {
            return false;
        }
    }
    else
    {
        return false;
    }
}

vector<int> solution(vector<string> genres, vector<int> plays) 
{
    vector<int> answer;
    vector<string> gName;
    map<string, int> gVisited;
    
    // 1. 속한 노래가 많이 재생된 장르를 먼저 수록합니다.
    for(int i = 0; i < genres.size(); i++)
    {
        if(gVisited[genres[i]] == 0)
        {
            gName.push_back(genres[i]);
        }
        
        gVisited[genres[i]] += plays[i];
    }
    
    // for(int i = 0; i < gName.size(); i++)
    // {
    //     cout << gName[i];
    // }
    
    vector<pair<int, string>> gRank;
    for(int i = 0; i < gName.size(); i++)
    {
        gRank.push_back({gVisited[gName[i]], gName[i]});
    }
    // 장르 순서 정렬
    sort(gRank.begin(), gRank.end(), greater<pair<int, string>>());
    
    // 2. 장르 내에서 많이 재생된 노래를 먼저 수록합니다.
    // 3. 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
    for(int i = 0; i < gRank.size(); i++)
    {
        // 노래 재생횟수 저장
        vector<pair<int, int>> reserve;
        
        for(int j = 0; j < genres.size(); j++)
        {
            if(gRank[i].second == genres[j])
            {
                reserve.push_back({plays[j], j});
            }
        }
        
        // 노래 순서 정렬
        sort(reserve.begin(), reserve.end(), cmp);
        
        if(reserve.size() == 1)
        {
            answer.push_back(reserve[0].second);
        }
        else
        {
            answer.push_back(reserve[0].second);
            answer.push_back(reserve[1].second);
        }
    }
    
    return answer;
}