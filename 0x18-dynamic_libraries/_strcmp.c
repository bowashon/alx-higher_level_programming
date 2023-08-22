#include "main.h"
#include <stdio.h>
#include <string.h>
/**
 * _strcmp - function that compares two string
 * @s1: first string to compare
 * @s2: second string to compare
 * Return: return 1 if they are equal and 0 if otherwise
 */
int _strcmp(char *s1, char *s2)
{
	int i;

	while (s1[i] != '\0' && s2[i] != '\0')
	{
		if (s1[i] != s2[i])
		{
			return (0);
		}
	}
	if (s1[i] == '\0' && s2[i] == '\0')
	{
		return (1);
	}
	return (1);
}
