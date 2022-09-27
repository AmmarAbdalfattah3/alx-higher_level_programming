#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: pointer to a head of list.
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
    listint_t *first_list_cycle, *second_list_cycle;
    first_list_cycle = list, second_list_cycle = list;
    while (second_list_cycle != NULL && second_list_cycle->next != NULL)
    {
        first_list_cycle = first_list_cycle->next;
        second_list_cycle = second_list_cycle->next->next;

        if (first_list_cycle == second_list_cycle)
        {
            return (1);
        }
    }
return (0);
}
