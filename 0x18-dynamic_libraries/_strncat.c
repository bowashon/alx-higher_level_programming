#include "main.h"
#include <stdio.h>
#include <stdlib.h>
/**
 * _strncat - function that concatenate n character from a source string
 * @dest: destination string
 * @src: source string
 * @n: the number of characters to concatenate
 * Return: return the destinated string with concatenate
 */
char *_strncat(char *dest, char *src, int n)
{
	int len1 = _strlen(dest);
	int i = 0;

	while (i < n)
	{
		dest[len1 + i] = src[i];
		i++;
	}
	dest[len1 + i] = '\0';

	return (dest);
}
