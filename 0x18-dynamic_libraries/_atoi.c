#include "main.h"
#include <stdio.h>
#include <stdlib.h>
/**
 * _atoi - function that converts string represtation of a digit to integer
 * @s: pointer to the string
 * Return: returns the integer representation of a string
 */
int _atoi(char *s)
{
	int sign = 1;
	int is_digit = 0;
	int result = 0;

	while (*s)
	{
		if (*s == '-')
		{
			sign *= -1;
		}
		else if (_isdigit(*s))
		{
			is_digit = 1;
			result = (result * 10) + (*s - '0');
		}
		if (is_digit == 1)
		{
			break;
		}
		s++;
	}
	return (result * sign);
}
