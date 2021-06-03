#include <stdio.h>
#include <iostream>
using namespace std;
struct vertices {
  int name;
  int g;
  int prev;
};

int DT[50][50];
int n;

vertices Open[50];
int nO = 0;
vertices Close[50];
int nC = 0;

void ReadFile(int DT[50][50], int &n) {
  FILE *f = fopen("test.txt", "r");
  fscanf(f, "%d", &n);
  for (int i = 0; i < n; i++)
    for (int j = 0; j < n; j++) fscanf(f, "%d", &DT[i][j]);
  fclose(f);
}

void AddVertices(vertices N, vertices Set[], int &nS) {
  Set[nS] = N;
  nS++;
}

void DeleteVertices(int vt, vertices Open[], int &nO) {
  for (int i = vt; i < nO - 1; i++) Open[i] = Open[i + 1];
  nO--;
}
int Min(vertices Open[], int nO) {
  int min = Open[0].g;
  int vt = 0;
  for (int i = 0; i < nO; i++) {
    if (min > Open[i].g) {
      min = Open[i].g;
      vt = i;
    }
  }
  return vt;
}

int Member(int node, vertices Set[], int nS) {
  for (int i = 0; i < nS; i++)
    if (Set[i].name == node) return i;
  return -1;
}

void Dijkstra(int S, int G) {
  vertices N;
  N.name = S;
  N.g = 0;
  N.prev = 0;
  AddVertices(N, Open, nO);

  while (nO != 0) {
    int vt = Min(Open, nO);
    vertices N = Open[vt];
    if (N.name == G) {
      AddVertices(N, Close, nC);
      break;
    } else {
      AddVertices(N, Close, nC);
      for (int node = 0; node < n; node++) {
        int belong = Member(node, Close, nC);
        if (belong == -1 && DT[N.name][node] > 0) {
          int k = Member(node, Open, nO);
          if (k >= 0) {
            vertices Q;
            Q = Open[k];
            if (N.g + DT[N.name][Q.name] < Q.g) {
              Open[k].g = N.g + DT[N.name][Q.name];
              Open[k].prev = N.name;
            }
          } else {
            vertices Q;
            Q.name = node;
            Q.g = N.g + DT[N.name][Q.name];
            Q.prev = N.name;
            AddVertices(Q, Open, nO);
          }
        }
      }
      DeleteVertices(vt, Open, nO);
    }
  }
}

int main() {
  ReadFile(DT, n);

  int S, G;
  printf("Enter the starting vertex : ");
  scanf("%d", &S);
  printf("Enter the ending vertex: ");
  scanf("%d", &G);

  Dijkstra(S, G);

  int vtG = Member(G, Close, nC);
  if (vtG >= 0) {
    printf("Distance from %d to %d is: %d \n", S, G, Close[vtG].g);
    printf("Path: %d <- ", G);
    int k = vtG;
    while (Close[k].prev != S) {
      cout << Close[k].prev << " <- ";
      k = Member(Close[k].prev, Close, nC);
    }
    printf("%d ", S);
  } else  // vtG < 0
    printf("\nThere is no way from %d to %d", S, G);
}

