#include "main.h"

/**
 * _putchar - writes the character c to stdout
 * @c: The character to print
 *
 * Return: On success 1.
 * On error, -1 is returned, and errno is set appropriately.
 */
int main(void)
{   

	char c;

	for (c = 'a'; c <= 'z'; ++c)
		_putchar(c);
	_putchar('\n');
	return (0);

}