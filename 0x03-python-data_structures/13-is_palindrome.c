#include "lists.h"
/**
 * is_palindrome - check if the number is palindrome
 * @head: the head of list
 * Return: integer
 */

int is_palindrome(listint_t **head)
{
	int i, j, r;
	int *array;
	listint_t *c = *head;

	if (head == 0 || *head == 0)
		return (1);
	for (i = 0; c != 0; i++)
		c = c->next;
	array = malloc(i * sizeof(int));
	if (array == 0)
		return (0);
	c = *head;
	for (j = 0; j < i; j++)
	{
		array[j] = c->n;
		c = c->next;
	}
	for (j = 0, r = i - 1; j < r; j++, r--)
	{
		if (array[j] != array[r])
		{
			free(array);
			return (0);
		}
	}

	free(array);
	return (1);
}
