#include "main.h"
#include <stdio.h>
#include <string.h>
/**
 * _strcpy - function that copy a string
 * @dest: destination
 * @src: source code
 * Return: return the copied string
 */
char *_strcpy(char *dest, char *src)
{
	int i;

	for (i = 0; i < _strlen(src); i++)
	{
		dest[i] = src[i];
	}
	return (dest);
}
