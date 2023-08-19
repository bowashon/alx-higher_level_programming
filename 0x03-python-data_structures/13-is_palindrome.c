#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * reverse_linked_list - function that reverses linked list
 * @head: pointer to the first data in the node
 * Return: return the reverse linked_list
 */
listint_t *reverse_linked_list(listint_t *head)
{
	listint_t *current = head;
	listint_t *next = NULL;
	listint_t *prev = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	return (prev);
}

/**
 * mid_point - finds the mid point of a list
 * @head: pointer to the first data
 * Return: return the middle node;
 */
listint_t *mid_point(listint_t *head)
{
	listint_t *fast = head;
	listint_t *slow = head;
	listint_t *prev_slow = NULL;

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev_slow = slow;
		slow = slow->next;
	}
	if (fast != NULL)
	{
		return (slow);
	}
	return (prev_slow);
}

/**
 * is_palindrome - checks if a list is palindrome or not
 * @head: pointer to a pointer head
 * Return: return 1 if is palindrom or 0 if otherwise
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL)
	{
		return (0);
	}

	listint_t *mid = mid_point(*head);
	listint_t *reversed_second_half = reverse_linked_list(mid->next);
	listint_t *current = *head;

	while (reversed_second_half != NULL)
	{
		if (current->n != reversed_second_half->n)
		{
			return (0);
		}
		current = current->next;
		reversed_second_half = reversed_second_half->next;
	}

	return (1);
}
