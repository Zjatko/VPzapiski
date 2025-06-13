#include <stdio.h>
#include <string.h>

const int width = 80;
const int height = 20;
const char node = '#';
const char edge = '*';

void readgrid(FILE *f, char grid[width][height])
{
	int n = 0;
	fscanf(f, "%d", &n);
	for (int i = 0; i < n; i++)
	{
		int x, y;
		fscanf(f, "%d %d", &x, &y);
		grid[x][y] = node;
	}
}

void fillline(char grid[width][height], int x1, int y1, int x2, int y2)
{
	int minx = x1 < x2 ? x1 : x2;
	int maxx = x1 > x2 ? x1 : x2;
	int miny = y1 < y2 ? y1 : y2;
	int maxy = y1 > y2 ? y1 : y2;

	float k = (float)(y2 - y1) / (x2 - x1);
	float n = y1 - k * x1;
	
	for (int x = minx; x <= maxx; x++)
	{
		for (int y = miny; y <= maxy; y++)
		{
			if (x == x1 && y == y1 || x == x2 && y == y2)
			{
				continue;
			}
			if (y == (int)(k * x + n))
			{
				grid[x][y] = edge;
			}
		}
	}
}

void drawgrid(char grid[width][height])
{
	for (int y = 0; y < height; y++)
	{
		for (int x = 0; x < width; x++)
		{
			printf("%c", grid[x][y]);
		}
		printf("\n");
	}
}

void fillgrid(FILE *f, char grid[width][height])
{
	int m = 0;
	fscanf(f, "%d", &m);
	for (int i = 0; i < m; i++)
	{
		int x1, y1, x2, y2;
		fscanf(f, "%d %d %d %d", &x1, &y1, &x2, &y2);
		fillline(grid, x1, y1, x2, y2);
	}
}

int main(int argc, char *argv[])
{
	FILE *f = fopen(argv[1], "r");
	char grid[width][height];
	for (int i = 0; i < width; i++)
	{
		memset(grid[i], ' ', height);
	}

	readgrid(f, grid);
	fillgrid(f, grid);
	drawgrid(grid);

	fclose(f);
	return 0;
}
