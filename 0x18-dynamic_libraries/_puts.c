#include "main.h"
#include <stdio.h>
#include <string.h>
/**
 * _puts - function that prints a string
 * @s: pointer to the string
 *
 */
void _puts(char *s)
{
	while (*s)
	{
		_putchar(*s);
		s++;
	}
}
