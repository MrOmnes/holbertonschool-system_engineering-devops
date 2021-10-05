#include "main.h"

/**
 * main - writes the character c to stdout
 * Return: On success 1.
 * On error, -1 is returned, and errno is set appropriately.
 */

int main(void)
{
	char c[8] = "_putchar";
	int i = 0;

	while (c[i] != '\0')
	{
	_putchar(c[i++]);
	}
	_putchar('\n');

	return (0);

}
