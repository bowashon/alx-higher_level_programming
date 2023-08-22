#include "main.h"

/**
 * _strspn - function that gets the length of a prefix substring.
 * @s: points to parents string
 * @accept: contains string to be checked
 *
 * Return: return number of byte in initial segment of s which consists of
 * bytes from accept
 */
unsigned int _strspn(char *s, char *accept)
{
	unsigned int count = 0;
	unsigned int i = 0;
	unsigned int j = 0;
	unsigned int match;

	while (s[i] != '\0')
	{
		match = 0;
		j = 0;

		while (accept[j] != '\0')
		{
			if (s[i] == accept[j])
			{
				match = 1;
				count++;
			}

			j++;
		}

		if (!match)
		{
			break;
		}

		i++;
	}
	return (count);
}
