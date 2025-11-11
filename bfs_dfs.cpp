#include <iostream> 
#include <vector> 
#include <queue> 
using namespace std; 
 
int main() { 
    int n, m; 
    cout << "Enter number of vertices: "; 
    cin >> n; 
 
    cout << "Enter number of edges: "; 
    cin >> m; 
 
    // Adjacency List 
    vector<vector<int>> adj(n + 1); 
 
    cout << "\nEnter the edges (format: u v):\n"; 
    for (int k = 1; k <= m; k++) { 
        int u, v; 
        cin >> u >> v; 
        adj[u].push_back(v);           // Directed graph 
        // adj[v].push_back(u);        // Uncomment for undirected graph 
    } 
 
    int start; 
    cout << "Enter initial vertex to traverse from: "; 
    cin >> start; 
 
    vector<int> visited(n + 1, 0); 
    queue<int> q; 
 
    cout << "Visited vertices: "; 
    cout << start << " "; 
    visited[start] = 1; 
    q.push(start); 
 
    while (!q.empty()) { 
        int v = q.front(); 
        q.pop(); 
 
        for (int u : adj[v]) { 
            if (!visited[u]) { 
                cout << u << " "; 
                visited[u] = 1; 
                q.push(u); 
            } 
        } 
    } 
 
    return 0; 
} 
 
 
 
