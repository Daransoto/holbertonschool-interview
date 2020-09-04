#include "lists.h"
#include <stdlib.h>

/**
* check_cycle - Finds the loop in a linked list.
* @list: Pointer to list.
* Return: 0 if there is no cycle, 1 if there is a cycle.
*/
int check_cycle(listint_t *list)
{

	if (!list)
		return (0);
	while (1)
	{
		if (list->next >= list || !list->next)
			break;
		list = list->next;
	}
	if (list->next)
		return (1);
	return (0);
}
