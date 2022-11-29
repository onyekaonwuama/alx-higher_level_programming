#include "lists.h"

/**
 * check_cycle - checks if singly linked list has a cycle within the list
 * @list: linked list
 * Return: 0 if no cycle esle 1
 */

int check_cycle(listint_t *list)
{
	listint_t *current = malloc(sizeof(listint_t));

	current = list;
	while (current != NULL)
	{
		if (current->next == list)
		{
			free(current);
			return (1);
		}
		current =  current->next;
	}
	free(current);
	return (0);
}


