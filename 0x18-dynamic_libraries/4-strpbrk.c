#include "main.h"
#include <stdio.h>

/**
 * _strpbrk - function that searches a string for any of a set of bytes.
 * @s: parent file
 * @accept: file to check
 * Return: return a pointer to s or NULL if no se
 */
char *_strpbrk(char *s, char *accept)
{

	while (*s != '\0')
	{
		char *str = accept;

		while (*str != '\0')
		{
			if (*s == *str)
			{
				return (s);
			}
		str++;
		}
		s++;
	}
	return (NULL);
}
