#include "main.h"
#include <stdio.h>
/**
 * _islower - function that check if a function is lower case character
 * @c: character to check
 * Return: return 1 if is lower of 0 if otherwise
 */
int _islower(int c)
{
	if (c >= 'a' && c <= 'z')
	{
		return (1);
	}
	return (0);
}
