#include "sandpiles.h"

/**
* sandpiles_sum - Computes the sum of two sandpiles.
* @grid1: First sandpile.
* @grid2: Second sandpile.
*/

void sandpiles_sum(int grid1[3][3], int grid2[3][3])
{
	int i, j, unstable, temp[3][3];

	for (i = 0; i < 3; i++)
		for (j = 0; j < 3; j++)
			grid1[i][j] += grid2[i][j];
	do {
		for (i = 0; i < 3; i++)
			for (j = 0; j < 3; j++)
				temp[i][j] = grid1[i][j];
		unstable = 0;
		for (i = 0; i < 3; i++)
		{
			for (j = 0; j < 3; j++)
			{
				if (temp[i][j] > 3)
				{
					if (!unstable)
						print_g(grid1);
					unstable = 1;
					grid1[i][j] -= 4;
					if (i > 0)
						grid1[i - 1][j] += 1;
					if (i < 2)
						grid1[i + 1][j] += 1;
					if (j > 0)
						grid1[i][j - 1] += 1;
					if (j < 2)
						grid1[i][j + 1] += 1;
				}
			}
		}
	} while (unstable);
}

/**
* print_g - Prints a 3 by 3 grid.
* @grid: Grid to be printed.
*/

void print_g(int grid[3][3])
{
	int i, j;

	puts("=");
	for (i = 0; i < 3; i++)
	{
		for (j = 0; j < 3; j++)
		{
			if (j)
				printf(" ");
			printf("%d", grid[i][j]);
		}
		printf("\n");
	}
}
