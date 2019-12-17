#include "lists.h"
/**
* is_palindrome - Check if a singly linked list is a palindrome
* @head: is a double pointer
*
* Return: 0 if it is not a palindrome, 1 if it is a palindrome
*/
int is_palindrome(listint_t **head)
{
listint_t *rak = *head;
int y = 0, z = 0;
char array[50];
if (head == NULL)
return (0);
if (*head == NULL || (*head)->next == NULL)
return (1);
if (lpcheck(rak) == 1)
return (0);
while (rak)
{
array[y] = rak->n;
y++;
rak = rak->next;
}
y--;
z = 0;
while (z < i)
{
if (array[z] != array[y])
return (0);
y--;
z++;
}
return (1);
}
/**
* lpcheck - Check if a singly linked list has a cycle in it
* @list: is a pointer
* Return: 0 if there is no cycle, 1 if there is a cycle
*/
int lpcheck(listint_t *list)
{
listint_t *som = list, *raf = list;
if (list == NULL)
return (0);
while (som && raf && som->next)
{
som = som->next->next;
raf = raf->next;
if (som == raf)
return (1);
}
return (0);
}
