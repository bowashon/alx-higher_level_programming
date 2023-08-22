#include "main.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
/**
 * _memset - function the sets n memory of area pointed by s by b characters
 * @s: the pointer to the memory area
 * @b: characters to fill
 * @n: the number of characaters to fill
 * Return: the area pointed by s
 */
char *_memset(char *s, char b, unsigned int n)
{
	unsigned int i = 0;

	while (i < n)
	{
		s[i] = b;
		i++;
	}
	return (s);
}
