#include "main.h"
#include <stdio.h>
#include <stdbool.h>

/**
 * _strstr -  function that locates a string
 * @haystack: pointer to the main string
 * @needle: pointer to the substring
 * Return: return a pointer to the beginning of the located substring, or
 * NULL if the substring is not found
 */
char *_strstr(char *haystack, char *needle)
{
	bool match = true;

	if (*needle == '\0')

	{
		return (haystack);
	}

	while (*haystack != '\0')
	{
		char *n = needle;
		char *h = haystack;

		match = true;
		while (*n != '\0')
		{
			if (*h != *n)
			{
				match = false;
				break;
			}

		n++;
		h++;
	}

	if (match)
	{
		return (haystack);
	}

	haystack++;

	}
	return (NULL);
}


