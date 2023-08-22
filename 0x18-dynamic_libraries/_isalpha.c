#include "main.h"
#include <stdio.h>
/**
 * _isalpha - function that checks if a character is alphabet
 * @c: character to check
 * Return: return 1 if its alpha or 0 if otherwise
 */
int _isalpha(int c)
{
	if ((c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z'))
	{
		return (1);
	}
	return (0);
}
