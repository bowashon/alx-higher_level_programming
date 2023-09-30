#include <stdio.h>
#include <stdlib.h>
#include "hash_tables.h"
/**
 * hash_table_create - function that create a hash table of size
 * @size: size of the table
 * Return: returns a pointer to the newly created hash table
 */
hash_table_t *hash_table_create(unsigned long int size)
{
	hash_table_t *table;
	int i;

	table = (hash_table_t *)malloc(sizeof(hash_table_t *));

	if (table == NULL)
	{
		return (NULL);
	}
	table->array = malloc(sizeof(hash_table_t *) * size);
	if (table->array == NULL)
	{
		free(table->array);
		return (NULL);
	}
	table->size = size;

	for (i = 0; i < size; i++)
	{
		table->array[i] = NULL;
	}
	return (table);
}
