#include "main.h"
#include <stdio.h>
#include <string.h>
/**
 * _strncpy - function that copy n characters of strings
 * @dest: destination string
 * @src: source string
 * @n: number of characters to copy
 * Return: return the dest containing the copied string
 */
char *_strncpy(char *dest, char *src, int n)
{
	int i;

	if (n < 0 || n > _strlen(src))
	{
		return (NULL);
	}
	else
	{
	for (i = 0; i < n; i++)
	{
		dest[i] = src[i];
	}
	}
	dest[i] = '\0';

	return (dest);
}
