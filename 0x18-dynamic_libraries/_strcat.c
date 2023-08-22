#include "main.h"
#include <stdio.h>
#include <stdlib.h>
/**
 * _strcat - function that concatenate tow strings
 * @dest: destination string
 * @src: source string
 * Return: returnt the concatenated string
 */
char *_strcat(char *dest, char *src)
{
	int len1 = _strlen(dest);
	int len2 = _strlen(src);
	int i;

	for (i = 0; i < len2; i++)
	{
		dest[len1 + i] = src[i];
	}
	dest[len1 + i] = '\0';

	return (dest);
}
