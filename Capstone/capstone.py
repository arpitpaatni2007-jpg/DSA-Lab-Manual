from collections import deque


class ProfileManager:

    def __init__(self):
        self.profiles = {}

    def add_user(self, u, name, age, interests, city):
        if u in self.profiles:
            print(f'{u} exists!')
            return

        self.profiles[u] = {
            'name': name,
            'age': age,
            'interests': set(interests),
            'city': city
        }
        print(f'Added: {u}')

    def update_profile(self, u, **kw):
        if u not in self.profiles:
            return

        for k, v in kw.items():
            if k == 'interests':
                self.profiles[u][k] = set(v)
            else:
                self.profiles[u][k] = v

        print(f'Updated: {u}')

    def display(self, u):
        p = self.profiles.get(u)
        if p:
            print(f'{u}: {p["name"]} | {p["city"]} | {", ".join(p["interests"])}')


class SocialGraph:

    def __init__(self):
        self.adj = {}

    def add_user(self, u):
        if u not in self.adj:
            self.adj[u] = set()

    def connect(self, u, v):
        self.add_user(u)
        self.add_user(v)
        self.adj[u].add(v)
        self.adj[v].add(u)

    def disconnect(self, u, v):
        self.adj.get(u, set()).discard(v)
        self.adj.get(v, set()).discard(u)

    def friends(self, u):
        return list(self.adj.get(u, []))


# ---------- BFS ----------
def bfs_path(g, src, dst):
    vis = {src: None}
    q = deque([src])

    while q:
        n = q.popleft()

        if n == dst:
            path = []
            while n:
                path.append(n)
                n = vis[n]
            return path[::-1]

        for nb in g.adj.get(n, []):
            if nb not in vis:
                vis[nb] = n
                q.append(nb)

    return None


# ---------- DFS ----------
def dfs_explore(g, src, max_d):
    vis = set()
    res = []

    def dfs(n, d):
        if d > max_d or n in vis:
            return

        vis.add(n)

        if n != src:
            res.append((n, d))

        for nb in g.adj.get(n, []):
            dfs(nb, d + 1)

    dfs(src, 0)
    return res


# ---------- RECOMMEND ----------
def recommend(pm, g, u, top=3):
    mi = pm.profiles.get(u, {}).get('interests', set())
    fr = set(g.friends(u))
    fr.add(u)

    cands = [
        (x, len(mi & d['interests']))
        for x, d in pm.profiles.items()
        if x not in fr
    ]

    return sorted(cands, key=lambda x: -x[1])[:top]


# ---------- DEMO ----------
pm = ProfileManager()
sg = SocialGraph()

data = [
    ('alice', 'Alice Sharma', 22, ['music', 'travel', 'coding'], 'Delhi'),
    ('bob', 'Bob Kumar', 24, ['gaming', 'coding', 'movies'], 'Mumbai'),
    ('carol', 'Carol Patel', 23, ['travel', 'cooking', 'music'], 'Pune'),
    ('dave', 'Dave Gupta', 25, ['sports', 'coding', 'travel'], 'Bangalore'),
    ('eve', 'Eve Singh', 21, ['music', 'art', 'cooking'], 'Delhi'),
    ('frank', 'Frank Mehta', 26, ['movies', 'sports', 'gaming'], 'Chennai')
]

for d in data:
    pm.add_user(*d)
    sg.add_user(d[0])

connections = [
    ('alice', 'bob'),
    ('alice', 'carol'),
    ('bob', 'dave'),
    ('carol', 'eve'),
    ('dave', 'frank'),
    ('alice', 'dave')
]

for u, v in connections:
    sg.connect(u, v)

pm.update_profile('alice', city='Noida')

print('--- Profiles ---')
for u in ['alice', 'carol', 'eve']:
    pm.display(u)

sg.disconnect('bob', 'dave')

print('--- BFS Paths ---')
for s, e in [('alice', 'eve'), ('bob', 'frank')]:
    path = bfs_path(sg, s, e)
    if path:
        print(f'{s}->{e}: {" -> ".join(path)} (deg={len(path)-1})')
    else:
        print(f'{s}->{e}: No path')

print('--- DFS (depth=2) from alice ---')
print(dfs_explore(sg, 'alice', 2))

print('--- Recommendations for alice ---')
for u, sc in recommend(pm, sg, 'alice'):
    print(f'  {u}: {sc} common interest(s)')