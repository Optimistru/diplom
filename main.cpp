#include <stdio.h>
#include <iostream>
#include <string.h>
#include <algorithm>
#include <stdlib.h>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <string.h>
#include <map>
using namespace std;

#define ll long long
#define mp make_pair

ll n, m, k, l, r, x, y, costA;

ll a[1010][1010], b[1010][1010];
ll pri[1010], prj[1010];

bool can(ll locm) {
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			b[i][j] = ((a[i][j] >= locm) ? 0 : 1);
		}
	}

	int ans = 0;
	vector<int> d(m, -1), d1(m), d2(m);
	stack<int> st;
	for (int i = 0; i<n; ++i) {
		for (int j = 0; j<m; ++j)
			if (b[i][j] == 1)
				d[j] = i;
		while (!st.empty()) st.pop();
		for (int j = 0; j<m; ++j) {
			while (!st.empty() && d[st.top()] <= d[j])  st.pop();
			d1[j] = st.empty() ? -1 : st.top();
			st.push(j);
		}
		while (!st.empty()) st.pop();
		for (int j = m - 1; j >= 0; --j) {
			while (!st.empty() && d[st.top()] <= d[j])  st.pop();
			d2[j] = st.empty() ? m : st.top();
			st.push(j);
		}
		for (int j = 0; j<m; ++j)
			ans = max(ans, (i - d[j]) * (d2[j] - d1[j] - 1));
	}

	return ans >= k;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	cin >> n >> m;

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cin >> a[i][j];
		}
	}

	cin >> k;

	ll l = 0, r = 1000, m;
	while (l + 1 < r) {
		m = l + (r - l) / 2;
		if (can(m)) {
			l = m;
		}
		else {
			r = m;
		}
	}

	if (can(r))
		cout << r;
	else
		cout << l;

}