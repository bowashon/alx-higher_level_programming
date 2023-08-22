#include "main.h"
#include <unistd.h>
#include <stdio.h>
/**
 * _putchar - function that print character to the stdout
 * @c: character to print
 * Return: return 1 if success or 0 if otherwise
 */
int _putchar(char c)
{
	return (write(1, &c, 1));
}
