# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 1/17/20

SAME CODE FOR JAVA PASSED
import java.io.*;
import java.util.*;


public class Main {

  public static void main(String[] args) {
    solve();
  }

  final static int MAXN = 5 * 1000000 + 5;
  final static int MAXK = 505;
  static int N = 0;
  static int M = 0;
  static int K = 0;
  static int W = 0;
  static int H = 0;
  static int[][] A;
  static long[][] dp;
  static int[][] pre;
  static int[][] g;
  static int curAns = Integer.MAX_VALUE;
  static long[] HASH = new long[MAXN];
  static long MOD = (1L << 50) + 7;


  static void solve() {
    FastReader scanner = new FastReader();
    PrintWriter out = new PrintWriter(System.out);

    N = scanner.nextInt();
    M = scanner.nextInt();
    K = scanner.nextInt();
    Long[] directDist = new Long[N+1];
    Long[] trainDist = new Long[N+1];
    Arrays.fill(directDist, Long.MAX_VALUE);
    Arrays.fill(trainDist, Long.MAX_VALUE);
    Map<Pair<Integer, Integer>, Long> dist = new HashMap<>();
    Map<Integer, List<Pair<Integer, Long>>> g = new HashMap<>();

    for (int i = 0; i < M; i++) {
      int u = scanner.nextInt();
      int v = scanner.nextInt();
      int w = scanner.nextInt();
      if (u == 1) {
        directDist[v] = Math.min(directDist[v], w);
      } else if (v == 1) {
        directDist[u] = Math.min(directDist[u], w);
      } else {
        Pair<Integer, Integer> k = u < v ? new Pair<>(u, v) : new Pair<>(v, u);
        dist.put(k, Math.min(dist.getOrDefault(k, Long.MAX_VALUE), w));
      }
    }

    for (Map.Entry<Pair<Integer, Integer>, Long> entry: dist.entrySet()) {
      Pair<Integer, Integer> p = entry.getKey();
      int u = p.getFirst();
      int v = p.getSecond();
      Long w = entry.getValue();
      if (!g.containsKey(u)) {
        g.put(u, new ArrayList<>());
      }
      g.get(u).add(new Pair<>(v, w));
      if (!g.containsKey(v)) {
        g.put(v, new ArrayList<>());
      }
      g.get(v).add(new Pair<>(u, w));
    }

    Set<Integer> train = new HashSet<>();
    for (int i = 0; i < K; i++) {
      int v = scanner.nextInt();
      long w = scanner.nextLong();
      if (w < directDist[v]) {
        directDist[v] = w;
        train.add(v);
      }
      trainDist[v] = Math.min(trainDist[v], w);
    }

    if (!g.containsKey(1)) {
      g.put(1, new ArrayList<>());
    }
    for (int v = 2; v <= N; v++) {
      if (directDist[v] < Long.MAX_VALUE) {
        g.get(1).add(new Pair<>(v, directDist[v]));

        if (!g.containsKey(v)) {
          g.put(v, new ArrayList<>());
        }
        g.get(v).add(new Pair<>(1, directDist[v]));
      }
    }


    Long[] distFromCap = new Long[N+1];
    Arrays.fill(distFromCap, Long.MAX_VALUE);
    distFromCap[1] = 0L;

    PriorityQueue<Pair<Long, Integer>> q = new PriorityQueue<>();
    int[] indegree = new int[N+1];

    for (int u = 1; u <= N; u++) {
      if (directDist[u] < Long.MAX_VALUE) {
        distFromCap[u] = directDist[u];
        q.add(new Pair<>(directDist[u], u));
        indegree[u] = 1;
      }
    }

    while (!q.isEmpty()) {
      Pair<Long, Integer> p = q.poll();
      long d = p.getFirst();
      int u = p.getSecond();
      if (d > distFromCap[u]) continue;
      for (Pair<Integer, Long> vw : g.getOrDefault(u, new ArrayList<>())) {
        int v = vw.getFirst();
        long w = vw.getSecond();
        Long nd = distFromCap[u] + w;
        if (nd < distFromCap[v]) {
          distFromCap[v] = nd;
          indegree[v] = 1;
          q.add(new Pair<>(nd, v));
        } else if(nd.equals(distFromCap[v])) {
          indegree[v] += 1;
        }
      }
    }

    int ans = K - train.size();
    for (int v: train) {
      if (distFromCap[v] < trainDist[v]) {
        ans += 1;
      } else if (distFromCap[v].equals(trainDist[v]) && indegree[v] > 1) {
        indegree[v] -= 1;
        ans += 1;
      }
    }

    out.println(ans);
    out.close();
  }


