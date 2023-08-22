#include "main.h"
#include <stdio.h>
#include <stdlib.h>
/**
 * _abs - function the returns the absolute value of an integer
 * @n: parameter to return its absolute value
 * Return: return the absolute value of the number
 */
int _abs(int n)
{
	if (n < 0)
	{
		n = -n;
	}
	return (n);
}
