#include "lists.h"

/**
* is_palindrome - Checks if a singly linked list is a palindrome.
* @head: Pointer to the first node of the list.
* Return: 0 if it is not a palindrome, 1 if it is a palindrome.
*/

int is_palindrome(listint_t **head)
{
	listint_t *p1, *p2, *prev, *next_n;

	if (!head || !*head)
		return (1);

	p1 = p2 = *head;

	while (p2 && p2->next)
	{
		p1 = p1->next;
		p2 = p2->next->next;
	}

	prev = NULL;
	p2 = *head;

	while (p1)
	{
		next_n = p1->next;
		p1->next = prev;
		prev = p1;
		if (!next_n)
			break;
		p1 = next_n;
	}

	while (p1)
	{
		if (p1->n != p2->n)
			return (0);
		p1 = p1->next;
		p2 = p2->next;
	}

	return (1);
}