  public static class FastReader {
    BufferedReader br;
    StringTokenizer st;


    public FastReader() {
      br = new BufferedReader(new InputStreamReader(System.in));
    }

    String next() {
      while (st == null || !st.hasMoreTokens()) {
        try {
          st = new StringTokenizer(br.readLine());
        } catch (Exception r) {
          r.printStackTrace();
        }
      }
      return st.nextToken();
    }

    int nextInt() {
      return Integer.parseInt(next());//converts string to integer
    }

    double nextDouble() {
      return Double.parseDouble(next());
    }

    long nextLong() {
      return Long.parseLong(next());
    }

    String nextLine() {
      String str = "";
      try {
        str = br.readLine();
      } catch (Exception r) {
        r.printStackTrace();
      }
      return str;
    }
  }
}

class UnioinSet {
  private Map<Long, Long> parents = new HashMap<>();

  public Long find(Long u) {
    if (parents.getOrDefault(u, u).equals(u)) {
      return u;
    }

    return find(parents.get(u));
  }

  public void union(Long u, Long v) {
    Long pu = find(u);
    Long pv = find(v);

    parents.put(pu, pv);
  }
}


class Pair<A, B> implements Comparable<Pair<A, B>>{
  private A first;
  private B second;

  public Pair(A first, B second) {
    super();
    this.first = first;
    this.second = second;
  }

  public String toString()
  {
    return "(" + first + ", " + second + ")";
  }

  public A getFirst() {
    return first;
  }

  public void setFirst(A first) {
    this.first = first;
  }

  public B getSecond() {
    return second;
  }

  public void setSecond(B second) {
    this.second = second;
  }

  @Override
  public int compareTo(Pair<A, B> o) {
    int cmp = compare(first, o.first);
    return cmp == 0 ? compare(second, o.second) : cmp;
  }

  private static int compare(Object o1, Object o2) {
    return o1 == null ? o2 == null ? 0 : -1 : o2 == null ? +1
      : ((Comparable) o1).compareTo(o2);
  }

  @Override
  public int hashCode() {
    return 31 * hashcode(first) + hashcode(second);
  }

  private static int hashcode(Object o) {
    return o == null ? 0 : o.hashCode();
  }

  public boolean equals(Object other) {
    if (other instanceof Pair) {
      Pair<A, B> otherPair = (Pair<A, B>) other;
      return
        ((  this.first == otherPair.first ||
          ( this.first != null && otherPair.first != null &&
            this.first.equals(otherPair.first))) &&
          (  this.second == otherPair.second ||
            ( this.second != null && otherPair.second != null &&
              this.second.equals(otherPair.second))) );
    }

    return false;
  }
}




"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List



INF = float('inf')
N, M, K = map(int, input().split())
directDist = [INF for _ in range(N+1)]
trainDist = [INF for _ in range(N+1)]
dist = {}
g = collections.defaultdict(list)
distFromCap = [INF for _ in range(N+1)]

for i in range(M):
    u, v, w = map(int, input().split())
    if u == 1:
        directDist[v] = min(directDist[v], w)
    elif v == 1:
        directDist[u] = min(directDist[u], w)
    else:
        k = (u, v)
        if k not in dist:
            dist[k] = w
        else:
            dist[k] = min(dist[k], w)

train = set()
for i in range(K):
    v, w = map(int, input().split())
    if w < directDist[v]:
        train.add(v)
        directDist[v] = w
    trainDist[v] = min(trainDist[v], w)

for (u, v), w in dist.items():
    g[u].append((v, w))
    g[v].append((u, w))

for v in range(2, N+1):
    if directDist[v] < INF:
        g[1].append((v, directDist[v]))
        g[v].append((1, directDist[v]))

q = []
indegree = [0 for _ in range(N+1)]
for v in range(2, N+1):
    if directDist[v] < INF:
        indegree[v] = 1
        distFromCap[v] = directDist[v]
        q.append((directDist[v], v))

heapq.heapify(q)
while q:
    d, u = heapq.heappop(q)
    if d > distFromCap[u]:
        continue
        
    for v, w in g[u]:
        nd = d + w
        if nd < distFromCap[v]:
            distFromCap[v] = nd
            indegree[v] = 1
            heapq.heappush(q, (nd, v))
        elif nd == distFromCap[v]:
            indegree[v] += 1
            
ans = K - len(train)
for v in train:
    if distFromCap[v] < trainDist[v]:
        ans += 1
    elif distFromCap[v] == trainDist[v] and indegree[v] > 1:
        ans += 1

print(ans)