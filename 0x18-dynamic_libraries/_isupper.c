#include "main.h"
#include <stdio.h>
/**
 * _isupper - function to check if a character is uppercase letter
 * @c: parameter to check
 * Return: return 1 if is upper or 0 if otherwise
 */
int _isupper(int c)
{
	if (c >= 'A' && c <= 'Z')
	{
		return (1);
	}
	return (0);
}
