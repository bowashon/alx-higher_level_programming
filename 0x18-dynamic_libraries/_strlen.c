#include "main.h"
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
/**
 * _strlen - function that calculate the length of a string
 * @s: the string character to calculate its length
 * Return: return the length of the string
 */
int _strlen(char *s)
{
	int len = 0;

	while (*s)
	{
		len++;
		s++;
	}
	return (len);
}
