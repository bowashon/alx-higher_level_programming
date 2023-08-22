#include "main.h"
#include <stdio.h>
#include <stdlib.h>
/**
 * _isdigit - function that checks if a paremeter is digit
 * @c: parameter to check
 * Return: return 1 if is digit or 0 if otherwise
 */
int _isdigit(int c)
{
	if (c >= '0' && c <= '9')
	{
		return (1);
	}
	return (0);
}
