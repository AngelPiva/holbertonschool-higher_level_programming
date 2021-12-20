#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 *
 *
 */

int check_cycle(listint_t *list)
{
	listint_t *a, *b;

	if (list == NULL || list->next == NULL)
		return (0);

	a = list->next;
	b = list->next->next;

	while (a && b && b->next)
	{
		if (a == b)
			return (1);
		a = a->next;
		b = b->next->next;
	}
	return (0);
}
