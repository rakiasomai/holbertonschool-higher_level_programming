#include "lists.h"

/**
 * is_palindrome - Check if a singly linked list is a palindrome
 * @head: double pointer to head node
 * An empty list is considered a palindrome
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *mover = *head;
	int i = 0, j = 0;
	char array[50];

	if (head == NULL)
		return (0);
	if (*head == NULL || (*head)->next == NULL)
		return (1);
	if (loopcheck(mover) == 1)
		return (0);
	while (mover)
	{
		array[i] = mover->n;
		i++;
		mover = mover->next;
	}
	i--;
	j = 0;
	while (j < i)
	{
		if (array[j] != array[i])
			return (0);
		i--;
		j++;
	}
	return (1);
}

/**
 * loopcheck - Check if a singly linked list has a cycle in it
 * @list: pointer to head of singly linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int loopcheck(listint_t *list)
{
	listint_t *fast = list, *slow = list;

	if (list == NULL)
		return (0);

	while (fast && slow && fast->next)
	{
		fast = fast->next->next;
		slow = slow->next;
		if (fast == slow)
			return (1);
	}
	return (0);
}
