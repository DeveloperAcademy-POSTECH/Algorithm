#include <iostream>
#include <vector>
#include <queue>
#include <iomanip>
using namespace std;

#define INF 1e9
#define ii pair<int, int>
#define iii tuple<int, int, int>

int n;
int board[22][22];
vector<int> fav[500];

vector<int> seq;
const int dx[] = {1,0,-1,0};
const int dy[] = {0,-1,0,1};

bool isBlank(int x,int y){
    if(x < 1 || y < 1 || x > n || y > n) return false;
    if(board[x][y] != 0) return false;
    return true;
}

vector<ii> getFav(int id) {
    vector<ii> ret;
    int mx = 0;
    int weight[23][23];
    for(int i=0; i<23; i++) fill(weight[i], weight[i]+23, 0);
    
    for(int i=1; i<=n; i++){
        for(int j=1; j<=n; j++){
            if(board[i][j] == 0) continue;
            
            // 그자리에 좋아하는사람이 앉았다면
            for(int f: fav[id]) {
                if(board[i][j] == f) {
                    for(int z=0; z<4; z++){ // 주위의 가중치를 +1한다
                        int x = i + dx[z];
                        int y = j + dy[z];
                        if(!isBlank(x, y)) continue;
                        weight[x][y]++;
                        if(mx == weight[x][y]) {
                            ret.push_back({x, y});
                        }
                        else if(mx < weight[x][y]) {
                            mx = weight[x][y];
                            ret.clear();
                            ret.push_back({x, y});
                        }
                        
                    }
                }
            }
        }
    }
    
    return ret;
}

int ans;

void didSeat(int x, int y, int id){
    board[x][y] = id;
}

int main() {
    cin.tie(0)->ios_base::sync_with_stdio(0);
    
    cin >> n;
    for(int i=0; i<n*n; i++){
        int id; cin >> id;
        for(int j=0; j<4; j++){
            int f; cin >> f;
            fav[id].push_back(f);
        }
        seq.push_back(id);
    }
    
    
    for(auto id: seq) {
        // 1번 규칙
        vector<ii> candidate = getFav(id);
        if(candidate.size() == 1) {
            ii& seat = candidate[0];
            didSeat(seat.first, seat.second, id);
            continue;
        }
        else if(candidate.size() == 0){
            for(int i=1; i<=n; i++){
                for(int j=1; j<=n; j++){
                    if(board[i][j] == 0){
                        candidate.push_back({i,j});
                    }
                }
            }
        }
        
        // 2번 규칙
        priority_queue<iii> pq;
        for(ii c : candidate) {
            int blankCnt = 0;
            for(int i=0; i<4; i++){
                int x = c.first + dx[i];
                int y = c.second + dy[i];
                if(!isBlank(x,y)) continue;
                blankCnt++;
            }
            pq.push({blankCnt, c.first, c.second});
        }
        
        priority_queue<ii, vector<ii>, greater<ii>> lastCandidate;
        
        auto [mxCnt, p, q] = pq.top();
        while(pq.size() && mxCnt == get<0>(pq.top())) {
            auto [cnt, _p, _q] = pq.top();
            pq.pop();
            lastCandidate.push({_p, _q});
        }
        if(lastCandidate.size() == 1) {
            auto [_p, _q] = lastCandidate.top();
            didSeat(_p, _q, id);
            
            continue;
        }
        
        // 3번 규칙
        
        auto [u, v] = lastCandidate.top();
        didSeat(u, v, id);
    }

    for(int i=1; i<=n; i++){
        for(int j=1; j<=n; j++){
            int total = 0;
            int id = board[i][j];
            
            for(int f: fav[id]) {
                for(int z=0; z<4; z++){
                    int nx = i + dx[z];
                    int ny = j + dy[z];
                    if(board[nx][ny] == f) {
                        total++;
                        break;
                    }
                }
            }
            if(total == 1) ans += 1;
            else if(total == 2) ans += 10;
            else if(total == 3) ans += 100;
            else if(total == 4) ans += 1000;
        }
    }
    cout << ans;
    
}
