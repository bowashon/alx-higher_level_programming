#include "main.h"
#include <stddef.h>

/**
 * _strchr - function to locate a character in a string
 * @s: pointer to a string
 * @c: character to be checked
 * Return: return a pointer to the string else returns NULL
 */
char *_strchr(char *s, char c)
{
	int i = 0;

	while (s[i] != '\0')
	{
		if (s[i] == c)
		return (s);
		s++;
	}
	if (c == '\0')
	{
		return (s);
	}
	return (NULL);
}
