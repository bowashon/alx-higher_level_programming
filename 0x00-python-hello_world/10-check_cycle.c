#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
 * check_cycle - function that check if a singly linked list has a cycle
 * using the Flyod_cycle_finding algorithm
 * @list: point to the first node or list
 * Return: return 1 if a cycle is found or 0 if otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *slow;
	listint_t *fast;

	if (list == NULL || list->next == NULL)
	{
		return (0);
	}
	slow = list;
	fast = list;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
		{
			return (1);
		}
	}
	return (0);
}
