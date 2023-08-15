#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
/**
 * insert_node - function that inserts a node in a sorted linked list
 * @head: pointer to the first node
 * @number: the value to be inserted
 * Return: returns the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current;
	listint_t *new_node;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
	{
		return (NULL);
	}
	new_node->n = number;
	current = *head;

	if (*head == NULL)
		*head = new_node;
	else
	{
		while (current->next != NULL && current->next->n < number)
		{
			current = current->next;
		}
		new_node->next = current->next;
		current->next = new_node;
	}

	return (new_node);
}
