#include "slide_line.h"

/**
* slide_line - Reproduces the 2048 game mechanics on a single horizontal line.
* @line: Points to an array of integers containing size elements.
* @size: Number of elements in line.
* @direction: Can be either SLIDE_LEFT or SLIDE_RIGHT.
* Return: 1 upon success, or 0 upon failure.
*/

int slide_line(int *line, size_t size, int direction)
{
	int p1 = 0, p2 = 1, step = 1;

	if (!line || size < 1 || (direction != 0 && direction != 1))
		return (0);
	if (direction == SLIDE_RIGHT)
	{
		p1 = size - 1;
		p2 = size - 2;
		step = -1;
	}
	while (direction == 0 ? p2 < (int) size : p2 >= 0)
	{
		if (line[p1] == 0 || line[p1] == line[p2])
		{
			line[p1] += line[p2];
			if (line[p1] != line[p2])
				p1 += step;
			line[p2] = 0;
			p2 += step;
		}
		else if (line[p2] != 0)
		{
			p1 += step;
			if (p1 == p2)
				p2 += step;
		}
		else
			p2 += step;
	}
	return (1);
}
